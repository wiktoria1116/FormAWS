from wtforms import Form, StringField, SelectField, RadioField, BooleanField

RadioYesNot=[('Tak', 'Tak'), ('Nie', 'Nie')]
RadioYesNotOr=[('nie dotyczy','nie dotyczy'),('Tak', 'Tak'), ('Nie', 'Nie')]

Age=[('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43'),('44','44'),('45','45'),('46','46'),('47','47'),('48','48'),('49','49'),('50','50'),('51','51'),('52','52'),('53','53'),('54','54'),('55','55'),('56','56'),('57','57'),('58','58'),('59','59'),('60','60'),('61','61'),('62','62'),('63','63'),('64','64'),('65','65'),('66','66'),('67','67'),('68','68'),('69','69'),('70','70'),('71','71'),('72','72'),('73','73'),('74','74'),('75','75'),('76','76'),('77','77'),('78','78'),('79','79'),('80','80'),('81','81'),('82','82')]
NumberOfChildren=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15')]
Distance=[('nie dotyczy','nie dotyczy'),('Mniej niż miesiąc','Mniej niż miesiąc'),('Miesiąc','Miesiąc'),('Dwa miesiące','Dwa miesiące'),('Trzy miesiące','Trzy miesiące'),('Cztery miesiące','Cztery miesiące'),('Pół roku','Pół roku'),('Rok','Rok'),('Ponad rok','Ponad rok')]

Praw = [('0.3','0.3'), ('0,4','0,4')]

class UsersSearchForm(Form):
    choices = [('', ''),('', '')]
    select = SelectField('',choices=choices)
    search = StringField('')

class ProjectForm(Form):
    wiek_matki = SelectField('1.Wiek matki podczas zajścia w ciążę', choices=Age)
    wiek_ojca= SelectField ('2.Wiek ojca w czasie prokreacji',choices=Age)
    krotka_szyja = BooleanField('')
    male_hypoplastyczne_malzowiny_uszne =  BooleanField('')
    plaska_twarz = BooleanField('')
    krotkie_dlonie = BooleanField('')
    skosno_ustawione_powieki = BooleanField('')
    opozniony_rozwoj = BooleanField('')
    wady_serca = BooleanField('')
    wady_sluchu = BooleanField('')
    wady_wzroku = BooleanField('')
    obnizona_odpornosc = BooleanField('')
    ilosc_dzieci_w_rodzinie = SelectField('4.Liczba dzieci urodzonych przez matkę', choices=NumberOfChildren)
    wystepowanie= RadioField ('5.Czy choroba wystepowała w rodzinie?', choices=RadioYesNot)
    kontakt_z_prom = RadioField ('6.Kontakt matki z promieniowaniem', choices=RadioYesNot)
	kontakt_z_sub = RadioField ('7.Kontakt matki ze szkodliwymi substancjami', choices=RadioYesNot)
    leki=RadioField('8.Czy zażywano silne leki,np.na trądzik(izotek)', choices=RadioYesNot)
    ciaza = RadioField('9.Czy zajście w ciążę nastąpiło podczas kuracji?', choices=RadioYesNotOr)
    odstep = SelectField('10.Odstęp między zakończeniem kuracji a zajściem w ciążę', choices=Distance)

