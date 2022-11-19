# skmadridista-django_git_exam
# Git repo setup complete.
# Library-Management-App.

Library app is a full featured Library app. You have to register in this app to view the Books and read them. If you already registered you can view the list of books available to read . Only the Librarian/Admin of the library can add book , edit book, update book, delete book. 

<h1>Getting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h2>Prerequisites</h2>
<code>python== 3.5 or up and django==4.0 or up</code>

<h2>To migrate the database open terminal in project directory and type</h2>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code>

<h2>To use admin panel you need to create superuser using this command </h2>
<code>python manage.py createsuperuser</code>

<h2> To run the program in local server use the following command </h2>
<code>python manage.py runserver</code>

<p>Then go to http://127.0.0.1:8000 in your browser</p>