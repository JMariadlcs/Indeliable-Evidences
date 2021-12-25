import tweepy
import json
import csv
import os
import hashlib

# Twitter APY keys
consumer_key = "cT33u7G9nw60gTlVJEVqPDp52"
consumer_secret = "L4jQxfFhKheLhyADER2P0ivjop0GdJXmfSXYfSUyIwrP52PdaH"
access_token = "1440638065106505736-jZRNBig4FwVhyYK6x22sejv0xMXJ4b"
access_token_secret = "KBs7mP4srzKSCPg2E8ZvU4Ebh9jAqfPYyBgPTeT0QBB9e"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def get_tweet_info(tweet_url):
    """
    This function is used to make the API call
    in order to obtain the JSON object with all the information
    from the input tweet URL
    """
    api = tweepy.API(auth,                       # Object used for the API calls
                 wait_on_rate_limit=True)

    splited = tweet_url.split('/')[-1].split('?')[0] #URL splitted to get user ID
    #print('splited is: ' + splited) #Uncomment to visualizate tweet user ID
    tweet_info_status = api.get_status(splited)  #Get tweet info
    #print(json.dumps(tweet_info_status._json, indent=4)) #Uncomment to see tweet information as JSON
    return tweet_info_status


def get_json(): 
    """
    This function is used to get an input tweet by the user 
    as an input in the terminal.
    In the input is wrong format or the tweet URL does not exist, 
    the user is asked to provided another value input.
    """  
    help = 0
    while(help == 0):   
        try:
           
            tweet_url = input("Enter tweet URL: ")    
            tweet_json = get_tweet_info(tweet_url)
            help = 1
            return tweet_json              
        except: 
            print("Tweet URL input is wrong format or does not exit. Pleasey try again.")


def json_to_CSV(status):
            """
            This function creates a CSV file and save the data from the input tweet into the CSV file
            with some of its most important attributes 
            """
            csv_file = open('tweetsdatabase.csv', 'a', encoding= 'utf-8', newline='')
            writer_in_csv = csv.writer(csv_file)
            
            if status is not False and status.text is not None:
                try:
                    texto = status.extended_tweet["full_text"]
                    print('textoes: ' + texto)
                except AttributeError:
                    texto = status.text
                texto = texto.replace('\n', ' ')
                print('Introduced tweet text: ' + texto)

                if os.stat('./tweetsdatabase.csv').st_size == 0:  #Check is file is empty to include table contents
                    table_contents = ['Tweet_Hash_Digest', 'Tweet_Hash', 'Texto', 'Created at', 'id', 'Source', 'Truncated', 
                    'in_reply_to_status_id', 'in_reply_to_user_id','in_reply_to_screen_name', 'geo', 'coordinates', 'place', 'contributor', 'lang', 'retweeted', 'user_info', 'entities'] #First line: CSV header
                    writer_in_csv.writerow(table_contents)
                
                #Tweet hasing in order to later create a Merkle Tree Hash
                string_status = str(status.created_at) + str(status.id) + str(status.text) #Concatenation of tweet date + user_id + text to get an unique string to hash
                encoded = string_status.encode()
                tweet_hash = hashlib.sha256(encoded)               
                tweet_hash_diggest = tweet_hash.hexdigest() #Hash represented in hexadecimal
                print('Your tweet input Hash is the following one, save it in a safe place because you will need it in case you want to verify it later: ' + tweet_hash_diggest)
                
                #Array containing the data we want to post in the csv file (database)
                information_to_include = [tweet_hash_diggest, tweet_hash, texto, status.created_at, 
                         status.id, status.source, status.truncated,
                         status.in_reply_to_status_id, status.in_reply_to_user_id,
                         status.in_reply_to_screen_name, status.geo, status.coordinates,
                         status.place,status.contributors, status.lang, status.retweeted, status.user, status.entities]
                information_to_include = information_to_include
                writer_in_csv.writerow(information_to_include)
     
            csv_file.close()
          
#Tweet url used to generate csv example (you can delete it and add your own tweet)
#https://twitter.com/elonmusk/status/1374617643446063105?lang=es