import os
import re

folder = r"C:\Users\fNoreen Asim.\Desktop\Important\PowerPair Sem 4\PowerPair Sem 3\Maaz"


if os.path.exists(folder):
    print("\nMatching .txt files starting with 'report':\n")
    
    for file in os.listdir(folder):
        if file.endswith(".txt") and file.lower().startswith("report"):
            print(file)
else:
    print("Folder not found. Please check the path and try again.")
