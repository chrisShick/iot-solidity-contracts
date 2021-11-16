import json
import sys
import os
from web3 import Web3
import time

def registerDomainManager(contract, fromAccount, file):
    start = time.time()
    register_domain = contract.functions.registerDomain().transact({'from': fromAccount})
    # get the receipt of the transaction
    register_domain_tx_receipt = web3.eth.waitForTransactionReceipt(register_domain)
    end = time.time()
    t = end - start

    txt = "Register Domain Manager," + str(t) + "," + str(register_domain_tx_receipt['gasUsed']) + "\n"
    print("Register Domain Manager \t " + str(t) + " \t " + str(register_domain_tx_receipt['gasUsed']))
    file.writelines(txt)

def getDomainManager(contract, fromAccount):
    start = time.time()
    get_domain_manager = contract.functions.getDomainManager().call({'from': fromAccount})
    # get the receipt of the transaction
    end = time.time()
    t = end - start
    print('Get Domain Manager', '\t', t)
    return get_domain_manager

def registerDomain(contract, domainAccount, fromAccount, file):
    start = time.time()
    register_domain = contract.functions.registerDomain(domainAccount).transact({'from': fromAccount})
    # get the receipt of the transaction
    register_domain_tx_receipt = web3.eth.waitForTransactionReceipt(register_domain)
    end = time.time()
    t = end - start

    txt = "Register Domain," + str(t) + "," + str(register_domain_tx_receipt['gasUsed']) + "\n"
    file.writelines(txt)
    print("Register Domain \t " + str(t) + " \t " + str(register_domain_tx_receipt['gasUsed']))

def getDomain(contract, domainAccount, fromAccount):
    start = time.time()
    get_domain = contract.functions.getDomain(domainAccount).call({'from': fromAccount})
    # get the receipt of the transaction
    end = time.time()
    t = end - start
    print('Get Domain', '\t', t)
    return get_domain

def addDevice(contract, fromAccount, file):
    start = time.time()
    add_device = contract.functions.addDevice().transact({'from': fromAccount})
    # get the receipt of the transaction
    add_device_tx_receipt = web3.eth.waitForTransactionReceipt(add_device)
    end = time.time()
    t = end - start

    txt = "Add Device," + str(t) + "," + str(add_device_tx_receipt['gasUsed']) + "\n"
    file.writelines(txt)
    print("Add Device \t " + str(t) + " \t " + str(add_device_tx_receipt['gasUsed']))

# Create the ganache connection
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
# # provide default account from which to run transactions
web3.eth.defaultAccount = web3.eth.accounts[0]

# get the compile contract abi and bytecode from remix
main_abi = json.loads('[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "_domainManager", "type": "address" } ], "name": "AccountRegistered", "type": "event" }, { "inputs": [], "name": "registerDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getDomainManager", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" } ]')
main_bytecode = '608060405234801561001057600080fd5b506119e3806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063246755f51461003b578063a91d826c14610059575b600080fd5b610043610063565b6040516100509190610208565b60405180910390f35b6100616100c9565b005b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b600030336040516100d9906101dd565b6100e4929190610223565b604051809103906000f080158015610100573d6000803e3d6000fd5b509050806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f415c9c2b518f5b14d4a1dd06e9ea39351fbcf788a8000a8726eb2ad48fca781f60405160405180910390a350565b6116f9806102b583390190565b6101f38161024c565b82525050565b6102028161027e565b82525050565b600060208201905061021d60008301846101ea565b92915050565b600060408201905061023860008301856101f9565b61024560208301846101ea565b9392505050565b60006102578261025e565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061028982610290565b9050919050565b600061029b826102a2565b9050919050565b60006102ad8261025e565b905091905056fe608060405234801561001057600080fd5b506040516116f93803806116f9833981810160405281019061003291906100e4565b81600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505061019b565b6000815190506100c98161016d565b92915050565b6000815190506100de81610184565b92915050565b600080604083850312156100fb576100fa610168565b5b6000610109858286016100cf565b925050602061011a858286016100ba565b9150509250929050565b600061012f82610148565b9050919050565b600061014182610124565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600080fd5b61017681610124565b811461018157600080fd5b50565b61018d81610136565b811461019857600080fd5b50565b61154f806101aa6000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c8063893d20e814610051578063b75d88f81461006f578063d17661351461008b578063e2ffea6e146100bb575b600080fd5b6100596100eb565b60405161006691906103f5565b60405180910390f35b61008960048036038101906100849190610378565b610114565b005b6100a560048036038101906100a09190610378565b6102ba565b6040516100b291906103f5565b60405180910390f35b6100d560048036038101906100d09190610378565b610323565b6040516100e29190610439565b60405180910390f35b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146101a3576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161019a90610454565b60405180910390fd5b600030836040516101b390610356565b6101be929190610410565b604051809103906000f0801580156101da573d6000803e3d6000fd5b50905080600260008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508073ffffffffffffffffffffffffffffffffffffffff163073ffffffffffffffffffffffffffffffffffffffff167f8a2a2ec1b46df2173b6b2ce7c17cd9ed571165f55f4780884162bad7c36bf69b60405160405180910390a3505050565b6000600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b60026020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b610fd58061054583390190565b6000813590506103728161052d565b92915050565b60006020828403121561038e5761038d6104ff565b5b600061039c84828501610363565b91505092915050565b6103ae81610485565b82525050565b6103bd816104b7565b82525050565b6103cc816104c9565b82525050565b60006103df601683610474565b91506103ea82610504565b602082019050919050565b600060208201905061040a60008301846103a5565b92915050565b600060408201905061042560008301856103b4565b61043260208301846103a5565b9392505050565b600060208201905061044e60008301846103c3565b92915050565b6000602082019050818103600083015261046d816103d2565b9050919050565b600082825260208201905092915050565b600061049082610497565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006104c2826104db565b9050919050565b60006104d4826104db565b9050919050565b60006104e6826104ed565b9050919050565b60006104f882610497565b9050919050565b600080fd5b7f53656e646572206e6f7420617574686f72697a65642e00000000000000000000600082015250565b61053681610485565b811461054157600080fd5b5056fe60806040523480156200001157600080fd5b5060405162000fd538038062000fd583398181016040528101906200003791906200011c565b81600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506000600160146101000a81548160ff02191690836001811115620000e157620000e0620001ab565b5b0217905550505062000213565b600081519050620000ff81620001df565b92915050565b6000815190506200011681620001f9565b92915050565b60008060408385031215620001365762000135620001da565b5b6000620001468582860162000105565b92505060206200015985828601620000ee565b9150509250929050565b600062000170826200018b565b9050919050565b6000620001848262000163565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b600080fd5b620001ea8162000163565b8114620001f657600080fd5b50565b620002048162000177565b81146200021057600080fd5b50565b610db280620002236000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c80631865c57d1461005c57806343baf5e51461007a578063893d20e814610084578063a008f709146100a2578063a9815351146100ac575b600080fd5b6100646100b6565b60405161007191906106c0565b60405180910390f35b6100826100cd565b005b61008c6102d8565b604051610099919061067c565b60405180910390f35b6100aa610301565b005b6100b4610476565b005b6000600160149054906101000a900460ff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461015c576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610153906106fb565b60405180910390fd5b600060018111156101705761016f61083b565b5b600160149054906101000a900460ff1660018111156101925761019161083b565b5b146101d2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101c9906106db565b60405180910390fd5b6000306003546040516101e4906105ed565b6101ef929190610697565b604051809103906000f08015801561020b573d6000803e3d6000fd5b5090508060026000600354815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060036000815480929190610275906107c3565b91905055508073ffffffffffffffffffffffffffffffffffffffff163073ffffffffffffffffffffffffffffffffffffffff167ffe60226b9c524c49ff3f012aea1c16166e24616cba2a64f33ad1befdf911891860405160405180910390a35050565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610390576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610387906106fb565b60405180910390fd5b600060018111156103a4576103a361083b565b5b600160149054906101000a900460ff1660018111156103c6576103c561083b565b5b14610406576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103fd906106db565b60405180910390fd5b60018060146101000a81548160ff0219169083600181111561042b5761042a61083b565b5b02179055503073ffffffffffffffffffffffffffffffffffffffff167f8ab8db78b8d08dfcc8b14f9bc4ae6c2da7482fb0f1dccc1afe43e94ce1d612b960405160405180910390a250565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610507576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104fe906106fb565b60405180910390fd5b6000600181111561051b5761051a61083b565b5b600160149054906101000a900460ff16600181111561053d5761053c61083b565b5b1461057d576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610574906106db565b60405180910390fd5b60018060146101000a81548160ff021916908360018111156105a2576105a161083b565b5b02179055503073ffffffffffffffffffffffffffffffffffffffff167f8ab8db78b8d08dfcc8b14f9bc4ae6c2da7482fb0f1dccc1afe43e94ce1d612b960405160405180910390a250565b6104ac806108d183390190565b6106038161072c565b82525050565b6106128161077b565b82525050565b6106218161078d565b82525050565b600061063460128361071b565b915061063f8261086a565b602082019050919050565b600061065760168361071b565b915061066282610893565b602082019050919050565b61067681610771565b82525050565b600060208201905061069160008301846105fa565b92915050565b60006040820190506106ac6000830185610609565b6106b9602083018461066d565b9392505050565b60006020820190506106d56000830184610618565b92915050565b600060208201905081810360008301526106f481610627565b9050919050565b600060208201905081810360008301526107148161064a565b9050919050565b600082825260208201905092915050565b600061073782610751565b9050919050565b600081905061074c826108bc565b919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b60006107868261079f565b9050919050565b60006107988261073e565b9050919050565b60006107aa826107b1565b9050919050565b60006107bc82610751565b9050919050565b60006107ce82610771565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8214156108015761080061080c565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b7f446f6d61696e206e6f74206163746976652e0000000000000000000000000000600082015250565b7f53656e646572206e6f7420617574686f72697a65642e00000000000000000000600082015250565b600281106108cd576108cc61083b565b5b5056fe608060405234801561001057600080fd5b506040516104ac3803806104ac833981810160405281019061003291906100ab565b81600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600181905550505061016c565b6000815190506100908161013e565b92915050565b6000815190506100a581610155565b92915050565b600080604083850312156100c2576100c1610139565b5b60006100d085828601610081565b92505060206100e185828601610096565b9150509250929050565b60006100f68261010f565b9050919050565b6000610108826100eb565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b600080fd5b610147816100fd565b811461015257600080fd5b50565b61015e8161012f565b811461016957600080fd5b50565b6103318061017b6000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c80631aa3a00814610030575b600080fd5b61003861003a565b005b6000600181111561004e5761004d61027a565b5b600260159054906101000a900460ff1660018111156100705761006f61027a565b5b146100b0576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100a790610229565b60405180910390fd5b600060018111156100c4576100c361027a565b5b600260149054906101000a900460ff1660018111156100e6576100e561027a565b5b1415610127576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161011e90610249565b60405180910390fd5b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163073ffffffffffffffffffffffffffffffffffffffff167fd1bf5725f9e2c326501a9777c6a5a3819cd20ac3c16efa678f1c596ddbcc03e260405160405180910390a3565b60006101f0601283610269565b91506101fb826102a9565b602082019050919050565b6000610213601983610269565b915061021e826102d2565b602082019050919050565b60006020820190508181036000830152610242816101e3565b9050919050565b6000602082019050818103600083015261026281610206565b9050919050565b600082825260208201905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b7f446576696365206e6f74206163746976652e0000000000000000000000000000600082015250565b7f44657669636520416c726561647920526567697374657265640000000000000060008201525056fea2646970667358221220157f289f1b5b8c981787aa317f5750dbc37589f1a697a8160b358e08760153c164736f6c63430008070033a264697066735822122088f9d38648e213a6391898684164b195f3c85c91461559e90b6699ae659156f564736f6c63430008070033a26469706673582212209e6bed546bd762a8c085d6626a571749d0a16ca21a5d7092eda6bf16cefcc08c64736f6c63430008070033a26469706673582212206322edcb6f26935919f7309619ebda57c2cc549dd45a66b22241dd379ab099d464736f6c63430008070033'

domain_manager_abi = json.loads('[ { "inputs": [ { "internalType": "contract Iot", "name": "_parentContract", "type": "address" }, { "internalType": "address", "name": "_account", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "_domain", "type": "address" } ], "name": "DomainRegistered", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "domains", "outputs": [ { "internalType": "contract Domain", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_domainKey", "type": "address" } ], "name": "getDomain", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_domainKey", "type": "address" } ], "name": "registerDomain", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')
domain_abi = json.loads('[ { "inputs": [ { "internalType": "contract DomainManager", "name": "_parentContract", "type": "address" }, { "internalType": "address", "name": "_publicKey", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_domain", "type": "address" }, { "indexed": true, "internalType": "address", "name": "_device", "type": "address" } ], "name": "DeviceAdded", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_domain", "type": "address" } ], "name": "DomainDeactived", "type": "event" }, { "inputs": [], "name": "addDevice", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "deactive", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getState", "outputs": [ { "internalType": "enum Domain.State", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "parentDeactive", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')
device_abi = json.loads('[ { "inputs": [ { "internalType": "contract Domain", "name": "_parentContract", "type": "address" }, { "internalType": "uint256", "name": "_index", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "_device", "type": "address" }, { "indexed": true, "internalType": "address", "name": "_account", "type": "address" } ], "name": "DeviceRegistered", "type": "event" }, { "inputs": [], "name": "register", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')

f1 = open("output.csv","w")
# create the contract
IotContract = web3.eth.contract(abi=main_abi, bytecode=main_bytecode)
start = time.time()
tx_hash = IotContract.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
end = time.time()
t = end - start

header = "Account, Action, Time, Gas Used \n"
f1.writelines(header)
print(header)
print("Deployed \t" + str(t) + "\t" + str(tx_receipt['gasUsed']))
f1.writelines(str(web3.eth.accounts[0]) + ",Deployed," + str(t) + "," + str(tx_receipt['gasUsed']) + "\n")


contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=main_abi
)

maxDomainManagers = 3
maxDomains = 6
maxDevices = 13
i = 1
currentPointer = 0
while (i <= maxDomainManagers):
    j = 1
    dmAccAddress = web3.eth.accounts[currentPointer]
    registerDomainManager(
        contract=contract,
        fromAccount=dmAccAddress,
        file=f1
    )
    domainManagerAddress = getDomainManager(
        contract=contract,
        fromAccount=dmAccAddress
    )
    domainManagerContract = web3.eth.contract(
        address=domainManagerAddress,
        abi=domain_manager_abi
    )
    i += 1
    currentPointer += 1
    while (j <= maxDomains):
        x = 1
        dAccAddress = web3.eth.accounts[currentPointer]
        registerDomain(
            contract=domainManagerContract,
            fromAccount=dmAccAddress,
            domainAccount=dAccAddress,
            file=f1
        )
        domainAddress = getDomain(
            contract=domainManagerContract,
            fromAccount=dmAccAddress,
            domainAccount=dAccAddress
        )
        domainContract = web3.eth.contract(
            address=domainAddress,
            abi=domain_abi
        )
        j += 1
        currentPointer += 1
        while (x <= maxDevices):
            addDevice(
                contract=domainContract,
                fromAccount=dAccAddress,
                file=f1
            )
            x += 1
            currentPointer += 1

f1.close()
