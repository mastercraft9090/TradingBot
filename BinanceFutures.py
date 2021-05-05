import logging
# requests allows to to get, put https responses from a server.
import requests
# this library allows us to view json content easily
import pprint


logger = logging.getLogger()
def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(response_object.status_code)
    #pprint.pprint(response_object.json())
    #We can print in the response object in the print section but here we will use pretty print
    #pprint.pprint(response_object.json()['symbols'])

    contracts = []

    for contract in response_object.json()['symbols']:
        #pprint.pprint(contract)
        #print(contract['pair'])
        contracts.append(contract['pair'])

    return contracts
print(get_contracts())
