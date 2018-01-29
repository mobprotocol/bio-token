from solc import compile_standard
from solc import compile_source, compile_files, link_code
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
        compile_contract(data)

def compile_contract(contract):
    compiled_data = compile_source(contract)
    print(compiled_data, type(compiled_data))

if __name__ == '__main__':
    #
    assert len(sys.argv) == 2
    # start script
    main()
