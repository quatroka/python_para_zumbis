#!/usr/bin/python3
# -*- coding: utf-8 -*-

cigarros_por_dia = int(input('Quantidade de cigarros por dia:'))
anos_fumando = int(input('Quantidade de anos fumando:'))
vida_perdida = anos_fumando * 365 * cigarros_por_dia * 10
print('Tempo de vida perdido: %d minutos.' % vida_perdida)
