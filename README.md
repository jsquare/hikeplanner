hikeplanner
===========

Find a hike you'll like!


Dev Machine Setup
=================

Ubuntu 12.04
------------
This is what we did, and it worked.

#### Install Python 2.7

- Ubuntu 12.04 comes with Python 2.7.3

#### Checkout code using Git

Install git and use it to checkout the hikeplanner code

- $ sudo apt-get install git-core
- $ git clone https://github.com/jsquare/hikeplanner

#### Install system dependencies (GDAL, GEOS, PROJ.4, PostgreSQL, PostGIS)
for us, PostGIS 2.0 did not install properly using just apt-get. To properly install PostGIS 2.0 we needed to add this repository:
- $ sudo apt-add-repository ppa:ubuntugis/ppa
- $ sudo apt-get update
in the hikeplanner/ repository root:
- $ cat requirements.system | xargs sudo apt-get -y install

#### Install Python dependencies
in the hikeplanner/ repository root:
- $ sudo pip install -r requirements.txt

#### Set up PostgreSQL database with PostGIS extension
 
When PostgreSQL is installed, it creates a user called 'postgres', which is used to access all postgres databases. To create the spatial database, switch to postgres user, create a PostgreSQl database, open it in the psql terminal and add the postgis extension

- $ sudo su - postgres
- $ createdb hikeplanner
- $ psql hikeplanner
- hikeplanner=# CREATE EXTENSION postgis;

Then create a *database* account named postgres. (It *must* be named postgres so it matches the system user account.) The settings.py in the Django project will need to match the database name, user, and pwd.

- $ sudo su - postgres
- $ psql
- postgres=# \password postgres
- Enter new password: (type "hiketime")
- Enter it again: (type "hiketime")
- postgres=# \q

#### Do the django dance
in the hikeplanner/ repository root:
- $ sudo su - postgres
- $ python manage.py syncdb
- $ python manage.py runserver
- visit http://localhost:8000 in a browser and you're good to go!

Windows
-------
After about five hours of trying to get the various libraries installed and working together on Windows, we finally figured out a reliable solution:

1. Install virtualbox on your windows machine and boot it into Ubuntu: [VirtualBox + Ubuntu](http://www.psychocats.net/ubuntu/virtualbox). 

    - I got VirtualBox from [here](http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#vbox)
    - I got Ubuntu 12.04 .iso from [here](http://www.ubuntu.com/download/desktop)

2. Follow Ubuntu instructions above. 
