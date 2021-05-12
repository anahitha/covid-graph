import pandas as pd
import plotly.express as px

f = pd.read_csv('info.csv')
graph = px.scatter(f, x="date", y = "cases", color = "country")
graph.show()