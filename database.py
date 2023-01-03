# from sqlalchemy import create_engine,MetaData
# engine=create_engine("mysql+pymysql://MatecharlaSreedharSanjana:cK592&TJw8ww@10.50.2.223/infinitylearn")
# meta=MetaData()
# conn=engine.connect()
#

from fastapi import FastAPI
from peewee import MySQLDatabase, Model, CharField

# Connect to the MySQL database
db = MySQLDatabase('infinitylearn', host='10.50.2.223', user='MatecharlaSreedharSanjana', password='cK592&TJw8ww')

# Define a model to represent a table in the database
class User(Model):
    username = CharField()










# import mysql.connector
# conn = mysql.connector.connect(
#     host="10.50.2.223",
#     user="MatecharlaSreedharSanjana",
#     password="cK592&TJw8ww",
#     database="mysql"
# )
#
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
#
# #mysql_engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format('root','root','localhost','3306','localhost'))
# mysql_engine = create_engine("mysql://MatecharlaSreedharSanjana:cK592&TJw8ww@10.50.2.223/infinitylearn")
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=mysql_engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
#
# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     import models.RoleModel
#     Base.metadata.create_all(bind=mysql_engine)
#

# from peewee import *
# user = 'MatecharlaSreedharSanjana'
# password = 'cK592&TJw8ww'
# db_name = 'infinitylearn'
# conn = MySQLDatabase(
#     db_name, user=user,
#     password=password,
#     host='10.50.2.223'
# )