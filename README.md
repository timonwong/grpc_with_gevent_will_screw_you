# Demonstrate that using grpc with gevent will screw you.

## Run

At first, please create a virtualenv and then issue `pip install -r requirements.txt`.

In order to run the grpc server:

```bash
./run_server.py
```

See a normal grpc client, use native threading:

```bash
./run_client_threading.py
```

The following will just screw you:

```bash
./run_client_gevent.py
```

## Results

```
$ ./run_client_threading.py

0: Start sending request...
1: Start sending request...
2: Start sending request...
3: Start sending request...
4: Start sending request...
1: Greeter client received: Hello, you!
3: Greeter client received: Hello, you!
0: Greeter client received: Hello, you!
2: Greeter client received: Hello, you!
4: Greeter client received: Hello, you!
Elapsed: 2.02s
```

```
$ ./run_client_gevent.py

0: Start sending request...
0: Greeter client received: Hello, you!
1: Start sending request...
1: Greeter client received: Hello, you!
2: Start sending request...
2: Greeter client received: Hello, you!
3: Start sending request...
3: Greeter client received: Hello, you!
4: Start sending request...
4: Greeter client received: Hello, you!
Elapsed: 10.05s
```

Congrats, 👻
