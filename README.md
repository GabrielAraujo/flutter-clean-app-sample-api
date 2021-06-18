# flutter-clean-app-sample-api
Flutter Clean App Sample API

# Description
This is a simple python project using the Flask to create REST endpoints. It also uses serverless framework to automate AWS infrastructure creation such as Lambda, Api Gateway and Dynamodb.

This project exposes a `/seed` path with a `GET` method and a `/seed/validate` path with a `POST` method.
The `/seed` get method is responsible to create a new randon seed and store it on dynamodb and the `/seed/validate` post method is responsible to validate if the informed seed is valid or not.

# Local Execution
Nodejs, python3 and java are needed in order to execute locally. Don't forget to also install virtualenv using pip.
`npm install`
`pip install virtualenv`
`virtualenv venv --python=python3`
`source venv/bin/activate`
`pip install flask`
`pip install boto3`
`npm install --save-dev serverless-dynamodb-local`
`sls dynamodb install`

The just start dynamodb and wsgi.
terminal 1 `sls dynamodb start`
terminal 2 `sls wsgi serve`

# Considerations
This is a really simple project that is not following the SOLID principles and was created with the sole purpose of providing a backend for the app as fast as possible.
