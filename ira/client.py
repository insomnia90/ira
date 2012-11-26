import zmq
import datetime
import sys
import csv
import time


class Mapper(object):

    def __init__(self, header):
        self._header = header

    def next(self, values):
        """
        Splits the values string with separator ',' and returns a dictionary
        {key: value, ...} with key, value from header and values
        """
        if isinstance(values, str):
            k = self._header.split(',')
            v = values.split(',')
            return dict(zip(k,v))
        else:
            raise TypeError


def start():

    host = 'tcp://127.0.0.1:1234'

    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect(host)


    header = sys.stdin.readline().strip()
    mapper = Mapper(header)

    listening = True
    cnt = 0
    while listening:
        sys.stdin.flush()
        recv_msg = sys.stdin.readline()
        msg = mapper.next(recv_msg)
        
        cnt += 1
        print cnt
        socket.send_json(msg)
        #socket.send(recv_msg)
        #socket.send('1')
        #cnt += 1
        #if cnt % 1000 == 0:
        #    print cnt


def main():
    start()


if __name__ == '__main__':
    main()