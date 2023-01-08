from collections import namedtuple, OrderedDict


FK = namedtuple("ForeignKey", "Ref Field")


STAGING_TBL_STRUCT = OrderedDict({
    "CATEGORY": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "CATEGORY_DESC": {
            "datatype": "VARCHAR2(1024)"
        }
    },
    "SUBCATEGORY": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "CATEGORY_ID": {
            "datatype": "NUMBER",
            "FK": FK("CATEGORY", "ID")
        },
        "SUBCATEGORY_DESC": {
            "datatype": "VARCHAR2(256)"
        },
    },
    "PRODUCT": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "SUBCATEGORY_ID": {
            "datatype": "NUMBER",
            "FK": FK("SUBCATEGORY", "ID")
        },
        "PRODUCT_DESC": {
            "datatype": "VARCHAR2(256)"
        }
    },
    "COUNTRY": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "COUNTRY_DESC": {
            "datatype": "VARCHAR2(256)"
        }
    },
    "REGION": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "COUNTRY_ID": {
            "datatype": "NUMBER",
            "FK": FK("COUNTRY", "ID")
        },
        "REGION_DESC": {
            "datatype": "VARCHAR2(256)"
        }
    },
    "STORE": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "COUNTRY_ID": {
            "datatype": "NUMBER",
            "FK": FK("COUNTRY", "ID")
        },
        "REGION_DESC": {
            "datatype": "VARCHAR2(256)"
        }
    },
    "CUSTOMER": {
        "ID": {
            "datatype": "NUMBER",
            "PK": True
        },
        "CUSTOMER_FIRST_NAME": {
            "datatype": "VARCHAR2(256)"
        },
        "CUSTOMER_MIDDLE_NAME": {
            "datatype": "VARCHAR2(256)"
        },
        "CUSTOMER_LAST_NAME": {
            "datatype": "VARCHAR2(256)"
        },
        "CUSTOMER_ADDRESS": {
            "datatype": "VARCHAR2(256)"
        }
    }
})


WAREHOUSE_TBL_STRUCT = {
    ""
}
