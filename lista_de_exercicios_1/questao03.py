#!/usr/bin/python3
# -*- coding: utf-8 -*-

dias = int(input('Digite os dias:')) * 86400
horas = int(input('Digite as horas:')) * 3600
minutos = int(input('Digite os minutos:')) * 60
segundos = int(input('Digite os segundos:'))
print('O total em segundos e: %d segundos.' % (dias + horas + minutos + segundos))
