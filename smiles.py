!pip install pandas
!pip install rdkit
import csv
import pandas as pd
import rdkit as rd

#読み込み
cf = pd.read_csv("/Users/aizawaharuka/Library/CloudStorage/OneDrive-学校法人明治薬科大学/春香/2023/AID_743240_datatable_all.csv")
cf.head()
print(cf.columns.to_list())
cf = cf.drop(0)
cf = cf.drop(1)
cf = cf.drop(2)
cf.head()
print(cf['PUBCHEM_EXT_DATASOURCE_SMILES'])
cf2 = cf.assign(PUBCHEM_EXT_DATASOURCE_SMILES = cf['PUBCHEM_EXT_DATASOURCE_SMILES'].str.split('.')).explode('PUBCHEM_EXT_DATASOURCE_SMILES')
print(cf2['PUBCHEM_EXT_DATASOURCE_SMILES'])

#塩を除く
cf3 = cf2.assign(smile_len = cf2['PUBCHEM_EXT_DATASOURCE_SMILES'].str.len())
cf4 = cf3.groupby('PUBCHEM_RESULT_TAG').filter(axis = "index",like = cf3.groupby("PUBCHEM_RESULT_TAG")["smile_len"].max())
