//Execute: node --experimental-json-modules App.mjs

import { ethers } from "ethers";
import abi from './utils/Database.json';
import abi2 from './utils/EvidenceNFT.json';
import dotenv from 'dotenv';
dotenv.config();

    //Create a variable here that holds the contract address after you deploy!
    /*ContractAddress and contractABI must be changed everytime our contract is deployed
    as contract are inmutables (all variables will be reseted)*/
    const contractAddressdatabase = "0x983A29E9EEEe5cf851C6F2D99acfBc864637b747";
    const contractAddressNFT = "0x287B72B703Fd770ad8585372d84D641E422792Fe";

    //Contract address we get when deploy our contract on the backed in Rinkeby testnet
    const contractABIdatabase = abi.abi; //From the artifacts json generated in backend
    const contractABINFT = abi2.abi;

    //Provider instantiation
    const provider = new ethers.providers.AlchemyProvider('rinkeby', process.env.STAGING_ALCHEMY_KEY);

//Function used to intereact with function 'storeTweet' from SmartContract (to store tweets)
const storeTweet = async (_tweet) =>  {
    try{

        //Instatiation of wallet object using provider and PRIVATE_KEY
        const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        const signer = wallet.connect(provider);

        //Instatiation of contract object to interactuate with functions inside the contract
        const contract = new ethers.Contract(contractAddressdatabase, contractABIdatabase, signer);
        const txResponse = await contract.storeTweet(_tweet);
        console.log("Mining block...");
        const txReceipt = await txResponse.wait();
        console.log(txReceipt);


    }catch(error){
        console.log(error.toString());
    }
}

const mintNFT = async (_tweetURL, _date) => {
    try{

        //Instatiation of wallet object using provider and PRIVATE_KEY
        const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        const signer = wallet.connect(provider);

        //Instatiation of contract object to interactuate with functions inside the contract
        const contractNFT = new ethers.Contract(contractAddressNFT, contractABINFT, signer);
        const txResponse = await contractNFT.makeNFT(_tweetURL, _date);
        console.log("Mining block and minting NFT...");
        const txReceipt = await txResponse.wait();
        console.log(txReceipt);
        console.log("⭐Your NFT is already MINTED⭐ Check your OPENSEA account in rinkeby network (may take some minutes to appear).");

    }catch(error){
        console.log(error.toString());
    }
}

//Function used to intereact with function 'getAllDatabases' and 'getTotalDatabases' from SmartContract (to store tweets)
const readStoredTweets = async () => {
    try{

        //Instatiation of wallet object using provider and PRIVATE_KEY
        const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        const signer = wallet.connect(provider);

        //Instatiation of contract object to interactuate with functions inside the contract
        const contract = new ethers.Contract(contractAddressdatabase, contractABIdatabase, signer);

        const numberTweets = await contract.getTotalTweets(); //Returned uint
        console.log ("The number of total tweet stored is: " + numberTweets);

        const allTweets = await contract.getAllTweets(); //Returned array
        console.log("Every tweet stored: " + allTweets);

    }catch(error){
        console.log(error.toString);
    }
}

//Function used to calculate a Timestamp for the NFT
const getCurrentTime = async () => {
    var currentdate = new Date(); 
    var datetime = "Last Sync: " + currentdate.getDate() + "/"
                    + (currentdate.getMonth()+1)  + "/" 
                    + currentdate.getFullYear() + " @ "  
                    + currentdate.getHours() + ":"  
                    + currentdate.getMinutes() + ":" 
                    + currentdate.getSeconds();
        
        return datetime;
}


async function main(){

    console.log("Do you want to: \n -Store a tweet in database (type: '1') \n -Store a tweet in database + mint EvidenceNFT (type: '2') \n -Show all stored tweets (type: '3').");
    var stdin = process.openStdin();
    var boolintroduced = false;
    var boolstored = false;
    var boolminted = false;

    stdin.addListener("data", function(d) {

            //Case user want to store a tweet in database
            if(d==1) {
               console.log("Introduce tweet-url you want to save in database (make sure url does exist at this moment, otherwise wrong url will be saved but wont serve as a proof for you in case you need it in the future");
                
               boolintroduced = true;
               //New data input by console
                stdin.addListener("data", function(d2){
                console.log("Tweet-url introduced by user: " + d2);
                storeTweet(d2.toString().trim());
                boolstored = true;
                process.stdin.destroy();
                });

            //Case user only want to store in database + mintNFT
            }else if(d==2) {
                console.log("Introduce tweet-url you want to save in database + EvidenceNFT mint (make sure url does exist at this moment, otherwise wrong url will be saved but wont serve as a proof for you in case you need it in the future");
                stdin.addListener("data", function(d2){   

                    console.log("Tweet-url introduced by user: " + d2);

                    //Calculation of Timestamp               
                    var timestamp = Date();
                    console.log("THIS IS DATE" + timestamp);
                    storeTweet(d2.toString().trim());
                    mintNFT(d2.toString().trim(), timestamp);
                    boolminted = true;
                    boolstored = true;

                    process.stdin.destroy();
                });

            //Case user only want to show database
            }else if(d==3){
                readStoredTweets();
                process.stdin.destroy();
            
            //Case when wrong input is introduced
            }else{
                if (boolintroduced == false && boolminted == false){
                    console.log("Wrong input, execute program again.");
                    }
                    process.stdin.destroy();
            }   
    });
}

main();

/*Tweet url used to generate csv example (you can delete it and add your own tweet)
https://twitter.com/elonmusk/status/1374617643446063105?lang=es*/
