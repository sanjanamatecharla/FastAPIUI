# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "mysql://MatecharlaSreedharSanjana:cK592&TJw8ww@host:3306/mysql"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# print("creating base")

# import mysql.connector
# mydb = mysql.connector.connect(
#     host="10.50.2.223",
#     user="MatecharlaSreedharSanjana",
#     password="cK592&TJw8ww",
#     database="mysql"
# )


from peewee import *
user = 'MatecharlaSreedharSanjana'
password = 'cK592&TJw8ww'
db_name = 'infinitylearn'
conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='10.50.2.223'
)


