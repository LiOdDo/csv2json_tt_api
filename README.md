# csv2json_tt_api
json file convertor and api auth_N_import script

build_import.py has the function to create json import file from on datasource which is csv format
the example..py is an example demo how to use it

for api batch/file endpoint post request, would use get_token.py and import.py. 
get_token.py has the function for requesting authentication token. 
import.py use get_token function to fetch token and send json import file (generated by build_import function) to batch/file endpoint
