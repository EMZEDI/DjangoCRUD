# Welcome to my CRUD website documentation! 
To run the website and use it, you have to make sure that you have python 3.9 installed:
To make sure, do the following tasks:
Download the repository and place it into your desktop and name it <b>djangoProject</b> <br>
1- Install Pycharm Community version from here: https://www.jetbrains.com/pycharm/download <br>
2- Open pycharm and create a new project.<br>
3- Make sure the python version used is 3.7 or above (3.9 recommended) make sure to mark the button where it says <b>New environment using: Virtualenv</b> along with the project.<br>
4- (unzip the repo folder) And choose repository folder in the desktop as your project location (which you have to choose on top of the page) And make the project!! You have to choose the "Create Project using the existing sources" option.<br>
5- When you enter the project, wait for a minute or so, to make sure pycharm installs everything.<br><br>
<b>If you have windows operating system:<br>
        TYPE the following lines of commands one at a time and press enter everytime you paste one line:<br>
        python -m pip install --upgrade pip<br>
        pip install -r requirements.txt<br>
        python manage.py makemigrations<br>
        python manage.py migrate<br>
        python manage.py runserver</b><br><br>
    <b>ELSE:<br>
    Go to the terminal and type <code> chmod u+x run.sh </code>.<br>
    Last step, in terminal type <code> ./run.sh </code>. <br><br></b>
    6- Wait until pycharm does everything for you. You will see a link after <b><code>Starting development server at</b></code>; this may take up to 30 seconds (python has to install packages). Click the link and you are good to go!<br>
    7- When you are done checking the website, you can press CONTROL + C on the same terminal tab as before to stop the server.

# Functionality of the website
1- Add inventory items that have name, quantity, and price. <br>
2- CRUD functionality which lets you edit the inventory items and update them as well as deleting them.<br>
3- You can download the information of each inventory item or all of the items as a csv file!<br>
# ENJOY!!!
