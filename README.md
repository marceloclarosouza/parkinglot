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

http://127.0.0.1:8000/feedback/ --Feedback form

http://127.0.0.1:8000/feedback-api/ --GET

http://127.0.0.1:8000/feedback-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/client-api/ --GET

http://127.0.0.1:8000/client-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/service-api/ --GET

http://127.0.0.1:8000/service-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/order-api/ --GET

http://127.0.0.1:8000/order-api/id/ --POST, PATCH, DELETE