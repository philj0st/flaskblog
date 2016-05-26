#### installation
clone repo
```
$ git clone https://github.com/phipix01/flaskblog
$ cd flaskblog
```
install pip, make sure you're using the latest version
```
$ sudo apt-get install python-pip python-dev build-essential
$ pip install --upgrade pip
```
install virtualenv. use sudo so pip is able to change the mode of `/usr/local/bin/virtualenv` to 755. (-v = --verbose)
```
$ sudo pip install virtualenv -v

```
create and activate a virtual environment for this project folder
```
$ virtualenv venv
$ source venv/bin/activate

```
installing the dependencies won't pollute `/usr/lib/python2.7/site-packages` now and they will co-exist on a project by project basis
```
$ pip install flask
$ pip install pymongo
```
if everything worked you can now run `python app.py` and visit `http://localhost:5000`

_note: if MONGODB_URI is not found try `$ source ~/.bashrc` and then `$ source venv/bin/activate` again._

#### prerequisites
set up some a MongoDB (i used mongoLab) and add MONGODB_URI to environment variables
