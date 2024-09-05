# django-vehicles-api

This platform aims to permit companies register their vehicles and extract them via an api.

## Instantiate the project

There are several ways to instantiate the project on a computer:
* python virtual environment
* docker

### Python virtual environment 

The following commands create a python virtual environment at the same level as the project. Then the two directory must be contained by another directory.

1. Creation of the encompassing directory. Name it according the name of the future git repository name.

> mkdir `project_name` \
cd `project_name` 

2. Fetch the *django-base* repository and name it *web*.

> git clone git@github.com:AlexandreAnsiau/django-base.git web \
 cd web

3. The *.git* repository must be deleted because the django-base must not be edited. 

> rm -rf .git

If the project must be gitted, the command **git init** must be done in the *web* repository. 

4. Creation of th python virtual environment. The current working directory is web. The python virtual environment must be generated at the same level as this last one.

> cd ../ \
> python -m venv env

5. Activation of the python virtual environment.

> source env/bin/activate

## Installation:

For the installation, you may follow the process described below or do the next command:

> python init.py

This command will automatically execute the following ones.

### 1. .env completion:

> cp .env.exemple .env 

### 2. Installation of the python dependencies

> pip install -r requirements.txt 

It must be done in a python virtual environment to install globally all the dependencies.

### 3. Installation of the npm packages

**The npm install must not be used**. It will try to install and upload as much as possible all the packages indicated in the package.json. That can create some problems. **npm ci** used the version indicated in the package-lock.json which is placed in the *frontend* directory.

> cd frontend \
npm ci \
npm run build

### 4. initiate the database

The database mentioned in the .env file must be created.

The tables of the django framework must be generated.

> cd ../ \
python manage.py migrate

### 5. Verification if the project displays pages. 

First at all, the django server must be turned on.

> python manage.py runserver

Then the content of the url 127.0.0.1:8000/test/ should be displayed in your browser.