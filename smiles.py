!pip install pandas
import csv
import pandas as pd

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

cf3 = cf2.assign(smile_len = cf2['PUBCHEM_EXT_DATASOURCE_SMILES'].str.len())
cf3
