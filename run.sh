# running this bash script will create the website locally for you and you can access the content

# first, install pip and install the dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# run the server and you are good to go
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



