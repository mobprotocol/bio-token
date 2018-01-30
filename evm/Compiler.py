
import os
import sys
from web3 import Web3, TestRPCProvider
from solc import compile_source

class Compiler():
    def __init__(self, config):
        self.contract_path = config['path']

        # # setup web3 provider
        self.w3 = Web3(TestRPCProvider())


    def compile_file(self, contract_name):
        contract_path = '{0}/{1}.sol'.format(self.contract_path, contract_name)

        # open file and read solidity code
        try:
            with open (contract_path, 'r') as data:
                solidity_txt = data.read()

        except IOError:
            print('could not read file {0}'.format(contract_path))

        # compile solidity using solc @ pip install py-solc
        contracts = compile_source(solidity_txt)

        # map through contract deploying them
        for contract in contracts:
            if contracts[contract]['bin']:
                self.deploy_contract(contracts[contract])

    def deploy_contract(self, contract):
        # create web3 contract object
        contract_payload = self.w3.eth.contract(
            abi=contract['abi'],
            bytecode=contract['bin']
        )
        print(contract_payload)
        # deploy to local testrpc instance
        tx_hash = contract_payload.deploy(transaction={ 'from': self.w3.eth.accounts[0], 'gas': 410000 })
        print(tx_hash)

config = {
 'path': './evm/contracts'
}

compiler = Compiler(config)
compiler.compile_file('Greeter')
