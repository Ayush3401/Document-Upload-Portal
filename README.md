# Document-Upload-Portal

# Introduction

The document upload portal is a file sharing platform where one can upload and share the files with other users.
The person needs to register themselves by making an account.
The person can then use it for storing, sharing and working together on multiple files.

### Main features

* Supports file and folder sharing with other users

* Supports multi-level folder hierarchy

* Live updation of shared files/folders.

# Usage

First clone the repository from Github.
Activate the virtualenv (if any) for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
You can access the default local server at http://127.0.0.1:8000/
