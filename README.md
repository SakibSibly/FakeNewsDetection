# Check the authencity of any news that are circulating at your vicinity

With the rapid using of technology the spreading of false news has become unavoidable in day to day life. This project aims to provide user with tools that will come in handy to check and varify the authenticity of any news.

## How to use the project locally:

- Python 3.9 or higher is recommended to run the project. 

- Move to the project directory and install the requirements for the project in a virtual environment:
```
pip install -r requirements.txt
```
- Run the server in local host:
```
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py migrate
python manage.py runserver
```
