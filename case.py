import pandas as pd 
import plotly_express as px
df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.scatter(df,x="country",y="date",color="cases",title="Corona Cases" )
fig.show()







