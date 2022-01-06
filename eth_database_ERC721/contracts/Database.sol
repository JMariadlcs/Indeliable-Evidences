// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.4;

import "hardhat/console.sol";

contract Database {
    uint256 totalTimesStored;

    event NewTweetStored(address indexed from, uint256 timestamp, string message);
    
    //Database struct is created
    struct database{
        address user; //Addres of the user who stores the database
        string message; //Information of the database
        uint256 timestamp; //Timestamp when the user store the database
    }

    database[] database_array;

    //We are creating a 'mapping' to prevent spams(to introduce cooldowns)
    mapping(address => uint256) public lastDatabaseStoredAt;

    constructor(){
        console.log("Database contract");
    }

    //Main function used to store the database into the ETH Blockchain
    function storeTweet(string memory _databaseString) public {
     
        //We check that current timestamp is higher than 40 secondsls than last timestamp was stored (to avoid spaming)
        require(
            lastDatabaseStoredAt[msg.sender] + 40 seconds < block.timestamp,
            "You need to wait 40 seconds before storing the database again!"
        );

        //Update the current timestamp we have for the user
        //If require is fulliled code will reach here. If not, function will finished above
        lastDatabaseStoredAt[msg.sender] = block.timestamp;

        totalTimesStored += 1;
        console.log("%s has just stored a tweet on the blockchain", msg.sender);

         database_array.push(database(msg.sender, _databaseString, block.timestamp)); //We push a database struct with its corresponding data into de database_array

         //emit of the event declared on top of the contract
        emit NewTweetStored(msg.sender, block.timestamp, _databaseString);
    
    }

    //Function for returning all the databases stored on the blockchain (array)
    function getAllTweets() public view returns (database[] memory){
        return database_array;
    }

    //Return number of databases stored (uint)
    function getTotalTweets() public view returns (uint256){
        console.log("There are %d databases stored on the blockchain", totalTimesStored);
        return totalTimesStored;
    }

}

