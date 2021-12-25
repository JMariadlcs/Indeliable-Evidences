//Script used to simulate real ETH-Blockchain to test contracts 
//Creates a local Ethereum simulated blockchain but got destroyed after execution

//Need to run local simulator eth blockchain: npx hardhat node
//Command for deployment: npx hardhat run scripts/deploy.js --network localhost
const main = async () => {
    const Database = await hre.ethers.getContractFactory('Database');
    const databaseContract = await Database.deploy();
    await databaseContract.deployed();
    console.log("Contract deployed to:", databaseContract.address);
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