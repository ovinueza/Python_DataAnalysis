import csv
import os

#Load file
file_to_load = os.path.join("Resources","election_data.csv")

#Set variables
total_votes = 0
unique_candidate_list = []
candidate_votes = {}
election_results =""
candidate_list=[]
#Create winner variable
winner=["",0]

#Start csv reader and convert to list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        #total number of votes  
        total_votes = total_votes + 1

        #specify where in csv to get candidate name
        candidate_name = row["Candidate"]

        #only append candidate name if it is a unique value not already on the list
        if candidate_name not in unique_candidate_list:
            unique_candidate_list.append(candidate_name)
            #start counting how many votes this candidate has
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        #print(candidate_votes)

    #list of chosen candidates, percentage of votes for each candidate who were chosen and votes they won
    #Loop through candidates
    for candidate in candidate_votes:
        #Create temp dictionary
        candidate_info={}
        votes = candidate_votes[candidate]
        #Fill dictionary with candidate information
        candidate_info["votes"] = votes
        candidate_info["name"] = candidate
        candidate_info["percentage"] = '{0:.3f}%'.format((votes/total_votes*100))
        candidate_list.append(candidate_info.copy())
        #Find winner
        if(votes>winner[1]):
            winner[0]=candidate
            winner[1]=votes

#Election Results Text File
file_to_output = "election_results.txt"
with open(file_to_output, "w") as txt_file:

    #Save results to election_results
    election_results = (
        f"Election Results\n"
        f"---------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------------\n")
    
    for candidate in candidate_list:
        election_results += f"{candidate['name']}: {candidate['percentage']} ({candidate['votes']})\n"
        
    election_results+= (  
        f"--------------------------------\n"
        f"Winner: {winner[0]}\n")

    print(election_results)
    txt_file.write(election_results)