#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 --------------------------------------------------------------------------------
 SPADE - Support for Provenance Auditing in Distributed Environments.
 Copyright (C) 2015 SRI International
 This program is free software: you can redistribute it and/or
 modify it under the terms of the GNU General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program. If not, see <http://www.gnu.org/licenses/>.
 --------------------------------------------------------------------------------

"""

from web3 import Web3
import csv
import pandas as pd
import numpy as np
from os.path import isfile, join
from os import listdir
import os

# sm_file = 'Smart_Contract_Addresses.list'
# sm_file = 'sm_add_nponzi.csv'
path = '../'
database_bcode = path + 'dataset/'

ponzi_addr_csv_path = '../dataset/ponzi_dataset/ponzi_collection.csv'
ponzi_bytecode_path = '../dataset/ponzi_dataset/bytecode/'
ponzi_opcode_path = '../dataset/ponzi_dataset/opcode/'

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/TO1X2JTG8k9PiaYd0iQr'))


def get_all_file_name(file_path):
    # get all files names
    files_names = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    name_array = []

    for name in files_names:
        if ".json" in name:
            name_array.append(name)

    return name_array


def download_bytecode(address_csv_path, bytecode_path):
    with open(address_csv_path) as f:
        df = pd.read_csv(f)

    address_list = df['Address']
    print(address_list)

    i = 0
    for ad in address_list:
        code = repr(web3.eth.getCode(web3.toChecksumAddress(ad)))[12:-2]
        if code:
            i += 1
            with open(bytecode_path + ad + '.json', 'w') as f:
                f.write(code)
                print(ad, ' is finished.')
            f.close()
        else:
            print(ad, 'cannot be processed.')
        # Disasemble
        # print(ad)
        # os.system('cat /Users/e31989/Documents/sm_database/bytecode/' + ad +'.json | evmdis > /Users/e31989/Documents/features/' + ad + '.json' )

    # for /r %i in (*.json); do cat "%i" | evmdis > "/Users/e31989/Documents/features/$~ni.json"; done
    # for %i in (*.json); do cat "%i" | evmdis > "/Users/e31989/Documents/features/$~ni.json"; done


def convertToOpCode(bytcode_path, opcode_path):
    file_list = get_all_file_name(bytcode_path)
    for bytecode_file in file_list:
        os.system(
            'cat ' + bytcode_path + bytecode_file + ' | /Users/Jinyue/go/bin/evmdis > ' + opcode_path + bytecode_file)
        print(bytecode_file, ' is converted to opcode.')


if __name__ == '__main__':
    download_bytecode(ponzi_addr_csv_path, ponzi_bytecode_path)
    # convertToOpCode(ponzi_bytecode_path, ponzi_opcode_path)
