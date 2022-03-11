#!/usr/bin/env python3
from litequeue import SQLQueue

db_file = "/tmp/captain.queue"

queue = SQLQueue(db_file, check_same_thread=False)

item = queue.pop()
if item:
    print(item)
    queue.done(item["message_id"])
    queue.prune()
else:
    print("queue empty")
