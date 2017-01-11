# BucketList Application API

Flask API for a bucket list service

## Specifications
Specification for the API is shown below.

This service implements Token Based Authentication for the API such that some methods are not accessible to unauthenticated users. Access control mapping is also listed below.


| EndPoint                            | Allowed Methods  | Functionality                                    | Requires Token |
|-------------------------------------|------------------|--------------------------------------------------|----------------|
| `/auth/login`                       | POST             | Logs a user in                                   | No             |
| `/auth/register`                    | POST             | Register a user                                  | No             |
| `/bucketlists`                      | POST, GET        | Create a retrieve all bucket lists               | Yes            |
| `/bucketlists/<id>`                 | GET, PUT, DELETE | Retrieve, update and delete a single bucket list | Yes            |
| `/bucketlists/<id>/items`           | POST             | Create a new item in bucket list                 | Yes            |
| `/bucketlists/<id>/items/<item_id>` | PUT, DELETE      | Delete an item in a bucket list                  | Yes            |

## Installation

Clone the repo from github
`git clone git@github.com:maquchizi/flask-bucket-list-api.git`

Change directory into package
`cd flask-bucket-list-api`

Install dependencies
`pip install requirements.txt`

## Dependencies
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy

## Testing
Use nosetests to run tests (with coverage) like this: `nosetests --with-coverage --cover-package=bucketlist`

## Usage
