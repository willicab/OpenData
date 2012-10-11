#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script para convertir los archivos csv del registro del CNE a sql
#
# Author: William Cabrera (aka willicab)
# Oct 11, 2012

import sys
from string import join
import codecs

if len(sys.argv) == 3:
    csvpath = sys.argv[1]
    sqlpath = sys.argv[2]
elif len(sys.argv) == 2:
    csvpath = sys.argv[1]
    sqlpath = join(sys.argv[1].split('.')[:-1],'.') + ".sql"

try:
    csvfile = codecs.open(csvpath, encoding='iso-8859-1')
    lineas = csvfile.readlines()
    sqlstring = "INSERT INTO votantes (cedula, nombre, nacionalidad, fnac, id_centro) VALUES\n"
    for linea in lineas:
        campos = linea.strip().split(';')
        if len(campos) == 5:
            nacionalidad = campos[0]
            cedula = campos[1]
            nombre = campos[2]
            idcentro = campos[3]
            if len(campos[4].split('/')) == 3:
                fecha = campos[4].split('/')
                fechanac = fecha[2] + '-' + fecha[1] + '-' + fecha[0]
                sqlstring = sqlstring + "(" + cedula + ", '" + nombre + "', '" + \
                            nacionalidad + "', '" + fechanac + "', " + idcentro + "),\n"
    csvfile.close()
except:
    print "El archivo no existe"
    
sqlfile = open(sqlpath, "w")
sqlfile.write(sqlfile[:-2] + ";")
sqlfile.close()
