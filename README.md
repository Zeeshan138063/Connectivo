# Connectivo
Connectivo Code Challenge

# Features #
* Django 2.0
* Uses PIP3 for python package management
* Postgres for database with Pyscopg2

# Pre requisites #

* Install Python 3.7 if not previously installed (for ubuntu 18.04).  
(furher info found here: https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
```  
* Install PostgreSQL if not previously installed.  
```
$ sudo apt-get install postgresql postgresql-contrib
$ sudo apt-get install libpq-dev
```

* Install Python Package Index Tool pip3  
```
$ sudo apt-get install -y python3-pip `  

* Install virtual environment wrapper  
(further info found here: [http://virtualenvwrapper.readthedocs.io/en/latest/install.html](http://virtualenvwrapper.readthedocs.io/en/latest/install.html))
`$ pip3 install virtualenv `  

```
* Create directory for development, name it anything.
```
$ mkdir connectivo
$ cd connectivo
```

* When inside the directory create virtual environment, called connectivo_venv in example. Then activate the environment.  
```
$ virtualenv --python=python3.7 connectivo_venv
$ source connectivo_venv/bin/activate
```  


# Installation #

1. Enter created directory for development (activating created virtual development environment) where project files will be stored.  
` (connectivo_venv) $ cd <directory name/location> `
2. Clone branch from repository.  
` (connectivo_venv) $ git clone <remote repository name> `

Example:
` (connectivo_venv) $ git clone https://github.com/Zeeshan138063/connectivo.git

At this moment last actual changes in project lives in `develop` branch. If you want checkout to that branch.  
` (connectivo_venv) $ git checkout develop`

3. Install requirements  
`sh scripts/install_requirements.sh`

3. Set up PostgreSQL  
Switch over to the postgres account by typing:  
`$ sudo -i -u postgres`   

You can now access a Postgres prompt immediately by typing:  
```
$ psql  
postgres=# ALTER USER postgres WITH ENCRYPTED PASSWORD SET_PASSWD;

postgres=# CREATE DATABASE sirmaya;

postgres=# CREATE ROLE ROLE_NAME WITH ENCRYPTED PASSWORD SET_PASSWD;

postgres=# GRANT ALL PRIVILEGES ON DATABASE sirmaya TO ROLE_NAME;

postgres=# ALTER ROLE ROLE_NAME WITH LOGIN;
```  



5. Set the shell environment variables, Write the following commands in bash Shell
```
export PG_DB_NAME='sirmaya'
export PG_USER=ROLE_NAME 
export PG_PASSWD=SET_PASSWE  
export PG_HOST='localhost'  
export SECRET_KEY='Your_secret_key'   
export DJANGO_SETTINGS_MODULE=sirmaya.settings.local
export HOST_URL='http://127.0.0.1:8000'
```


6. RUN Admin site migrations and other django app migrations.  
`python manage.py migrate`

7. Run the server
`python manage.py runserver`

This should run the server and give an IP address that when entered into a web browser will bring up the development server. Address of the server is your IP address
most likely http://127.0.0.1:8000/.
