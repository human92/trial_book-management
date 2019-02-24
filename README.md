# trial_book-management
====

Book management application with modern web browser.
For my practice, I have developed simple book_management tool by Vue.js, django and MySQL.
You can manage your favorite books with category easily.

## What you can do

1. Register and list your favotrite books.
2. Edit your fovorite books information.

**book list image**
#![md](img/list_screen.PNG)#
**post screen  image**
#![md](img/post_screen.PNG)#

# Dependency

## Script

### Server-Side
* Python == 3.6.6 (Anaconda Custome)
## Required package
Please check Pipfile

### Front-Side
* Vue == 3.0.5

## DB

* MySQL 8.0.12

# Setup(Server-Side)

**This application is developed by Python Anaconda custome, and development environment is based on Windows.**

0. Install Anaconda.(Reference ⇒ [Anaconda Download](https://www.anaconda.com/download/)
1. Set up Django environment.(Reference ⇒　[Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)
2. Set up MySQL environment. (Reference ⇒ [MySQL Download](https://www.mysql.com/jp/downloads/)
3. Set up Django and Mysql connection. Update following code in "setting.py".
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your db',  
        'USER': 'root',  
        'PASSWORD': 'hogehogehoghe',  
        'HOST': '', 
        'PORT': '', 
    }
}
```
4. Download all directory from my repogitory.
5. Add installed apps in "setting.py".
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```
6. Run following code.
```
python manage.py runserver
```
7. Access following address.
```
http://127.0.0.1:8000/
```

# Setup(Front-Side)
0. Install Vue-CLI ⇒ [Vue-CLI Install](https://cli.vuejs.org/guide/installation.html)
1. Setup Vuetify ⇒ [Vuetify Setup](https://vuetifyjs.com/ja/getting-started/quick-start)
2. Download all directory from my repogitory.
3. Access following address.
```
http://127.0.0.1:8080/
```

# Licence
This software is released under the MIT License, see LICENSE.

# Authors

* human92
* ystk

# References
* [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)
* [Django Official Document](https://www.djangoproject.com/)
* [Vue-CLI Official Document](https://cli.vuejs.org/)
* [Vuetify Official Document](https://vuetifyjs.com/ja/)
