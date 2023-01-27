import json
import logging
import random
import time

# import env
import os
from dotenv import load_dotenv

# import lib for connect postgresql
import psycopg2   

load_dotenv()

# connect to DB
db=os.getenv("database")
username=os.getenv("username")
passwd=os.getenv("passwd")
post=os.getenv("port")
commit=os.getenv("commit")   # count rows have to do commit
host=os.getenv("DB_HOST")
conn = psycopg2.connect(database=db, host=host, user=username, password=passwd, port=post)
db=conn.cursor()


# Insert a new row into the 'logs' table.
def addrow(data):
    query_sql = """ insert into logs (id, stats) values (DEFAULT,'""" + data + """');"""
    db.execute( query_sql   )

# select count row for commit
def countrow():
    query="select * from logs;"
    db.execute(query)
    return db.rowcount

def currentrowmonitor(data):
    y=json.loads(data)
    if y["ask_01"]+y["bid_01"]<105:
        return 1
    else:
        return 0


logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
)
logger = logging.getLogger(__name__)




if __name__ == "__main__":
    while True:
        msg = dict()
        for level in range(50):
            (
                msg[f"bid_{str(level).zfill(2)}"],
                msg[f"ask_{str(level).zfill(2)}"],
            ) = (
                random.randrange(1, 100),
                random.randrange(100, 200),
            )
        msg["stats"] = {
            "sum_bid": sum(v for k, v in msg.items() if "bid" in k),
            "sum_ask": sum(v for k, v in msg.items() if "ask" in k),
        }
        # add new message to DB
        addrow(f"{json.dumps(msg)}")
        if countrow()%int(commit)==0:
            print("insert " + str(countrow()))
            conn.commit()
        if currentrowmonitor(f"{json.dumps(msg)}")==1:
            logger.info(f"{json.dumps(msg)}")
        time.sleep(0.001)
