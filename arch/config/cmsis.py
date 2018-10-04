"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

def instantiateComponent(cmsisComponent):

    cmsisSupportedVersion = "5.4.0"

    cmsisInformation = cmsisComponent.createCommentSymbol("cmsisInformation", None)
    cmsisError = cmsisComponent.createCommentSymbol("cmsisError", None)
    cmsisError.setLabel("Error: This version of CMSIS Pack is not supported! Supported version is " + cmsisSupportedVersion)
    cmsisError.setVisible(False)

    import xml.etree.ElementTree as ET
    cmsisDescriptionFile = open(Variables.get("__CMSIS_PACK_DIR") + "/ARM.CMSIS.pdsc", "r")
    cmsisDescription = ET.fromstring(cmsisDescriptionFile.read())
    for release in cmsisDescription.iter("release"):
        cmsisInformation.setLabel("Release Information: " + str(release.attrib))
        if release.attrib['version'] != cmsisSupportedVersion:
            Log.writeErrorMessage("Error: This version of CMSIS Pack is not supported! Supported version is " + cmsisSupportedVersion)
            cmsisError.setVisible(True)
            return
        break
		
    archNode = ATDF.getNode('/avr-tools-device-file/devices')
    coreFile = "core_c" + str(archNode.getChildren()[0].getAttribute("architecture").split("CORTEX-")[1].lower()) + ".h"

    # add core header files
    headerFileNames = ["cmsis_compiler.h", "cmsis_gcc.h", "tz_context.h", str(eval('coreFile')), "mpu_armv7.h", "cmsis_version.h"]

    for headerFileName in headerFileNames:
        szSymbol = "{}_H".format(headerFileName[:-2].upper())
        headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Core/Include/" + headerFileName)
        headerFile.setOutputName(headerFileName)
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
        headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
        headerFile.setType("HEADER")

    # add dsp header files
    headerFileNames = ["arm_common_tables.h", "arm_const_structs.h", "arm_math.h"]

    for headerFileName in headerFileNames:
        szSymbol = "{}_H".format(headerFileName[:-2].upper())
        headerFile = cmsisComponent.createFileSymbol(szSymbol, None)
        headerFile.setRelative(False)
        headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/DSP/Include/" + headerFileName)
        headerFile.setOutputName(headerFileName)
        headerFile.setMarkup(False)
        headerFile.setOverwrite(True)
        headerFile.setDestPath("../../packs/CMSIS/CMSIS/DSP/Include/")
        headerFile.setProjectPath("packs/CMSIS/CMSIS/DSP/Include/")
        headerFile.setType("HEADER")
