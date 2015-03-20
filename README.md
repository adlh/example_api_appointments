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

    pip install -r requirements.txt

2. Install bower:
    
    npm install -g bower

3. Install assets
    
    npm install
    bower install

4. Setup the database and install fixtures

    make all

5. Run the server

    ./manage.py runserver

