import json
import os
import psycopg2
import string
import psycopg2.extras
import random
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
ENV = os.environ.get("FLASK_ENV")

MIN_TOOL_COUNT = 1
MAX_TOOL_COUNT = 3
MIN_TOOL_PRICE = 100
MAX_TOOL_PRICE = 10000

def randomString(stringLength=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


tools = ["ball peen hammer",
    "claw hammer",
    "club hammer",
    "dead blow hammer",
    "framing hammer",
    "rubber mallet",
    "joiners mallet",
    "sledge hammer",
    "tack hammer",
    "blacksmith hammer",
    "blocking hammer",
    "brass hammer",
    "brick hammer",
    "bushing hammer",
    "cross peen hammer",
    "cross peen pin hammer",
    "chasing hammer",
    "drywall hammer",
    "electricians hammer",
    "engineering hammer",
    "hatchet hammer",
    "linemans hammer",
    "mechanics hammer",
    "piton hammer",
    "planishing hammer",
    "power hammer",
    "rip hammer",
    "rock hammer",
    "scaling hammer",
    "scutch hammer",
    "shingle hammer",
    "soft-faced hammer",
    "spike maul hammer",
    "stone sledge hammer",
    "straight peen hammer",
    "tinners hammer",
    "toolmakers hammer",
    "trim hammer",
    "welding hammer",
    "adjustable wrench",
    "allen wrench",
    "box-ended wrench",
    "combination wrench",
    "crowfoot wrench",
    "impact wrench",
    "lug wrench",
    "oil filter wrench",
    "open-ended wrench",
    "pipe wrench",
    "ratcheting wrench",
    "socket wrench",
    "torque wrench",
    "alligator wrench",
    "armorers wrench",
    "basin wrench",
    "bionic wrench",
    "bung wrench",
    "cone wrench",
    "die stock holder wrench",
    "dog bone wrench",
    "fan clutch wrench",
    "fire hydrant wrench",
    "flare nut wrench",
    "garbage disposal wrench",
    "hammer wrench",
    "monkey wrench",
    "pedal wrench",
    "pliers wrench",
    "plumbers wrench",
    "spanner wrench",
    "spark plug wrench",
    "spoke wrench",
    "spud wrench",
    "strap wrench",
    "stubby wrench",
    "tap wrench",
    "tension wrench",
    "duplex nails",
    "annular ring nails",
    "spiral flooring nails",
    "cut flooring nails",
    "masonry nails",
    "roofing nails",
    "casing nails",
    "box nails",
    "finishing nails"]

tools.sort()

db = create_engine('postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':5432/' + DATABASE)
conn = db.connect()

insert_tool_stmt = sqlalchemy.text(
	"INSERT INTO tools (name, type, sku, image, price)"
	" VALUES (:name, :type, :sku, :image, :price)"
)

create_tools_table_stmt = sqlalchemy.text(
	"CREATE TABLE tools("
    "id SERIAL PRIMARY KEY NOT NULL,"
    "name VARCHAR NOT NULL,"
    "type VARCHAR NOT NULL,"
    "sku VARCHAR NOT NULL,"
    "image VARCHAR NOT NULL,"
    "price INTEGER NOT NULL)"
)

drop_tools_table_stmt = sqlalchemy.text(
	"DROP TABLE IF EXISTS tools"
)

insert_inventory_stmt = sqlalchemy.text(
	"INSERT INTO inventory(sku, count)"
	" VALUES (:sku, :count)"
)

create_inventory_table_stmt = sqlalchemy.text(
	"CREATE TABLE inventory("
    "id SERIAL PRIMARY KEY NOT NULL,"
    "sku VARCHAR NOT NULL,"
    "count INTEGER NOT NULL)"
)

drop_inventory_table_stmt = sqlalchemy.text(
	"DROP TABLE IF EXISTS inventory"
)

for tool in tools:
    if "nail" in tool.lower():
        tool_type = "nails"
    elif "wrench" in tool.lower():
        tool_type = "wrench"
    elif "hammer" in tool.lower() or "mallet" in tool.lower():
        tool_type = "hammer"
    else:
        tool_type = ""
    print tool + ": " + tool_type
    for i in range(random.randint(MIN_TOOL_COUNT,MAX_TOOL_COUNT)):
        print i
        #create tool
        sku = randomString(16)
        conn.execute(insert_tool_stmt, 
            name=tool, 
            type=tool_type, 
            sku=sku, 
            image=tool_type+".png", 
            price=random.randint(MIN_TOOL_PRICE,MAX_TOOL_PRICE))

        conn.execute(insert_inventory_stmt, 
            sku=sku, 
            count=random.randint(1,30))

conn.close()



##NEED TO LOAD NEW DATA? DROP AND RECREATE THE TABLES
# r = conn.execute("select * from inventory").fetchall()
# conn.execute(drop_inventory_table_stmt)
# conn.execute(create_inventory_table_stmt)
# r = conn.execute("select * from inventory").fetchall()
# conn.execute(insert_inventory_stmt, sku="dfadfadfadfa", count=23)
# r = conn.execute("select * from inventory").fetchall()

# r = conn.execute("select * from tools").fetchall()
# conn.execute(drop_tools_table_stmt)
# conn.execute(create_tools_table_stmt)
# r = conn.execute("select * from tools").fetchall()
# tool = "ball peen hammer"
# tool_type = "hammer"
# conn.execute(insert_tool_stmt, name=tool, type=tool_type, sku=randomString(16), image=tool_type+".png", price=random.randint(MIN_TOOL_PRICE,MAX_TOOL_PRICE))
# r = conn.execute("select * from tools").fetchall()

