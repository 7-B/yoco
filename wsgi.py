# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
from app import app

if __name__ == "__main__": app.run()

# add your project directory to the sys.path
# project_home = u'/home/Crispiness/project-YOCO_WEB'
# if project_home not in sys.path:
#     sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from app import app as application  # noqa
