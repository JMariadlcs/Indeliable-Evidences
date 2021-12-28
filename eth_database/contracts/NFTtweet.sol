pragma solidity ^0.8.0;

//We first import some OpenZeppelin Contracts.
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "hardhat/console.sol";

//Used later for URI dinamycally generation on chain
import {Base64} from "./libraries/Base64.sol";

//We inherit the contract we imported. This means we'll have access
//to the inherited contract's methods.
contract EvidenceNFT is ERC721URIStorage {

    //Track of tokenIds provided by OpenZeppelin
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds; //Definition of field ID (unique for each NFT)

    //Used later to give the users a link to their OpenSea minted NFT! 
    event NewEpicNFTMinted(address sender, uint256 tokenId);

    //NFT name and symbol provided in the constructor
    constructor() ERC721 ("EvidenceNFT", "EVIDENCENFT") {
    console.log("This is the EvidenceNFT contract!");
  }
  

  // Function for actually mining the NFT
  function makeNFT(string memory _tweetURL) public {

    // Get the current tokenId (starts at 0)
    uint256 newItemId = _tokenIds.current();

    

    //Definitions of the part of the NFT URI
    string memory EvidenceNFTname = "EvidenceNFT";
    string memory EvidenceNFTdescription = "EvidenceNFT generated for serving as an evidence for the existance of tweet: ";
    string memory EvidenceNFTtime = "at time: ";
    string memory nameURI = "EvidenceNFT";
    string memory descriptionURI = string(abi.encodePacked(EvidenceNFTdescription, _tweetURL, EvidenceNFTtime, block.timestamp));

    // Get all the JSON metadata in place and base64 encode it.
        string memory json = Base64.encode(
            bytes(
                string(
                 abi.encodePacked(
                     '{"name": "',
                        // We set the title of our NFT as the generated word.
                        nameURI,
                        '", "description": "',_tweetURL,'", "image": "data:image/svg+xml;base64,',
                        // We add data:image/svg+xml;base64 and then append our base64 encode our svg.
                        Base64.encode(bytes("PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaW5ZTWluIG1lZXQiIHZpZXdCb3g9IjAgMCAzNTAgMzUwIj4KICAgIDxzdHlsZT4uYmFzZSB7IGZpbGw6IHdoaXRlOyBmb250LWZhbWlseTogc2VyaWY7IGZvbnQtc2l6ZTogMTRweDsgfTwvc3R5bGU+CiAgICA8cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJibGFjayIgLz4KICAgIDx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBjbGFzcz0iYmFzZSIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RXBpY0xvcmRIYW1idXJnZXI8L3RleHQ+Cjwvc3ZnPg==")),
                        '"}'
                    )
                )
            )
        );
    
    // Just like before, we prepend data:application/json;base64, to our data..
    string memory finalTokenUri = string(
        abi.encodePacked("data:application/json;base64,", json)
    );

        console.log("\n--------------------");
        console.log(finalTokenUri);
        console.log("--------------------\n");

     //Actually mint the NFT to the sender using msg.sender.
    _safeMint(msg.sender, newItemId);

    // Set the NFTs data.
    _setTokenURI(newItemId, finalTokenUri);

    // Increment the counter for when the next NFT is minted.
    _tokenIds.increment();
    console.log("An EvidenceNFT w/ ID %s has been minted to %s", newItemId, msg.sender);

    //Used to give the users their link to the minted NFT when the block is already minted!
    emit NewEpicNFTMinted(msg.sender, newItemId);
  }
}