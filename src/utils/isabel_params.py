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

## Location of feedfiles
feed_loc = "../feed/"





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
            "params_input": feed_loc + "age_groups_input.json"
        },

        "regions": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + "regions_input.json"
        },

        "countries": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + "countries_input.json"
        },

        "pregnancies": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": feed_loc + "pregnancies_input.json"
        },

        "ranked_differential_diagnoses": {
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
            "params_input": feed_loc + "ranked_differential_diagnoses_input.json"
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
