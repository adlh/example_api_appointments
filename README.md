example-api-appointments
======================

This is an example web api to demostrate the integration of Django (with the
Django REST framework) and AngularJS to build an application for people to
schedule appointments.

This project was strongly based on Kevin Stone's tutorial:
http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html

#DEPENDENCIES:

This project was written under a virtualenv using python 3.3 and the
requirements listed on the `requirements.txt` file

Also, to get this project running, you'll need npm to install js dependencies.


#INSTALLATION:

1. Setup a virtualenv and install the requirements:

        mkvirtualenv --python=/usr/bin/python3.3 --no-site-packages my_api
        pip install -r requirements.txt

2. Install bower:
    
        npm install -g bower

    or if you don't have root access, install as user

        npm install bower


3. Install assets
    
        npm install
        bower install

    if you didn't installed bower globally, then you'll have to run bower from
        the .bin folder like this, or add a link to your bin folder.
        
        ./node_modules/.bin/bower install

4. Setup the database and install fixtures

        make all

5. Run the server

        ./manage.py runserver

6. The URL to enter the admin is

        /admin

    Login credentials are admin/pass

