

"""
Config module: Store configurations of project
"""

import pandas 
import time


STUDENT_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\students.csv"

COURSES_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\courses.csv"

FEES_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\fees.csv"

ATTENDANCE_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\attendance.csv"

MARKS_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\marks.csv"

ACTIVITIES_DATASET_PATH = r"D:\Advance_Python\projects\universty_data_analytics\data\activities.csv"



def loader_animation():
    time.sleep(0.85)
    print(".",end="")
    time.sleep(0.85)
    print(".",end="")
    time.sleep(0.85)
    print(".",end="")