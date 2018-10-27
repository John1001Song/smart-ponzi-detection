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

#sm_file = 'Smart_Contract_Addresses.list'
sm_file='not_ponzi.csv'
path = '../dataset/'
database_bcode = path + 'bytecode_np/'

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/TO1X2JTG8k9PiaYd0iQr'))


with open(path + sm_file, 'rt') as f:
    truc = csv.reader(f)
    add = list(truc)


addresses = [pk[:42] for pklist in add for pk in pklist] 
            
# print('addresses: ', addresses)
# print('add: ', add)

# for ad in addresses:
for ad in add:
    if '0x' in ad[1]:
        with open(database_bcode + ad[1] + '.json', 'w') as f:
            # print(type(ad))
            print(ad[1])
            f.write(repr(web3.eth.getCode(web3.toChecksumAddress(ad[1])))[12:-2])
        f.close()
    #Disasemble
    #print(ad)
    #os.system('cat /Users/e31989/Documents/sm_database/bytecode/' + ad +'.json | evmdis > /Users/e31989/Documents/features/' + ad + '.json' )
    
#for /r %i in (*.json); do cat "%i" | evmdis > "/Users/e31989/Documents/features/$~ni.json"; done
#for %i in (*.json); do cat "%i" | evmdis > "/Users/e31989/Documents/features/$~ni.json"; done