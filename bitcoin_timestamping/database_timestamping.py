import os
from merkle_tree_hashing import get_hashes_from_database, MerkleTreeHash

def merkle_root_file_creation(merkle_root):
    txt_path = './timestamped_hashes/timestampedHash_' + merkle_root + '.txt'
    file = open(txt_path, "w")
    file.write(merkle_root)
    file.close()
    print('A txt file that contains the Hash of the Merkle Root of your tweets database has been created')

def ots_timestamping_command(merkle_root):
    txt_path = './timestamped_hashes/timestampedHash_' + merkle_root + '.txt'
    ots_comand = 'ots stamp ' + txt_path
    print('The executed ots command is: ' + ots_comand)
    os.system(ots_comand)


if __name__ == '__main__':   
    all_hashes = get_hashes_from_database() #Hashes loaded from tweets database to compute Merkle Tree Hash Root
    cls = MerkleTreeHash() 
    merkle_root = cls.compute_merkle_root(all_hashes)
    print('this is the merkle root: '+ merkle_root)    
    merkle_root_file_creation(merkle_root)
    ots_timestamping_command(merkle_root)