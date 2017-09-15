from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run(i):
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  print("%d: Start sending request..." % (i))
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("%d: Greeter client received: %s" % (i, response.message))

