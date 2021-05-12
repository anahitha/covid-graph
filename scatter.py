import pandas as pd
import plotly.express as px

f = pd.read_csv('csv files/data.csv')
graph = px.scatter(f, x="Population", y = "Per capita", size = "Percentage", color = "Country")
graph.show()