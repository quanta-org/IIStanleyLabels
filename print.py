import sys
import socket

# The IP address of the printer. Hardcoded for now
ip = "192.168.1.222"

# The telnet port of the printer. Hardcoded for now
port = 9100

# The input file path. Hardcoded for now
input_path = "output.zpl"


# Read the input file
with open(input_path, 'rb') as f:
    input = f.read()

# Open a telnet connection to the printer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
try: 
    s.connect((ip, port))
except:
    print("Unable to connect to printer")
    sys.exit(1)

print("Connected!")
#print("Sending input: "+input)

# Send the ZPL to the printer
s.send(input)

print("Sent!")

# Close the connection
s.close()

print("Goodbye!")