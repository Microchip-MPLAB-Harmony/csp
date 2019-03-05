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

Log.writeInfoMessage("Loading Matrix for " + Variables.get("__PROCESSOR"))

configName = Variables.get("__CONFIGURATION_NAME")

matrixFile = coreComponent.createFileSymbol("MATRIX_C", None)
matrixFile.setSourcePath("../peripheral/matrix_44025/templates/plib_matrix.c")
matrixFile.setOutputName("plib_matrix.c")
matrixFile.setDestPath("peripheral/matrix/")
matrixFile.setProjectPath("config/" + configName + "/peripheral/matrix/")
matrixFile.setType("SOURCE")
matrixFile.setMarkup(False)

matrixHeader = coreComponent.createFileSymbol("MATRIX_H", None)
matrixHeader.setSourcePath("../peripheral/matrix_44025/templates/plib_matrix.h")
matrixHeader.setOutputName("plib_matrix.h")
matrixHeader.setDestPath("peripheral/matrix/")
matrixHeader.setProjectPath("config/" + configName + "/peripheral/matrix/")
matrixHeader.setType("HEADER")
matrixHeader.setMarkup(False)

matrixSystemInitFile = coreComponent.createFileSymbol("matrixSystemInitFile", None)
matrixSystemInitFile.setType("STRING")
matrixSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
matrixSystemInitFile.setSourcePath("../peripheral/matrix_44025/templates/system/initialization.c.ftl")
matrixSystemInitFile.setMarkup(True)

matrixSystemDefFile = coreComponent.createFileSymbol("matrixSystemDefFile", None)
matrixSystemDefFile.setType("STRING")
matrixSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
matrixSystemDefFile.setSourcePath("../peripheral/matrix_44025/templates/system/definitions.h.ftl")
matrixSystemDefFile.setMarkup(True)

