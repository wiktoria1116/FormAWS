#models.py
from app import db

class Osoba(db.Model):
    __tablename__ = "osoba"
    id = db.Column(db.Integer, primary_key=True)
    ilosc_dzieci_w_rodzinie = db.Column(db.String)
    wiek_ojca=db.Column(db.String)
    wiek_matki = db.Column(db.String)
    wystepowanie=db.Column(db.String)
    kontakt_z_prom=db.Column(db.String)
    kontakt_z_sub=db.Column(db.String)
    leki=db.Column(db.String)
    ciaza=db.Column(db.String)
    odstep=db.Column(db.String)
    krotka_szyja =db.Column(db.String)
    male_hypoplastyczne_malzowiny_uszne = db.Column(db.String)
    plaska_twarz = db.Column(db.String)
    krotkie_dlonie = db.Column(db.String)
    skosno_ustawione_powieki = db.Column(db.String)
    opozniony_rozwoj = db.Column(db.String)
    wady_serca = db.Column(db.String)
    wady_sluchu = db.Column(db.String)
    wady_wzroku = db.Column(db.String)
