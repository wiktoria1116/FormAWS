# main.py
from app import app
from db_setup import init_db, db_session
from forms import UsersSearchForm,ProjectForm
from flask import flash, render_template, request, redirect
from models import Osoba

init_db()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/', methods=['GET', 'POST'])
def index():
    search = UsersSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html',form=search)


@app.route('/new_project', methods=['GET', 'POST'])
def new_project():
    form = ProjectForm(request.form)
    if request.method == 'POST' and form.validate():
        # save the project
        osoba = Osoba()
        save_changes(osoba, form, new=True)
        flash('Project created successfully!')
        return redirect('/')
    return render_template('new_project.html', form=form)

def save_changes(osoba, form, new=False):
    osoba = Osoba()
    osoba.ilosc_dzieci_w_rodzinie = form.ilosc_dzieci_w_rodzinie.data
    osoba.wiek_ojca = form.wiek_ojca.data
    osoba.wiek_matki = form.wiek_matki.data
    osoba.wystepowanie = form.wystepowanie.data
    osoba.kontakt_z_prom = form.kontakt_z_prom.data
    osoba.kontakt_z_sub = form.kontakt_z_sub.data
    osoba.leki = form.leki.data
    osoba.ciaza = form.ciaza.data
    osoba.odstep = form.odstep.data
    osoba.krotka_szyja = form.krotka_szyja.data
    osoba.male_hypoplastyczne_malzowiny_uszne = form.male_hypoplastyczne_malzowiny_uszne.data
    osoba.plaska_twarz = form.plaska_twarz.data
    osoba.krotkie_dlonie = form.krotkie_dlonie.data
    osoba.skosno_ustawione_powieki = form.skosno_ustawione_powieki.data
	osoba.opozniony_rozwoj = form.opozniony_rozwoj.data
    osoba.wady_serca = form.wady_serca.data
    osoba.wady_sluchu = form.wady_sluchu.data
    osoba.wady_wzroku = form.wady_wzroku.data
    osoba.obnizona_odpornosc = form.obnizona_odpornosc.data

    if new:
        # Add the new project to the database
        db_session.add(osoba) # commit the data to the database

    db_session.commit()
