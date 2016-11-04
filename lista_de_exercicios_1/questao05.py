#!/usr/bin/python3
# -*- coding: utf-8 -*-

preco = float(input('Digite o valor da mercadoria: R$'))
porcentagem = float(input('Digite a porcentagem do desconto:'))
desconto = porcentagem / 100 * preco
total = preco - desconto
print('O valor do desconto e: R$ %.2f .' % desconto)
print('Valor com desconto: R$ %.2f .' % total)
