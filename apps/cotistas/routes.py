# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.cotistas import blueprint
from flask import render_template, redirect, request, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.cotistas.models import Cotistas , add_cotista , list_all_cotistas , view_id_cotistas , add_endereco , add_conta


@blueprint.route('/')
#@login_required
def index():
    data = list_all_cotistas()
    return render_template('cotistas/index.html' , data=data)


@blueprint.route('/ver/<id>')
#@login_required
def view(id):
    cotista = view_id_cotistas(id)
    return render_template('cotistas/view.html' , cotista=cotista)


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

@blueprint.route('/cadastrar_endereco')
#@login_required
def create_endereco():
    
    add_endereco(
    cotistas_id=2,
    street="Rua Nova",
    number="456",
    city="Rio de Janeiro",
    state="RJ",
    cep="23456-789"
    )

    
    return render_template('home/calendar.html')


@blueprint.route('/cadastrar_conta')
#@login_required
def create_conta():
    
    add_conta(
    cotistas_id=1,
    bank="Banco do Brasil",
        number_bank="001",
        agency="200",
        number_account="2038-1",
        adress="avenida nove de julho"
    )

    
    return render_template('home/calendar.html')



