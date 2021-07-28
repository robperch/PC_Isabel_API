## MODULE WITH PARAMETERS FOR ISABEL





"----------------------------------------------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Standard library imports


## Third party imports


## Local application imports





"----------------------------------------------------------------------------------------------------------------------"
########################
## General parameters ##
########################

## Location of credentials
crds_loc = "../conf/local/credentials.yaml"

## Location of feed files
feed_loc = "../feed/"

## Reference for input/output files for API calls
inout_files = {
    "age_groups": {
        "input": "age_groups_input.json",
        "output": "age_groups_output.json"
    },
    "regions": {
        "input": "regions_input.json",
        "output": "regions_output.json"
    },
    "countries": {
        "input": "countries_input.json",
        "output": "countries_output.json"
    },
    "pregnancies": {
        "input": "pregnancies_input.json",
        "output": "pregnancies_output.json"
    },
    "rdd": {
        "input": "rdd_input.json",
        "output": "rdd_output.json"
    },
}





"----------------------------------------------------------------------------------------------------------------------"
#######################
## Isabel parameters ##
#######################

isabel_api_params = {
    "base_url": "https://apiscsandbox.isabelhealthcare.com/v2/",
    "methods": {

        "age_groups": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + inout_files["age_groups"]["input"]
        },

        "regions": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + inout_files["regions"]["input"]
        },

        "countries": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + inout_files["countries"]["input"]
        },

        "pregnancies": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + inout_files["pregnancies"]["input"]
        },

        "rdd": {
            "params_required": [
                "specialties", ## 28 for rdd
                "dob", ## format: YYMMDD
                "sex", ## "m" (male) or "f" (female)
                "pregnant", ## "n" (no), "y" (pregnant), "blank" (not specified)
                "region", ## there is a reference table; this parameter is only used when `country_id` is not passed
                "country_id", ## api (method "countries") is the reference
                "querytext", ## symptoms comma separated “,” E.g. – fever,cold,nausea
                "flag", ## Pass “red_flag” for don't miss diagnoses or “sortbyRW_advanced” for most relevant diagnoses (ranked list of diagnoses)
                "suggest", ## Suggest+Differential+Diagnosis (fixed value)
                "searchType", ## 0 (fixed value)
                "web_service", ## json (fixed value)
            ],
            "params_input": feed_loc + inout_files["rdd"]["input"]
        },

    },
}





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
