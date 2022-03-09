# captain

Forwards REST calls to a sqlite queue.

```console
$ curl localhost:18000/api/some/command
{"success":true}
$ sqlite3 /tmp/captain.queue
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> SELECT * FROM Queue;
some/command|df7044bc01c6fb268b453fd00c08298d|0|1646751944||
sqlite>
```

### How to start captain? 

```console
python3 server.py
```
