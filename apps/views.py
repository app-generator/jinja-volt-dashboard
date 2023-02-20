# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='index', parent='pages')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404

# Pages -- Dashboard
@app.route('/pages/dashboard/')
def pages_dashboard():
  return render_template('pages/dashboard/dashboard.html', segment='dashboard', parent='pages')

# Pages

@app.route('/pages/transactions/')
def pages_transactions():
  return render_template('pages/transactions.html', segment='transactions', parent='pages')

@app.route('/pages/settings/')
def pages_settings():
  return render_template('pages/settings.html', segment='settings', parent='pages')

@app.route('/pages/upgrade-to-pro/')
def pages_upgrade_to_pro():
  return render_template('pages/upgrade-to-pro.html', segment='upgrade_to_pro', parent='pages')

# Pages -- Tables

@app.route('/pages/tables/bootstrap-tables/')
def pages_tables_bootstrap_tables():
  return render_template('pages/tables/bootstrap-tables.html', segment='bootstrap_tables', parent='tables')

# Pages -- Pages examples

@app.route('/pages/examples/404/')
def pages_examples_404():
  return render_template('pages/examples/404.html', segment='404', parent='pages')

@app.route('/pages/examples/500/')
def pages_examples_500():
  return render_template('pages/examples/500.html', segment='500', parent='pages')

# Accounts

@app.route('/accounts/sign-in/')
def accounts_sign_in():
  return render_template('accounts/sign-in.html', segment='sign_in', parent='accounts')

@app.route('/accounts/sign-up/')
def accounts_sign_up():
  return render_template('accounts/sign-up.html', segment='sign_up', parent='accounts')

@app.route('/accounts/forgot-password/')
def accounts_forgot_password():
  return render_template('accounts/forgot-password.html', segment='forgot_password', parent='accounts')

@app.route('/accounts/reset-password/')
def accounts_reset_password():
  return render_template('accounts/reset-password.html', segment='reset_password', parent='accounts')

@app.route('/accounts/lock/')
def accounts_lock():
  return render_template('accounts/lock.html', segment='lock', parent='accounts')

@app.route('/accounts/password-change/')
def accounts_password_change():
  return render_template('accounts/password-change.html', segment='password-change', parent='accounts')

# Pages Components

@app.route('/pages/components/buttons/')
def pages_components_buttons():
  return render_template('pages/components/buttons.html', segment='buttons', parent='components')

@app.route('/pages/components/notifications/')
def pages_components_notifications():
  return render_template('pages/components/notifications.html', segment='notifications', parent='components')

@app.route('/pages/components/forms/')
def pages_components_forms():
  return render_template('pages/components/forms.html', segment='forms', parent='components')

@app.route('/pages/components/modals/')
def pages_components_modals():
  return render_template('pages/components/modals.html', segment='modals', parent='components')

@app.route('/pages/components/typography/')
def pages_components_typography():
  return render_template('pages/components/typography.html', segment='typography', parent='components')
