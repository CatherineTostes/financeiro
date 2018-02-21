# -*- coding: utf-8 -*-
# Catherine Tostes
# Aula de Nivelamento em Python Básico
# Exercício Funções em Python

# Essa função faz o cálculo do INSS
def calcula_inss(salario_bruto):
    if salario_bruto <= 1000.00:
        return 0.0
    if salario <= 2000.00:
        return salario_bruto * 0.1
    else:
        return salario_bruto * 0.2

#Essa função faz o cálculo de desconto por dependentes
def dependentes(numero_dependentes):
    desconto = 100.00
    desconto_dependentes = desconto * numero_dependentes
    return desconto_dependentes

def imposto de renda(salario_liquido):
    if salario_liquido <= 1400.00:
        return 0.0
    if salario_liquido <= 2500.00:
        return salario_liquido * 0.12
    if salario_liquido <= 5000.00:
        return salario_liquido * 0.2
    else:
        return salario_liquido * 0.27
