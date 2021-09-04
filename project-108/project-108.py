import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("project108Data.csv")

figure = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brands in use"],show_hist=False)
figure.show()

# figure2 = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating by users"],show_hist=False)
# figure2.show()