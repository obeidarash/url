# Link Shortener 
### How to install the Link Shortener web app
#### This is a basic link shortener web app made by the Django framework which doesn't have any javascript code on it, and it is a beta version. you can use this repo for learning purposes etc.

##### how to install:  
1. Install the Django framework (if you have one, skip this step):
```
pip install Django
```
2. Download repository:
```
git clone https://github.com/obeidarash/url.git
```
3. Go to url folder and run these two codes (you can use _cd url_ in the 
terminal):
```
python manage.py makemigration
python manage.py migrate
```
4. Create a user:
```
python manage.py createsuperuser
```
5. And at the end run the server:
```
python manage.py runserver
```
Enjoy!

### how to change style 
front-end of this app made by the bootstrap framework
go to static/css and change the variables in the bootstrap_custom.scss file,
after that use this command to apply changes
```
sass --watch bootstrap_custom.scss:bootstrap_custom.css
```
### Google Recaptcha
This mini project in the admin login page uses Google ReCaptcha for more security.
be sure you change the private and public security keys in the settings
you can generate a new key from [this link](https://link-url-here.org).
```
RECAPTCHA_PRIVATE_KEY = 'YOUR SECRET KEY'
RECAPTCHA_PUBLIC_KEY = 'YOUR SITE KEY'
```
