SET search_path TO public;
CREATE TABLE movie(
	movie_id VARCHAR ( 250 )PRIMARY KEY,
	title VARCHAR ( 250 ) NOT NULL,
	duration int,
	released timestamp
	);