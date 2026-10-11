"""
Main Module: Main Module Controls Whole Workflow
""" 
from src.inspection import (
    DataInspection,
    chose_dataSet_menu,
    inspection_menu
)
from src.config import loader_animation
from src.loader import dataFrames
import time

class App:
    
    def launch(self):
        
        print("="*41)
        print("Welcome To A Student Data Analytic System")
        print("="*41)
        print("\nLoading DataSets",end="")
        loader_animation()
        print("\nDataSets Loaded Successfully\n")
        
        while True:
            print("-"*20)
            print("Main Menu of System.")
            print("-"*20)
            print("\nSelect Your Operation from Main Menu.")
            print("1: Data Inspection.")
            print("2: Data Filtering.")
            print("3: Data Refining.")
            print("4: Data Aggregiation.")
            print("5: CRUD Operations (Create|Read|Update|Delete).")
            print("6: Data Sorting.")
            print("7: Data Merging/Joining.")
            print("8: Export / Save Excel.")
            print("0: Close Application.")
            
            choice = int(input("\nEnter Choice from Above Menu: "))
            
            if choice == 1:
                inspection_obj = chose_dataSet_menu(dataFrames=dataFrames)
            elif choice == 2:
                ...
            elif choice == 3:
                ...
            elif choice == 4:
                ...
            elif choice == 5:
                ...
            elif choice == 6:
                ...
            elif choice == 7:
                ...
            elif choice == 8:
                ...
            elif choice == 0:
                print("Closing Application",end="")
                loader_animation()
                print("\nApplication Closed")
                break
            else:
                print("Invalid Choice ! Chose B/W (0-8) ")
                

if __name__ == "__main__":
    app = App()
    app.launch()