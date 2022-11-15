import pandas as pd
import numpy as np
from numpy import nan
import scipy.stats as stats
import matplotlib.pyplot as plt

print ("***Welcome to Independent T-Testing for CSV Files!***")
print ("Please have your CSV file properly formatted and in the same directoy as this script.")
data = input("Input file for t-testing:   ")
location1 = str(input("Input first study location:   "))
location2 = str(input("Input second study location:  "))
metric1 = str(input("Input first study metric (generally Location)  "))
metric2 = str(input("Input second study metric (Time, Weight, BP, etc)  "))

df = pd.read_csv(data)

print(df)

first_location = df.loc[df [f"{metric1}"] == f"{location1}"]
firstLocationList = list(first_location[f"{metric2}"])

second_location = df.loc[df[f"{metric1}"] == f"{location2}"]
secondLocationList = list(second_location[f"{metric2}"])

print(stats.ttest_ind(firstLocationList, secondLocationList, axis=0, nan_policy='omit'))
box_plot_data=[firstLocationList, secondLocationList]
plt.boxplot(box_plot_data, )
plt.show()
    
