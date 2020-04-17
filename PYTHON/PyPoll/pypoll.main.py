#PyPoll
import os
import csv

# set a csv file path for the data
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# define
def results(data):

    # define variables
    total_votes_cast = 0
    votes_candidates = []
    candidate_win_counts = []
    candidates = []
    percent = []
     
    
    for row in data:

        
        total_votes_cast += 1

       
        if row[2] not in candidates:
            candidates.append(row[2])

       
        votes_candidates.append(row[2])

    
    for candidate in candidates:
        candidate_win_counts.append(votes_candidates.count(candidate))
        percent.append(round(votes_candidates.count(candidate)/total_votes_cast*100,3))


    winner = candidates[candidate_win_counts.index(max(candidate_win_counts))]
    
    #print
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes_cast}')
    print('--------------------------------')
    for i in range(len(candidates)):
        print(f'{candidates[i]}: {percent[i]}% {candidate_win_counts[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    #exit
    poll_output = os.path.join("PyPollResults.txt")

    #totextfile
    with open(poll_output, "w") as file:
        file.write('Election Results')
        file.write('\n------------------------------------')
        file.write(f'\nTotal Votes: {total_votes_cast}')
        file.write('\n------------------------------------')
        for i in range (len(candidates)):
            file.write(f'\n{candidates[i]}: {percent[i]}% {candidate_win_counts[i]}')
            file.write('\n------------------------------------')
            file.write(f'\nWinner: {winner}')
            file.write('\n------------------------------------')


# csv read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    
    # use function
    results(csvreader)
        
        