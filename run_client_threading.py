#!/usr/bin/env python
from __future__ import print_function

import time
import threading
import grpc

import helloworld_pb2
import helloworld_pb2_grpc
from greeter_client import run


if __name__ == '__main__':
  ts = []
  start = time.time()
  for i in range(5):
      t = threading.Thread(target=run, args=(i,))
      t.start()
      ts.append(t)
  for t in ts:
    t.join()
  print('Elapsed: %.2fs' % (time.time() - start))
