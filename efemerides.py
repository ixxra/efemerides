#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This program prints Wikipedias efemerids in spanish.
Modifying the wikipedia dictionary below you could easily adapt it to other
locales.

Este programa imprime las efemerides del dia de Wikipedia en español.
Modificando el diccionario `wikipedia` abajo podria adaptarse facilmente
a otros idiomas.
'''
from urllib import request
from datetime import datetime
import locale
import xml.etree.ElementTree as ET

ns = {'default': 'http://www.mediawiki.org/xml/export-0.10/'}
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

then = datetime.now()
today = then.strftime('%d_de_%B')

wikipedia = {
    'root': 'https://es.wikipedia.org/wiki',
    'export': 'Especial:Exportar',
    'template': 'Plantilla:Efem%C3%A9rides',
    'today': today
}

url='{root}/{export}/{template}_-_{today}'.format(**wikipedia)
content =  request.urlopen(url).read()
doc = ET.fromstring(content)
for item in doc.findall('.//default:text', ns):
    print(item.text)
