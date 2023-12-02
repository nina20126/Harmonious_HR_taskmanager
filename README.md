# Harmonious HR Taskmanager

This is a Django project, so to make it work you should have django and python installed. You can istall django by typing command
```
pip install django
```
or check if you already have django installed by typing command
```
py -m django --version
```
Check the version of python 
```
python --version
```
... or [install python](https://www.python.org/downloads/) if you don't have it

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
