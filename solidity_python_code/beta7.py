import json
import web3

from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.21;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
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
contract_interface = compiled_sol['<stdin>:Greeter']

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'],
                          bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)
# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)
print(greeter)
# Display the default greeting from the contract
print('Default contract greeting: {}'.format(
    greeter.functions.greet().call()
))

print('Setting the greeting to Nihao...')
tx_hash = greeter.functions.setGreeting('Nihao').transact()
print(tx_hash)
# Wait for transaction to be mined...
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    greeter.functions.greet().call()
))

