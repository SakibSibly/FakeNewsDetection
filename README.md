# Check the authencity of any news that are circulating at your vicinity

With the rapid using of technology the spreading of false news has become unavoidable in day to day life. This project aims to provide user with tools that will come in handy to check and varify the authenticity of any news.

## How to use the project locally

clone the project

```sh
git clone https://github.com/SakibSibly/FakeNewsDetection.git
```

Move to the project directory

```sh
cd FakeNewsDetection
```

Install the requirements

```sh
pip install -r requirements.txt
```

Make migrations and apply the migration files

```sh
python manage.py makemigrations
python manage.py migrate
```

Run the project

```sh
python manage.py runserver
```

It should output something like this

```txt
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
MM DD, YYYY - HH:MM:SS
Django version 5.X.X, using settings 'FakeNewsDetection.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open the link `http://127.0.0.1:8000/` in the browser.

### Prerequisites

- Python 3.10 or higher is recommended to run the project.
- Setting up the required `.env` file. To know more about the `.env` variables contact the developers
