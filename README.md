# Sistema de Cotação de Moedas

## Conteúdo

-  [Visão Geral](#visao-geral)
    - [Créditos](#creditos)
- [Visual](#visual)
- [Funcionamento](#funcionamento)
- [Autoria](#autoria)
- [:heavy_exclamation_mark: IMPORTANTE :heavy_exclamation_mark:](#importante)

<a id="visao-geral"></a>
## Visão Geral

Esta é uma interface gráfica construída em python com o objetivo de obter cotações de moedas em tempo real. 

É uma interface simples mas 100% funcional em relação ao seu objetivo. Foi contrída com o CustomTkinter que, para aqueles não 
familiarizados, é uma biblioteca do python baseada no Tkinter. E para seu funcionamento a API Awesome API foi implementada.

<a id="creditos"></a>
### Créditos

#### Awesome API

A Awesome API é uma API de autoria do usuário [Ranielly Ferreira](https://github.com/raniellyferreira) que tem como objetivo 
a cotação de moedas e a consulta de CEPs.

- [Documentação da API](https://docs.awesomeapi.com.br/)
- [Repositório do autor da API](https://docs.awesomeapi.com.br/)

#### CustomTkinter

CustomTkinter é uma biblioteca do python criada pelo usuário [Tom Schimansky](https://github.com/TomSchimansky) baseada na biblioteca nativa Tkinter. A diferença é que com a CustomTkinter existe a possibilidade de aplicar visuais mais modernos nas nossas interfaces. 

- [Documentação da biblioteca](https://customtkinter.tomschimansky.com/documentation/)
- [Repositório do autor da biblioteca](https://github.com/TomSchimansky/CustomTkinter)

<a id="visual"></a>
## Visual

Como dito acima, esta é uma interface simples mas que cumpre 100% o seu objetivo.

Abaixo estão disponíveis algumas imagens com o visual do programa

<div align="center">

![Selecionando a moeda](imagens/SistemaCotaçãoMoedas1.jpg)

</div>

<div align="center">

![Selecionando a data](/imagens/SistemaCotaçãoMoedas2.jpg)

</div>

<div align="center">

![Retorno com a cotação](/imagens/SistemaCotaçãoMoedas3.jpg)

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

<a id="importante"></a>
## IMPORTANTE

:heavy_exclamation_mark: Por algum motivo, o sistema da API que deveria retornar a cotação de várias moedas em um período 
específico está retornando apenas a cotação da última data selecionada. Esta é uma questão da API então não cabe a mim a 
solução. Manterei o programa atualizado, e assim que a API for atualizada com esta questão resolvida, eu também devo fazer a 
atualização do código
