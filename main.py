# 
#import csv
#import json
#import logging
#import os

# 1. Create project folder
#PROJECT_FOLDER = "data_pipeline"

#os.makedirs(PROJECT_FOLDER, exist_ok=True)

# 2. File names
#config_file = os.path.join(PROJECT_FOLDER, "config.json")
#input_file = os.path.join(PROJECT_FOLDER, "input.csv")
#output_file = os.path.join(PROJECT_FOLDER, "output.csv")
#log_file = os.path.join(PROJECT_FOLDER, "pipeline.log")
#readme_file = os.path.join(PROJECT_FOLDER, "README.md")
#requirements_file = os.path.join(PROJECT_FOLDER, "requirements.txt")

# 3. Create configuration file
#config = {
#    "input_file": "input.csv",
#    "output_file": "output.csv",
#    "missing_age": 0,
#    "missing_marks": 0
#}

#with open(config_file, "w") as file:
#    json.dump(config, file, indent=4)

# 4. Set up logging
#logging.basicConfig(
#    filename=log_file,
#    level=logging.INFO,
#    format="%(asctime)s - %(levelname)s - %(message)s"
#)

#logging.info("Data processing pipeline started")

# 5. Create sample input CSV
#sample_data = [
#    ["name", "age", "marks", "email"],
#    ["Ravi", "20", "85.5", "ravi@gmail.com"],
#    ["Sita", "", "90", "sita@gmail.com"],
#    ["Arun", "abc", "75", ""],
#    ["Meena", "21", "", "meena@gmail.com"],
#    ["", "19", "88", "unknown@gmail.com"]
#]

#with open(input_file, "w", newline="") as file:
#    writer = csv.writer(file)
#    writer.writerows(sample_data)

#logging.info("Input CSV file created")

# 6. Read and clean the data
#cleaned_data = []

#with open(input_file, "r", newline="") as file:
#    reader = csv.DictReader(file)

#    for row in reader:
#        # Handle missing name
#        name = row.get("name", "").strip()

#        if name == "":
#            name = "Unknown"

#        # Convert age into integer
#        try:
#            age = int(row.get("age", "").strip())

#            if age < 0 or age > 120:
#                age = 0

#        except (ValueError, TypeError):
#            age = 0

#        # Convert marks into float
#        try:
#            marks = float(row.get("marks", "").strip())

#            if marks < 0 or marks > 100:
#                marks = 0

#        except (ValueError, TypeError):
#            marks = 0

#        # Handle missing email
#        email = row.get("email", "").strip()

#        if email == "":
#            email = "not_provided"

#        # Add cleaned record
#        cleaned_data.append({
#            "name": name,
#            "age": age,
#            "marks": marks,
#            "email": email
#        })

#logging.info("Missing values handled")
#logging.info("Data types converted")

# 7. Write cleaned data to output CSV
#with open(output_file, "w", newline="") as file:
#    fieldnames = ["name", "age", "marks", "email"]

#    writer = csv.DictWriter(file, fieldnames=fieldnames)
#    writer.writeheader()
#    writer.writerows(cleaned_data)

#logging.info("Cleaned output CSV created")
#logging.info("Data processing pipeline completed")

# 8. Create README file
#readme_content = """# Data Processing Pipeline

## Project Description
#This project reads raw data from a CSV file,
#cleans the data, converts data types,
#handles missing values, and creates
#a cleaned output CSV file.

## Features
#- Reads CSV input data
#- Handles missing values
#- Converts age to integer
#- Converts marks to float
#- Handles invalid values
#- Creates output CSV
#- Implements logging
#- Uses configuration management

## How to Run
#1. Install Python 3.
#2. Run main.py.
#3. Check the data_pipeline folder.
#4. Open output.csv to see cleaned data.

## Files
#- main.py: Main Python program
#- input.csv: Raw input data
#- output.csv: Cleaned data
#- config.json: Configuration settings
#- pipeline.log: Log file
#- requirements.txt: Required libraries
#"""

#with open(readme_file, "w") as file:
#    file.write(readme_content)

# 9. Create requirements.txt
#with open(requirements_file, "w") as file:
#    file.write("# No external libraries required\n")

#print("================================")
#print("DATA PROCESSING PIPELINE")
#print("================================")
#print("Pipeline completed successfully!")
#print()
#print("Created folder:", PROJECT_FOLDER)
#print("Created files:")
#print("- input.csv")
#print("- output.csv")
#print("- config.json")
#print("- pipeline.log")
#print("- README.md")
#print("- requirements.txt")
#print()
#print("Cleaned data:")
#print()

#for record in cleaned_data:
#    print(record)
