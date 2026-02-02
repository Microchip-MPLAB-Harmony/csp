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
    cmsisNnPath = Variables.get("__FRAMEWORK_ROOT") + "/CMSIS-NN/"

    pdscPath = os.path.join(cmsisNnPath, "ARM.CMSIS-NN.pdsc")
    cmsisReleaseInfo = ET.parse(pdscPath).getroot().find("releases/release")
    cmsisNnPath = os.path.dirname(pdscPath)

    cmsisVersion = cmsisComponent.createCommentSymbol("CMSIS_NN_VERSION", None)
    cmsisVersion.setLabel("Release version: {0}".format(cmsisReleaseInfo.get("version")))

    cmsisReleaseDate = cmsisComponent.createCommentSymbol("CMSIS_NN_RELEASE_DATE", None)
    cmsisReleaseDate.setLabel("Release date: {0}".format(cmsisReleaseInfo.get("date")))


################################################################################
############################### CMSIS NN ######################################
################################################################################

    # Enables cmsis-nn
    cmsisNNEnableSym = cmsisComponent.createBooleanSymbol("CMSIS_NN_ENABLE", None)
    cmsisNNEnableSym.setLabel("Enable CMSIS NN")
    cmsisNNEnableSym.setDescription("Copies cmsis Neural Network (NN) files into the project and adds it into project path")
    cmsisNNEnableSym.setDefaultValue(True)

    # Add all CMSIS-NN header files from 'Include' directory
    cmsisNNIncludePath = os.path.join(cmsisNnPath, "Include")
    for includePath, _, headerFiles in os.walk(cmsisNNIncludePath):
        for headerFileName in headerFiles:
            if headerFileName.endswith(".h"):
                filePath = os.path.join(includePath, headerFileName).replace("\\", "/")
                projPath = os.path.relpath(includePath, cmsisNnPath).replace("\\", "/")
                szSymbol = headerFileName.replace(".", "_").upper()
                headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
                headerFile.setRelative(False)
                headerFile.setSourcePath(filePath)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/CMSIS-NN/{0}/".format(projPath))
                headerFile.setProjectPath("packs/CMSIS-NN/{0}/".format(projPath))
                headerFile.setType("HEADER")
                headerFile.setEnabled(cmsisNNEnableSym.getValue())
                headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

                if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                    # For secure project
                    headerFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                    headerFile.setRelative(False)
                    headerFile.setSourcePath(filePath)
                    headerFile.setOutputName(headerFileName)
                    headerFile.setMarkup(False)
                    headerFile.setOverwrite(True)
                    headerFile.setDestPath("../../packs/CMSIS-NN/{0}/".format(projPath))
                    headerFile.setProjectPath("packs/CMSIS-NN/{0}/".format(projPath))
                    headerFile.setType("HEADER")
                    headerFile.setSecurity("SECURE")
                    headerFile.setEnabled(cmsisNNEnableSym.getValue())
                    headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

    cmsisNNSourcePath = os.path.join(cmsisNnPath, "Source")
    for sourcePath, _, sourceFiles in os.walk(cmsisNNSourcePath):
        for sourceFileName in sourceFiles:
            if sourceFileName.endswith(".c") or sourceFileName.endswith(".cpp") or sourceFileName.endswith(".h"):
                filePath = os.path.join(sourcePath, sourceFileName).replace("\\", "/")
                projPath = os.path.relpath(sourcePath, cmsisNnPath).replace("\\", "/")
                szSymbol = sourceFileName.replace(".", "_").upper()
                sourceFile = cmsisComponent.createFileSymbol(szSymbol, None)
                sourceFile.setRelative(False)
                sourceFile.setSourcePath(filePath)
                sourceFile.setOutputName(sourceFileName)
                sourceFile.setMarkup(False)
                sourceFile.setOverwrite(True)
                sourceFile.setDestPath("../../packs/CMSIS-NN/{0}/".format(projPath))
                sourceFile.setProjectPath("packs/CMSIS-NN/{0}/".format(projPath))
                if sourceFileName.endswith(".h"):
                    sourceFile.setType("HEADER")
                else:
                    sourceFile.setType("SOURCE")
                sourceFile.setEnabled(cmsisNNEnableSym.getValue())
                sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

                if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
                    # For secure project
                    sourceFile = cmsisComponent.createFileSymbol("SEC_" + szSymbol, None)
                    sourceFile.setRelative(False)
                    sourceFile.setSourcePath(filePath)
                    sourceFile.setOutputName(sourceFileName)
                    sourceFile.setMarkup(False)
                    sourceFile.setOverwrite(True)
                    sourceFile.setDestPath("../../packs/CMSIS-NN/{0}/".format(projPath))
                    sourceFile.setProjectPath("packs/CMSIS-NN/{0}/".format(projPath))
                    if sourceFileName.endswith(".h"):
                        sourceFile.setType("HEADER")
                    else:
                        sourceFile.setType("SOURCE")
                    sourceFile.setSecurity("SECURE")
                    sourceFile.setEnabled(cmsisNNEnableSym.getValue())
                    sourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_NN_ENABLE"])

    #CMSIS NN include path setting symbol
    cmsisNNIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_NN_INCLUDE_DIRS", None)
    cmsisNNIncludeSetting.setCategory("C32")
    cmsisNNIncludeSetting.setKey("extra-include-directories")
    cmsisNNIncludeSetting.setValue("../src/packs/CMSIS-NN/;../src/packs/CMSIS-NN/Include/;../src/packs/CMSIS-NN/Include/Internal/")
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
        cmsisNNIncludeSetting.setValue("../src/packs/CMSIS-NN/;../src/packs/CMSIS-NN/Include/;../src/packs/CMSIS-NN/Include/Internal/")
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


