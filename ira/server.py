import zmq
#import gevent
#from gevent_zeromq import zmq
import sys


def serve():

    host = 'tcp://127.0.0.1:1234'
    context = zmq.Context()
    server = context.socket(zmq.PULL)
    server.bind(host)
    
    cnt = 0
    while True:
        #msg = server.recv()
        msg = server.recv_json()
        cnt += 1
        print cnt
        #sys.stdout.flush()

def main():
    #gevent.joinall([
    #    gevent.spawn(serve),
    #    ])
    serve()


if __name__ == '__main__':
    main()