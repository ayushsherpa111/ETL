from consts import STAGING_SCHEMA, TARGET_SCHEMA, TEMP_SCHEMA
from tables import STAGING_TBL_STRUCT
from context import curs


def ensure_exists():
    prep_schema(STAGING_SCHEMA)
    prep_schema(TEMP_SCHEMA)
    prep_schema(TARGET_SCHEMA)

    for (table_name, fields) in STAGING_TBL_STRUCT.items():
        prep_tables(STAGING_SCHEMA, table_name, fields, "STG", "TBL")


def prep_schema(schema_name: str) -> None:
    print(f"Creating schema {schema_name}")
    curs.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")


def prep_tables(schema_name: str, table_name: str,
                field: dict, prefix: str, postfix: str) -> None:
    curs.execute(f"USE SCHEMA {schema_name}")
    sql_bfr = f"Create table {prefix}_{table_name}_{postfix} if not exists(\n"
    field_bfr = []
    fk_bfr = []

    for (field_name, props) in field.items():
        field_bfr.append(f"{field_name} {props.get('datatype')}"
                         + (" PRIMARY KEY" if props.get("PK") else ""))

        if props.get("FK"):
            fk_bfr.append(f"foreign key({field_name}) \
references {prefix}_{props.get('FK').Ref}_{postfix}({props.get('FK').Field})")

    print(f"******************************\
CREATING TABLE : {table_name}******************************")
    print(sql_bfr + ",".join(field_bfr) +
          (","+",\n".join(fk_bfr) if len(fk_bfr) > 0 else "\n")+")")
    print("******************************\
***********************************************************")

    curs.execute(sql_bfr + ",".join(field_bfr) +
                 (","+",\n".join(fk_bfr) if len(fk_bfr) > 0 else "\n")+")")
