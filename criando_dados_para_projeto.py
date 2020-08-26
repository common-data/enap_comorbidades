# ##########################################################################
# Esse código visa criar uma base de dados para o projeto da ENAP filtrando
# o que já temos no projeto geral do common_data com o banco da Covid-19
# e criando uma base com os indicadores com dados do covid
# This code was made to create a database for the ENAP project filtering
# what we have for the general project for common_data with the covid data
# and create a database with indicators as the base adding covid data
# ##########################################################################

import pandas as pd
import numpy as np
import os
import inspect

################################
# Acumulado - Cumulative
################################

# Pegando a base e filtrando pro período do estudo e retirando as cidades Indefinidas
# Getting the database and filtering on the period and excluding the cities "Indefinidas"
covid = pd.read_csv("common_data\data\caso_full_with_indicators.csv")
covid["date"] = pd.to_datetime(covid['date'], format="%Y/%m/%d")
covid = covid[(covid["date"] <= "2020-07-31") & (covid["city_ibge_code"] != 9)]
covid.sort_values(["city_ibge_code", "state", "date"], inplace=True)

# Criando novas variáveis
# Creating new variables
covid["order_for_place_deaths"] = 0
covid.loc[covid["last_available_deaths"] > 0, ["order_for_place_deaths"]] = covid[covid["last_available_deaths"] > 0].groupby(["city_ibge_code", "state"])["date"].cumcount() + 1

covid["last_available_deaths_per_100k_inhabitants"] = (covid["last_available_death_rate"] * 100000)
covid["last_available_confirmed_per_100k_inhabitants"] = (covid["last_available_confirmed"] / covid["estimated_population_2019"] * 100000)

covid["place_subtype"] = covid["place_type"]
covid.loc[(covid["distance_capital"] == 0) & (covid["place_type"] == "city"), ["place_subtype"]] = "capital"

covid.loc[covid["place_type"] == "state", ['distance_capital', 'distance_nearest_capital','distance_nearest_bigcity']] = np.nan


# Ordenando a base de dados e renomeando as variáveis
# Sorting the database and renaming variables
covid = covid[['city_ibge_code','name','code_state','state','Region','place_type','place_subtype','health_region',
     'estimated_population_2019','date','order_for_place','order_for_place_deaths','epidemiological_week',
     'last_available_confirmed','last_available_deaths','last_available_confirmed_per_100k_inhabitants',
     'last_available_deaths_per_100k_inhabitants','new_confirmed','new_deaths',
     'latitude','longitude','distance_capital','distance_nearest_capital','distance_nearest_bigcity',
     'RAZDEP','GINI','PIND','PMPOB','PPOB','RDPC','T_AGUA','T_BANAGUA','T_DENS','AGUA_ESGOTO', 'T_RMAXIDOSO',
     'IDHM', 'IDHM_E', 'IDHM_L', 'IDHM_R']]

covid.columns = ["COD_IBGE","Nome","COD_UF","UF","Regiao","Classe_local","Subclasse_local","Regiao_saude",
                  "Pop_estimada_2019","Data","Dias_primeiro_confirmado","Dias_primeira_morte","Semana_epidemiologica",
                  "Confirmados","Mortes","Confirmados_100mil","Mortes_100mil","Novos_confirmados","Novas_mortes",
                  "Latitude","Longitude","Distancia_capitalUF","Distancia_capital_mais_proxima",
                  "Distancia_cidade150mil","Razao_dependencia","Gini","Perc_extremamente_pobres_menos70",
                  "Perc_pobres_menos140","Perc_vulneraveis_pobreza_menos255","RDPC","Perc_dom_agua_encanada",
                  "Perc_dom_banheiro_agua_encanada","Perc_pop_densidade_2dorm","Perc_pop_agua_esgoto_inadequado",
                  "Perc_pop_vulneraveis_depIdoso","IDHM","IDHM_E","IDHM_L","IDHM_R"]


# Transformando em um banco de dados CSV
# Sending to a CSV file
covid.to_csv("enap_comorbidades\dados\covid_indicadores_acumulado_20200731.csv", index=False, encoding='utf-8-sig')
covid.columns


################################
# Indicadores + Covid - Indicators + Covid
################################

# Pegando a base de indicadores
# Getting indicators base
indicadores = pd.read_csv("common_data\data\outras\IndicadoresSociais_mun_distance.csv")
indicadores.sort_values(["codigo_ibge"], inplace=True)

# Corrigindo alguns nomes
# Fixing some names
indicadores.loc[indicadores["codigo_ibge"] == 2405306,["nome"]] = "Januário Cicco"
indicadores.loc[indicadores["codigo_ibge"] == 2512606,["nome"]] = "Quixaba"
indicadores.loc[indicadores["codigo_ibge"] == 2613107,["nome"]] = "São Caitano"
indicadores.loc[indicadores["codigo_ibge"] == 2918753,["nome"]] = "Lagoa Real"
indicadores.loc[indicadores["codigo_ibge"] == 2918803,["nome"]] = "Laje"
indicadores.loc[indicadores["codigo_ibge"] == 2918902,["nome"]] = "Lajedão"
indicadores.loc[indicadores["codigo_ibge"] == 2919009,["nome"]] = "Lajedinho"
indicadores.loc[indicadores["codigo_ibge"] == 2919058,["nome"]] = "Lajedo do Tabocal"
indicadores.loc[indicadores["codigo_ibge"] == 3122900,["nome"]] = "Dona Euzébia"
indicadores.loc[indicadores["codigo_ibge"] == 4215687,["nome"]] = "Santa Terezinha do Progresso"
indicadores.loc[indicadores["codigo_ibge"] == 4215695,["nome"]] = "Santiago do Sul"

indicadores.loc[indicadores["tipo"] == "CapitalMun",["tipo"]] = "Capital"


# Renomeando as variàveis e reordenando
# Renaming the variables and reordering columns
indicadores.rename(columns={"codigo_ibge":"COD_IBGE","nome":"Nome","codigo_uf":"COD_UF","Região":"Regiao",
    "tipo":"Classe_local","health_region":"Regiao_saude", "POP_TCU":"Pop_estimada_2019", "latitude":"Latitude",
    "longitude":"Longitude", "distance_capital":"Distancia_capitalUF",
    "distance_nearest_capital":"Distancia_capital_mais_proxima",
    "distance_nearest_bigcity":"Distancia_cidade150mil", 'RAZDEP':"Razao_dependencia","GINI":"Gini",
    'PIND':"Perc_extremamente_pobres_menos70",'PMPOB':"Perc_pobres_menos140",'PPOB':"Perc_vulneraveis_pobreza_menos255",
    'T_AGUA':"Perc_dom_agua_encanada",'T_BANAGUA':"Perc_dom_banheiro_agua_encanada",
    'T_DENS':"Perc_pop_densidade_2dorm",'AGUA_ESGOTO':"Perc_pop_agua_esgoto_inadequado",
    'T_RMAXIDOSO':"Perc_pop_vulneraveis_depIdoso"}, inplace=True)
columns_to_keep_as_it_is = ["COD_IBGE","Nome","COD_UF","UF", "Regiao","Classe_local","Regiao_saude",
                            "Pop_estimada_2019","Latitude","Longitude","Distancia_capitalUF",
                            "Distancia_capital_mais_proxima","Distancia_cidade150mil"]
columns_to_keep_as_it_is.extend(indicadores.columns.to_list()[15:-27])
indicadores = indicadores[columns_to_keep_as_it_is]

# Adicionando variáveis Covid para o dia 31/07
# Adding variables Covid for 31/07
adicionar = covid[covid["Data"] == "2020-07-31"][["COD_IBGE", 'Confirmados', 'Mortes', 'Confirmados_100mil',
       'Mortes_100mil', 'Dias_primeiro_confirmado', 'Dias_primeira_morte']]
# 0 significa sem nenhuma morte, pra diferenciar de quem teve morte no primeiro dia nos cálculos seguintes
# 0 means no death, to differentiate to those that had death on first day, we´re nullifying
adicionar.loc[adicionar["Dias_primeira_morte"] == 0, "Dias_primeira_morte"] = np.nan
# Calcular as varíaveis extras
# Calculating extra variables
adicionar["Dias_ate_morte"] = adicionar["Dias_primeiro_confirmado"] - adicionar["Dias_primeira_morte"]
adicionar["Dias_ate_confirmado_brasil"] = max(adicionar["Dias_primeiro_confirmado"]) - adicionar["Dias_primeiro_confirmado"]
adicionar["Aceleracao_confirmados"] = adicionar["Confirmados"] / adicionar["Dias_primeiro_confirmado"]
adicionar["Aceleracao_mortes"] = adicionar["Mortes"] / adicionar["Dias_primeira_morte"]

indicadores = indicadores.merge(adicionar, how='left', on='COD_IBGE', copy=False, validate="one_to_one")


# Transformando variáveis Covid em 0 ou nulo
# Transform Covid variables in 0 or null
indicadores.loc[indicadores["Confirmados"].isna(),
                ["Dias_primeiro_confirmado", "Dias_primeira_morte", "Dias_ate_morte", "Dias_ate_confirmado_brasil"]] = np.nan

indicadores.loc[indicadores["Confirmados"].isna(),
                ["Confirmados", "Mortes", "Confirmados_100mil", "Mortes_100mil",
                 "Aceleracao_confirmados", "Aceleracao_mortes"]] = 0


# Criando variáveis
# Creating variables
conditions = [
    (indicadores["Confirmados"] > 0) & (indicadores["Mortes"] > 0),
    (indicadores["Confirmados"] > 0)]
choices = ['Confirmados com Mortes', 'Confirmados sem Mortes']
indicadores["Status_Covid"] = np.select(conditions, choices, default='Sem confirmados')


# Adicionando auxìlio emergencial abril-julho
# Adding emergencial from April to July
aux_emerg = pd.read_csv("enap_comorbidades\dados\AE_04_07.csv", encoding="utf-8") # , delimiter=";"
aux_emerg.drop(["ENQUADRAMENTO_n", "VALORBENEFÍCIO_mean"], axis=1, inplace=True)
aux_emerg.columns = ['COD_IBGE', 'Aux_emerg_abril_n', 'Aux_emerg_abril_valor',
                     'Aux_emerg_maio_n', 'Aux_emerg_maio_valor',
                     'Aux_emerg_junho_n', 'Aux_emerg_junho_valor',
                     'Aux_emerg_julho_n', 'Aux_emerg_julho_valor']
indicadores = indicadores.merge(aux_emerg, how='left', on='COD_IBGE', copy=False, validate="one_to_one")


# Transformando em um banco de dados CSV
# Sending to a CSV file
indicadores.to_csv("enap_comorbidades\dados\covid_indicadores_20200731.csv", index=False, encoding='utf-8-sig')
indicadores.columns
