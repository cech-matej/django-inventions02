# Web application about inventions using Django
## Setup
The first thing to do is to clone the repository:

```
$ git clone https://github.com/cech-matej/django-inventions.git
$ cd django-inventions
```

Activate the virtualenv for your project.

Install project dependencies:
```
$ pip install -r requirements.txt
```

Then simply apply the migrations:
```
$ python manage.py migrate
```

You can now run the development server:
```
$ python manage.py runserver
```

## Superuser
Creating an admin user
```
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```
Username: admin
```

You will then be prompted for your desired email address:
```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```

### Start the development server
The Django admin site is activated by default.
```
$ python manage.py runserver
```
Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:
![login page](/img/login.JPG)

### Active admin users
Username | Password
-------- | --------
matej | matej

### Other users
Username | Password
-------- | --------
editor | matej1234
správce | matej1234