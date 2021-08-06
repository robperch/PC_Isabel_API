## MODULE TO EXECUTE EVERYTIME A USER WANTS TO USE THE API SO THAT THE MENUS ARE UPDATED CALLING THE API





"----------------------------------------------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Standard library imports
import requests


## Third party imports


## Local application imports
from src.utils.isabel_funcs import (
    url_api_request,
    enhance_api_response,
    write_json,
)

from src.utils.isabel_params import (
    inout_files,
    out_loc,
    isabel_api_params,
)





"----------------------------------------------------------------------------------------------------------------------"
###################
## Main function ##
###################

## Main function to populate all menus in user interface
def main_func_pop_menus():
    """
    Main function to populate all menus in user interface

    :return none:
    """

    ## Executing all methods with data for the GUI

    #### List of methods relevant to the GUI
    methods = [mthd for mthd in isabel_api_params["methods"] if isabel_api_params["methods"][mthd]["usage"] == "GUI"]

    #### Loop to update the output files of every selected method
    for method in methods:

        ###### Building the URL required for the API requests
        api_call_url = url_api_request(method)

        ###### Sending the request to the API
        req = requests.get(api_call_url)

        ###### Formatting and enhancing the response
        api_resp = enhance_api_response(req.text)

        ###### Writing result in output file
        path = out_loc + inout_files[method]["output"]
        write_json(path, req.text)

    return







"----------------------------------------------------------------------------------------------------------------------"
################################
## Execution of main function ##
################################

## Automate execution of main function
if __name__ == "__main__":
    main_func_pop_menus()





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
