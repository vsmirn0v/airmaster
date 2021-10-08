import socket
import binascii
import sys
import struct
import json
import itertools

if "poll" in sys.argv:
    poll = True
else:
    poll = False

if "-h" in sys.argv:
    host = sys.argv[sys.argv.index("-h")+1]
else:
    host = '192.168.88.13'

if "-p" in sys.argv:
    port = sys.argv[sys.argv.index("-p")+1]
else:
    port = 12416

def reconnect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    handshake = bytes.fromhex('000000030f000008000a54454b4153485559524c05')
    s.settimeout(10)
    s.connect((host, int(port)))
    s.settimeout(None)
    s.sendall(handshake)
    handshake_response = s.recv(1024)
    data = True
    return s


def decode(data):
    labels = {
        17: "PM2.5",
        19: "PM10",
        21: "HCHO",
        22: "TVOC",
        23: "TVOC",
        24: "CO2",
        26: "TEMP",
        27: "TEMP",
        28: "RH"
    }
    types = {
        17: "H",
        19: "H",
        24: ">H",
        26: "<B",
        27: "<B",
        28: ">H"
    }
    sensors = { }
    bytemap = list(itertools.chain(range(17,21,2), range(21, 24, 1), range(24, 26, 2), range(26, 28, 1), range(28, 31, 2)))
    for index, bytenum in enumerate(bytemap):
        if len(bytemap) <= index + 1:
            continue
        datasize = bytemap[index+1]-bytenum

        if bytenum in labels:
            label = labels[bytenum]
        else:
            label = str(bytenum)

        if bytenum in types:
            datatype = types[bytenum]
        elif datasize == 2:
            datatype = 'e'
        elif datasize == 1:
            datatype = 'B'
        
        try:
            prepend = sensors[label] + "."
        except:
            prepend = ""
        try:
            val = str(struct.unpack(datatype,data[bytenum:bytemap[index+1]])[0])
            if datatype == "B" and len(val) == 1 and val != "0":
                val = "0" + val
            if label == "HCHO":
                prepend = "0."
            elif label == "RH":
                val = str("%.2f" % (float(val) / 100))
            sensors[label] = prepend + val
        except:
            print(str(datasize) + ' ' + str(bytenum))
    
    print(json.dumps(sensors, indent=4))


ping = bytes.fromhex('0000000303000006')
while True:
    s = reconnect(host, port)
    data = True
    rerun = False
    while data:
        data = s.recv(1024)
        if len(data) > 29:
            decode(data)
            rerun = False
        else:
            rerun = True
        #print (decode(data))
        s.sendall(ping)
        pong_response = s.recv(1024)
        if (not poll or not pong_response) and not rerun:
            data = False
    s.close()
    if not poll and not rerun:
        break
