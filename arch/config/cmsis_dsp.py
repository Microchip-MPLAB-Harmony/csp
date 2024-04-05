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
import xml.etree.ElementTree as ET

CMSIS_FILE_LIST ="/config/filelist/cmsis_dsp_files.xml"

XML_ATTRIB_NAME = "name"
XML_ATTRIB_COPY = "copy"
XML_ATTRIB_DIR  = "dir"
XML_ATTRIB_FILE  = "file"


def instantiateComponent(cmsisComponent):

    cmsisPath = Variables.get("__FRAMEWORK_ROOT") + "/CMSIS-DSP/"

    pdscPath = os.path.join(cmsisPath, "ARM.CMSIS-DSP.pdsc")
    cmsisReleaseInfo = ET.parse(pdscPath).getroot().find("releases/release")

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

    AddCMSISFiles(cmsisComponent, Variables.get("__FRAMEWORK_ROOT"), Module.getPath()+CMSIS_FILE_LIST)

    #CMSIS DSP include path setting symbol
    cmsisDSPIncludeSetting = cmsisComponent.createSettingSymbol("CMSIS_DSP_INCLUDE_DIRS", None)
    cmsisDSPIncludeSetting.setCategory("C32")
    cmsisDSPIncludeSetting.setKey("extra-include-directories")
    cmsisDSPIncludeSetting.setValue("../src/packs/CMSIS-DSP/PrivateInclude/;../src/packs/CMSIS-DSP/Include/;../src/packs/CMSIS-DSP/Include/dsp")
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



def enable_cmsis_dsp_files(symbol, event):
    symbol.setEnabled(event["value"])

# Add File
def AddFile(child,component, sourcePath, fileName, destPath, projectPath):
    tfliteAddFile = component.createFileSymbol(fileName.upper(), None)
    tfliteAddFile.setSourcePath(sourcePath)
    tfliteAddFile.setOutputName(fileName)
    tfliteAddFile.setDestPath(destPath)
    tfliteAddFile.setProjectPath(projectPath)
    tfliteAddFile.setMarkup(False)
    tfliteAddFile.setOverwrite(True)
    tfliteAddFile.setRelative(False)
    tfliteAddFile.setEnabled(True)
    tfliteAddFile.setDependencies(enable_cmsis_dsp_files, ["CMSIS_DSP_ENABLE"])

    if(".h" in fileName):
        tfliteAddFile.setType("HEADER")
    else:
        tfliteAddFile.setType("SOURCE")

    if XML_ATTRIB_COPY in child.attrib and child.attrib[XML_ATTRIB_COPY] == "True":
        tfliteAddFile.setExcludeFromProject(True)

def AddDir(root,component,h3path,rpath):
    for child in root:
        if child.tag == XML_ATTRIB_FILE:
            fileName = str(child.attrib[XML_ATTRIB_NAME])
            sourceDir=h3path + "/" + rpath
            sourcePath = os.path.normpath(os.path.join(sourceDir, fileName))
            destPath = os.path.normpath("../../packs/" + rpath)
            projectPath = os.path.normpath("/packs/" + rpath)
            AddFile(child,component, sourcePath, fileName, destPath, projectPath)

def AddCMSISFiles(component, h3path, file):
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            rpath=child.attrib[XML_ATTRIB_NAME]
            AddDir(child,component,h3path,rpath)




