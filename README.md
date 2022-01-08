<p align = "center">
<img src = "https://github.com/JMariadlcs/Indeliable-Evidences/blob/main/logo.png" />
</p>

<badges align = "center">
 ![GitHub language count](https://img.shields.io/github/languages/count/JMariadlcs/Indeliable-Evidences) ![GitHub last commit](https://img.shields.io/github/last-commit/JMariadlcs/Indeliable-Evidences) ![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)  ![donations](https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat) />
</badges>

A Timestamping service over Bitcoin blockchain and a parallel process for proving ownership by ERC-721 standar and token generation developed on a Ethereum database implementation.

[Usage](#Usage)


# Features
- Tweet timestamping over Bitcoin blockchain.
- Incorruptible database generation due to hashing implementation.
- Smart contracts usage for Ethereum database development.
- ERC-721 dynamic on chain token generation for proving timestamping ownership.

# Tech
Indeliable Evidences uses a number of open source projects to work properly:

- [opentimestamps] - for the timestamping service over bitcoin blockchain
- [node.js] - evented I/O for the backend
- [hardhat] - for the blockchain management part
- [ethers.js] - librarie for interacting with Ethereum blockchain
- [nomic labs] - for Ethereum database development
- [alchemy] - for Rinkeby network set up
- [open zeppelin] - auxiliar smart contract providers
- [tweepy] - for twitter API management

Indeliable Evidences is also an open source project with a [public repository][ie] on Github.

# Usage

All the required dependencies and libraries needed for the execution of the project are included in [requirements.txt](https://github.com/JMariadlcs/Indeliable-Evidences/blob/main/requirements.txt)

Indeliable Evidence is formed by two parallel processes, the [Bitcoin timestamping process](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/bitcoin_timestamping) and the [Ethereum database + ERC721 token generation](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/eth_database_ERC721) one.

Both processes form a whole timestamping and verification project whose prototype is detailed below.

<p align = "center">
<img src = "https://github.com/JMariadlcs/Indeliable-Evidences/blob/main/prototype_design/FULLSERVICE.png" />
</p>

## BITCOIN TIMESTAMPING AND VERFICIATION
### Bitcoin Timestamping

For using the Bitcoin timestamping service, user must:

- install the [OpenTimestamp client](https://github.com/opentimestamps/opentimestamps-client).
- dive into the [bitcoin_timestamping](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/bitcoin_timestamping) directory.

&#8594; **Adding tweet to database**
```bash
python3 add_tweet_to_database.py
```

You will be ask to introduce a tweet URL as input of the program. If the input is wrong format you will be asked to repeat the action.
If the input is correctly introduced you will receive a `hash` for the introduced tweet. You should keep this hash in a safe place because this will be the key used for the verification process.
You will also notice that a `.csv` file is created containing all the tweet metadata and the previously metioned hash.

&#8594; **Database timestamping**
```bash
python3 database_timestamping.py
```

You will notice that a `.txt` file inside [timestamped_hashed](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/bitcoin_timestamping/timestamped_hashes) directory has been generated and that the Opentimestamp `ots stamp` command is being executed.

After following the previously steps your database should be in process of being timestamped, you just need to wait until the OpenTimestamp protocol has finished doing its job.

### Timestamping verification

Make sure you are inside the [bitcoin_timestamping directory](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/bitcoin_timestamping).

&#8594; **Timestamping verification**
```bash
python3 verify_tweet.py
```

You will be asked to introduce a tweet hash. The hash you must introduced is one genereated for your input tweet when you executed the timestamping process.
Once you have introduced the corresponding hash, if the tweet is included in the database you will receive the timestamping proof from the OpenTimestamp protocol because of the `ots verify` command and a `.json` object will be generated inside the [verified_tweets_info](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/bitcoin_timestamping/verified_tweets_info) directory containing all the metadata from your tweet.

## ETHEREUM DATABASE + ERC-721 TOKEN GENEATION

For using the Ethereum datatabase and ERC-721 token geneartion service, user must:

- Have an Ethereum account.
- Have Rinkeby Network configured.
- Have funds (`eth`) inside the wallet: funds can be request from a [faucet](https://faucet.rinkeby.io/).
- For interacting with the smart contracts, the user must create a `.env` file.
- Node.js must be installed

Inside the file the following variables must be declared:

- STAGING_ALCHEMY_KEY: Alchemy key can be generated [here](https://www.alchemy.com/).
- PRIVATE_KEY: Ethereum private key.

For executing the process make sure you are inside [App](https://github.com/JMariadlcs/Indeliable-Evidences/tree/main/App/src) directory.

&#8594; **Process execution**
```bash
node --experimental-json-modules App.mjs
```

After that you will be asked for choosing between:



- Store an evidence in database (type: '1')
    - Store an evidence in database + mint EvidenceNFT (type: '2')
    - Show all stored evidences (type: '3')

If you choose the first and second options you will need to introduce a tweet URL and it will be stored on the database and in the second case a ERC-721 standard token (NFT) will be generated containing the tweet url + timestamp in the image and description.

After some minutes you can have a look to your NFT using [Opensea Rinkeby](https://testnets.opensea.io/).

# Contributing

Contributions are welcome!⭐
Please take a look at the [contributing](https://github.com/JMariadlcs/Indeliable-Evidences/blob/main/CONTRIBUTING.md) guidelines if you are willing to help!

# Licence

Indeliable Evidences is an open-source project.

# Donations

Donations are always helpfull for open-source project developers🤠
&#8594; Ethereum address: 0x0aEbeBee37D530961e05FF525409801Ab97341dE
&#8594; Bitcoin address: 1E4Yr47RPL1CDrRe3SrnmkwQPHguMB3gaz




#
 [node.js]: <http://nodejs.org>
[opentimestamps]: <https://github.com/opentimestamps>
[hardhat]: <https://hardhat.org/>
[ie]: <https://github.com/JMariadlcs/Indeliable-Evidences>
[tweepy]: <https://www.tweepy.org/>
[nomic labs]: <https://github.com/nomiclabs>
[open zeppelin]: <https://openzeppelin.com/>
[ethers.js]: <https://docs.ethers.io/v5/>
[alchemy]: <https://www.alchemy.com/>
