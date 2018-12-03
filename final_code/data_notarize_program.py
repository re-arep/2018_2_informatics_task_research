import json
import web3

from web3 import Web3, HTTPProvider
from solc import compile_source

import Chdata

# Solidity source code
contract_source_code = '''
contract KeyValueStore {
    uint256 keyIndex;
    struct values {
        string value1;
        string value2;
    }
    mapping (uint256 => values) Obj;
    function setValue(string _value1, string _value2) constant returns (uint256) {
        Obj[keyIndex].value1 = _value1;
        Obj[keyIndex].value2 = _value2;
        keyIndex++;
        return keyIndex;
    }
    function getValue1(uint _key) constant returns (string) {
        return Obj[_key].value1;
    }
    function getValue2(uint _key) constant returns (string) {
        return Obj[_key].value2;
    }
    function Time_call() returns (uint256) {
        return now;
    }
}
'''

#Web3 setting
rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Compiled source code
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:KeyValueStore']

# Instantiate and deploy contract
Contract = w3.eth.contract(abi=contract_interface['abi'],
                          bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Contract.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("contractAddress : ",tx_receipt.contractAddress)
print("GasUsed : ",tx_receipt.cumulativeGasUsed)

# Create the contract instance with the newly-deployed address
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress,
                          abi=contract_interface['abi'])

NumBer = 0

while True:
    numb = str(input("Do you want to more?(yes or no) : "))
    if numb == 'no':
        break
    a = format(contract_instance.functions.Time_call().call())
    indata = input("input your data type(text, image, video, audio) : ")
    if indata == "text":
        data3 = str(input("input your text data path: "))
        b = Chdata.text(data3)
    elif indata == "image":
        data3 = str(input("input your image data path: "))
        b = Chdata.image(data3)
    elif indata == "video":
        data3 = str(input("input your video data path: "))
        b = Chdata.video(data3)
    elif indata == "audio":
        data3 = str(input("input your audio data path: "))
        b = Chdata.audio(data3)
    else :
        print("we not apply that type")
        b = 'dummy'

    print('Applying...')
    tx_hash = contract_instance.functions.setValue(a,b).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print("GasUsed : ",tx_receipt.cumulativeGasUsed)
    # Wait for transaction to be mined...
    w3.eth.waitForTransactionReceipt(tx_hash)

    # Display the new greeting value
    print('Contract Value time : {}'.format(contract_instance.functions.getValue1(NumBer).call()))
    print('Contract Value : {}'.format(contract_instance.functions.getValue2(NumBer).call()))
    NumBer += 1
