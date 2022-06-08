# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:21:22 2022

@author: Byungki Ryu at KERI
teMatDb for thermoelectric materials properties (TEPs).
TEPs were digitized using webplotdigitizer ("https://automeris.io/WebPlotDigitizer/").
materials data from journal papers: 300-300 material samples.

Data digitization by Byungki Ryu, Ji-Hee Son, Su-Ji Park, Hye-Jin Lim, Jaywan Chung, Sungjin Park under supervision of Byungki Ryu.
This is the csv reader of teMatDb using url address in github.

""" 



import pandas as pd
url = 'https://raw.githubusercontent.com/byungkiryu/teMatDb/v10.00/'
csv = 'tematdb_completeteps_csv_v10.00_20220606_0full_1_to_424.csv'
df = pd.read_csv(url+csv,parse_dates=['update'])

