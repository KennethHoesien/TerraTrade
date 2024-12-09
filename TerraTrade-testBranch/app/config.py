# change this file according to your MySQl
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Chunniboy123#'
MYSQL_DB = 'soilmarket'

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
SQLALCHEMY_TRACK_MODIFICATION = False