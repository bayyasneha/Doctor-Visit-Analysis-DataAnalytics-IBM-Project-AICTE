

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from google.colab import files
uploaded=files.upload()

import io
df=pd.read_csv(io.BytesIO(uploaded['DoctorVisits - DA.csv']))

df.head(5190)

df.shape

df.info()

df["illness"].value_counts()

df["gender"].value_counts()

y=list(df.income)
plt.boxplot(y)
plt.show()

df.groupby(['gender','reduced']).mean()

sns.heatmap(df.isnull(),cbar=False,cmap='viridis')

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')

plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')

sns.histplot(df.gender,bins=2)

label=['yes','no']
Y=df[df['freepoor']=='yes']
N=df[df['freepoor']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health Insurance due to low income")
plt.show()

Y=df[df['private']=='yes']
N=df[df['private']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people having private health Insurance ")
plt.show()

Y=df[df['freerepat']=='yes']
N=df[df['freerepat']=='no']
x=[Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health Insurance due to old age, disability or veteran status" )
plt.show()

db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
plt.barh(db['gender'],db['reduced'],color=['cornflowerblue','lightseagreen'])
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
plt.show()