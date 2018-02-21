# -*- coding: utf-8 -*-
# Catherine Tostes
# Aula de Nivelamento em Python Básico
# Exercício Funções em Python

# Essa função faz o cálculo do INSS
def calcula_inss(salario_bruto):
    inss = salario_bruto * 0.2
    return inss

#Essa função faz o cálculo de desconto por dependentes
def dependentes(numero_dependentes):
    desconto = 100.00
    desconto_dependentes = desconto * numero_dependentes
    return desconto_dependentes
