import time
import random

import psycopg2
import json

#from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'


conn = psycopg2.connect(database="database", host="db", user="username", password="secret", port="5432")
# Connecto to the database
#db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
#db = create_engine(db_string)
db=conn.cursor()

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+\
        "VALUES ("+\
        str(n) + "," + \
        str(int(round(time.time() * 1000))) + ");")
    print("insert" + str(db.rowcount))
    data='{"bid_00": 58, "ask_00": 144, "bid_01": 97, "ask_01": 163, "bid_02": 79, "ask_02": 150, "bid_03": 71, "ask_03": 140, "bid_04": 93, "ask_04": 144, "bid_05": 7, "ask_05": 147, "bid_06": 48, "ask_06": 196, "bid_07": 13, "ask_07": 121, "bid_08": 81, "ask_08": 142, "bid_09": 76, "ask_09": 121, "bid_10": 14, "ask_10": 110, "bid_11": 33, "ask_11": 146, "bid_12": 91, "ask_12": 180, "bid_13": 2, "ask_13": 148, "bid_14": 30, "ask_14": 163, "bid_15": 53, "ask_15": 142, "bid_16": 73, "ask_16": 134, "bid_17": 28, "ask_17": 128, "bid_18": 67, "ask_18": 131, "bid_19": 14, "ask_19": 102, "bid_20": 57, "ask_20": 135, "bid_21": 69, "ask_21": 197, "bid_22": 78, "ask_22": 150, "bid_23": 41, "ask_23": 124, "bid_24": 15, "ask_24": 195, "bid_25": 72, "ask_25": 149, "bid_26": 49, "ask_26": 108, "bid_27": 1, "ask_27": 116, "bid_28": 80, "ask_28": 165, "bid_29": 83, "ask_29": 180, "bid_30": 1, "ask_30": 165, "bid_31": 28, "ask_31": 103, "bid_32": 67, "ask_32": 114, "bid_33": 43, "ask_33": 184, "bid_34": 24, "ask_34": 191, "bid_35": 97, "ask_35": 189, "bid_36": 40, "ask_36": 173, "bid_37": 96, "ask_37": 176, "bid_38": 68, "ask_38": 169, "bid_39": 90, "ask_39": 106, "bid_40": 98, "ask_40": 133, "bid_41": 51, "ask_41": 181, "bid_42": 32, "ask_42": 110, "bid_43": 66, "ask_43": 110, "bid_44": 28, "ask_44": 154, "bid_45": 39, "ask_45": 153, "bid_46": 1, "ask_46": 101, "bid_47": 38, "ask_47": 136, "bid_48": 14, "ask_48": 139, "bid_49": 8, "ask_49": 115, "stats": {"sum_bid": 2502, "sum_ask": 7273}}'
    query_sql = """ insert into logs (id, stats) values (1,'""" + data + """');"""
    print(query_sql)
    db.execute( query_sql   )
    db.execute("COMMIT;")

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number " + \
            "FROM numbers " # + \
#            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" +\
#            "LIMIT 1"
    db.execute(query)
    return db.rowcount

    #result_set = db.execute(query)  
    #for (r) in result_set:  
    #    return r[0]

if __name__ == '__main__':
    print('Application started')

    while True:
        add_new_row(random.randint(1,100000))
        #print('The last value insterted is: {}'.format(get_last_row()))
        print('The last value insterted is: ' + str(get_last_row()))
        time.sleep(5)

