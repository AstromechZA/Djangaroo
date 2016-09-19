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

One of the goals was to use as few 3rd party modules as possible so we 
only use:

- `Django==1.10.1`
- `PyYaml` (no really necessary, but makes fixtures nicer)

## TODO

- demonstrate unit and functional tests
- improve error messages for forms
- add flash messages to top of pages