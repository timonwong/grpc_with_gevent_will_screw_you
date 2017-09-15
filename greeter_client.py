from __future__ import print_function

#import gevent.monkey; gevent.monkey.patch_all()
import threading
import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  print("Start sending request...")
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  ts = []
  for i in range(5):
      t = threading.Thread(target=run)
      t.start()
      ts.append(t)
  for t in ts:
    t.join()

