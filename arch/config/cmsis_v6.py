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

def instantiateComponent(cmsisComponent):

    cmsisPath = Variables.get("__FRAMEWORK_ROOT") + "/CMSIS_6/"

    pdscPath = os.path.join(cmsisPath, "ARM.CMSIS.pdsc")
    cmsisReleaseInfo = ET.parse(pdscPath).getroot().find("releases/release")
    cmsisPath = os.path.dirname(pdscPath)

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
        coreHeaderFileNames = [ "core_c" + cortexType + ".h",
                                "cmsis_version.h",
                                "cmsis_compiler.h",
                                "cmsis_iccarm.h",
                                "m-profile/cmsis_iccarm_m.h",
                                "cmsis_gcc.h",
                                "m-profile/cmsis_gcc_m.h",
                                "cmsis_armclang.h",
                                "m-profile/cmsis_armclang_m.h",
                                "m-profile/armv" + ("8" if cortexType in v8Cores else "7") + "m_mpu.h",  #v8 cores uses MPUv8
                                "m-profile/armv7m_cachel1.h" #v3.7.0 supports  enhanced cache functions for ARM-v7M
                              ]

        #v8 cores support trustZone
        if cortexType in v8Cores:
            coreHeaderFileNames.append("tz_context.h")

        for headerFileName in coreHeaderFileNames:
            szSymbol = headerFileName.replace(".", "_").upper()
            headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            # Patch header file with inline function for ACLE intrinsics to build with XC32
            headerFile.setSourcePath(cmsisPath + "/CMSIS/Core/Include/" + headerFileName)
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
                # Patch header file with inline function for ACLE intrinsics to build with XC32
                headerFile.setSourcePath(cmsisPath + "/CMSIS/Core/Include/" + headerFileName)
                headerFile.setOutputName(headerFileName)
                headerFile.setMarkup(False)
                headerFile.setOverwrite(True)
                headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
                headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
                headerFile.setType("HEADER")
                headerFile.setSecurity("SECURE")
                headerFile.setEnabled(cmsisCoreEnableSym.getValue())
                headerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["CMSIS_CORE_ENABLE"])

    #If this is a cortex A device
    elif cortexType.startswith("a"):
################################################################################
############################### CMSIS Core #####################################
################################################################################

        headerFileNames = ["cmsis_compiler.h", "cmsis_gcc.h", "a-profile/cmsis_gcc_a.h", "cmsis_iccarm.h", "a-profile/cmsis_iccarm_a.h", "a-profile/cmsis_cp15.h", "core_ca.h"]

        # add core header files for cortex a devices
        for headerFileName in headerFileNames:
            szSymbol = "CORE_A_{}_H".format(headerFileName[:-2].upper())
            headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
            headerFile.setRelative(False)
            headerFile.setSourcePath(cmsisPath + "/CMSIS/Core/Include/" + headerFileName)
            headerFile.setOutputName(headerFileName)
            headerFile.setMarkup(False)
            headerFile.setOverwrite(True)
            headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
            headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
            headerFile.setType("HEADER")
