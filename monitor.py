import socket
import struct
import sys

# CAN frame packing/unpacking (see `struct can_frame` in <linux/can.h>)
can_frame_fmt = "=IB3x8s"

# Threshold for DDos frame id.
thresh = 0x50

def get_frame_id(frame):
    can_id, _, _ = struct.unpack(can_frame_fmt, frame)
    return can_id

if len(sys.argv) != 2:
    print('Provide CAN device name (can0, vcan0 etc.)')
    sys.exit(0)

# create a raw socket and bind it to the given CAN interface
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind((sys.argv[1],))

counter = 0  # Count 10 continuous malicious frames.
while True:
    frame, _ = s.recvfrom(16)

    temp_id = get_frame_id(frame)
    if temp_id < 0x50:
        counter += 1
        # A DDos pattern is detected.
        if counter >= 10:
            call([''sudo'', ''ifconfig'', ''vcan0'', ''down''])
            # The program can quit because no more CAN traffic can be sent.
            exit(0)
    else:
        counter = 0