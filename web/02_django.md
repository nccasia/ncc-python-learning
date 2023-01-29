- [Web framework](#web-framework)
- [Django](#django)
    - [Django ORM](#django-orm)
    - [Sequelize](#sequelize)
    - [sqlalchemy](#sqlalchemy)
    - [django-filter](#django-filter)
- [Basic steps to build a web for selling](#basic-steps-to-build-a-web-for-selling)

# Web framework

A web framework (WF) or web application framework (WAF) is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs. Web frameworks provide a standard way to build and deploy web applications on the World Wide Web.

It is a collection of packages or modules which allow developers to write Web applications (see WebApplications) or services without having to handle such low-level details as protocols, sockets or process/thread management.

Generally, frameworks provide support for a number of activities such as 
 - URL routing and interpreting requests (getting form parameters, handling cookies and sessions, authentication)
 - producing responses (presenting data as HTML or in other formats)
 - integrating with some frontend javascript technology (AJAX, angular, reactjs, etc)
 - storing data persistently, ORM, caching and so on
 - ability to run and manage migrations
 - basic security features such as XSS and CRSF prevention
 - support for feature or unit-testing
 - Inbuilt development web server
 - logging
 - external modules, libraries management

Many frameworks now provide an element of customization in their support for the above activities and abstractions, utilizing components in that they provide abstractions only for certain specific things. As a result, it can be possible for you to build your own full-stack framework almost entirely from existing components.

# Django

 - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django together with https://github.com/mdn/django-locallibrary-tutorial
 - https://learndjango.com/tutorials/how-learn-django


The Django framework is one of the most used Python web frameworks for developing large-scale web applications and websites. It tends to follow the MVC architecture minutely enough to be known as an MVC framework. 

This Python web development framework uses its ORM (Object Relational Mapper) for mapping objects to multi-database tables which allows the code to work across multiple databases and template engines to make it easier to migrate from one database to the other. 

Django provides a range of inbuilt libraries and database support – MySQL, SQLite, PostgreSQL, and Oracle. The Python MVC framework also supports other databases and templating systems via third-party adapters, drivers, and content management systems.

Support for localization, user authentication, sessions, cookies, web server, web browser compatibility, is one of the main reasons, Django is considered to better than other Python frameworks.


### Django ORM

*   [ ] You are able to create Models
*   [ ] You used proxy model
*   [ ] You know how to chain queries using custom Manager
*   [ ] You can create model inheritance

### Sequelize

*   [ ] You can create Model
*   [ ] You know how to create virtual fields

### sqlalchemy

*   [ ] You know how to configure a connection
*   [ ] You can setup/create migrations
*   [ ] You use sub queries

### django-filter

*   [ ] You can create full text search query
*   [ ] You know how to use ordering query
*   [ ] You can use it with DRF Generic View
*   [ ] You know how to create custom queryset for a filter

# Basic steps to build a web for selling

1. Create a new Django project and set up a new app for your store.

```bash
django-admin startproject mystore
cd mystore
python manage.py startapp store
```

2. Create models for your products, categories, and orders.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
```

3. Create views and html templates to handle requests for the homepage, product pages, and the checkout process.

```python
from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})

def checkout(request):
    products = request.session.get('products', [])
    total_price = sum([p.price for p in products])
    return render(request, 'checkout.html', {'products': products, 'total_price': total_price})
```

4. Create URLs for the homepage, product pages, and checkout process using the URLs patterns provided by Django.

```python
from django.urls import path
from .views import home, product, checkout

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product, name='product'),
    path('checkout/', checkout, name='checkout'),
]
```

6. Run the development server and test your website

```bash
python manage.py runserver
```