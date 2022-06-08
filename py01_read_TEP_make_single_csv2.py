# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:32:28 2022

@author: byungkiryu
"""

from datetime import datetime
from pykeri.thermoelectrics.TEProp_xls import TEProp
import pandas as pd
# import openpyxl

# DIR_tematdb = 'R:/old OneD  2021 1223/10-ResMAIN/00-RES/11-etaMap/00 keri db/100-teMatDb/teMatDb/1-문헌_0손박임/210824 SnSe 3.1/'
# DIR_tematdb = './210824 SnSe 3.1/'
# DIR_tematdb = './tematdb v10.00 20220418 tep check brjcsjp/'
DIR_tematdb = "./"

fileseq = 1
idx_ini = 1  + (fileseq-1)*50
idx_fin = 50 + (fileseq-1)*50


filename1 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(1,50)
filename2 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(51,100)
filename3 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(101,150)
filename4 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(151,200)
filename5 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(201,250)
filename6 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(251,300)
filename7 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(301,350)
filename8 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(351,400)
filename9 = "_tematdb_tep_excel_v10.00_{:05d}-{:05d}_confirmed_220606.xlsx".format(401,450)


files = [filename1, filename2, filename3, filename4, filename5, filename6,
         filename7, filename8, filename9 ]

# sampleid_ini, sampleid_fin = 1, 4
# sampleid_ini, sampleid_fin = 291, 310
# sampleid_ini, sampleid_fin = 1, 350
sampleid_ini, sampleid_fin = 1, 430
df_tep_list = []
for idx in range(sampleid_ini,sampleid_fin+1):
    fileindex = int((idx-1)/50)
    filename = files[fileindex]
    sheetname = "#{:05d}".format(idx)
    
    # df_mat.loc[idx,'id_tematdb'] = idx
    # tep_valid_TF = True

    try:
        mat = TEProp.from_dict({'xls_filename': DIR_tematdb+filename,
                                'sheetname': sheetname, 'color': (idx/255, 0/255, 0/255)} )
    except:
        print(filename, idx, 'no data')
        continue
    
    df_tep_each = pd.DataFrame()
    df_alpha_each = pd.DataFrame(mat.Seebeck.raw_data(), columns=['Temperature','tepvalue'] )
    df_alpha_each['tepname'] = 'alpha'
    
    df_rho_each = pd.DataFrame(mat.elec_resi.raw_data(), columns=['Temperature','tepvalue'] )
    df_rho_each['tepname'] = 'rho'
    
    df_kappa_each = pd.DataFrame(mat.thrm_cond.raw_data(), columns=['Temperature','tepvalue'] )
    df_kappa_each['tepname'] = 'kappa'
    
    df_ZT_each = pd.DataFrame(mat.ZT.raw_data(), columns=['Temperature','tepvalue'] )
    df_ZT_each['tepname'] = 'ZT'
    
    df_tep_each = pd.concat([df_alpha_each, df_rho_each, df_kappa_each, df_ZT_each])
    df_tep_each['sampleid'] = idx
    
    df_tep_list.append( df_tep_each.copy() )
    
    len_alpha = len(df_alpha_each)
    len_rho   = len(df_rho_each)
    len_kappa = len(df_kappa_each)
    len_ZT    = len(df_ZT_each)
    len_tep   = len(df_tep_each)
    
    print(filename, sheetname, " data lenghs of alpha/rho/kappa/ZT/all=",
          len_alpha, len_rho, len_kappa, len_ZT, len_tep)



dbtype = 'tematdb_by_keri'
versionprefix = 'tematdb_completeteps_csv_v10.00_20220606'

df_tep_raw = pd.concat( df_tep_list, copy=True,ignore_index=True)
datetimeupdate =  datetime.now()

df_tep_all = df_tep_raw[['sampleid','tepname','Temperature','tepvalue']].copy()
sampleid_min = df_tep_all.sampleid.min()
sampleid_max = df_tep_all.sampleid.max()

versiontype ="0full"
versionlabel = versionprefix+'_{:s}_{:d}_to_{:d}'.format(versiontype,sampleid_min, sampleid_max)

df_tep_all['id_tematdb'] = df_tep_all.sampleid.copy()
df_tep_all['dbtype']  = dbtype
df_tep_all['version'] = versionlabel
df_tep_all['update']  = datetimeupdate
df_tep_all.to_csv( versionlabel+'.csv',index=False )


# df_tep_all = df_tep_all[ df_tep_all.sampleid <= 302 ].copy()
# sampleid_min = df_tep_all.sampleid.min()
# sampleid_max = df_tep_all.sampleid.max()
# # versiontype ="1share_shryu_wabi"
# # versionlabel = versionprefix+'_{:s}_{:d}_to_{:d}'.format(versiontype,sampleid_min, sampleid_max)

# df_tep_all['id_tematdb'] = df_tep_all.sampleid.copy()
# df_tep_all['dbtype']  = dbtype
# df_tep_all['version'] = versionlabel
# df_tep_all['update']  = datetimeupdate
# df_tep_all.to_csv( versionlabel+'.csv',index=False )





