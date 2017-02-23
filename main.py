from flask import Flask, url_for, render_template, request, redirect
from flask import session, make_response
from flask.ext.triangle import Triangle
from flask_jsglue import JSGlue
from GameDatabase import Base, Users, Matches
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import string, random
from CookieMaker import *
from PassHashing import *

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
	session_token = check_cookie(request.cookies.get('session_token'))

	if session_token and session_token == session['session_token']:
		user = database.query(Users).filter(Users.username == session['username']).one()
		return render_template('playerDash.html', user=user.client_side_user_data())
	else:
		return render_template('loginSignup.html')

@app.route('/login', methods=['POST'])
def login():

	username = request.form.get('username')
	password = request.form.get('password')

	if username and password:
		try:
			user = database.query(Users).filter(Users.username == username).one()
		except:
			return render_template('loginSignup.html', login_error='Username not found...')

		if user.passHash == hash_pass(password, user.salt):
			# create and set session_token
			session['session_token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
			session['username'] = user.username
			# return user info and session_token
			resp = make_response(render_template('playerDash.html', user=user.client_side_user_data()))
			resp.set_cookie('session_token', make_cookie(session['session_token']))
			resp.set_cookie('username', make_cookie(session['username']))
			resp.set_cookie('xp', make_cookie(user.XP))
			return resp
		else:
			return render_template('loginSignup.html', login_error='Invalid Password.')
	else:
		return render_template('loginSignup.html', login_error='Please Enter Both Username and Password...')


@app.route('/signup', methods=['POST'])
def signup():
	try:
		firstName = request.form.get('FirstName')
		lastName = request.form.get('LastName')
		email = request.form.get('email')
		username = request.form.get('username')
		password = request.form.get('password')
	except:
		return render_template('loginSignup.html', signup_error='All fields are required.')

	try:
		user = database.query(Users).filter(Users.username == username).one()
	except:
		user = None

	if user:
		return render_template('loginSignup.html', signup_error='User Already Exists.')
	else:
		try:
			salt = make_salt()
			newUser = Users(
				username=username,
				firstName=firstName, 
				lastName = lastName,
				email=email,
				passHash=hash_pass(password, salt),
				salt=salt
				)
			database.add(newUser)
			database.commit()
		except:
			return render_template('loginSignup.html', signup_error='Error creating new user. Please try again.')

	session['session_token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	session['username'] = newUser.username

	resp = make_response(render_template('playerDash.html', user=user.client_side_user_data()))
	resp.set_cookie('session_token', make_cookie(session['session_token']))
	return resp


@app.route('/logout', methods=['POST'])
def logout():
	pass


if __name__ == '__main__':
	app.secret_key = "secret_key12846214dyjkehyishjtidyh"
	app.run(debug=True, host='127.0.0.1', port=5000)