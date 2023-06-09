!pip install pandas
!pip install rdkit
import csv
import pandas as pd
import rdkit as rd

#読み込み
cf = pd.read_csv("AID_743240_datatable_all.csv")
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
cf4 = cf3.groupby('PUBCHEM_RESULT_TAG').apply(lambda x: x[x["smile_len"] == x["smile_len"].max()])
cf4["PUBCHEM_EXT_DATASOURCE_SMILES"]

#molオブジェクト・分子図の生成
from rdkit.Chem import Draw
cf5 = cf4.assign(molobj = cf4["PUBCHEM_EXT_DATASOURCE_SMILES"].apply(Chem.MolFromSmiles))
mollist = [x for x in cf5["molobj"] if x is not None]
mollist = cf5["molobj"].to_list()
#多すぎるのでとりあえず頭の８個だけ
img=Draw.MolsToGridImage(mollist[:8],molsPerRow=4,subImgSize=(1200,1200))
img.show()