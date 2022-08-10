# Fastapi-boilerplate
A simple framework

## prerequisite
1. python 3.10
1. postgresql 12 or docker-compose


## How to install
1. clone this repo `git clone https://github.com/rizkydarmadi/Fastapi-boilerplate.git`
1. create virtual environtment `python -m venv env`
1. add package `pip install -r requirements.txt`
1. set up database:
    - the simple way database config
      - make sure docker and docker compose already installed in your local machine
      - and run command `sudo docker-compose up`
      - change config.json.copy to config.json and set up you config your database database
    - if you have postgresql database in local machine 
      - create database
      - change config.json.copy to config.json and set up you config your database database
    
