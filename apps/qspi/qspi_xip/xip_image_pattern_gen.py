"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

import binascii
import os
import sys

filename = "./xip_image/firmware/sam_e70_xult.X/dist/sam_e70_xult\
/production/sam_e70_xult.X.production.bin"
destinationFile = "./xip_main/firmware/src/config/sam_e70_xult/\
xip_image_pattern_hex.h"
if os.path.exists(filename):
    count = 16

    binfile = open(filename, "rb")
    if (os.path.exists(destinationFile)):
        os.remove(destinationFile)

    headerfile = open(destinationFile, 'w+')

    size = os.stat(filename)

    print >> headerfile, "#ifndef XIP_IMAGE_PATTERN_HEX_H_"
    print >> headerfile, "#define XIP_IMAGE_PATTERN_HEX_H_\n"
    print >> headerfile, "const uint8_t xip_image_pattern[" + str(
        size.st_size) + "] = \n{"

    while True:
        byte = binfile.read(1)
        if byte:
            count = count - 1
            hex_str = binascii.hexlify(byte)
            print >> headerfile, "0x" + hex_str + ",",
            if (count == 0):
                print >> headerfile, ""
                count = 16
        else:
            break

    binfile.close()
    print >> headerfile, "\n};\n"
    print >> headerfile, "#endif"
    headerfile.close()
else:
    print("\nUnable to locate sam_e70_xult.X.production.bin")
