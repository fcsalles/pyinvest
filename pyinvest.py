############################################################# BIBLIOTECA ################################################################
import math
import random
import datetime
import statistics 
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

intro = print("Bem-vindo(a) ao simulador de investimentos!")
capital_inicial = float(input("Insira o capital inicial (R$): "))
aporte_mensal = float(input("Insira o aporte mensal desejado (R$): "))
prazo_investimento = int(input("Insira o prazo desejado (em meses): "))
cdi_ano = int(input("Insira a taxa do CDI (%): ")) / 100
cdi_mes = ((1 + cdi_ano) ** (1/12)) - 1
total_investido = capital_inicial + (aporte_mensal * prazo_investimento)

############################################################# FORMATACOES ###############################################################

def cdb(): 
    taxa = cdi_mes
    montante = capital_inicial * (1 + taxa) ** prazo_investimento + aporte_mensal * (((1 + taxa) ** prazo_investimento - 1) / taxa)
    lucro = montante - total_investido
    imposto = lucro * 0.15
    return montante - imposto
    

def lci_lca():
    taxa = cdi_mes
    montante = capital_inicial * (1 + taxa) ** prazo_investimento + aporte_mensal * (((1 + taxa) ** prazo_investimento - 1) / taxa)
    return montante

def poupanca():
    taxa = 0.005
    montante = capital_inicial * (1 + taxa) ** prazo_investimento + aporte_mensal * (((1 + taxa) ** prazo_investimento - 1) / taxa)
    return montante

def fii():
    taxa = cdi_mes
    montante = capital_inicial * (1 + taxa) ** prazo_investimento + aporte_mensal * (((1 + taxa) ** prazo_investimento - 1) / taxa)
    v1 = montante + (montante * random.uniform(-0.03, 0.03))
    v2 = montante + (montante * random.uniform(-0.03, 0.03))
    v3 = montante + (montante * random.uniform(-0.03, 0.03))
    v4 = montante + (montante * random.uniform(-0.03, 0.03))
    v5 = montante + (montante * random.uniform(-0.03, 0.03))
    valores = [v1, v2, v3, v4, v5]
    media = statistics.mean(valores)
    mediana = statistics.median(valores)
    desvio = statistics.stdev(valores)
    return media, mediana, desvio

valor_cdb = cdb()
valor_lci = lci_lca()
valor_poupanca = poupanca()
media_fii, mediana_fii, desvio_fii = fii()

######################################################### TELA DE RESULTADOS ############################################################

def barra(valor, maior):
    tamanho = int((valor / maior) * 50)
    return "█" * tamanho

maior = max(valor_cdb, valor_lci, valor_poupanca, media_fii)

hoje = datetime.datetime.now()
resgate = hoje + datetime.timedelta(days=prazo_investimento * 30)

def f(valor):
    return locale.currency(valor, grouping=True)

print("=" * 60)
print("RELATÓRIO PYINVEST".center(60))
print("=" * 60)

print(f"Data: {hoje.strftime('%d/%m/%Y')}")
print(f"Resgate: {resgate.strftime('%d/%m/%Y')}")
print(f"Total investido: {f(total_investido)}")

print("-" * 60)

print(f"{'CDB':<15}: {f(valor_cdb)}")
print(f"{'Gráfico':<15}: {barra(valor_cdb, maior)}")

print(f"{'LCI/LCA':<15}: {f(valor_lci)}")
print(f"{'Gráfico':<15}: {barra(valor_lci, maior)}")

print(f"{'Poupança':<15}: {f(valor_poupanca)}")
print(f"{'Gráfico':<15}: {barra(valor_poupanca, maior)}")

print(f"{'FII (Média)':<15}: {f(media_fii)}")
print(f"{'Gráfico':<15}: {barra(media_fii, maior)}")

print("-" * 60)

print("Estatísticas FII")
print(f"Média: {f(media_fii)}")
print(f"Mediana: {f(mediana_fii)}")
print(f"Desvio: {f(desvio_fii)}")