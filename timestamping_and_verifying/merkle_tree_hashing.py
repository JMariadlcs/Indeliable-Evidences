import hashlib
import csv

class MerkleTreeHash(object):
    def __init__(self):
        pass

    def compute_merkle_root(self, file_hashes):
        """
        This function creates a Merkle Tree Hash by ordering all the Hashes
        from the database where tweets are saved and then compute and return
        the value of the Merkle Tree Hash Root
        """       
        blocks = []

        if not file_hashes:
            raise ValueError('File hashes for computing merkle tree and root hash is not provided')

        #Compute merkle tree by sorting the tweet hashes
        for m in sorted(file_hashes):
            blocks.append(m)

        list_lenght = len(blocks)

        """
        Adjust the blocks of hashes until we have an even number of hashes in the blocks[]
        If an odd number is on the blocks[] append must be done to get an even one
        """
        while list_lenght % 2 != 0:
            blocks.extend(blocks[-1:])
            list_lenght = len(blocks)

        #Even number is obtained in blocks
        #Next step: separate hashes in group of 2 (leaves of the tree)
        secondary = []
        for k in [blocks[x:x+2] for x in range(0, len(blocks), 2)]:
            # k is a list with only 2 items, which is what we want
            # This is so that we can concatinate them and create a new hash from them
            hasher = hashlib.sha256()
            hasher.update(k[0].encode('utf-8') + k[1].encode('utf-8'))
            secondary.append(hasher.hexdigest())

        """
        The Merkle Root Hash is obtained if there is one 1 item left on the list
        if not, recursion must be applied until the single item is obtained and returned
        """
        if len(secondary) == 1:
            #There is only 1 item left in the list so it is the Merkle Root
            return secondary[0]
           
        else:
            #There is more than 1 item in the list, recursion is applied
            return self.compute_merkle_root(secondary)

#Method for loading Hash attribute of every tweet in the database
def get_hashes_from_database():
    with open("./tweetsdatabase.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        all_hashes = []
        next(reader)
        for row in reader:
            all_hashes.append(row[0])
    return all_hashes



