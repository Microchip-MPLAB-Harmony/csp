import binascii
import sys
import os

filename = sys.argv[1]
count = 16

binfile = open(filename, "rb")
headerfile = open('./xip_image_pattern_hex.h', 'w+')

size = os.stat(filename)

print >> headerfile, "#ifndef XIP_IMAGE_PATTERN_HEX_H_"
print >> headerfile, "#define XIP_IMAGE_PATTERN_HEX_H_\n"
print >> headerfile, "const uint8_t xip_image_pattern["+str(size.st_size)+"] = \n{"

while True:
    byte = binfile.read(1)
    if byte:
       count = count - 1
       hex_str = binascii.hexlify(byte)
       print >> headerfile, "0x"+hex_str+",",
       if (count == 0):
           print >> headerfile, ""
           count = 16
    else:
            break

binfile.close()
print >> headerfile, "\n};\n"
print >> headerfile, "#endif"
headerfile.close()
