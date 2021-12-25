from jsontweet_to_database import get_json, json_to_CSV
from merkle_tree_hashing import get_hashes_from_database, MerkleTreeHash
import os
 
if __name__ == '__main__':           
    tweet_json  = get_json() #Tweet JSON obtained
    json_to_CSV(tweet_json)
    all_hashes = get_hashes_from_database() #Hashes loaded from tweets database to compute Merkle Tree Hash Root
    cls = MerkleTreeHash() 
    merkle_root = cls.compute_merkle_root(all_hashes)
    print('Merkle Tree Hash Root : {0}'.format(merkle_root))
  