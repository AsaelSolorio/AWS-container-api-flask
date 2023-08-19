install:
		pip3 install --upgrade pip 
		pip3 install -r requirements.txt
		pip3 install psycopg-binary
		python -m pip install virtualenv
		pip3 install SQLAlchemy
		pip3 install python-dotenv
		pip3 install flask-cors
		pip3 install python-decouple
		sudo apk add gcc python3-dev
	    apk add --no-cache python3-dev
	    pip3 install Flask
	    apk add postgresql postgresql-contrib


lint:
		pylint --disable=R,C app.py
	
format:
		black *.py