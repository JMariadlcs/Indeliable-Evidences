//Execute: npx hardhat run scripts/deploy-nft.js --network rinkeby

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

const main = async () => {
    const nftContractFactory = await hre.ethers.getContractFactory('EvidenceNFT');
    const nftContract = await nftContractFactory.deploy();
    await nftContract.deployed();
    console.log("Contract deployed to:", nftContract.address);

    //Calculation of currentTime
    var currentTime = (await getCurrentTime()).toString();
  
    // Call the function. (Tweet example)
    let txn = await nftContract.makeNFT("https://twitter.com/elonmusk/status/1374617643446063105?lang=es", currentTime);
    // Wait for it to be mined.
    await txn.wait();
    console.log("⭐Your NFT is already MINTED⭐ Check your OPENSEA account in rinkeby network (may take some minutes to appear).");
  };
  
  const runMain = async () => {
    try {
      await main();
      process.exit(0);
    } catch (error) {
      console.log(error);
      process.exit(1);
    }
  };
  
  runMain();