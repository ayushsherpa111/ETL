from context import curs, ctx
from os import getenv, mkdir
from shutil import rmtree
from consts import DIMENSION_HEIRARCHY, OUTPUT_DIR, FACT_TBL
from extract import extract_tbl
from prep import ensure_exists

ensure_exists()

test = True

if test:
    rmtree(OUTPUT_DIR)

try:
    mkdir(OUTPUT_DIR, mode=777)
    print("Output Directory created")
except FileExistsError:
    print("Output directory already exists")

curs.execute("USE SCHEMA {}".format(getenv("SOURCE_SCHEMA")))


extract_tbl(DIMENSION_HEIRARCHY["LOCATION"], curs, OUTPUT_DIR)
extract_tbl([FACT_TBL], curs, OUTPUT_DIR)


ctx.close()  # END
