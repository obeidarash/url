# Link Shortener 
### How to install Link Shortener web app
#### this is a basic link shortener web app made by Django framework witch doesn't have any javascript code on it and it is beta version. you can use this repo for learning purpose etc.

##### how to install:  
1- Install django framework (if you have , skip this step):

```
pip install django
```
2- Download repository:
```
git clone https://github.com/obeidarash/url.git
```
3- Go to url folder and run these two codes (you can use _cd url_ in the terminal):
```
python manage.py makemigration
python manage.py migrate
```
4- Create a user:
```
python manage.py createsuperuser
```
5- And at the end run the server:
```
python manage.py runserver
```
Enjoy!

### how to change style 
frontend of this app made by bootstrap framework
go to static/css and change the variables in the bootstrap_custom.scss file, after that use this command to apply changes
```
sass --watch bootstrap_custom.scss:bootstrap_custom.css
```
