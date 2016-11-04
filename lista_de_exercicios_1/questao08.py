#!/usr/bin/python3
# -*- coding: utf-8 -*-

temp = float(input('Digite a temperatura em Fahrenheit(°F):'))
temp_em_c = ((temp - 32) / 9) * 5
print('Temperatura em Celcius(°C): %.2f.' % temp_em_c)
