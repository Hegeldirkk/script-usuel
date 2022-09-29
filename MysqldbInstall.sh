#!/usr/bin/env bash

##############################################
#   					     #
#  Install MySQLdb module version 2.0.x	     #
#	and SQL Alchemy v 1.4.x              #
#       ORM Python(Ikary Script)	     #
#					     #
# For installing MySQLdb, you need to have   #
# MySQL installed: How to install MySQL 8.0  #
# in Ubuntu 20.04			     #
##############################################

sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient

sudo pip3 install SQLAlchemy
