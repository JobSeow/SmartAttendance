import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Chicken101@localhost/SmartAttendance'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

#     POSTGRES = {
#     'user': 'postgres',
#     'pw': 'Chicken101',
#     'db': 'SmartAttendance',
#     'host': 'localhost',
#     'port': '5432'
#     }

#     DEBUG = True


#     SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#     SQLALCHEMY_TRACK_MODIFICATIONS = False