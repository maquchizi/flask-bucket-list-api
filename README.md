# BucketList Application API

Flask API for a bucket list service

## Specifications
Specification for the API is shown below.

This service implements Token Based Authentication for the API such that some methods are not accessible to unauthenticated users. Access control mapping is also listed below.


| EndPoint                            | Allowed Methods  | Functionality                                            | Requires Token |
|-------------------------------------|------------------|----------------------------------------------------------|----------------|
| `/auth/login`                       | POST             | Logs a user in                                           | No             |
| `/auth/register`                    | POST             | Register a user                                          | No             |
| `/bucketlists`                      | POST, GET        | Create and retrieve all bucket lists                     | Yes            |
| `/bucketlists/<id>`                 | GET, PUT, DELETE | Retrieve, update and delete a single bucket list         | Yes            |
| `/bucketlists/<id>/items`           | POST             | Create a new item in bucket list                         | Yes            |
| `/bucketlists/<id>/items/<item_id>` | PUT, DELETE      | Edit, delete an item in a bucket list                    | Yes            |

## Installation

Clone the repo from github
`git clone git@github.com:maquchizi/flask-bucket-list-api.git`

Change directory into package
`cd flask-bucket-list-api`

Install dependencies
`pip install requirements.txt`

To run the app, navigate to the project folder and run `python index.py`

You can access the app at `http://127.0.0.1:5000`

## Use
To interact with the API, send it HTTP requests using your favourite tool (cURL, Postman, HTTP etc)

Note that all requests *MUST* be of the Content-Type `application/json`

### Registration
To register, send a POST request to `/auth/register` with the `forename`, `surname`, `email` and `password` of the new user

HTTP
```
POST /auth/register HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache

{"forename":"Salt","surname":"Bae","password":"superawesomepassword","email":"salt.bae@example.com"}

```

cURL
```
curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" 
-d '{"forename":"Salt","surname":"Bae","password":"superawesomepassword","email":"salt.bae@example.com"}' 
"http://127.0.0.1:5000/auth/register"
```

Postman
![alt text](http://i.imgur.com/6yncdNq.png)

### Logging In
To log in, send a POST request to `auth/login` with the `email` and `password`

On successful log in, the API will return a JSON object with an `access_token`. Use this token in subsequent requests to routes that require a token

HTTP
```
POST /auth/login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache

{"email":"salt.bae@example.com","password":"superawesomepassword"}
```

cURL
```
curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache"
-d '{"email":"salt.bae@example.com","password":"superawesomepassword"}'
"http://127.0.0.1:5000/auth/login"
```

Postman
![alt text](http://i.imgur.com/CqbTVi4.png)

### Sending Resource Requests
Sending resource requests is just like the two examples above only that you have to include an `Authorization` header.

The format of the Authorization header is `Authorization: JWT the-access-toke-goes-here`

See the example below:

#### Getting all bucketlists

HTTP
```
GET /bucketlists HTTP/1.1
Host: 127.0.0.1:5000
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MzA5LCJpYXQiOjE0ODQyMTIxOTksIm5iZiI6MTQ4NDIxMjE5OSwiZXhwIjoxNDg0MjE1MTk5fQ._QC2nSgHDYilIY5jh6MIbhApiTAzjFmF4sCmCSYTch8
Cache-Control: no-cache
```

cURL
```
curl -X GET 
-H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MzA5LCJpYXQiOjE0ODQyMTIxOTksIm5iZiI6MTQ4NDIxMjE5OSwiZXhwIjoxNDg0MjE1MTk5fQ._QC2nSgHDYilIY5jh6MIbhApiTAzjFmF4sCmCSYTch8"
-H "Cache-Control: no-cache"
"http://127.0.0.1:5000/bucketlists"
```

Postman
![alt text](http://i.imgur.com/kztWCK2.png)


## Dependencies

- Flask
- Flask-RESTful
- Flask-JWT
- Flask-SQLAlchemy

## Testing
Use nosetests to run tests (with coverage) like this: `nosetests --with-coverage --cover-package=bucketlist`
