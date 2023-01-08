from os import getcwd
from os.path import join

DIMENSION_HEIRARCHY = {
    "LOCATION": ["STORE", "REGION", "COUNTRY"],
    "PURCHASE": ["EMPLOYEE"],
    "PRODUCT": ["PRODUCT", "SUBCATEGORY", "CATEGORY"],
}

FACT_TBL = "SALES"

OUTPUT_DIR = join(getcwd(), "Output")

STAGING_SCHEMA = "DW_STG"
TEMP_SCHEMA = "DW_TMP"
TARGET_SCHEMA = "DW_TAR"
