import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

ctx = snowflake.connector.connect(
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    account=os.getenv("ACCOUNT"),
    database=os.getenv("DATABASE"),
    warehouse=os.getenv("WAREHOUSE")
)

curs = ctx.cursor()
