"""Q4. Student Score Tracker (Dictionary + Function)
Task:
Ask the user to enter names and marks of 3 students (name: mark).
Store in a dictionary.
Create a function top_scorer(score_dict) that:
Returns the name of the student with the highest mark.
📌 Use: dictionary, function, max logic """

import math

def top_scorer(score_dict):

    marks=max(score_dict.values())
    for name, score in score_dict.items():
        if score==marks:
            print(f'{name}:{marks}')
top_scorer(score_dict={
    "Neha Gayen":90,
    "Max Adit":75,
    "Scott Charch":89
})