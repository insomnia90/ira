import time
import subprocess
import os
import datetime

server_path = os.environ['PROJECT_HOME'] + '/ira/ira/'
path = os.environ['PROJECT_HOME'] + '/ira/ira/'


server = subprocess.Popen(['python', server_path + 'server.py'], shell=False, bufsize=1, stdout=subprocess.PIPE)

client = subprocess.Popen(['python', path + 'client.py'], shell=False, bufsize=1, stdin=subprocess.PIPE)
client.stdin.write('type,value,jobId\n')

start = datetime.datetime.now()
total_sent = 0
while (datetime.datetime.now() - start).seconds <= 1:
    client.stdin.write('d,user,2\n')
    #client.stdin.flush()
    total_sent += 1

time.sleep(1)
client.kill()
server.kill()


total_recv = 0
for line in server.stdout:
    total_recv += 1
    print line
print 'Sent %d, received %d' % (total_sent, total_recv)
