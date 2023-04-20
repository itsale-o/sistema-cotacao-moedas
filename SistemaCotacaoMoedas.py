import tkinter as tk
import pandas as pd
import requests
import numpy as np
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
from datetime import datetime

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())


def obter_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?' \
           f'start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = float(cotacao[0]['bid'])
    label_textocotacao['text'] = f'O {moeda} no dia {data_cotacao} fechou em R$ {valor_moeda:.2f}'


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title='Selecione o arquivo contendo as moedas')
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo selecionado: {caminho_arquivo}'


def atualizar_cotacoes():
    try:
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]
        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]
        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/{moeda}-BRL/31?" \
                   f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
                   f"end_date={ano_final}{mes_final}{dia_final}"
            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan
                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel('Teste.xlsx')
        label_atualizarcotacoes['text'] = 'Arquivo criado com sucesso!'
    except:
        label_atualizarcotacoes['text'] = 'Selecione um arquivo com o formato correto'


janela = tk.Tk()
janela.title('Ferramenta de Cotação de Moedas')

label_cotacaomoeda = tk.Label(text='Cotação de uma moeda',
                              borderwidth=1,
                              relief='solid',
                              background='#3b5e37',
                              foreground='#e1e3e1')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecione a moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selecionardata = tk.Label(text='Selecione a data que deseja obter a cotação', anchor='e')
label_selecionardata.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

botao_obtercotacao = tk.Button(text='Obter Cotação', command=obter_cotacao)
botao_obtercotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

# cotação várias moedas
label_cotacaovariasmoedas = tk.Label(text='Cotação de múltiplas moedas',
                                     borderwidth=1,
                                     relief='solid',
                                     background='#3b5e37',
                                     foreground='#e1e3e1')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

var_caminhoarquivo = tk.StringVar()
label_selecionararquivo = tk.Label(text='Selecione um arquivo em Excel com as moedas\n'
                                        '(os nomes das moedas devem estar na Coluna A)')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

botao_selecionararquivo = tk.Button(text='Selecionar Arquivo', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

label_datainicial = tk.Label(text='Data Inicial', borderwidth=2, relief='solid')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
label_datafinal = tk.Label(text='Data Final', borderwidth=2, relief='solid')
label_datafinal.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

calendario_datainicial = DateEntry(year=2023, locale='pt_br', anchor='w')
calendario_datainicial.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')
calendario_datafinal = DateEntry(year=2023, locale='pt_br')
calendario_datafinal.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')

botao_atualizarcotacoes = tk.Button(text='Atualizar Cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=11, column=0, padx=10, pady=10, sticky='nsew')

label_atualizarcotacoes = tk.Label(text='', font='bold')
label_atualizarcotacoes.grid(row=9, column=2, columnspan=2, padx=10, pady=10, sticky='nsew')

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=11, column=2, padx=10, pady=10, sticky='nsew')

janela.mainloop()