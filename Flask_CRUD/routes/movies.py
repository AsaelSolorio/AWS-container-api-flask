from flask import Blueprint, jsonify, request
import uuid

#entities
from models.entities.Movie import Movie
#models
from models.MovieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movie()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
        

@main.route('/add', methods = ['POST'])
def add_movies():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie_id = uuid.uuid4()
        movie = Movie(str(movie_id), title, duration, released)
        
        affected_rows = MovieModel.add_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie.movie_id)
        else:
            return jsonify({"message" : "Error on insert"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
        

@main.route('/delete/<movie_id>', methods = ['DELETE'])
def delete_movies(movie_id):
    try:
        movie = Movie(movie_id)
        
        affected_rows = MovieModel.delete_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie_id)
        else:
            return jsonify({"message" : "No movie deleted"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
        
        
@main.route('/update/<movie_id>', methods = ['PUT'])
def update_movies(movie_id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(movie_id, title, duration, released)
        
        affected_rows = MovieModel.update_movie(movie)
        
        if affected_rows == 1:
            return jsonify(movie.movie_id)
        else:
            return jsonify({"message" : "No movie updated"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500