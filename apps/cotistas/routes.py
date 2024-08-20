# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.cotistas import blueprint
from flask import render_template, redirect, request, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.cotistas.models import Cotistas , add_cotista , list_all_cotistas


@blueprint.route('/')
#@login_required
def index():
    data = list_all_cotistas()
    return render_template('cotistas/index.html' , data=data)


@blueprint.route('/cadastrar')
#@login_required
def create():
    
    add_cotista(
        name="dadinhi",
        email="dadaedoneves@example.com",
        cpf="12345278902",
        birth="1982-03-01",
        telephone="322456789",
        cell="987656331",
        active=True,
        code="ABC6545",
        income_tax=False
    )
    
    return render_template('home/calendar.html')



