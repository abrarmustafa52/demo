 






//-------------------------to init project---------------------------// 
cd ->to project directory
python3 -m venv env_demo  
source env_demo/bin/activate

//-------------------------to configure project---------------------------// 

sudo pip3 install -r requirements.txt
python3 manage.py makemigrations users
python manage.py migrate users
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0:8000 --insecure --noreload

 
//-------------------------to request with auth token---------------------------// 
Authorization:token 851170af4116de171212c24c6cf675f4b2182e16   <="851170af4116de171212c24c6cf675f4b2182e16" replace with real token,its currently of admin token

 