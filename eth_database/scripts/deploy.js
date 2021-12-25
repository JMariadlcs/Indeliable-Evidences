//Script used to create a local network alive on Rinkeby Network
//Command for deployment: npx hardhat run scripts/deploy.js --network rinkeby

const main = async () => {
    const [deployer] = await hre.ethers.getSigners();
    const accountBalance = await deployer.getBalance();
  
    console.log('Deploying contracts with account: ', deployer.address);
    console.log('Account balance: ', accountBalance.toString());
  
    const Token = await hre.ethers.getContractFactory('Database');
    const databaseContract = await Token.deploy();
    await databaseContract.deployed();
  
    console.log('Database address: ', databaseContract.address);
  };
  
  const runMain = async () => {
    try {
      await main();
      process.exit(0);
    } catch (error) {
      console.error(error);
      process.exit(1);
    }
  };
  
  runMain();