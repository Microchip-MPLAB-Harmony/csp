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
import os
global setDspLibParameters
def setDspLibParameters(dspLibSym, compilerID):
    libCoreName = dspLibSym.getID().split("CMSIS_DSP_LIB_")[1]
    # For IAR compiler, M7 fp libraries are named differently
    if compilerID == 1:
        libCoreName = libCoreName.replace("M7lfdp", "M7lf").replace("M7lfsp", "M7lfs")
    compilerList = ["GCC", "IAR", "ARM"]
    prefixList   = ["libarm_", "iar_", "arm_"]
    suffixList   = ["_math.a", "_math.a", "_math.lib"]
    cmsisRelPath = os.path.relpath(Variables.get("__CMSIS_PACK_DIR"), Module.getPath())
    libFileName = prefixList[compilerID] + libCoreName + suffixList[compilerID]

    sourcePath = os.path.join(cmsisRelPath, "CMSIS", "DSP", "Lib",compilerList[compilerID], libFileName)
    dspLibSym.setSourcePath(sourcePath)
    dspLibSym.setOutputName(libFileName)
    dspLibSym.setDestPath("../../packs/CMSIS/CMSIS/DSP/Lib/" + compilerList[compilerID])

def dspLibCallback(symbol, event):
    if event["id"] == "CMSIS_DSP_ENABLE":
        symbol.setEnabled(event["value"])
    else:
        setDspLibParameters(symbol, event["value"])


def instantiateComponent(cmsisComponent):
    import xml.etree.ElementTree as ET
    pdscPath = os.path.join(Variables.get("__CMSIS_PACK_DIR"), "ARM.CMSIS.pdsc")
    cmsisReleaseInfo = ET.parse(pdscPath).getroot().find("releases/release")

    cmsisVersion = cmsisComponent.createCommentSymbol("CMSIS_VERSION", None)
    cmsisVersion.setLabel("Release version: {0}".format(cmsisReleaseInfo.get("version")))

    cmsisReleaseDate = cmsisComponent.createCommentSymbol("CMSIS_RELEASE_DATE", None)
    cmsisReleaseDate.setLabel("Release date: {0}".format(cmsisReleaseInfo.get("date")))

    archNode = ATDF.getNode('/avr-tools-device-file/devices')
    cortexType = archNode.getChildren()[0].getAttribute("architecture").split("CORTEX-")[1].lower()

    #Enables cmsis-core. This option is enabled and readonly symbol since
    # harmony projects relies on cmsis-core
    cmsisCoreEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_CORE_ENABLE", None)
    cmsisCoreEnableSym.setReadOnly(True)
    cmsisCoreEnableSym.setDefaultValue(True)
    cmsisCoreEnableSym.setLabel("Enable CMSIS Core")
    cmsisCoreEnableSym.setDescription("Copies cmsis-core files into the project and adds it into project path")

    #If it is a cortex M device
    if cortexType.startswith("m"):
        v8Cores = ["m23", "m33"]
        v7VFPCores = ["m4", "m7"]

################################################################################
############################### CMSIS Core #####################################
################################################################################
        # add core header files
        coreHeaderFileNames = [ "cmsis_version.h",
                                "cmsis_compiler.h",
                                "cmsis_iccarm.h",
                                "cmsis_gcc.h",
                                "cmsis_armcc.h",
                                "cmsis_armclang.h",
                                "cmsis_armclang_ltm.h",
                                "core_c" + cortexType + ".h",
                                "mpu_armv" + ("8" if cortexType in v8Cores else "7") + ".h",  #v8 cores uses MPUv8
                                "cachel1_armv7.h" #v3.7.0 supports  enhanced cache functions for ARM-v7M
                              ]

        #v8 cores support trustZone
        if cortexType in v8Cores:
            coreHeaderFileNames.append("tz_context.h")

        for headerFileName in coreHeaderFileNames:
            szSymbol = headerFileName.replace(".", "_").upper()
            headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Core/Include/" + headerFileName)
            headerFile.setOutputName(headerFileName)
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
            headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
            headerFile.setType("HEADER")
            headerFile.setEnabled(cmsisCoreEnableSym.getValue())
            headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_CORE_ENABLE"])

            if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                #for Secure
                headerFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Core/Include/" + headerFileName)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
                headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
                headerFile.setType("HEADER")
                headerFile.setSecurity("SECURE")
                headerFile.setEnabled(cmsisCoreEnableSym.getValue())
                headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_CORE_ENABLE"])

################################################################################
############################### CMSIS DSP ######################################
################################################################################

        #Enables cmsis-dsp
        cmsisDSPEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_DSP_ENABLE", None)
        cmsisDSPEnableSym.setLabel("Enable CMSIS DSP")
        cmsisDSPEnableSym.setDescription("Copies cmsis-dsp files into the project and adds it into project path")

        # add dsp header files
        cmsisDSPIncludePath = os.path.join(Variables.get("__CMSIS_PACK_DIR"), "CMSIS", "DSP", "Include")
        for includePath, _, headerFiles in os.walk(cmsisDSPIncludePath):
            for headerFileName in headerFiles:
                filePath = os.path.join(includePath, headerFileName).replace("\\", "/")
                projPath = os.path.relpath(includePath, Variables.get("__CMSIS_PACK_DIR")).replace("\\", "/")
                szSymbol = headerFileName.replace(".", "_").upper()
                headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(filePath)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/CMSIS/{0}/".format(projPath))
                headerFile.setProjectPath("packs/CMSIS/{0}/".format(projPath))
                headerFile.setType("HEADER")
                headerFile.setEnabled(cmsisDSPEnableSym.getValue())
                headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

                if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                    #for Secure
                    headerFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                    headerFile.setRelative(False)
                    headerFile.setSourcePath(filePath)
                    headerFile.setOutputName(headerFileName)
                    headerFile.setMarkup(False)
                    headerFile.setOverwrite(True)
                    headerFile.setDestPath("../../packs/CMSIS/{0}/".format(projPath))
                    headerFile.setProjectPath("packs/CMSIS/{0}/".format(projPath))
                    headerFile.setType("HEADER")
                    headerFile.setSecurity("SECURE")
                    headerFile.setEnabled(cmsisDSPEnableSym.getValue())
                    headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

        #CMSIS DSP include path setting symbol
        cmsisDSPIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_DSP_INCLUDE_DIRS", None)
        cmsisDSPIncludeSetting.setCategory("C32")
        cmsisDSPIncludeSetting.setKey("extra-include-directories")
        cmsisDSPIncludeSetting.setValue("../src/packs/CMSIS/CMSIS/DSP/Include/")
        cmsisDSPIncludeSetting.setAppend(True, ";")
        cmsisDSPIncludeSetting.setEnabled(cmsisDSPEnableSym.getValue())
        cmsisDSPIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

        cmsisDSPXc32cppIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_DSP_XC32CPP_INCLUDE_DIRS", None)
        cmsisDSPXc32cppIncludeSetting.setCategory("C32CPP")
        cmsisDSPXc32cppIncludeSetting.setKey("extra-include-directories")
        cmsisDSPXc32cppIncludeSetting.setValue(cmsisDSPIncludeSetting.getValue())
        cmsisDSPXc32cppIncludeSetting.setAppend(True, ";")
        cmsisDSPXc32cppIncludeSetting.setEnabled(cmsisDSPEnableSym.getValue())
        cmsisDSPXc32cppIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            #CMSIS DSP include path setting symbol for Secure
            cmsisDSPIncludeSetting = cmsisComponent.createSettingSymbol("SEC_CMSIS_DSP_INCLUDE_DIRS", None)
            cmsisDSPIncludeSetting.setCategory("C32")
            cmsisDSPIncludeSetting.setKey("extra-include-directories")
            cmsisDSPIncludeSetting.setValue("../src/packs/CMSIS/CMSIS/DSP/Include/")
            cmsisDSPIncludeSetting.setAppend(True, ";")
            cmsisDSPIncludeSetting.setEnabled(cmsisDSPEnableSym.getValue())
            cmsisDSPIncludeSetting.setSecurity("SECURE")
            cmsisDSPIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

            cmsisDSPXc32cppIncludeSetting = cmsisComponent.createSettingSymbol("SEC_CMSIS_DSP_XC32CPP_INCLUDE_DIRS", None)
            cmsisDSPXc32cppIncludeSetting.setCategory("C32CPP")
            cmsisDSPXc32cppIncludeSetting.setKey("extra-include-directories")
            cmsisDSPXc32cppIncludeSetting.setValue(cmsisDSPIncludeSetting.getValue())
            cmsisDSPXc32cppIncludeSetting.setAppend(True, ";")
            cmsisDSPXc32cppIncludeSetting.setEnabled(cmsisDSPEnableSym.getValue())
            cmsisDSPXc32cppIncludeSetting.setSecurity("SECURE")
            cmsisDSPXc32cppIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

        # Construct the library name
        if cortexType in v8Cores:
            libCoreName = "ARMv8M{}l".format("BL" if cortexType in ["m23"] else "ML")
            #NOTE: Currently we do not support any armV8M Main Line cores in H3
            # BL variants do not support FPU and DSP hence no suffix needed
        else:
            libCoreName = "cortex{}l".format(cortexType.replace("plus","").upper())

            # m4 and m7 supports optional VFPs
            if cortexType in v7VFPCores:
                fpuNode = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name=\"__FPU_PRESENT\"]')
                dpNode = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name=\"__FPU_DP\"]')

                if fpuNode and fpuNode.getAttribute("value") == "1":
                    libCoreName += "f"

                    # m7 VFPs can be of single or double precision
                    if cortexType == "m7":
                        if dpNode and dpNode.getAttribute("value") == "1":
                            libCoreName += "dp"
                        else:
                            libCoreName += "sp"

        # core component which contains the symbol "COMPILER_CHOICE" is not yet
        # created, so initialize with default compiler
        libraryFileSym = cmsisComponent.createLibrarySymbol("CMSIS_DSP_LIB_" + libCoreName, None)
        setDspLibParameters(libraryFileSym,0)
        libraryFileSym.setEnabled(cmsisDSPEnableSym.getValue())
        libraryFileSym.setDependencies(dspLibCallback, ["CMSIS_DSP_ENABLE","core.COMPILER_CHOICE"])

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            #for Secure
            libraryFileSym = cmsisComponent.createLibrarySymbol("SEC_CMSIS_DSP_LIB_" + libCoreName, None)
            setDspLibParameters(libraryFileSym,0)
            # TO-DO Uncomment this once MHC supports it for Library interface
            #libraryFileSym.setSecurity("SECURE")
            libraryFileSym.setEnabled(cmsisDSPEnableSym.getValue())
            libraryFileSym.setDependencies(dspLibCallback, ["CMSIS_DSP_ENABLE","core.COMPILER_CHOICE"])

################################################################################
############################### CMSIS NN #######################################
################################################################################
        #Enables cmsis-nn
        cmsisNNEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_NN_ENABLE", None)
        cmsisNNEnableSym.setLabel("Enable CMSIS NN")
        cmsisNNEnableSym.setDescription("Copies cmsis Neural Network (NN) files into the project and adds it into project path")

        #Create Include file symbols
        cmsisNNIncludePath = os.path.join(Variables.get("__CMSIS_PACK_DIR"), "CMSIS", "NN", "Include")
        for headerFileName in  os.listdir(cmsisNNIncludePath):
            szSymbol = headerFileName.replace(".", "_").upper()
            headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(cmsisNNIncludePath + os.sep + headerFileName)
            headerFile.setOutputName(headerFileName)
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/CMSIS/CMSIS/NN/Include/")
            headerFile.setProjectPath("packs/CMSIS/CMSIS/NN/Include/")
            headerFile.setType("HEADER")
            headerFile.setEnabled(cmsisNNEnableSym.getValue())
            headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

            if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                #for Secure
                headerFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(cmsisNNIncludePath + os.sep + headerFileName)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/CMSIS/CMSIS/NN/Include/")
                headerFile.setProjectPath("packs/CMSIS/CMSIS/NN/Include/")
                headerFile.setType("HEADER")
                headerFile.setEnabled(cmsisNNEnableSym.getValue())
                headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])
                headerFile.setSecurity("SECURE")

        #CMSIS NN include path setting symbol
        cmsisNNIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_NN_INCLUDE_DIRS", None)
        cmsisNNIncludeSetting.setCategory("C32")
        cmsisNNIncludeSetting.setKey("extra-include-directories")
        cmsisNNIncludeSetting.setValue("../src/packs/CMSIS/CMSIS/NN/Include/")
        cmsisNNIncludeSetting.setAppend(True, ";")
        cmsisNNIncludeSetting.setEnabled(cmsisNNEnableSym.getValue())
        cmsisNNIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

        cmsisNNXc32cppIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_NN_XC32CPP_INCLUDE_DIRS", None)
        cmsisNNXc32cppIncludeSetting.setCategory("C32CPP")
        cmsisNNXc32cppIncludeSetting.setKey("extra-include-directories")
        cmsisNNXc32cppIncludeSetting.setValue(cmsisNNIncludeSetting.getValue())
        cmsisNNXc32cppIncludeSetting.setAppend(True, ";")
        cmsisNNXc32cppIncludeSetting.setEnabled(cmsisNNEnableSym.getValue())
        cmsisNNXc32cppIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            #CMSIS NN include path setting symbol for Secure
            cmsisNNIncludeSetting = cmsisComponent.createSettingSymbol("SEC_CMSIS_NN_INCLUDE_DIRS", None)
            cmsisNNIncludeSetting.setCategory("C32")
            cmsisNNIncludeSetting.setKey("extra-include-directories")
            cmsisNNIncludeSetting.setValue("../src/packs/CMSIS/CMSIS/NN/Include/")
            cmsisNNIncludeSetting.setAppend(True, ";")
            cmsisNNIncludeSetting.setEnabled(cmsisNNEnableSym.getValue())
            cmsisNNIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])
            cmsisNNIncludeSetting.setSecurity("SECURE")

            cmsisNNXc32cppIncludeSetting = cmsisComponent.createSettingSymbol("SEC_CMSIS_NN_XC32CPP_INCLUDE_DIRS", None)
            cmsisNNXc32cppIncludeSetting.setCategory("C32CPP")
            cmsisNNXc32cppIncludeSetting.setKey("extra-include-directories")
            cmsisNNXc32cppIncludeSetting.setValue(cmsisNNIncludeSetting.getValue())
            cmsisNNXc32cppIncludeSetting.setAppend(True, ";")
            cmsisNNXc32cppIncludeSetting.setEnabled(cmsisNNEnableSym.getValue())
            cmsisNNXc32cppIncludeSetting.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])
            cmsisNNXc32cppIncludeSetting.setSecurity("SECURE")

        #Create source file symbols
        cmsisNNSourcePath = os.path.join(Variables.get("__CMSIS_PACK_DIR"), "CMSIS", "NN", "Source")
        supportedExtension = ["c", "h", "s"]
        for root,_,files in os.walk(cmsisNNSourcePath):
            for sourceFileName in files:
                if sourceFileName.split(".")[1].lower() in supportedExtension:
                    szSymbol = sourceFileName.replace(".", "_").upper()
                    sourceFile = cmsisComponent.createFileSymbol(szSymbol, None)
                    sourceFile.setRelative(False)
                    sourceFile.setSourcePath(os.path.join(root, sourceFileName))
                    sourceFile.setOutputName(sourceFileName)
                    sourceFile.setMarkup(False)
                    sourceFile.setOverwrite(True)
                    sourceFile.setDestPath(os.path.normpath("../../packs/CMSIS/CMSIS/NN/Source/" + os.path.basename(root)))
                    sourceFile.setProjectPath(os.path.normpath("packs/CMSIS/CMSIS/NN/Source/" + os.path.basename(root)))
                    sourceFile.setType("SOURCE")
                    sourceFile.setEnabled(cmsisNNEnableSym.getValue())
                    sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

                    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                        #for Secure
                        sourceFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                        sourceFile.setRelative(False)
                        sourceFile.setSourcePath(os.path.join(root, sourceFileName))
                        sourceFile.setOutputName(sourceFileName)
                        sourceFile.setMarkup(False)
                        sourceFile.setOverwrite(True)
                        sourceFile.setDestPath(os.path.normpath("../../packs/CMSIS/CMSIS/NN/Source/" + os.path.basename(root)))
                        sourceFile.setProjectPath(os.path.normpath("packs/CMSIS/CMSIS/NN/Source/" + os.path.basename(root)))
                        sourceFile.setType("SOURCE")
                        sourceFile.setSecurity("SECURE")
                        sourceFile.setEnabled(cmsisNNEnableSym.getValue())
                        sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

    #If this is a cortex A device
    elif cortexType.startswith("a"):
################################################################################
############################### CMSIS Core #####################################
################################################################################

        headerFileNames = ["cmsis_compiler.h", "cmsis_gcc.h", "cmsis_iccarm.h", "cmsis_cp15.h", "core_ca.h"]

        # add core header files for cortex a devices
        for headerFileName in headerFileNames:
            szSymbol = "CORE_A_{}_H".format(headerFileName[:-2].upper())
            headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Core_A/Include/" + headerFileName)
            headerFile.setOutputName(headerFileName)
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core_A/Include/")
            headerFile.setProjectPath("packs/CMSIS/CMSIS/Core_A/Include/")
            headerFile.setType("HEADER")


