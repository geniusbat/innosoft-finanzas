Pip version: 20.0.2
Django version: 3.2.8
python version: 3.8.10

Session handling:
In order to see the user's permision, in the views.py  access to request.session["session"], it will return a string of the following form: 
NA: nada
MB: miembro
CD: coordinador
PR: profesor
SU: superuser
Cada permiso tiene un cierto nivel de acceso.

Working with static files (css, js...):
Add a cs/js/... folder in the module you are working (ie: if working in inventario, add a folder "css" with a file "style.css"). To access to the static file do:
{% load static %}
{% static 'module/folder/file name' %}

ie:
{% load static %}
link rel="stylesheet" href="{% static 'inventario/css/style.css' %}"

Working with templates and inheritance:
There will be a base template where every other template can build upon. To extend it use: {% extends "baseTemplates/base.html" %}
It contains the following blocks: head, header, navBar, content and footer.
There will be also small predefined templates such as the navigation bar and the footer to reduce redundance. To use it use: {% include "baseTemplates/templateYouWantToAdd" %}

Gestión de Issues:
Véase la wiki.
