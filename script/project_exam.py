#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:05:56 2023

@author: Annika
"""

import pandas as pd 
import numpy as np

file = "/Users/Annika/Documents/GitHub/project-repo/data/StudentsPerformance.csv"
df = pd.read_csv(file)
data = df

#IDEAS

#visualizing the 3 scores of 1 person
#from all people: what exam got the highest grades?
#is there a correlation bewtween preperation course and score?
#is there a correlation bewtween parental degree and score?
#gender and math score
#gender and reading score

#Adding the total marks of each student and the percentage of total marks to the dataset

df["Total marks"] = df["math score"] + df["reading score"] + df["writing score"]
df["Percentage"] = df["Total marks"] / 3
df.head()

#Adding grades A-F to each score 

def Grade(marks):
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    elif marks >= 50:
        grade = 'E'
    else:
        grade = 'F'
    return grade
        
        
df["Grade_math"] = df["math score"].apply(lambda s: Grade(s))
df["Grade_reading"] = df["reading score"].apply(lambda s: Grade(s))
df["Grade_writing"] = df["writing score"].apply(lambda s: Grade(s))
df["Overall_grade"] = df["Percentage"].apply(lambda s: Grade(s))
df.head()

