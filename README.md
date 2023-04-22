# Sistema de Cotação de Moedas

## Conteúdo

-  [Visão Geral](#visao-geral)
    - [Créditos](#creditos)
- [Visual](#visual)
- [Funcionamento](#funcionamento)
- [Autoria](#autoria)
- [Observação :heavy_exclamation_mark:](#observacao)

<a id="visao-geral"></a>
## Visão Geral

Esta é uma interface gráfica construída em python com o objetivo de obter cotações de moedas em tempo real. 

É uma interface simples mas 100% funcional em relação ao seu objetivo. Foi contrída com o tkinter que, para aqueles não 
familiarizados, é uma biblioteca nativa do python. E para seu funcionamento a API Awesome API foi implementada.

<a id="creditos"></a>
### Créditos

A Awesome API é uma API de autoria do usuário [Ranielly Ferreira](https://github.com/raniellyferreira) que tem como objetivo 
a cotação de moedas e a consulta de CEPs.

- [Documentação da API](https://docs.awesomeapi.com.br/)
- [Repositório do autor da API](https://docs.awesomeapi.com.br/)

<a id="visual"></a>
## Visual

Como dito acima, esta é uma interface simples mas que cumpre 100% o seu objetivo.

Abaixo estão disponíveis algumas imagens com o visual do programa

<div align="center">

![Selecionando a moeda](/imagens/SistemaCotacaoMoedas1.jpg)

</div>

<div align="center">

![Selecionando a data](/imagens/SistemaCotacaoMoedas2.jpg)

</div>

<div align="center">

![Retorno com a cotação](/imagens/SistemaCotacaoMoedas3.jpg)

</div>

<a id="funcionamento"></a>
## Funcionamento

#### Cotação de uma moeda

Para se obter a cotação de apenas uma moeda o funcionamento do sistema é bem simples e intuitivo. Basta selecionar a moeda para qual se deseja obter a cotação, selecionar uma data e clicar no botão **Obter Cotação** e na mesma janela será imprimido um texto com o valor da cotação na data e moeda desejadas.

#### Cotação de várias moedas

Para a cotação de várias moedas o funcionamento do sistema é ligeiramente mais complexo mas segue uma lógica bem simples. A ideia desta parte é, além de se obter a cotação de várias moedas, obtê-las em um dado período e não apenas em um dia.

**Passos**

- Você precisa carregar um arquivo em Excel (.xlsx) contendo apenas os nomes das moedas das quais deseja obter as cotações
    - Observação: no arquivo em Excel, os nomes das moedas devem estar todos na coluna A, um em cada linha
- Após carregar o arquivo, você deve escolher duas datas: a data inicial e a data final para o período desejado
- Clicar e **Obter Cotações**

Após estes passos, será gerado um outro arquivo em Excel contendo todas as cotações. Este arquivo será salvo na mesma pasta onde este programa estiver salvo.

<a id="autoria"></a>
## Autoria

Aqui estão as minha redes. Fique a vontade para me acompanhar por lá:

- LinkedIn - [alessandra-santos-oliveira](https://www.linkedin.com/in/alessandra-santos-oliveira/)
- Twitter - [@itsale_o](https://www.twitter.com/itsale_o)

<a id="observacao"></a>
## Observação

:heavy_exclamation_mark: Por algum motivo, o sistema da API que deveria retornar a cotação de várias moedas em um período 
específico está retornando apenas a cotação da última data selecionada. Esta é uma questão da API então não cabe a mim a 
solução. Manterei o programa atualizado, e assim que a API for atualizada com esta questão resolvida, eu também devo fazer a 
atualização do código
