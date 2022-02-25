 






//-------------------------to init project---------------------------// 
cd ->to project directory
source env_demo/bin/activate

//-------------------------to configure project---------------------------// 

sudo pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0:8000 --insecure --noreload

 


 