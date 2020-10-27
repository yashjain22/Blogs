## Environment Setup

1. install python 3.7.9 from [here](https://www.python.org/downloads/)
2. install Postgresql from [here](https://www.postgresql.org/download/)
3. Setup postgresql


## Installation

1. setup virtualenv by running venv [env_name] in project dir
2. activate virtual env by navigating to [env_name]/Scripts and run activate.bat
3. after virtual env is activated install the required dependencies by running `pip install -r      requirements.txt` in project_dir
4. navigate to Blogs\Blog\myproj\settings.py and change database settings to appropriate user,password,host and port,add secret key
5. create migrations by `python manage.py makemgrations`
6. apply migrations by `python manage.py migrate`
7. runserver using `python manage.py runserver`


## API Documentation

1. `api/blog/register` [POST]
    
    |Parameter|Required/Optional|Data type|
    |-------|----------------- |---------|
    |Username|         Required|   string|
    |Password1|        Required|   string|
    |Password2|        Required|   string|

2. `api/blog/login` [POST]
    
    |Parameter|Required/Optional|Data type|
    |-------|----------------- |---------|
    |Username|         Required|   string|
    |Password|         Required|   string|


3. `api/blog/logout` [POST]


4. `api/blog/createpost` [POST]

    |Parameter|Required/Optional|Data type|
    |-------|----------------- |---------|
    |title  |          Required|   string|
    |title_tag|        Required|   string|
    |body|             Required|   string|

5. `api/blog/fetchallpost` [GET]
    |Parameter|Required/Optional|Data type|
    |-------|----------------- |---------|
    |orderbydate  |          Optional|   integer 0 or 1|

6. `api/blog/fetchpostbyid` [GET]
    |Parameter|Required/Optional|Data type|
    |-------|----------------- |---------|
    |postid  |          Required|   integer|


## Other

If running on postman make sure to clear cookie appropriately
The code can also be accessed here https://github.com/yashjain22/Blogs
