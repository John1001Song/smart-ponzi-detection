# Reproduce Document
## Data aggregation
    
1. Get ponzi data\
    [ponzi address data source](goo.gl/CvdxBp)\
	What I do: manually collect the data from the link.
	
2. Get non-ponzi\
    [non-ponzi adress data source](https://docs.google.com/spreadsheets/d/1pd9rO2Hykqhe3U9kzMyLvV23nbeP-4ILulPlT1VOqlU/edit)\
    What I do: manually collected.

3. Run import_data.py\
    This file downloads the internal and normal information of smart contracts for both ponzi and non-ponzi.
       
4. Run import_bcode.py\
    After the import_data.py finishes its job, run import_bcode.py.\
    It reads the hexi addr and downloads the bytecode for both ponzi and non-ponzi.

5. Run bcode_to_opcode.py
    After the ponzi and non-ponzi data are both downloaded, this file converts the bytecode to opcode.
    
6.    
 
    
