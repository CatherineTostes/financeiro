# -*- coding: utf-8 -*-
# Catherine Tostes
# Aula de Nivelamento em Python Básico
# Exercício Funções em Python

# Essa função faz o cálculo do INSS
def calcula_inss(salario_bruto):
    if salario_bruto <= 1000.00:
        return 0.0
    if salario_bruto <= 2000.00:
        return salario_bruto * 0.1
    else:
        return salario_bruto * 0.2

# Essa função faz o cálculo do desconto por número de dependentes
def calc_dependentes(num_dependentes):
    desc = 100.00
    desc_dependentes = desc * num_dependentes
    return desc_dependentes

# Essa função faz o cálculo do imposto de renda
def imposto_de_renda(salario_bruto, num_dependentes):
    if salario_bruto <= 1400.00:
        return 0.0
    if salario_bruto <= 2500.00:
        return (salario_bruto * 0.12) - calcula_inss(sal_bruto) - calc_dependentes(num_dependentes)
    if salario_bruto <= 5000.00:
        return (salario_bruto * 0.2) - calcula_inss(sal_bruto) - calc_dependentes(num_dependentes)
    else:
        return (salario_bruto * 0.27) - calcula_inss(sal_bruto) - calc_dependentes(num_dependentes)

sal_bruto = input('Digite o salário bruto: ')
num_dependentes = input('Digite o número de dependentes: ')

def calc_salario_liquido(sal_bruto):
    salario_liquido = sal_bruto - calcula_inss(sal_bruto) - imposto_de_renda(sal_bruto, num_dependentes)
    return salario_liquido

print(calc_salario_liquido(sal_bruto))
