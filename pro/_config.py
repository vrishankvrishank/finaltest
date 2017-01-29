
import os
basedir=os.path.abspath(os.path.dirname(__file__))
#abspath returns absolute path of a path like Desktop/python/project-----
# dirname returns the python folder if the fileas are like Desktop/python /project and I ask for dirname(project) in other words top of the folder

DATABASE='flasktaskr.db'
USERNAME='vrishank'
PASSWORD='vrishank'
WTF_CSRF_ENABLED = True


SECRET_KEY='myprecious'

DATABASE_PATH=os.path.join(basedir,DATABASE)
#for joining

