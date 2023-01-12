# Election_Analysis

---
## Project overview

---
The following tasks were completed for the Colorado Board of Elections for an election audit in a local congressional election.

1. Calculate the total number of votes cast in the congressional district.
2. Create a list of all candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Determine the winner of the election.

---
## Resources

---
* Source data: election_results.csv
* Software used: 
  - Python 3.7.6
  - VS Code 1.74.3
* Output file: election_analysis.txt


---
## Summary

---
* Total Votes cast:  369,711
* Candidates, vote percentage received, and raw votes received
  - Charles Casper Stockham; 23.0%; 85,213
  - Diana DeGette; 73.8%; 272,892
  - Raymon Anthony Doane; 3.1%; 11,606
* The winner of the election was Diana DeGette with 73.8% of the vote (272,892 votes received).

---
## Challenge

---
### Election Audit Overview

---
The election audit was requested by the Coloroado Board of Elections, and it tracks the voter turnout by county and the election results by candidate. If this analysis tool works accurately and efficiently, it may be deployed to additional elections in Colorado at both the state and local level.

---
### Election Audit Results

---
The audit results are as follows:
* Total Votes Cast: 369,711
* Votes by County
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
* **Denver** had the largest voter Turnout.
* Votes for each canidate:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
* Winning Candidate
  - **Diana DeGette**
  - Vote Count: 272,892
  - Percentage: 73.8%

---
### Election Audit Summary

---
This script can be used for any number of candidates in any election that has a single winner, assuming that the data is structured similarly to the data provided. If it structured differently, small adjustments can be made (the column designator for the Candidates and County). Likewise, precincts can be substituted for counties for state-wide elections. For elections that have multiple winners (top two or more vote-getters), the code would need more extensive modifications to call the winner but could still be used tio tabulate votes.
