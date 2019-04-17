"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

def instantiateComponent(dfpComponent):

    from os import listdir
    import xml.etree.ElementTree as ET

    MCC_HEADERS_SUBPATH = "/include"

    dfpDevice = dfpComponent.createCommentSymbol("dfpDevice", None)
    dfpDevice.setLabel("Device: " + Variables.get("__PROCESSOR"))

    #get pack information
    dfpInformation = dfpComponent.createCommentSymbol("dfpInformation", None)

    dfpFiles = listdir(Variables.get("__DFP_PACK_DIR"))
    dfpInfoFound = False
    for dfpFile in dfpFiles:
        if dfpFile.find(".pdsc") != -1:
            dfpDescriptionFile = open(Variables.get("__DFP_PACK_DIR") + "/" + dfpFile, "r")
            dfpDescription = ET.fromstring(dfpDescriptionFile.read())
            dfpInfoFound = True
            for release in dfpDescription.iter("release"):
                dfpInformation.setLabel("Release Information: " + str(release.attrib))
                break

    if dfpInfoFound == False:
        dfpFiles = listdir(Variables.get("__DFP_PACK_DIR")+"/..")
        for dfpFile in dfpFiles:
            if dfpFile.find(".pdsc") != -1:
                dfpDescriptionFile = open(Variables.get("__DFP_PACK_DIR") + "/../" + dfpFile, "r")
                dfpDescription = ET.fromstring(dfpDescriptionFile.read())
                for release in dfpDescription.iter("release"):
                    dfpInformation.setLabel("Release Information: " + str(release.attrib))
                    break

    processorName = Variables.get("__PROCESSOR")

    deviceHeaderFile = dfpComponent.createFileSymbol("deviceHeaderFile", None)
    deviceHeaderFile.setMarkup(True)
    deviceHeaderFile.setSourcePath("templates/device.h.ftl")
    deviceHeaderFile.setOutputName("device.h")
    deviceHeaderFile.setDestPath("../../packs/" + processorName + "_DFP/")
    deviceHeaderFile.setProjectPath("packs/" + processorName + "_DFP/")
    deviceHeaderFile.setType("HEADER")
    deviceHeaderFile.setOverwrite(True)

    if( "PIC32M" not in processorName):
        #add pack files to a project
        headerFileNames = listdir(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component")

        for headerFileName in headerFileNames:
            szSymbol = "PART_PERIPH_{}_DEFS".format(headerFileName[:-2].upper())
            headerFile = dfpComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component/" + headerFileName)
            headerFile.setOutputName(headerFileName)
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/" + processorName + "_DFP/component/")
            headerFile.setProjectPath("packs/" + processorName + "_DFP/component/")
            headerFile.setType("HEADER")

        headerFile = dfpComponent.createFileSymbol("PART_MAIN_DEFS", None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/" + processorName.replace("ATSAM", "SAM").lower() + ".h")
        headerFile.setOutputName(processorName.lower() + ".h")
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/" + processorName + "_DFP/")
        headerFile.setProjectPath("packs/" + processorName + "_DFP/")
        headerFile.setType("HEADER")

        headerFile = dfpComponent.createFileSymbol("PART_IO_DEFS", None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/pio/" + processorName.replace("ATSAM", "SAM").lower() + ".h")
        headerFile.setOutputName(processorName.replace("ATSAM", "SAM").lower() + ".h")
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/" + processorName + "_DFP/pio/")
        headerFile.setProjectPath("packs/" + processorName + "_DFP/pio/")
        headerFile.setType("HEADER")
