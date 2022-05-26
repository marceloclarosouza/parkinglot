# Parking Lot
Simple application to manage a parking lot/car washing

# Python versiom
python==3.10 

## Open the terminal an go to the directory of your application
Ex: /home/project/parkinglot

## Environment
pip install -r requirements.txt

## Migration
python manage.py migrate

## Create super user
python manage.py createsuperuser

## Run the application
python manage.py runserver


## On the browser
http://127.0.0.1:8000/admin/ --Admin pannel

http://127.0.0.1:8000/services/feedback/ --Feedback form

http://127.0.0.1:8000/services/feedback-api/ --GET

http://127.0.0.1:8000/services/feedback-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/services/client-api/ --GET

http://127.0.0.1:8000/services/client-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/services/service-api/ --GET

http://127.0.0.1:8000/services/service-api/id/ --POST, PATCH, DELETE

http://127.0.0.1:8000/services/order-api/ --GET

http://127.0.0.1:8000/services/order-api/id/ --POST, PATCH, DELETE