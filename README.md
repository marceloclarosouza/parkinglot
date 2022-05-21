# Parking Lot
Simple application to manage a parking lot/car washing

## Open the terminal an go to the directory of your application
Ex: /home/project/parkinglot

## Environment
pip install -r requirements.txt

## Migration
python manage.py migrate

## Create super user
python manage.py create superuser

## Run the application
python manage.py runserver


## On the browser
http://127.0.0.1:8000/admin/ --Admin pannel

http://127.0.0.1:8000/feedback/  --Feedback form

http://127.0.0.1:8000/feedback-api/

http://127.0.0.1:8000/feedback-api/<int:id>/

http://127.0.0.1:8000/client-api/

http://127.0.0.1:8000/client-api/<int:id>/

http://127.0.0.1:8000/service-api/

http://127.0.0.1:8000/service-api/<int:id>/

http://127.0.0.1:8000/order-api/

http://127.0.0.1:8000/order-api/<int:id>/