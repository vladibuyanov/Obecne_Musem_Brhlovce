# [Web page for local museum in Brhlovce](https://web-production-0449.up.railway.app/)

## Tech
- Python
- [Django](https://www.djangoproject.com/)

## Start App

To run the application, you need to add environment variables.

You also need to install dependencies:

```commandline
pip install -r requirements.txt
```

Once the dependencies have been installed, navigate to the 
root directory of the project and run the following command:

```commandline
python manage.py runserver
```

This will start the development server and the application can be 
accessed at http://localhost:8000/.

The application also includes an admin panel that can be accessed
by navigating to http://localhost:8000/admin/ and logging in with 
the provided credentials. The admin panel allows for easy management of the posts, links and files.

## Start Tests

To run tests, use the command

```commandline
python manage.py test
```
