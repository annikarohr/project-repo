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

#4 Is there a correlation between writing and reading?

plt.figure()
reading = df["reading score"]
writing = df["writing score"]

fig, ax = plt.subplots()
ax.scatter(x=reading, y=writing, c="seagreen", edgecolors = "darkseagreen", alpha = 0.6, s = 8)
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Correlation between reading and writing Score")


correlation = np.corrcoef(reading, writing)[0,1]
print(correlation)

#As you could already see from the scatterplot, there is a positive correlation of 0.95 between reading and writing scores


#5 Distribution of male and female with a pie chart

gender = df["gender"]

filter_female = df["gender"] == "female"
filter_male = df["gender"] == "male"

print(df['gender'].value_counts()['male'])     
print(df['gender'].value_counts()['female'])  

amount_male = 482
amount_female = 518

gender = ["Female", "Male"]
g_amount = [518,482]
g_colors = ["crimson", "steelblue"]


def make_autopct(g_amount):
    def my_autopct(pct):
        total = sum(g_amount)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

fig, ax = plt.subplots()
plt.pie(g_amount, labels = gender, colors = g_colors, wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'}, autopct = make_autopct(g_amount))
plt.title("Amount of Females and Males")


# catplot for gender and grades

plt.figure()
sns.countplot(x = "gender", data = df, hue = "Overall_grade", hue_order = [grade_order], palette = "Paired")
plt.xlabel("Gender")
plt.ylabel("Number of students")
plt.title("Gender Difference in Exam Performance")
plt.ylim(0, 160)


#Pie chart of course preparation

filter_completed = df["test preparation course"] == "completed"
filter_none = df["test preparation course"] == "none"

print(df['test preparation course'].value_counts()['completed'])     
print(df['test preparation course'].value_counts()['none'])  

amount_completed = 358
amount_none = 642

course_prep = ["completed", "none"]
prep_amount = [358,642]
prep_colors = ["mediumseagreen", "tomato"]

def make_autopct(prep_amount):
    def my_autopct(pct):
        total = sum(prep_amount)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

fig, ax = plt.subplots()
plt.pie(prep_amount, labels = course_prep, colors = prep_colors, wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'}, autopct = make_autopct(prep_amount))
plt.title("Course Preparation")


#Preparation for the Exam and outcome

plt.figure()
sns.countplot(x = "test preparation course", hue = "Overall_grade", data = df, hue_order = grade_order, palette = 'Paired')
plt.legend()
plt.xlabel("Preparation Course")
plt.ylabel("Number of students")
plt.title("Preparation vs. no Preparation for the Exam")
plt.ylim(0, 180)


           



