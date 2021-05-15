# dsi202_final_project Installation guise
Represent by Quackkkkk

1.Create a new directory for project

    1.1 mkdir 'project'
    
    1.2 use 'project' as a working directory

2.Create a new Python virtual environment and install Django web framework

    2.1 conda create -n dsi202_2021 python=3.6
    
    2.2 conda activate dsi202_2021
    
    2.3 conda install django=2.2

3. Create Django project called “myproject” and runserver

    3.1 django-admin startproject myproject
   
    3.2 cd myproject
    
    3.3 python manage.py runserver 127.0.0.1:8008
    
    3.4 Go to browser and enter url
    
        3.4.1 http://127.0.0.1:8008/
        
        5.4.2 http://localhost:8008/

4. python manage.py startapp myapp

5. Create a super user account

    5.1 python manage.py makemigrations
   
    5.2 python manage.py migrate
    
    5.3 python manage.py createsuperuser

6. Edit settings.py with vscode

    INSTALLED_APPS = 
        
        [ . . . ,

        'myapp',

        . . . ]

7. Edit Database, Frontend and Backend with vscode

8. Install more packages for edit our website e.g.

        pip install social-auth-app-django

        pip install django-javascript-settings

        pip install django-bootstrap4

        pip install django-filter

        pip install django-bootstrap-form

        etc.
