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

MIN_TOOL_COUNT = 2
MAX_TOOL_COUNT = 10
MIN_TOOL_PRICE = 5
MAX_TOOL_PRICE = 100

def randomString(stringLength=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


tools = ["Ball Peen Hammer",
    "Claw Hammer",
    "Club Hammer",
    "Dead Blow Hammer",
    "Framing Hammer",
    "Rubber Mallet",
    "Joiners Mallet",
    "Sledge Hammer",
    "Tack Hammer",
    "Blacksmith Hammer",
    "Blocking Hammer",
    "Brass Hammer",
    "Brick Hammer",
    "Bushing Hammer",
    "Cross Peen Hammer",
    "Cross Peen Pin Hammer",
    "Chasing Hammer",
    "Drywall Hammer",
    "Electricians Hammer",
    "Engineering Hammer",
    "Hatchet Hammer",
    "Linemans Hammer",
    "Mechanics Hammer",
    "Piton Hammer",
    "Planishing Hammer",
    "Power Hammer",
    "Rip Hammer",
    "Rock Hammer",
    "Scaling Hammer",
    "Scutch Hammer",
    "Shingle Hammer",
    "Soft-Faced hammer",
    "Spike Maul Hammer",
    "Stone Sledge Hammer",
    "Straight Peen Hammer",
    "Tinners Hammer",
    "Toolmakers Hammer",
    "Trim Hammer",
    "Welding Hammer",
    "Adjustable Wrench",
    "Allen Wrench",
    "Box-Ended Wrench",
    "Combination Wrench",
    "Crowfoot Wrench",
    "Impact Wrench",
    "Lug Wrench",
    "Oil Filter Wrench",
    "Open-Ended Wrench",
    "Pipe Wrench",
    "Ratcheting Wrench",
    "Socket Wrench",
    "Torque wrench",
    "Alligator Wrench",
    "Armorers Wrench",
    "Basin Wrench",
    "Bionic Wrench",
    "Bung Wrench",
    "Cone Wrench",
    "Die Stock Holder Wrench",
    "Dog Bone Wrench",
    "Fan Clutch Wrench",
    "Fire Hydrant Wrench",
    "Flare Nut Wrench",
    "Garbage Disposal Wrench",
    "Hammer Wrench",
    "Monkey Wrench",
    "Pedal Wrench",
    "Pliers Wrench",
    "Plumbers Wrench",
    "Spanner Wrench",
    "Spark Plug Wrench",
    "Spoke Wrench",
    "Spud Wrench",
    "Strap Wrench",
    "Stubby Wrench",
    "Tap Wrench",
    "Tension Wrench",
    "Duplex Nails",
    "Annular Ring Nails",
    "Spiral Flooring Nails",
    "Cut Flooring Nails",
    "Masonry Nails",
    "Roofing Nails",
    "Casing Nails",
    "Box Nails",
    "Finishing Nails"]



db = create_engine('postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':5432/' + DATABASE)
conn = db.connect()

stmt = sqlalchemy.text(
	"INSERT INTO tools(name, type, sku, image, price)"
	" VALUES (:name, :type, :sku, :image, :price)"
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
        conn.execute(stmt, 
            name=tool, 
            type=tool_type, 
            sku=randomString(16), 
            image=tool_type+".png", 
            price=random.randint(MIN_TOOL_PRICE,MAX_TOOL_PRICE))

conn.close()
