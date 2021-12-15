This document describes the process of deploying and launching a project.

After we have cloned and unpacked our project

1. Install Python 3.9.0
2. Need install virtual environment. in command line / terminal enter: pip3 install virtualenv / pip install virtualenv
3. Create a virtual environment: virtualenv venv
4. Activate venv: source venv/bin/activate / venv/bin/activate (for windows)
5. So now we can install other program packages in command line / terminal enter: pip install pip install -r requirements.txt

When the installation process is complete. We can run server.
1. Let's go to the directory with the project: cd car_park_api
2. Enter: python manage.py runserver
7. Then open the browser and enter the address http://127.0.0.1:8000/admin
for login enter:
login: admin
password: admin1234!

Next instruction read in readme.md file.
