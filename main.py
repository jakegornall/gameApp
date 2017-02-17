from flask import Flask, url_for, render_template, request, redirect
from flask.ext.triangle import Triangle
from flask_jsglue import JSGlue
from GameDatabase import Base, Users, Matches
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///GameDatabase')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
database = DBSession()

app = Flask(__name__)
jsglue = JSGlue(app)
Triangle(app)


@app.route('/', methods=['GET'])
def main():
	return render_template('loginSignup.html')

@app.route('/login', methods=['POST'])
def login():
	username = request.get('username')
	password = request.get('password')

	try:
		user = database.query(Users).filter(Users.username == username).one()
	except:
		return jsonify(success=False, message='username not found...')



@app.route('/signup', methods=['POST'])
def signup():
	firstName = request.get('FirstName')
	lastName = request.get('LastName')
	email = request.get('email')
	username = request.get('username')
	password = request.get('password')



if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)