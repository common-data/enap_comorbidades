# Dicionário de variáveis

Esse documento visa apresentar o que cada variàvel significa no banco de dados `covid_indicadores_20200731.csv`. Cada linha é equivalente a um código IBGE (podendo ser município ou Unidade da Federação do Brasil). Esse arquivo consta todos os municípios e Unidades da Federação do Brasil.

As fontes de dados utilizadas foram:
- [Atlas do IDH-M](http://atlasbrasil.org.br/2013/) para os indicadoresç
- IBGE 2018 para latitude e longitude utilizados para o cálculo das distâncias.
- [Brasil.io](https://brasil.io/home/) usando Secretarias de Saúde das Unidades Federativas como fonte e com dados tratados por Álvaro Justen
e colaboradores para dados do Covid-19;

As colunas finais são:
- `COD_IBGE`: código IBGE da cidade/UF.
- `Nome`: nome do município ou UF.
- `COD_UF`: primeiros 2 dígitos do código IBGE, sendo referentes a UF. Mesmo que `COD_IBGE` para estados 
- `UF`: sigla da Unidade Federativa, por exemplo SP.
- `Regiao`: região brasileira
- `Classe_local`: tipo de local que esse registro descreve, pode ser `city` ou
  `state`.
- `Regiao_saude`: regiões de saúde previstas na RN nº 259 de 2011
- `Pop_estimada_2019`: população estimada para esse município/estado em
  2019, segundo o IBGE.
- `Latitude`: latitude central do município/UF
- `Longitude`: longitude central do município/UF
- `Distancia_capitalUF`: distância, em km, entre o município e a capital da UF, é nulo para as UFs.
- `Distancia_capital_mais_proxima`: minima distância, em km, entre o município e uma capital, podendo ser a da UF, é nulo para as UFs.
- `Distancia_cidade150mil`: minima distância, em km, entre o município e um município de mais de 150 mil habitantes, é `0` para as cidades com mais de 150 mil habitantes e nulo para as UFs.
- `Razao_dependencia`: percentual da população de menos de 15 anos e de 65 anos ou mais em relação à população de 15 a 64 anos.
- `Gini`: Índice de Gini, que indica desigualdade de renda. O índice varia entre 0 e 1, quanto mais próximo de `1` mais desigual.
- `Perc_extremamente_pobres_menos70`: percentual dos indivíduos com renda domiciliar per capita igual ou inferior a R$ 70,00 mensais em agosto de 2010. O universo de indivíduos é limitado àqueles que vivem em domicílios particulares permanentes.
- `Perc_pobres_menos140`: percentual dos indivíduos com renda domiciliar per capita igual ou inferior a R$ 140,00 mensais em agosto de 2010. O universo de indivíduos é limitado àqueles que vivem em domicílios particulares permanentes.
- `Perc_vulneraveis_pobreza_menos255`: percentual dos indivíduos com renda domiciliar per capita igual ou inferior a R$ 255,00 mensais em agosto de 2010, equivalente a 1/2 salário mínimo nessa data. O universo de indivíduos é limitado àqueles que vivem em domicílios particulares permanentes.
- `RDPC`: renda domiciliar per capita.
- `Perc_dom_agua_encanada`: percentual da população que vive em domicílios com água encanada.
- `Perc_dom_banheiro_agua_encanada`: percentual da população que vive em domicílios com banheiro e água encanada.
- `Perc_pop_densidade_2dorm`: percentual da população que vive em domicílios com densidade superior a 2 pessoas por dormitório.
- `Perc_pop_agua_esgoto_inadequado`: percentual de pessoas em domicílios com abastecimento de água e esgotamento sanitário inadequados.
- `Perc_pop_vulneraveis_depIdoso`: razão entre as pessoas que vivem em domicílios vulneráveis à pobreza (com renda per capita inferior a 1/2 salário mínimo de agosto de 2010) e nos quais a principal fonte de renda provém de moradores com 65 anos ou mais de idade e população total residente em domicílios particulares permanentes multiplicado por 100
- `IDHM`: Índice de Desenvolvimento Humano Municipal é uma medida composta de indicadores de três dimensões do desenvolvimento humano: longevidade, educação e renda. O índice varia de 0 a 1. Quanto mais próximo de 1, maior o desenvolvimento humano.
- `IDHM_E`: a parte da educação do IDHM.
- `IDHM_L`: a parte da longevidade do IDHM.
- `IDHM_R`: a parte da renda do IDHM.

- `Confirmados`: número de casos confirmados acumulados até o dia 31/07/1986.
- `Mortes`: número de mortes acumuladas até o dia 31/07/1986.
- `Confirmados_100mil`: número de casos confirmados acumulados até o dia 31/07/1986 por 100.000 habitantes do Código IBGE.
- `Mortes_100mil`: número de mortes acumuladas até o dia 31/07/1986 por 100.000 habitantes do Código IBGE.
- `Dias_primeiro_confirmado`: número de dias entre 31/07/1986 e a data do primeiro caso confirmado.
- `Dias_primeira_morte`: número de dias entre 31/07/1986 e a data da primeira morte.
- `Dias_ate_morte`: número de dias entre o primeiro caso confirmado e a primeira morte.
- `Dias_ate_confirmado_brasil`: número de dias entre o primeiro caso brasileiro e o primeiro caso confirmado no município/UF.
- `Aceleracao_confirmados`: número médio de confirmados por dia no municipio/UF.
- `Aceleracao_mortes`: número médio de mortes por dia no município/UF.
- `Status_Covid`: status do município/UF de acordo com o Covid-19, podendo ser `Confirmados com Mortes`, `Confirmados sem Mortes` ou `Sem confirmados`.

- 'Aux_emerg_abril_n': número de pessoas que receberam o auxílio emergencial em abril/2020.
- 'Aux_emerg_abril_valor': valor médio do auxílio emergencial em abril/2020.
- 'Aux_emerg_maio_n': número de pessoas que receberam o auxílio emergencial em maio/2020.
- 'Aux_emerg_maio_valor': valor médio do auxílio emergencial em maio/2020
- 'Aux_emerg_junho_n': número de pessoas que receberam o auxílio emergencial em junho/2020.
- 'Aux_emerg_junho_valor': valor médio do auxílio emergencial em junho/2020.
- 'Aux_emerg_julho_n': número de pessoas que receberam o auxílio emergencial em julho/2020.
- 'Aux_emerg_julho_valor': valor médio do auxílio emergencial em julho/2020.
- `Aux_emerg_valor_medio`: valor médio mensal do auxílio emergencial entre abril e julho/2020.
- `Aux_emerg_maio_n_100mil`: número de pessoas que receberam o auxílio emergencial em maio/2020 por 100.000 habitantes do Código IBGE.
