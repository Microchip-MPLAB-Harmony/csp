# coding: utf-8
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

###################################################################################################
########################################## Component  #############################################
###################################################################################################
def wakeupEnableCalculate(symbol, event):
    wakeupId = int(event["id"].split("_")[1])
    if event["value"]:
        symbol.setValue((symbol.getValue() | 1 << wakeupId), 2)
    else:
        symbol.setValue((symbol.getValue() & ~(1 << wakeupId)), 2)

def wakeupPolarityCalculate(symbol, event):
    wakeupId = int(event["id"].split("_")[1])
    if event["value"] == 1:
        symbol.setValue((symbol.getValue() | 1 << wakeupId), 2)
    else:
        symbol.setValue((symbol.getValue() & ~(1 << wakeupId)), 2)

def instantiateComponent(rstcComponent):
    rstcWakeupNum = None
    rstcInstanceName = rstcComponent.createStringSymbol("RSTC_INSTANCE_NAME", None)
    rstcInstanceName.setVisible(False)
    rstcInstanceName.setDefaultValue(rstcComponent.getID().upper())

    rstcSym_Enable = rstcComponent.createBooleanSymbol("RSTC_ENABLE", None)
    rstcSym_Enable.setLabel("Use Reset Controller ?")
    rstcSym_Enable.setDefaultValue(True)
    rstcSym_Enable.setReadOnly(True)

    rstcResetCause = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/register-group@[name="RSTC"]/register@[name="RCAUSE"]')

    rstcSym_RCAUSE_Index = rstcComponent.createIntegerSymbol("RSTC_RCAUSE_LENGTH", None)
    rstcSym_RCAUSE_Index.setDefaultValue(len(rstcResetCause.getChildren()))
    rstcSym_RCAUSE_Index.setVisible(False)

    for id in range(0,len(rstcResetCause.getChildren())):
        rstcSym_RCAUSE = rstcComponent.createKeyValueSetSymbol("RSTC_RCAUSE"+str(id), None)
        rstcSym_RCAUSE.setLabel(str(rstcResetCause.getChildren()[id].getAttribute("caption")))
        rstcSym_RCAUSE.addKey(rstcResetCause.getChildren()[id].getAttribute("name"), str(id), rstcResetCause.getChildren()[id].getAttribute("caption"))
        rstcSym_RCAUSE.setOutputMode("Key")
        rstcSym_RCAUSE.setDisplayMode("Description")
        rstcSym_RCAUSE.setVisible(False)

    rstcBkup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/register-group@[name="RSTC"]/register@[name="BKUPEXIT"]')
    if rstcBkup != None:
        rstcSym_BKUPEXIT_Index = rstcComponent.createIntegerSymbol("RSTC_BKUPEXIT_LENGTH", None)
        rstcSym_BKUPEXIT_Index.setDefaultValue(len(rstcBkup.getChildren()))
        rstcSym_BKUPEXIT_Index.setVisible(False)

        for id in range(0,len(rstcBkup.getChildren())):
            rstcSym_BKUPEXIT = rstcComponent.createKeyValueSetSymbol("RSTC_BKUPEXIT"+str(id), None)
            rstcSym_BKUPEXIT.setLabel(str(rstcBkup.getChildren()[id].getAttribute("caption")))
            rstcSym_BKUPEXIT.addKey(rstcBkup.getChildren()[id].getAttribute("name"), str(id), rstcBkup.getChildren()[id].getAttribute("caption"))
            rstcSym_BKUPEXIT.setOutputMode("Key")
            rstcSym_BKUPEXIT.setDisplayMode("Description")
            rstcSym_BKUPEXIT.setVisible(False)

    rstcWakeup = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="RSTC"]/instance/parameters')
    for id in range(0,len(rstcWakeup.getChildren())):
        if rstcWakeup.getChildren()[id].getAttribute("name") == "NUMBER_OF_EXTWAKE":
            if int(rstcWakeup.getChildren()[id].getAttribute("value")) > 0:
                wakeupEnableDependencyList = []
                wakeupPolarityDependencyList = []
                rstcWakeupNum = rstcComponent.createIntegerSymbol("RSTC_WAKEUP_PIN_NUMBER", None)
                rstcWakeupNum.setVisible(False)
                rstcWakeupNum.setDefaultValue(int(rstcWakeup.getChildren()[id].getAttribute("value")))

                rstcwakeupMenu = rstcComponent.createMenuSymbol("RSTC_WAKEUP_MENU", None)
                rstcwakeupMenu.setLabel("Wakeup Configuration")

                
                node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/value-group@[name="RSTC_WKDBCONF__WKDBCNT"]')
                nodeValues = node.getChildren()
                rstcDebounce = rstcComponent.createKeyValueSetSymbol("RSTC_DEBOUNCE", rstcwakeupMenu)
                rstcDebounce.setLabel("Wakeup Debounce Counter Value")
                for index in range(0, len(nodeValues)):
                    key =  nodeValues[index].getAttribute("name")
                    value =  nodeValues[index].getAttribute("value")
                    description =  nodeValues[index].getAttribute("caption")
                    rstcDebounce.addKey(key, value, description)
                rstcDebounce.setDefaultValue(0)
                rstcDebounce.setOutputMode("Value")
                rstcDebounce.setDisplayMode("Description")

                for i in range(0, rstcWakeupNum.getValue()):
                    wakeupEnable = rstcComponent.createBooleanSymbol("WAKEUP_" + str(i) + "_ENABLE" , rstcwakeupMenu)
                    wakeupEnable.setLabel("Enable Wakeup " + str(i))
                    wakeupEnable.setDefaultValue(False)
                    wakeupEnableDependencyList.append("WAKEUP_" + str(i) + "_ENABLE")

                    wakeupPolarity = rstcComponent.createKeyValueSetSymbol("WAKEUP_" + str(i) + "_POLARITY", wakeupEnable)
                    wakeupPolarity.setLabel("Wakeup Polarity")
                    wakeupPolarity.addKey("Active Low", "0", "Input pin x is active low.")
                    wakeupPolarity.addKey("Active High", "1", "Input pin x is active High.")
                    wakeupPolarity.setDefaultValue(0)
                    wakeupPolarity.setOutputMode("Value")
                    wakeupPolarity.setDisplayMode("Key")
                    wakeupPolarityDependencyList.append("WAKEUP_" + str(i) + "_POLARITY")
                
                wakeupEnableValue = rstcComponent.createHexSymbol("WAKEUP_ENABLE_VALUE", rstcwakeupMenu)
                wakeupEnableValue.setVisible(False)
                wakeupEnableValue.setDefaultValue(0)
                wakeupEnableValue.setDependencies(wakeupEnableCalculate, wakeupEnableDependencyList)

                wakeupPolarityValue = rstcComponent.createHexSymbol("WAKEUP_POLARITY_VALUE", rstcwakeupMenu)
                wakeupPolarityValue.setVisible(False)
                wakeupPolarityValue.setDefaultValue(0)
                wakeupPolarityValue.setDependencies(wakeupPolarityCalculate, wakeupPolarityDependencyList)
            
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
    rstcModuleID = rstcModuleNode.getAttribute("id")

    rstcSym_HeaderFile = rstcComponent.createFileSymbol("RSTC_HEADER", None)
    rstcSym_HeaderFile.setSourcePath("../peripheral/rstc_u2239/templates/plib_rstc.h.ftl")
    rstcSym_HeaderFile.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".h")
    rstcSym_HeaderFile.setDestPath("peripheral/rstc/")
    rstcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_HeaderFile.setType("HEADER")
    rstcSym_HeaderFile.setMarkup(True)

    rstcSym_SourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
    rstcSym_SourceFile.setSourcePath("../peripheral/rstc_u2239/templates/plib_rstc.c.ftl")
    rstcSym_SourceFile.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".c")
    rstcSym_SourceFile.setDestPath("peripheral/rstc/")
    rstcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_SourceFile.setType("SOURCE")
    rstcSym_SourceFile.setMarkup(True)

    rstcSym_SystemDefFile = rstcComponent.createFileSymbol("RSTC_SYS_DEF", None)
    rstcSym_SystemDefFile.setType("STRING")
    rstcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSym_SystemDefFile.setSourcePath("../peripheral/rstc_u2239/templates/system/definitions.h.ftl")
    rstcSym_SystemDefFile.setMarkup(True)

    if rstcWakeupNum != None:
        RSTCSystemInitFile = rstcComponent.createFileSymbol("RSTC_INIT", None)
        RSTCSystemInitFile.setType("STRING")
        RSTCSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        RSTCSystemInitFile.setSourcePath("../peripheral/rstc_u2239/templates/system/initialization.c.ftl")
        RSTCSystemInitFile.setMarkup(True)
