#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:25:16 2021

@author: cstephenson
"""

import csv
import matplotlib.pyplot as plt


input_file = "iris.csv"
plt.figure(figsize=(7.5, 4.25))
plt.style.use("classic")

with open(input_file, "r") as iris_data:
    irises = list(csv.reader(iris_data))

virginica_petal_length = []

num_bins = 10

for petal in range(0, len(irises)-1):
    if irises[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(float(irises[petal][2]))

plt.hist(virginica_petal_length, num_bins, facecolor="red", alpha=0.75)

plt.title("Iris-viginica petal length", fontsize=12)
plt.xlabel("Petal length (cm)", fontsize=10)
plt.ylabel("Probability", fontsize=10)

plt.show()
