#!/usr/bin/python3
# -*- coding: utf-8 -*-

km_rodados = float(input('Kilometros percorridos:'))
qtd_dias = float(input('Quantidade de dias alugado:'))
preco = (km_rodados * 0.15) + (qtd_dias * 60)
print('Total a pagar: R$ %.2f .' % preco)
