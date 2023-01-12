# Import dependenies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to load a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the data and Perform the Analysis
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)


    # How many total votes were cast?
    # List candidates who received votes
    # How many total votes did each candidate receive?
    # What percentage of the vote did each candidate get?
    # Who won the ection by garnering the most votes?

#    print(election_data)
# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nArapahoe")
