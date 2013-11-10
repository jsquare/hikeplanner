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

#### Install Geometry libraries (GDAL, GEOS, PROJ.4)
- $ sudo apt-get install binutils libproj-dev gdal-bin

#### Install PostgreSQL 9.1
- $ sudo apt-get install postgresql-9.1 postgresql-9.1-postgis postgresql-server-dev-9.1
- $ sudo apt-get install python-psycopg2

#### Install PostGIS 2.0
PostGIS 2.0 is a geometry extension for PostgreSQL. For us, PostGIS 2.0 did not install properly using just apt-get. To properly install PostGIS 2.0:

- $ sudo apt-get install python-software-properties
- $ sudo apt-add-repository ppa:ubuntugis/ppa
- $ sudo apt-get update
- $ sudo apt-get install postgresql-9.1-postgis

#### Set up PostgreSQL database with PostGIS extension
 
When PostgreSQL is installed, it creates a user called 'postgres', which is used to access all postgres databases. To create the spatial database, switch to postgres user, create a PostgreSQl database, open it in the psql terminal and add the postgis extension

- $ su postgres
- $ createdb <db name>
- $ psql <db name>
- postgres=# CREATE EXTENSION postgis;

Then create a *database* account named postgres. (It *must* be named postgres so it matches the system user account.) The settings.py in the Django project will need to match the database name, user, and pwd.

- $ su postgres
- postgres=# \password postgres
- Enter new password: 
- Enter it again: 
- postgres=# \q

#### Checkout code using Git

Install git and use it to checkout the hikeplanner code

- $ sudo apt-get install git-core
- $ git clone https://github.com/jsquare/hikeplanner


Windows
-------
After about five hours of trying to get the various libraries installed and working together on Windows, I gave up an used a VirtualBox to boot Ubuntu.

Follow these instructions to install virtualbox on your windows machine and boot it into Ubuntu: [VirtualBox + Ubuntu](http://www.psychocats.net/ubuntu/virtualbox). Then follow Ubuntu instructions above. 

- I got VirtualBox from [here](http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html#vbox)
- I got Ubuntu 12.04 .iso from [here](http://www.ubuntu.com/download/desktop)