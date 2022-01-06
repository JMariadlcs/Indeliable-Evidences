import csv
import json
import os
from merkle_tree_hashing import get_hashes_from_database, MerkleTreeHash

#Global variables of csv_file 
#User can change them depending of the case
csvFilePath = r'tweetsdatabase.csv'

def tweet_hash_to_verify(): 
    """
    This function is used to get the tweet whose existance prior in time the user wants
    to verify as input in terminal.
    We user must enter a Hash value, in case
    of any other format input or wrong value the program will obviously 
    return that the tweet linked to the input did not existed in the past.
    """  
    help = 0
    tweet_json = 0
    while(help == 0):      
            tweet_input_hash = input("Enter tweet Hash whose existance prior in time you want to verify: ")    
            jsonFilePath = r'./verified_tweets_info/' + tweet_input_hash + '.json'
            tweet_json = make_json(csvFilePath, jsonFilePath, tweet_input_hash)
            if tweet_json != 0: #checkear que valor da si no existe (no creo que sea None)
                help = 1 

            if tweet_json == 0:          
                print("There is not a linked tweet to the Hash provided on the database, try with another Hash value.")

def ots_verifying_command(merkle_root):
    """
    This function is execute the OpenTimestamps Protocol command
    to verify the status in the Bitcon Blockchain of the input Hash Tweet
    This function internally works as executing the ots command with
    the root Hash of the Merkle Hash Tree containing the stored tweets in the database
    it was the Hash previously timestamped.
    """
    
    print('this is the merkle root: '+ merkle_root)
    txt_path = './timestamped_hashes/timestampedHash_' + merkle_root + '.txt.ots'
    ots_comand = 'ots verify ' + txt_path
    print('The executed ots command is: ' + ots_comand)
    print('The status of the blockchain timestamped of your tweet is the following: ')
    os.system(ots_comand)
    

def make_json(csvFilePath, jsonFilePath, tweet_hash):
    """
    This function is read a specified by path csvFile and
    search for the introduced Hash an element of the CSV and 
    save it in a JSON file with the information corresponding to the tweet
    """
    info = {}
     
    with open(csvFilePath, encoding='utf-8') as csvf: #Csv file is opened 
        json_not_empty = 0
        csvReader = csv.DictReader(csvf)
         
        for rows in csvReader: #Rows of CSV file are stored in 'info' dictionary
             
            key = rows['Tweet_Hash_Digest'] #Check the value of the first colum of the csv file
            if rows['Tweet_Hash_Digest'] == tweet_hash: #Search for the specific Hash value of the tweet provided as input
                info[key] = rows
                json_not_empty = 1

    if json_not_empty == 1: #Only create a json file is the Hash introduced as input exists on the tweets database
     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(info, indent=4))
        print('A json file named as the Hash input tweet has been generated containing the information of the Hash tweet provided as input. Please check your directory named verified_tweets_info.')

    return json_not_empty
         
 
if __name__ == '__main__':
    all_hashes = get_hashes_from_database() #Hashes loaded from tweets database to compute Merkle Tree Hash Root
    cls = MerkleTreeHash() 
    merkle_root = cls.compute_merkle_root(all_hashes)
    tweet_hash_to_verify()
    ots_verifying_command(merkle_root)
   