from sqlalchemy import create_engine

HBNB_MYSQL_USER = 'hbnb_dev'
HBNB_MYSQL_PWD = 'hbnb_dev_pwd'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'hbnb_dev_db'

engine = create_engine(f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}')

try:
    connection = engine.connect()
    print("Connection to the database was successful!")
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")

