# Import dependenies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to load a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidates
candidate_options = []

# Election Data
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the data and Perform the Analysis
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

    # Loop through each row in the csv file to get the total votes cast
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add unique candidate names to the candidate list
        if candidate_name not in candidate_options:
        
            # Add new candidate name
            candidate_options.append(candidate_name)

            # Track candidate votes
            candidate_votes[candidate_name] = 0

        # Add votes to each candidate
        candidate_votes[candidate_name] +=1
    # Loop through Candidate list
    for candidate_name in candidate_votes:

        # Retreive vote count for each candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes

        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes

            winning_percentage = vote_percentage

            # Set the winning_candidate to candidate name
            winning_candidate = candidate_name

        # print candidate name and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote count: {winning_count:,}\n"
        f"Winning PErcentage: {winning_percentage:.1f}%\n"
        f"------------------------------------\n"
    )

    print(winning_candidate_summary)

    # Print the total votes
    # print(total_votes)
  
    # Print candidate list
    # print(candidate_votes)
    

    # Who won the ection by garnering the most votes?

#    print(election_data)
# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:

#    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nArapahoe")
