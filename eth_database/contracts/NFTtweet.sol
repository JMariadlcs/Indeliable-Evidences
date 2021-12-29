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

    //Needed for using uint256 as String
    using Strings for uint256;

    //Track of tokenIds provided by OpenZeppelin
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds; //Definition of field ID (unique for each NFT)

    //Used later to give the users a link to their OpenSea minted NFT! 
    event NewEVIDENCENFTMinted(address sender, uint256 tokenId);

    //NFT name and symbol provided in the constructor
    constructor() ERC721 ("EvidenceNFT", "EVIDENCENFT") {
    console.log("This is the EvidenceNFT contract!");
  }

  // Function for actually mining the NFT
  function makeNFT(string memory _tweetURL, string memory _date) public {

    // Get the current tokenId (starts at 0)
    uint256 newItemId = _tokenIds.current();

    //Definitions of the part of the NFT JSON
    //NFTnameURI
    string memory EvidenceNFTname = "EvidenceNFT #";
    string memory itemIDuri = newItemId.toString();
    string memory NFTnameURI = string(abi.encodePacked(EvidenceNFTname, itemIDuri));
    
    //descriptionURI
    string memory EvidenceNFTdescription = "EvidenceNFT generated for serving as an evidence for the existance of tweet: ";
    string memory EvidenceNFTtime = " at time: ";
    string memory descriptionURI = string(abi.encodePacked(EvidenceNFTdescription, _tweetURL, EvidenceNFTtime, _date));
    
    //finalSVGuri
    string memory firstpartSVG = "<svg xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMinYMin meet' viewBox='0 0 350 350'><style>.base { fill: white; font-family: serif; font-size: 24px; }</style><rect width='100%' height='100%' fill='black' /><text x='50%' y='50%' class='base' dominant-baseline='middle' text-anchor='middle'> INDELIABLE ENVIDENCES <tspan x='50%' y='10%' alignment-baseline='text-before-edge'  textLength='250' lengthAdjust='spacingAndGlyphs' >";
    string memory secondpartSVG = "</tspan><tspan x='50%' y='30%' alignment-baseline='text-before-edge'  textLength='250' lengthAdjust='spacingAndGlyphs' >";
    string memory finalSVGuri = string(abi.encodePacked(firstpartSVG, _tweetURL, secondpartSVG, _date,  "</tspan></text></svg>"));


    // Get all the JSON metadata in place and base64 encode it.
        string memory json = Base64.encode(
            bytes(
                string(
                 abi.encodePacked(
                     '{"name": "',
                        // We set the title of our NFT as the generated word.
                        NFTnameURI,
                        '", "description": "',descriptionURI,'", "image": "data:image/svg+xml;base64,',
                        // We add data:image/svg+xml;base64 and then append our base64 encode our svg.
                        Base64.encode(bytes(finalSVGuri)),
                        '"}'
                    )
                )
            )
        );
    
    // Just like before, we prepend data:application/json;base64, to our data..
    string memory finalUri = string(
        abi.encodePacked("data:application/json;base64,", json)
    );

        console.log("\n--------------------");
        console.log(finalUri);
        console.log("--------------------\n");

     //Actually mint the NFT to the sender using msg.sender.
    _safeMint(msg.sender, newItemId);

    // Set the NFTs data.
    _setTokenURI(newItemId, finalUri);

    // Increment the counter for when the next NFT is minted.
    _tokenIds.increment();
    console.log("An EvidenceNFT w/ ID %s has been minted to %s", newItemId, msg.sender);

    //Used to give the users their link to the minted NFT when the block is already minted!
    emit NewEVIDENCENFTMinted(msg.sender, newItemId);
  }
}