from build_import import build_import
import os
import json

lookup_list = ['name', 'account']  # add the lookup field values, this
# define the path of data source file, for this example, the path of 'checkpoint import.csv'
os.chdir('G:/My Drive/example-testing')
# need to define 3 args, lookup_list, source e.g. 'chekcpoint import.csv' and specify endpoint, e.g. checkpoints
test = build_import(lookup_list, 'checkpoints import.csv', 'checkpoints')

# put the json name that you'd like to define
with open('checkpoints import.json', 'w') as outfile:
    json.dump(test, outfile)
