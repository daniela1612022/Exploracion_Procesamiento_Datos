# -*- coding: utf-8 -*-
"""Onehot_Ordinal_Dp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lolx5GMWrzyhKGDjmRSOApR8qWa4RA5I

#***One Hot y Ordinal***
----
>**Author :**
* Daniela Pinzon
"""

import pandas as pd
import numpy as np

# Crear Dataframe
data = {
	'Nacionalidad': ['Colombiano','Venezolano','Colombiano','Peruano'],
  'Nivel_Ingreso': ['Alto','Medio','Bajo','Alto'],
  'Edad' : [21,20,19,15],
  'Sexo': ['M','F','M','F'],
  'Estado_Civil': ['Soltero','Casado','Union Libre','Casado']
}
df = pd.DataFrame(data, columns=['Nacionalidad','Nivel_Ingreso','Sexo','Estado_Civil'])
print("Dataframe is : ")
print(df)

df = pd.DataFrame(data = [['Colombiano' , 'Alto' ,21, 'M' , 'Soltero'],
                          ['Venezolano' , 'Medio' ,20,'F' , 'Casado'],
                          ['Colombiano' , 'Bajo' , 19,'M' , 'Union Libre'],
                          ['Peruano  ' , 'Alto' , 15,'F' , 'Casado']],
                  columns=['Nacionalidad','Nivel_Ingreso','Edad','Sexo','Estado_Civil'])

df

# One hot
pd.get_dummies(df)

# Eliminar una columna de cada variable
pd.get_dummies(df,drop_first=True)

pd.get_dummies(df['Nacionalidad'])

pd.get_dummies(df['Nivel_Ingreso'])

pd.get_dummies(df['Sexo'])

pd.get_dummies(df['Estado_Civil'])

from sklearn.preprocessing import OneHotEncoder ,OrdinalEncoder

# One hot
# sparce  = Matriz de binarios . ocupa mas espacios (solo guarda el 1)
encoder = OneHotEncoder(sparse = False)

encoder.fit(df.drop('Edad',axis=1))

encoder.transform(df.drop('Edad',axis=1))

encoder.categories_

# Ordinal
encoder1 = OrdinalEncoder()

encoder1.fit(df.drop('Edad',axis=1))

encoder1.transform(df.drop('Edad',axis=1))

encoder1.categories_

# Combinacion de transformadores

from sklearn.compose import ColumnTransformer

# Combinacion de transformadores es una clase porque piensa en mayusculas
columnTransformer = ColumnTransformer(
    [
        # nombre , clase (constructor),arreglo
       ('OneHot',OneHotEncoder(sparse = False),[0,3,4]),
       ('Ordinal',OrdinalEncoder(categories=[['Bajo','Medio','Alto']]),[1]),
        # passthrough sin transformaciones
       ('reminder','passthrough',[2])
    ]
)

columnTransformer.fit(df)

columnTransformer.transform(df)

columnTransformer.transformers_[0][1].categories_

columnTransformer.transformers_[1][1].categories_

"""#***Data School***
----
"""

df = pd.read_csv('/content/school_grades_dataset.csv')

df.isnull().sum()

df

df.info()

df.reason.unique()

df.activities.unique()

columnTransformer = ColumnTransformer(
    [
        # nombre , clase (constructor),arreglo
       ('OneHot',OneHotEncoder(sparse = False),[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,32]),
       ('Ordinal',OrdinalEncoder(),[]),
        # passthrough sin transformaciones
       ('reminder','passthrough',[14,22,18])
    ]
)

columnTransformer.fit(df)

columnTransformer.transform(df)

columnTransformer.transformers_[0][1].categories_