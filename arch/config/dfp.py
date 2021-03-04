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
    from os import path
    import xml.etree.ElementTree as ET

    configName =    Variables.get( "__CONFIGURATION_NAME" )

    MCC_HEADERS_SUBPATH = "/include"

    instanceDir = path.normpath(path.join(Variables.get("__DFP_PACK_DIR"), "include", "instance"))

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
    deviceHeaderFile.setDestPath("")
    deviceHeaderFile.setProjectPath("config/" + configName + "/")
    deviceHeaderFile.setType("HEADER")
    deviceHeaderFile.setOverwrite(True)

    coreArch = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "architecture" )
    if("MIPS" not in coreArch):
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

        if path.isdir(instanceDir):
            for headerFileName in listdir(instanceDir):
                szSymbol = "PART_PERIPH_{}_INSTANCE".format(headerFileName[:-2].upper())
                headerFile = dfpComponent.createFileSymbol(szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/instance/" + headerFileName)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/" + processorName + "_DFP/instance/")
                headerFile.setProjectPath("packs/" + processorName + "_DFP/instance/")
                headerFile.setType("HEADER")


        headerFile = dfpComponent.createFileSymbol("PART_MAIN_DEFS", None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/" + processorName.lower().lstrip("at") + ".h")
        headerFile.setOutputName(processorName.lower().lstrip("at") + ".h")
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/" + processorName + "_DFP/")
        headerFile.setProjectPath("packs/" + processorName + "_DFP/")
        headerFile.setType("HEADER")

        headerFile = dfpComponent.createFileSymbol("PART_IO_DEFS", None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/pio/" + processorName.lower().lstrip("at") + ".h")
        headerFile.setOutputName(processorName.lower().lstrip("at") + ".h")
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/" + processorName + "_DFP/pio/")
        headerFile.setProjectPath("packs/" + processorName + "_DFP/pio/")
        headerFile.setType("HEADER")

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        secDeviceHeaderFile = dfpComponent.createFileSymbol("secure_deviceHeaderFile", None)
        secDeviceHeaderFile.setMarkup(True)
        secDeviceHeaderFile.setSourcePath("templates/device.h.ftl")
        secDeviceHeaderFile.setOutputName("device.h")
        deviceHeaderFile.setDestPath("")
        deviceHeaderFile.setProjectPath("config/" + configName + "/")
        secDeviceHeaderFile.setType("HEADER")
        secDeviceHeaderFile.setOverwrite(True)
        secDeviceHeaderFile.setSecurity("SECURE")
        if( "MIPS" not in coreArch):
            #add pack files to a project
            secHeaderFileNames = listdir(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component")

            for headerFileName in secHeaderFileNames:
                szSymbol = "secure_" + "PART_PERIPH_{}_DEFS".format(headerFileName[:-2].upper())
                headerFile = dfpComponent.createFileSymbol(szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component/" + headerFileName)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/" + processorName + "_DFP/component/")
                headerFile.setProjectPath("packs/" + processorName + "_DFP/component/")
                headerFile.setType("HEADER")
                headerFile.setSecurity("SECURE")

            if path.isdir(instanceDir):
                for headerFileName in listdir(instanceDir):
                    szSymbol = "secure_" + "PART_PERIPH_{}_INSTANCE".format(headerFileName[:-2].upper())
                    headerFile = dfpComponent.createFileSymbol(szSymbol, None)
                    headerFile.setRelative(False)
                    headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/instance/" + headerFileName)
                    headerFile.setOutputName(headerFileName)
                    headerFile.setMarkup(False)
                    headerFile.setOverwrite(True)
                    headerFile.setDestPath("../../packs/" + processorName + "_DFP/instance/")
                    headerFile.setProjectPath("packs/" + processorName + "_DFP/instance/")
                    headerFile.setType("HEADER")
                    headerFile.setSecurity("SECURE")

            headerFile = dfpComponent.createFileSymbol("secure_PART_MAIN_DEFS", None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/" + processorName.lower().lstrip("at") + ".h")
            headerFile.setOutputName(processorName.lower().lstrip("at") + ".h")
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/" + processorName + "_DFP/")
            headerFile.setProjectPath("packs/" + processorName + "_DFP/")
            headerFile.setType("HEADER")
            headerFile.setSecurity("SECURE")

            headerFile = dfpComponent.createFileSymbol("secure_PART_IO_DEFS", None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/pio/" + processorName.lower().lstrip("at") + ".h")
            headerFile.setOutputName(processorName.lower().lstrip("at") + ".h")
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/" + processorName + "_DFP/pio/")
            headerFile.setProjectPath("packs/" + processorName + "_DFP/pio/")
            headerFile.setType("HEADER")
            headerFile.setSecurity("SECURE")