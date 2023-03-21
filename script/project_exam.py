#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:05:56 2023

@author: Annika
"""

import pandas as pd 
import numpy as np

file = "/Users/Annika/Documents/GitHub/project-repo/project-repo/data/StudentsPerformance.csv"
df = pd.read_csv(file)
data = df

#IDEAS

#visualizing the 3 scores of 1 person
#from all people: what exam got the highest grades?
#is there a correlation between preperation course and score?
#is there a correlation between parental degree and score?
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

#1 distribution of the math grades

import matplotlib.pyplot as plt
import seaborn as sns 

plt.figure()
grade_order = ["A","B","C","D","E","F"]
sns.countplot("Grade_math", data = df, order = grade_order, palette = "crest_r")
plt.xlabel("Math Grades")
plt.ylabel("Number of students")
plt.title("Distribution of Math Grades")
plt.ylim(0, 300)

#2 distribution of reading grades

plt.figure()
sns.countplot("Grade_reading", data = df, order = grade_order, palette = "flare_r")
plt.xlabel("Reading Grades")
plt.ylabel("Number of students")
plt.title("Distribution of Reading Grades")
plt.ylim(0, 300)

#3 distribution of writing grades

plt.figure()
sns.countplot("Grade_writing", data = df, order = grade_order, palette = "YlOrRd_r")
plt.xlabel("Writing Grades")
plt.ylabel("Number of students")
plt.title("Distribution of Writing Grades")
plt.ylim(0, 300)

#Is there a correlation between writing and reading?

reading = df["reading score"]
writing = df["writing score"]

fig, ax = plt.subplots()
ax.scatter(x=reading, y=writing, c="seagreen", edgecolors = "darkseagreen", alpha = 0.6, s = 8)
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Correlation between reading and writing Score")


np.corrcoef(reading, writing)[0,1]
           



