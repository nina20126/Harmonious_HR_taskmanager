# Harmonious HR Taskmanager

This is a Django project, so to make it work you should have django and python installed. To check the version of python open console and type
```
python --version
```
If you don't have python installed, you can [download it here.](https://www.python.org/downloads/)  

To check the version of django, type 
```
py -m django --version
```
If you don't have django installed, you can istall it by typing
```
pip install django
```

### Project Setup

Clone repository
```
git clone https://github.com/nina20126/Harmonious_HR_taskmanager.git
```
Move to the folder that includes manage.py file
```
cd Harmonious_HR_taskmanager
```
Create virtual environment (Windows)
```
py -m venv venv
```
Activate virtual environment (Windows)
```
venv/Scripts/activate
```
Install requirements
```
pip install -r requirements.txt
```
Make migrations
```
py manage.py makemigrations
```
migrate
```
py manage.py migrate
```
Run server
```
py manage.py runserver
```
