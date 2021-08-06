## MODULE TO GET ALL INFORMATION CAPTURED BY THE CLIENT AND CALL ISABEL API TO GET RDD





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
    write_json
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

## Main operative function to automate rdd's requests to API
def main_func_rdd():
    """
    Main function to automate rdd's requests to API

    :return none:
    """

    ## Building the URL required for the API request
    method = [mthd for mthd in isabel_api_params["methods"] if isabel_api_params["methods"][mthd]["usage"] == "rdd"][0]
    api_call_url = url_api_request(method)

    ## Sending the request to the API
    req = requests.get(api_call_url)

    ## Formatting and enhancing the response
    api_resp = enhance_api_response(req.text)

    ## Writing result in output file
    path = out_loc + inout_files[method]["output"]
    write_json(path, req.text)

    return





"----------------------------------------------------------------------------------------------------------------------"
################################
## Execution of main function ##
################################

## Automate execution of main function
if __name__ == "__main__":
    main_func_rdd()





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
