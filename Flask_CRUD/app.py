from flask import Flask
from routes import movies


app = Flask(__name__)

#Error handlers
def page_not_found(error):
    return "<h1> Not found page Asael </h1>", 404


if __name__ == "__main__":
    #Error handlers
    app.register_error_handler(404, page_not_found)
    #Blueprints register
    app.register_blueprint(movies.main, url_prefix='/api/movies')
    app.run(host= "0.0.0.0",port=8080, debug=True)