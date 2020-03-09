#db_creator.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///myusers.db', echo=True)
Base = declarative_base()



class Osoba(Base):
    __tablename__ = "osoba"
    id = Column(Integer, primary_key=True)
    ilosc_dzieci_w_rodzinie = Column(String)
    wiek_ojca = Column(String)
    wiek_matki = Column(String)
    wystepowanie = Column(String)
    kontakt_z_prom = Column(String)
    kontakt_z_sub = Column(String)
    leki = Column(String)
    ciaza = Column(String)
    odstep= Column(String)
    krotka_szyja = Column(String)
    male_hypoplastyczne_malzowiny_uszne = Column(String)
    plaska_twarz = Column(String)
    krotkie_dlonie = Column(String)
    skosno_ustawione_powieki = Column(String)
    opozniony_rozwoj = Column(String)
    wady_serca = Column(String)
    wady_sluchu = Column(String)
    wady_wzroku = Column(String)
    obnizona_odpornosc = Column(String)

#create tables
Base.metadata.create_all(engine)
