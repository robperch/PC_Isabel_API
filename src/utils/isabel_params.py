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

## Credentials info
crds_loc = "conf/local/credentials.yaml"
crd_use = "sandbox_auth_key_SC"


## Base URL that is being used
sel_base_url = "sandbox_sc_spanish"


## Location of input files
input_loc = "input/"
out_loc = "output/"


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
    "ranked_differential_diagnoses": {
        "input": "ranked_differential_diagnoses_input.json",
        "output": "ranked_differential_diagnoses_output.json"
    },
    "triage_score": {
        "input": "triage_score_input.json",
        "output": "triage_score_output.json"
    },
}


## Reference limits for triage score
triage_reference_limits = {
    "VERDE - Ir a clínica/Telemedicina": {
        "il": 0,
        "sl": 39
    },
    "AMBAR - Médico familiar/Clínica de cuidados urgentes/Unidad de heridas menores": {
        "il": 40,
        "sl": 79
    },
    "ROJO - Servicios de emergencia/Unidad de urgencias": {
        "il": 80,
        "sl": 150
    },
}





"----------------------------------------------------------------------------------------------------------------------"
#######################
## Isabel parameters ##
#######################

## Reference of all the base URL's available for the API calls
isabel_base_urls = {

    ## English resources
    "predictive_text_english": "https://apiscsandbox.isabelhealthcare.com/predictive-text",
    "sandbox_sc_english": "https://apiscsandbox.isabelhealthcare.com/v2/",

    ## Spanish resources
    "sandbox_sc_spanish": "https://esscstsandbox.isabelhealthcare.com/v2/",
    "sandbox_pro_spanish": "https://esapisandbox.isabelhealthcare.com/v2/"

}


## Reference of all the API parameters required
isabel_api_params = {

    "base_url": isabel_base_urls[sel_base_url],

    "methods": {

        "age_groups": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": input_loc + inout_files["age_groups"]["input"],
            "usage": "GUI"
        },

        "regions": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": input_loc + inout_files["regions"]["input"],
            "usage": "GUI"
        },

        "countries": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": input_loc + inout_files["countries"]["input"],
            "usage": "GUI"
        },

        "pregnancies": {
            "params_required": [
                "language",
                "web_service"
            ],
            "params_input": input_loc + inout_files["pregnancies"]["input"],
            "usage": "GUI"
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
                # "language",  ## json (fixed value)
            ],
            "params_input": input_loc + inout_files["ranked_differential_diagnoses"]["input"],
            "usage": "rdd"
        },

        "triage_score": {
            "params_required": [
                "dx", ## Fixed value of 1 (I guess)
                "age",
                "sex",
                "pregnancy",
                "region",
                "text",
                "Q1",
                "Q2",
                "Q3",
                "Q4",
                "Q5",
                "Q6",
                "Q7",
                "web_service", ## json (fixed value)
            ],
            "params_input": input_loc + inout_files["triage_score"]["input"],
            "usage": "triage"
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
