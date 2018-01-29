from solc import compile_standard
from solc import compile_source, compile_files, link_code
from web3 import Web3, TestRPCProvider
import os
import json
import sys

'''
    python3 evm/compile.py [contract_name]
'''

def main():
    contract_path = './evm/contracts/{0}.sol'.format(sys.argv[1])

    # make sure contract exists in file-system
    assert os.path.exists(contract_path)

    # read text from solidity file
    with open(contract_path, 'r') as contract:
        data = contract.read()

    # comile contract and return json interface
    interface = compile_contract(data)

    # setup web3 provider to testrpc
    w3 = Web3(TestRPCProvider())

    deploy_contract(interface, w3)


def compile_contract(contract):
    compiled_data = compile_source(contract)
    return compiled_data['<stdin>:{0}'.format(sys.argv[1])]

def deploy_contract(interface, w3):
    print(interface['bin'])
    contract = w3.eth.contract(
        abi=interface['abi'],
        bytecode=interface['bin'])
    print(contract, type(contract))

    tx_hash = contract.deploy(transaction={ 'from': w3.eth.accounts[0], 'gas': 410000 })
    print(tx_hash)



if __name__ == '__main__':
    #
    assert len(sys.argv) == 2
    # start script
    main()
