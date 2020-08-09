# ##########################################################################
# Esse código visa criar uma base de dados para o projeto da ENAP filtrando
# o que já temos no projeto geral do common_data com o banco da Covid-19
# This code was made to create a database for the ENAP project filtering
# what we have for the general project for common_data with the covid data
# ##########################################################################

import pandas as pd
import numpy as np
import os
import inspect

# Utilizando a pasta no meu computador
# Using the folder in my computer
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

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

covid.columns = ["COD_IBGE","Nome","COD_UF","UF","Regiao","Classe_cidade","Subclasse_cidade","Regiao_saude",
                  "Pop_estimada_2019","Data","Dias_primeiro_confirmado","Dias_primeira_morte","Semana_epidemiologica",
                  "Confirmados","Mortes","Confirmados_100mil","Mortes_100mil","Novos_confirmados","Novas_mortes",
                  "Latitude","Longitude","Distancia_capitalUF","Distancia_capital_mais_proxima",
                  "Distancia_cidade150mil","Razao_dependencia","Gini","Perc_extremamente_pobres_menos70",
                  "Perc_pobres_menos140","Perc_vulneraveis_pobreza_menos255","RDPC","Perc_dom_agua_encanada",
                  "Perc_dom_banheiro_agua_encanada","Perc_pop_densidade_2dorm","Perc_pop_agua_esgoto_inadequado",
                  "Perc_pop_vulneraveis_depIdoso","IDHM","IDHM_E","IDHM_L","IDHM_R"]


# Transformando em um banco de dados CSV
# Sending to a CSV file
covid.to_csv("enap_comorbidades\dados\covid_indicadores_20200731.csv", index=False, encoding='utf-8-sig')
covid.columns

