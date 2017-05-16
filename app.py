#!flask/bin/python

'''
DATABASE connection
       Username: openconfirm
       Password: POSTGRES_PASSWORD   open-confirm-conf.db.pswd
  Database Name: openconfirm
 Connection URL: postgresql://postgresql:5432/
'''

from flask import Flask
from flask.ext.restful import Api, Resource
import pgdb
import os

hostname = 'postgresql'
username = 'openconfirm'
password = os.environ['POSTGRES_PASSWORD']
database = 'openconfirm'


app = Flask(__name__)

@app.route('/')
def index():
	testDBConnection()
	return "Hello, World!"


def testDBConnection():
	print 'try db connection....',hostname,username,password,database
	myConnection = pgdb.connect( host=hostname, user=username, password=password, dbname=database )
	myConnection.close()
	print 'DB Connection ok'

if __name__ == '__main__':
	app.run('0.0.0.0',8080)
