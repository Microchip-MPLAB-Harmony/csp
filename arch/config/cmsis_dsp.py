"""*****************************************************************************
* Copyright (C) 2026 Microchip Technology Inc. and its subsidiaries.
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

def instantiateComponent(cmsisComponent):
    import xml.etree.ElementTree as ET
    cmsisDspPath = Variables.get("__FRAMEWORK_ROOT") + "/CMSIS-DSP/"

    pdscPath = os.path.join(cmsisDspPath, "ARM.CMSIS-DSP.pdsc")
    cmsisReleaseInfo = ET.parse(pdscPath).getroot().find("releases/release")
    cmsisDspPath = os.path.dirname(pdscPath)

    cmsisVersion = cmsisComponent.createCommentSymbol("CMSIS_DSP_VERSION", None)
    cmsisVersion.setLabel("Release version: {0}".format(cmsisReleaseInfo.get("version")))

    cmsisReleaseDate = cmsisComponent.createCommentSymbol("CMSIS_DSP_RELEASE_DATE", None)
    cmsisReleaseDate.setLabel("Release date: {0}".format(cmsisReleaseInfo.get("date")))

################################################################################
############################### CMSIS DSP ######################################
################################################################################

    #Enables cmsis-dsp
    cmsisDSPEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_DSP_ENABLE", None)
    cmsisDSPEnableSym.setLabel("Enable CMSIS DSP")
    cmsisDSPEnableSym.setDescription("Copies cmsis-dsp files into the project and adds it into project path")
    cmsisDSPEnableSym.setDefaultValue(True)

    # Add all DSP header files from 'Include' and 'PrivateInclude' directories
    includeDirs = ["Include", "PrivateInclude"]
    for dirName in includeDirs:
        cmsisDSPIncludePath = os.path.join(cmsisDspPath, dirName)
        for includePath, _, headerFiles in os.walk(cmsisDSPIncludePath):
            for headerFileName in headerFiles:
                if headerFileName.endswith(".h"):
                    filePath = os.path.join(includePath, headerFileName).replace("\\", "/")
                    projPath = os.path.relpath(includePath, cmsisDspPath).replace("\\", "/")
                    szSymbol = headerFileName.replace(".", "_").upper()
                    headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
                    headerFile.setRelative(False)
                    headerFile.setSourcePath(filePath)
                    headerFile.setOutputName(headerFileName)
                    headerFile.setMarkup(False)
                    headerFile.setOverwrite(True)
                    headerFile.setDestPath("../../packs/CMSIS-DSP/{0}/".format(projPath))
                    headerFile.setProjectPath("packs/CMSIS-DSP/{0}/".format(projPath))
                    headerFile.setType("HEADER")
                    headerFile.setEnabled(cmsisDSPEnableSym.getValue())
                    headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

                    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                        # For secure project
                        headerFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                        headerFile.setRelative(False)
                        headerFile.setSourcePath(filePath)
                        headerFile.setOutputName(headerFileName)
                        headerFile.setMarkup(False)
                        headerFile.setOverwrite(True)
                        headerFile.setDestPath("../../packs/CMSIS-DSP/{0}/".format(projPath))
                        headerFile.setProjectPath("packs/CMSIS-DSP/{0}/".format(projPath))
                        headerFile.setType("HEADER")
                        headerFile.setSecurity("SECURE")
                        headerFile.setEnabled(cmsisDSPEnableSym.getValue())
                        headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

    # Add all DSP source files from 'Source' directory
    cmsisDSPSourcePath = os.path.join(cmsisDspPath, "Source")
    for sourcePath, _, sourceFiles in os.walk(cmsisDSPSourcePath):
        for sourceFileName in sourceFiles:
            if sourceFileName.endswith(".c") or sourceFileName.endswith(".cpp") or sourceFileName.endswith(".h"):
                filePath = os.path.join(sourcePath, sourceFileName).replace("\\", "/")
                projPath = os.path.relpath(sourcePath, cmsisDspPath).replace("\\", "/")
                szSymbol = sourceFileName.replace(".", "_").upper()
                sourceFile = cmsisComponent.createFileSymbol(szSymbol, None)
                sourceFile.setRelative(False)
                sourceFile.setSourcePath(filePath)
                sourceFile.setOutputName(sourceFileName)
                sourceFile.setMarkup(False)
                sourceFile.setOverwrite(True)
                sourceFile.setDestPath("../../packs/CMSIS-DSP/{0}/".format(projPath))
                sourceFile.setProjectPath("packs/CMSIS-DSP/{0}/".format(projPath))
                if sourceFileName.endswith(".h"):
                    sourceFile.setType("HEADER")
                else:
                    sourceFile.setType("SOURCE")
                sourceFile.setEnabled(cmsisDSPEnableSym.getValue())
                sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])
                if "_" in sourceFileName:
                    sourceFile.setExcludeFromProject(True)

                if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                    # For secure project
                    sourceFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                    sourceFile.setRelative(False)
                    sourceFile.setSourcePath(filePath)
                    sourceFile.setOutputName(sourceFileName)
                    sourceFile.setMarkup(False)
                    sourceFile.setOverwrite(True)
                    sourceFile.setDestPath("../../packs/CMSIS-DSP/{0}/".format(projPath))
                    sourceFile.setProjectPath("packs/CMSIS-DSP/{0}/".format(projPath))
                    if sourceFileName.endswith(".h"):
                        sourceFile.setType("HEADER")
                    else:
                        sourceFile.setType("SOURCE")
                    sourceFile.setSecurity("SECURE")
                    sourceFile.setEnabled(cmsisDSPEnableSym.getValue())
                    sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])
                    if "_" in sourceFileName:
                        sourceFile.setExcludeFromProject(True)

    cmsisDsPIncludePath = "../src/packs/CMSIS-DSP/PrivateInclude/;../src/packs/CMSIS-DSP/Include/;../src/packs/CMSIS-DSP/Include/dsp"

    if ATDF.getNode('/avr-tools-device-file/devices').getChildren()[0].getAttribute("architecture").split("CORTEX-")[1].lower().startswith("a"):
        cmsisComputeLibEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_COMPUTE_LIB_ENABLE", cmsisDSPEnableSym)
        cmsisComputeLibEnableSym.setLabel("Enable Compute Library")
        cmsisComputeLibEnableSym.setDescription("Copies ComputeLibrary files into the project and adds it into project path")
        cmsisComputeLibEnableSym.setDefaultValue(False)
        cmsisComputeLibEnableSym.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_DSP_ENABLE"])

        cmsisDsPIncludePath = cmsisDsPIncludePath + "/;../src/packs/CMSIS-DSP/ComputeLibrary/Include"

        # Add all files from 'ComputeLibrary' directory
        Dirs = ["ComputeLibrary"]
        for dirName in Dirs:
            cmsisDSPSourcePath = os.path.join(cmsisDspPath, dirName)
            for sourcePath, _, sourceFiles in os.walk(cmsisDSPSourcePath):
                for sourceFileName in sourceFiles:
                    if sourceFileName.endswith(".c") or sourceFileName.endswith(".cpp") or sourceFileName.endswith(".h"):
                        filePath = os.path.join(sourcePath, sourceFileName).replace("\\", "/")
                        projPath = os.path.relpath(sourcePath, cmsisDspPath).replace("\\", "/")
                        szSymbol = sourceFileName.replace(".", "_").upper()
                        sourceFile = cmsisComponent.createFileSymbol(szSymbol, None)
                        sourceFile.setRelative(False)
                        sourceFile.setSourcePath(filePath)
                        sourceFile.setOutputName(sourceFileName)
                        sourceFile.setMarkup(False)
                        sourceFile.setOverwrite(True)
                        sourceFile.setDestPath("../../packs/CMSIS-DSP/{0}/".format(projPath))
                        sourceFile.setProjectPath("packs/CMSIS-DSP/{0}/".format(projPath))
                        if sourceFileName.endswith(".h"):
                            sourceFile.setType("HEADER")
                        else:
                            sourceFile.setType("SOURCE")
                        sourceFile.setEnabled(cmsisComputeLibEnableSym.getValue())
                        sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_COMPUTE_LIB_ENABLE"])

    # Set include path for compiler
    cmsisDSPIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_DSP_INCLUDE_DIRS", None)
    cmsisDSPIncludeSetting.setCategory("C32")
    cmsisDSPIncludeSetting.setKey("extra-include-directories")
    cmsisDSPIncludeSetting.setValue(cmsisDsPIncludePath)
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
        cmsisDSPIncludeSetting.setValue("../src/packs/CMSIS-DSP/PrivateInclude/;../src/packs/CMSIS-DSP/Include/;../src/packs/CMSIS-DSP/Include/dsp")
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

