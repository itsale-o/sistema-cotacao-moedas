import tkinter as tk
import customtkinter
import requests
import pandas as pd
import numpy as np
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
    label_textocotacao = customtkinter.CTkLabel(janela, font=fonte_cotacaoobtida, text_color="#2FA572", anchor='w',
                                                text=f'Em {data_cotacao} o {moeda} fechou em R$ {valor_moeda:.2f}')
    label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title='Selecione o arquivo desejado')
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado = customtkinter.CTkLabel(janela, text='')
        label_arquivoselecionado.grid(row=6, column=0, columnspan=2)
        label_arquivoselecionado = customtkinter.CTkLabel(janela,
                                                          font=fonte_arquivo,
                                                          text=f'Arquivo Selecionado: {caminho_arquivo}',
                                                          anchor='e')
        label_arquivoselecionado.grid(row=6, column=0, columnspan=2, padx=10, sticky='nsew')
    else:
        label_arquivoselecionado = customtkinter.CTkLabel(janela, text='')
        label_arquivoselecionado.grid(row=6, column=0, columnspan=2)
        label_arquivoselecionado = customtkinter.CTkLabel(janela,
                                                          font=fonte_arquivo,
                                                          text='Nenhum arquivo selecionado',
                                                          anchor='e')
        label_arquivoselecionado.grid(row=6, column=0, columnspan=2, padx=10, sticky='nsew')


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
        df.to_excel('Cotações.xlsx')
        label_atualizarcotacoes = customtkinter.CTkLabel(janela,
                                                         font=fonte_cotacaoobtida,
                                                         text_color="#2FA572",
                                                         text='Arquivo gerado com sucesso!')
        label_atualizarcotacoes.grid(row=9, column=1, padx=10, sticky='nsew')
    except:
        label_atualizarcotacoes = customtkinter.CTkLabel(janela,
                                                       font=fonte_cotacaoobtida,
                                                       text_color="#BA150F",
                                                       text='Selecione um arquivo\n'
                                                            'no formato correto')
        label_atualizarcotacoes.grid(row=9, column=1, padx=10, sticky='nsew')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.title('Cotações de Moedas')

# Configuração das fontes
fonte_titulo = customtkinter.CTkFont(family="Segoe UI", size=18, weight="bold")
fonte_label = customtkinter.CTkFont(family="Segoe UI", size=15)
fonte_cotacaoobtida = customtkinter.CTkFont(family="Segoe UI", size=15, weight="bold")
fonte_botao = customtkinter.CTkFont(family="Segoe UI", size=13, weight="bold")
fonte_arquivo = customtkinter.CTkFont(family="Segoe UI", size=11, slant="italic")

# Estilo da janela
label_cotacaomoeda = customtkinter.CTkLabel(janela, font=fonte_titulo, text='Cotação de uma moeda')
label_cotacaomoeda.grid(row=0, column=0, pady=10, columnspan=2, sticky='nsew')

label_selecionarmoeda = customtkinter.CTkLabel(janela, font=fonte_label, text='Selecione a moeda')
label_selecionarmoeda.grid(row=1, column=0, padx=10, sticky='nsew')

combobox_selecionarmoeda = customtkinter.CTkComboBox(master=janela, values=lista_moedas, corner_radius=6)
combobox_selecionarmoeda.set("")
combobox_selecionarmoeda.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

label_selecionardata = customtkinter.CTkLabel(janela, font=fonte_label, text='Selecione uma data')
label_selecionardata.grid(row=2, column=0, padx=10, sticky='nsew')

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

botao_obtercotacao = customtkinter.CTkButton(master=janela,
                                             font=fonte_botao,
                                             text='Obter Cotação',
                                             command=obter_cotacao)
botao_obtercotacao.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

# Cotação várias moedas e período específico
label_cotacaovariasmoedas = customtkinter.CTkLabel(janela, font=fonte_titulo, text='Cotação de múltiplas moedas')
label_cotacaovariasmoedas.grid(pady=10, columnspan=2)

var_caminhoarquivo = tk.StringVar()

label_selecionararquivo = customtkinter.CTkLabel(janela, font=fonte_label, text='Selecione um arquivo')
label_selecionararquivo.grid(padx=10, pady=10, sticky='nsew')

botao_selecionararquivo = customtkinter.CTkButton(master=janela,
                                                  font=fonte_botao,
                                                  text='Selecionar Arquivo',
                                                  command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

label_arquivoselecionado = customtkinter.CTkLabel(janela,
                                                  font=fonte_arquivo,
                                                  text='Nenhum arquivo selecionado',
                                                  anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, columnspan=2, sticky='nsew')

label_datainicial = customtkinter.CTkLabel(janela, font=fonte_label, text="Data Inicial", anchor='w')
label_datainicial.grid(row=7, column=0, padx=10, sticky='nsew')

label_datafinal = customtkinter.CTkLabel(janela, font=fonte_label, text="Data Final", anchor='w')
label_datafinal.grid(row=9, column=0, padx=10, sticky='nsew')

calendario_datainicial = DateEntry(year=2023, locale='pt_br', anchor='w')
calendario_datainicial.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

calendario_datafinal = DateEntry(year=2023, locale='pt_br', anchor='w')
calendario_datafinal.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')

botao_atualizarcotacoes = customtkinter.CTkButton(master=janela,
                                                  font=fonte_botao,
                                                  text='Obter Cotações',
                                                  command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=11, column=0, padx=10, pady=10, sticky='nsew')

botao_fechar = customtkinter.CTkButton(master=janela,
                                       font=fonte_botao,
                                       text='Fechar',
                                       fg_color="#BA150F",
                                       hover_color="#7D0D09",
                                       command=janela.quit)
botao_fechar.grid(row=11, column=1, padx=10, pady=10, sticky='nsew')

janela.mainloop()
