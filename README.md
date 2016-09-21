# Djangaroo

A template for a basic Django 1.10 site including the things I usually 
use:

- Bootstrap
- jQuery
- Font Awesome

## The example app demonstrates a variety of things:

- views
- forms
- create, edit, and delete flows
- templatetags
- admin models
- separate apps
- static files
- custom error templates/views
- fixtures
- unit test samples for models and views
- flash messages
- basic json api
- docker build and prod deployment

One of the goals was to use as few 3rd party modules as possible so we 
only use:

- `Django==1.10.1`
- `PyYaml` (no really necessary, but makes fixtures nicer)
- `django-fullclean`

# How to use this example/template:

This repo is mostly for my own use when setting up simple projects, but 
if you want to use it:

- clone or fork it
- remove the request routing to the `example_app` and remove it from
the `INSTALLED_APPS` list. 
- rename the various folders to match your naming scheme, I suggest
using PyCharm or the like so that it renamed all references for you

# More resources:

- **Remember to look at https://github.com/rosarior/awesome-django**
- https://djangopackages.org/
- if you want tags use this: https://github.com/alex/django-taggit/ 
    don't reinvent them
- if you need auto complete use this: https://github.com/yourlabs/django-autocomplete-light/
- if you need more complex API stuff look at the REST framework
    
## TODO

- Make scripts for setting up the prod install
    - allow mount settings file 
    - allow mount db directory
