//Execute: npx hardhat run scripts/run-nft.js

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
  
    // Call the function.
    let txn = await nftContract.makeNFT("https://twitter.com/elonmusk/status/1374617643446063105?lang=es", currentTime);
    // Wait for it to be mined.
    await txn.wait()
  
    // Mint another NFT for fun.
    txn = await nftContract.makeNFT("https://twitter.com/elonmusk/status/1374617643446063105?lang=es", currentTime);
    // Wait for it to be mined.
    await txn.wait()
  
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
  
  runMain();