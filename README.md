# Django-Rest-Api

This is a light weight application that manages Post and Vote api. Client can access resources via HTTP in JSON format. Request methods include GET, POST, PUT, PATCH and DELETE. Built in DRF TokenAuthentication classes was used depending on whether an endpoint require to be authenticated


## Features

 - **RESTful Api** - It follows Rest architectural style
 - **User registration - POST** - Receive a Json data, parse it and return user Token
 - **User login API - POST** - Receive a Json data(Userna & Password), Token specify in headers
 - **View PostList - GET** - User needs to be authenticated -H 'Authorization: Token'
 - **Update own POST- PUT, PATCH** - User must own Post, be authenticated or read only
 - **Create Vote - POST** - User must be authenticated
 - **Delete own POST- DELETE** - User must own Post, be authenticated or read only


### How to Set up the application

Open terminal and use git clone command to download the remote Github repository to your computer

```bash
  1. git clone https://github.com/Jibril14/Django-Rest-Api.git
  2. cd Django-Rest-Api
  3. python3 -m venv venv
  4. venv/bin/activate
  5. pip3 install -r requirements.txt
  6. Generate a new secret key
  7. python manage.py makemigrations
  8. python manage.py migrate
  9. python manage.py createsuperuser
  10. python manage.py runserver
  11. use command line or api client to test the different endpoints
  12. or remove permision classes in views to allow for testing on the DRF web browsable API
```


## Playing with endpoints Locally

Run below codes in the terminal or use any api client such as postman.

```bash
$ cmd
```

User Registration (sign up):
```bash
curl  -X "POST" -d  "{\"username\": \"JohnDoe\", \"password\":\"poiuytrewq\"}" -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/user/register/

```

 return something like:
```bash
HTTP/1.1 201 Created
...
{"token": "c75df26a23927e7f7b456b5b25f688c910c41346"}
```

User Login (sign in):
```bash
curl  -X "POST" -d  "{\"username\": \"JohnDoe\", \"password\":\"poiuytrewq\"}" -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/user/login/


```

 return something like:
```bash
HTTP/1.1 201 Created
...
{"token": "c75df26a23927e7f7b456b5b25f688c910c41346"}


View all Posts (Needs to be signed in):
```bash
curl  http://127.0.0.1:8000/api/all-posts/ -H 'Authorization: Token 5ca989e6b40a98117da304f2b188c84dd7a33527

```
 return something like:
```bash
HTTP/1.1 201 Created
...
[{"id":1,"title":"Lorem ipsum sitdolo ame","url":"http://google.com/","poster":"John", "createdon":"2021-01-09T08:26:34.536046Z","all_votes":2},{"id":2,"title":"Lorem ipsum sitdolo ame","url":"http://garrypoter.com/","poster":"Doe","createdon":"2021-01-09T08:46:34.536046Z","all_votes":0}, }]

```
