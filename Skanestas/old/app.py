import json
import logging
import random
import time


logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    #query_sql = " insert into json_table select * from json_populate_recordset(NULL::json_table, %s) "
    #cur.execute(query_sql, (json.dumps(message),))
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
        logger.info(f"{json.dumps(msg)}")
        time.sleep(1)
