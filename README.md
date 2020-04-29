# Load Json

This application uploaded on [Github](https://github.com/hasansajedi/loadJSON).

This is a simple application to load json file and then save all of them in database and after that show as presentable data. 

## Installation
To build, test and deploy application please, run bash.sh file in root directory:

```bash
> ./script.sh
```
or
```bash
> python3.8 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
> source .envrc
> python ./manage.py migrate
> python ./manage.py test
> pipenv run python manage.py runserver 
```
or, You can use CircleCI to build, test and deploy the project. The config file is in '.circleci' folder.

## Features

1. **Login**: You can reach all urls when you authenticated.
2. **Load file**: Load Json file and then check item is not present in table and save instance in table.
3. **report**: View all instances of Email as a HTML.

## Usage

> To access **admin** page or **login**, http://127.0.0.1:8000/admin .
> 
> To access load file ui, http://127.0.0.1:8000/ .
> 
> To access all data, http://127.0.0.1:8000/report . 


To access admin panel you can use below information:
* Username: admin
* Password: qazWSX@123