# captain

Forwards REST calls to a sqlite queue. Not yet ready for producation. I use captain as a remote control for my "linux-enabled speaker". A local daemon

## Example use

Start captain server:
```console
python3 server.py
```

Enqueue some data using curl:
```console
$ curl -k -u role_001:1234 https://localhost:10443/api/some/command
{"success":true}
```

Let's see if something is in the queue:
```console
$ sqlite3 /tmp/captain.queue
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> SELECT * FROM Queue;
some/command|df7044bc01c6fb268b453fd00c08298d|0|1646751944||
sqlite>
```

Pop something from the queue:
```console
python3 pop.py
{'message': 'some/command', 'message_id': 'df7044bc01c6fb268b453fd00c08298d'}
```

## Using captain with self-signed SSL certificates

Above use of curl uses the `-k` flag to disable certificate validation, to avoid this you can do:

### On the server:
```console
cd captain
mkdir ssl ; cd ssl
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
cd ..
python3 server.py
```

### On the client:
```console
echo quit | openssl s_client -showcerts -servername server -connect localhost:10443 > cacert.pem
```
Subsequent calls to curl can leave the `-k` flag away but specify the pem file.
```console
curl --cacert cacert.pem -u role_001:1234 https://localhost:10443/api/some/command
```

## TODO

- [ ] litequeue hook/trigger so that I don't have to busy-loop over pop
- [ ] Run server properly via wsgi (or so) 
- [ ] Make this easy to install (git clone https://github.com/8327/captain && captain/install.sh
 
