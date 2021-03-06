## MODULE WITH FUNCTIONS FOR ISABEL





"----------------------------------------------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Standard library imports
import yaml

import re

import json


## Third party imports


## Local application imports
from src.utils.isabel_params import (
    crds_loc,
    crd_use,
    input_loc,
    out_loc,
    inout_files,
    isabel_api_params,
)





"----------------------------------------------------------------------------------------------------------------------"
#########################
## Ancillary functions ##
#########################


## Read yaml file
def read_yaml(crds_loc):
    """
    Read yaml file

    :param crds_loc: (string) location of yaml file
    :return config: (?) read file
    """

    ## Configuration parameter
    config = None

    ## Safe loading file
    try:
        with open(crds_loc, "r") as file:
            config = yaml.safe_load(file)
    except:
        raise FileNotFoundError("Could not load file")

    return config



## Get isabel credentials
def get_isabel_crds():
    """
    Get isabel credentials

    :return isabel_crds: (?) Isabel credentials
    """

    ## Reading file with crds
    crds = read_yaml(crds_loc)

    ## Selecting the right credentials
    isabel_crds = crds["isabel"]

    return isabel_crds



## Clean the API request output
def clean_api_request(api_txt):
    """
    Clean the API request output

    :param api_txt: (str) raw api response
    :return api_txt: (str) api response without certain initial and final parts
    """

    ## Eliminating all characters until the first "{"
    api_txt = re.sub(r'^.*?{', '{', api_txt)

    ## Eliminating the last two characters ");"
    api_txt = api_txt[:-2]

    return api_txt



## Print api response with visual and content improvements
def enhance_api_response(api_resp):
    """
    Print api response with visual and content improvements

    :param api_resp: (str) API raw response as string
    :return api_resp: (str) enhanced API response
    """

    ## Eliminating characters outside json format
    api_resp = clean_api_request(api_resp)

    ## Formatting response
    api_resp = json.dumps(json.loads(api_resp), ensure_ascii=False, indent=2)

    return api_resp



## Read JSON file
def read_json(path):
    """
    Read JSON file

    :param path: (str) path where .json file that will be read is located
    :return json_cont: (dict) contents extracted from selected json file
    """

    ## Storing opened file in variable
    file = open(path, )
    json_cont = json.load(file)

    return json_cont



## Writing a JSON file
def write_json(path, enhanced_api_text_output):
    """
    Writing a JSON file

    :param path: (str) location of output file
    :param enhanced_api_text_output: (str) API cleaned with the `enhance_api_response` function
    :return None:
    """

    ## Creating open file object
    jsonFile = open(path, "w")

    ## Writing formated API response into file
    jsonFile.write(enhanced_api_text_output)

    ## Closing file
    jsonFile.close()

    return





"----------------------------------------------------------------------------------------------------------------------"
######################
## Isabel functions ##
######################


## Create URL for API request
def url_api_request(method):
    """
    Create URL for API request

    :param method: (str) name of the method that will be called using the API
    :return api_call_url: (str) final URL that will be used to interact the Isabel's API
    """

    ## Creating the base URL that will be enhanced later on
    api_call_url = isabel_api_params["base_url"]

    ## Pasting the method to the URL
    api_call_url += method + "?"

    ## Pasting the call back parameter
    api_call_url += "callback=" + method

    ## Pasting authorization credentials
    api_call_url += "&authorization=" + get_isabel_crds()[crd_use]


    ## Adding method parameters

    #### Reading json file with inputs for parameters
    json_cont = read_json(isabel_api_params["methods"][method]["params_input"])

    #### Adding parameters and their values to URL
    for param in isabel_api_params["methods"][method]["params_required"]:
        api_call_url += "&" + param + "=" + json_cont[param]


    return api_call_url



## Add new information to API response
def complement_api_response(method, api_txt):
    """

    :param method: (str) name of the method that will be called using the API
    :param api_txt: (str) raw api response
    :return:
    """
    
    ## Adding new data depending on the method called
    if method == "triage_score":
        print("hola")
    else:
        print("No complementary information was added to the response")





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"