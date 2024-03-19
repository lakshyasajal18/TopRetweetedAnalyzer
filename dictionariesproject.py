def top_retweeted(tweets_file_name, num_top_retweeted):
    """
    Extracts information from a file containing tweets and returns the top users with the most retweets.

    Parameters:
    - tweets_file_name (str): The name of the file containing tweets.
    - num_top_retweeted (int): The number of top retweeted users to retrieve.

    Returns:
    - dict: A dictionary containing the top retweeted users and their respective retweet counts.
    """

    # Setting variables
    retweet_tweets = 0  
    retweet_counts = {} 
    total_tweets = 0 
    
    # Open the file for reading
    with open(tweets_file_name, 'r', encoding='utf-8') as file:
        # Iterate through each line in the file
        for line in file:
            total_tweets += 1  
            # Check if the line is a retweet
            if line.startswith('RT '):
                retweet_tweets += 1 
                # Extract the Twitter handle of the retweeted user
                retweeted_user = line.split()[1][1:].rstrip(":")
                # Update the retweet count for the user in the dictionary
                retweet_counts[retweeted_user] = retweet_counts.get(retweeted_user, 0) + 1

    # Print summary information about the tweets
    print(f'There were {total_tweets} tweets in the file, {retweet_tweets} of which were retweets.')

    # Sort the dictionary by values and get the top N items
    sorted_retweeted_users = sorted(retweet_counts.items(), key=lambda item: item[1], reverse=True)[:num_top_retweeted]
    # Create a dictionary with formatted user handles and their respective retweet counts
    top_users = {f'@{user}': count for user, count in sorted_retweeted_users}

    # Return the dictionary of top retweeted users
    return top_users

#Sample code-1
fn = "top_retweets1.txt"
nt = 6
print(top_retweeted(fn, nt))
#Sample code-2
fn = "top_retweets2.txt"
nt = 6
print(top_retweeted(fn, nt))
#Sample code-3
fn = "top_retweets3.txt"
nt = 6
print(top_retweeted(fn, nt))
