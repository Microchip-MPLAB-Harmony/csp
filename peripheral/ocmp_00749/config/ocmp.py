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

################################################################################
#### Register Information ####
################################################################################
ocmpValGrp_OCxCON_OCM       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__OCM"]')
ocmpValGrp_OCxCON_OC32      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__OC32"]')
ocmpValGrp_OCxCON_SIDL      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__SIDL"]')

cfgBifield_OCACLK           = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGCON"]/bitfield@[name="OCACLK"]')

################################################################################
#### Global Variables ####
################################################################################

global ocmpInstanceName
global ocmpSym_OCxCON_OCM
global ocmpSym_OCxCON_OCTSEL
global ocmpSym_OCxCON_OC32
global ocmpSym_OCxCON_SIDL
global ocmpSym_OCxCON_OCTSEL_ALT
global ocmpSym_CFGCON_OCACLK

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################

def setOCMPInterruptData(status):

    Database.setSymbolValue("core", ocmpInterruptVector, status, 1)
    Database.setSymbolValue("core", ocmpInterruptHandlerLock, status, 1)

    interruptName = ocmpInterruptHandler.split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", ocmpInterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", ocmpInterruptHandler, interruptName + "_Handler", 1)

def updateOCMPInterruptData(symbol, event):

    if event["id"] == "OCMP_INTERRUPT_ENABLE":
        setOCMPInterruptData(event["value"])

    if ocmpSymInterruptMode.getValue() == True and Database.getSymbolValue("core", ocmpInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    return regName

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for bitfield in reversed(valueNodes):   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))
            if "irq-name" in param.getAttributeList():
                name = str(param.getAttribute("irq-name"))
            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):

    vector_index = "-1"

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

def combineValues(symbol, event):
    ocmValue = ocmpSym_OCxCON_OCM.getValue() << 0

    if cfgBifield_OCACLK != None:
        if(ocmpSym_CFGCON_OCACLK.getValue() == True):
            octselValue = ocmpSym_OCxCON_OCTSEL_ALT.getValue() << 3
        else:
            octselValue = ocmpSym_OCxCON_OCTSEL.getValue() << 3
    else:
        octselValue = ocmpSym_OCxCON_OCTSEL.getValue() << 3

    oc32Value   = ocmpSym_OCxCON_OC32.getValue() << 5
    sidlValue   = int(ocmpSym_OCxCON_SIDL.getValue()) << 13
    ocxconValue = sidlValue + oc32Value + octselValue + ocmValue

    symbol.setValue(ocxconValue, 2)

def ocmpSymbolVisible(symbol, event):
    symbol.setVisible(event["value"])

def ocmpTimerSourceVisibility(symbol, event):
    symbol.setVisible(not event["value"])

def ocmpCompareMax(symbol, event):
    if(event["value"] == 0):
        symbol.setMax(65535)
    else:
        symbol.setMax(4294967295)

def ocmpSecondaryCompare(symbol, event):
    if (event["id"] == "OCMP_OCxCON_OC32"):
        if(event["value"] == 0):
            symbol.setMax(65535)
        else:
            symbol.setMax(4294967295)
    if(event["id"] == "OCMP_OCxCON_OCM"):
        #Secondary compare value is required only for dual compare match modes
        if(event["value"] == 4 or event["value"] == 5):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def ocmpCommentVisible(symbol, event):
    #Only for PWM mode and continuous pulse
    if (int(event["value"]) > 4):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateOCMPClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])
################################################################################
#### Component ####
################################################################################

def instantiateComponent(ocmpComponent):

    global ocmpInstanceName
    global ocmpSymInterruptMode
    global ocmpSym_OCxCON_OCM
    global ocmpSym_OCxCON_OCTSEL
    global ocmpSym_OCxCON_OCTSEL_ALT
    global ocmpSym_OCxCON_OC32
    global ocmpSym_OCxCON_SIDL
    global ocmpSym_CFGCON_OCACLK
    global ocmpInterruptVector
    global ocmpInterruptHandlerLock
    global ocmpInterruptHandler
    global ocmpInterruptVectorUpdate

    #instance
    ocmpInstanceName = ocmpComponent.createStringSymbol("OCMP_INSTANCE_NAME", None)
    ocmpInstanceName.setVisible(False)
    ocmpInstanceName.setDefaultValue(ocmpComponent.getID().upper())
    Log.writeInfoMessage("Running " + ocmpInstanceName.getValue())

    ocmpInstanceNum = ocmpComponent.createStringSymbol("OCMP_INSTANCE_NUM", None)
    ocmpInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(ocmpComponent.getID()))
    ocmpInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", ocmpInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    ocmpSymInterruptMode = ocmpComponent.createBooleanSymbol("OCMP_INTERRUPT_ENABLE", None)
    ocmpSymInterruptMode.setLabel("Enable Interrupt ?")

    ocmpxOCM_names = []
    _get_bitfield_names(ocmpValGrp_OCxCON_OCM, ocmpxOCM_names)
    ocmpSym_OCxCON_OCM = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OCM", None)
    ocmpSym_OCxCON_OCM.setLabel("Select Output Compare Mode")
    ocmpSym_OCxCON_OCM.setDefaultValue(1)
    ocmpSym_OCxCON_OCM.setOutputMode("Value")
    ocmpSym_OCxCON_OCM.setDisplayMode("Description")
    for ii in ocmpxOCM_names:
        ocmpSym_OCxCON_OCM.addKey( ii['desc'], ii['value'], ii['key'] )

    if cfgBifield_OCACLK != None:
        ocmpSym_CFGCON_OCACLK = ocmpComponent.createBooleanSymbol("OCMP_CFGCON_OCACLK", None)
        ocmpSym_CFGCON_OCACLK.setLabel("Use Alternate Timer Source")
        ocmpSym_CFGCON_OCACLK.setVisible(cfgBifield_OCACLK != None)

    ocmpxOCTSEL_names = []
    ocmpSym_OCxCON_OCTSEL_ALT = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OCTSEL_ALT", None)
    ocmpSym_OCxCON_OCTSEL_ALT.setLabel("Select Timer Source")
    ocmpSym_OCxCON_OCTSEL_ALT.setDefaultValue(0)
    ocmpSym_OCxCON_OCTSEL_ALT.setOutputMode("Value")
    ocmpSym_OCxCON_OCTSEL_ALT.setDisplayMode("Description")
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"OCMP\"]/instance@[name=\""+ocmpInstanceName.getValue()+"\"]/parameters")
    ocmpxOCTSEL_names = node.getChildren()
    for ii in range(len(ocmpxOCTSEL_names)):
        if("TMR_ALTERNATE_SRC" in ocmpxOCTSEL_names[ii].getAttribute("name") ):
            ocmpSym_OCxCON_OCTSEL_ALT.addKey(ocmpxOCTSEL_names[ii].getAttribute("name"),
            ocmpxOCTSEL_names[ii].getAttribute("value"), ocmpxOCTSEL_names[ii].getAttribute("caption") )
    ocmpSym_OCxCON_OCTSEL_ALT.setVisible(False)
    ocmpSym_OCxCON_OCTSEL_ALT.setDependencies(ocmpSymbolVisible, ["OCMP_CFGCON_OCACLK"])

    ocmpxOCTSEL_names = []
    ocmpSym_OCxCON_OCTSEL = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OCTSEL", None)
    ocmpSym_OCxCON_OCTSEL.setLabel("Select Timer Source")
    ocmpSym_OCxCON_OCTSEL.setDefaultValue(0)
    ocmpSym_OCxCON_OCTSEL.setOutputMode("Value")
    ocmpSym_OCxCON_OCTSEL.setDisplayMode("Description")
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"OCMP\"]/instance@[name=\""+ocmpInstanceName.getValue()+"\"]/parameters")
    ocmpxOCTSEL_names = node.getChildren()
    for ii in range(len(ocmpxOCTSEL_names)):
        if("TMR_SRC" in ocmpxOCTSEL_names[ii].getAttribute("name") ):
            ocmpSym_OCxCON_OCTSEL.addKey(ocmpxOCTSEL_names[ii].getAttribute("name"),
            ocmpxOCTSEL_names[ii].getAttribute("value"), ocmpxOCTSEL_names[ii].getAttribute("caption") )
    ocmpSym_OCxCON_OCTSEL.setDependencies(ocmpTimerSourceVisibility, ["OCMP_CFGCON_OCACLK"])

    ocmpSym_TIMER_COMMENT = ocmpComponent.createCommentSymbol("OCMP_TIMER_COMMENT", None)
    ocmpSym_TIMER_COMMENT.setLabel("**** Configure Selected Timer Source (Timer x) in TMRx Component ****")

    ocmpxOC32_names = []
    _get_bitfield_names(ocmpValGrp_OCxCON_OC32, ocmpxOC32_names)
    ocmpSym_OCxCON_OC32 = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OC32", None)
    ocmpSym_OCxCON_OC32.setLabel("Select Timer Width")
    ocmpSym_OCxCON_OC32.setDefaultValue(0)
    ocmpSym_OCxCON_OC32.setOutputMode("Value")
    ocmpSym_OCxCON_OC32.setDisplayMode("Description")
    for ii in ocmpxOC32_names:
        ocmpSym_OCxCON_OC32.addKey( ii['desc'], ii['value'], ii['key'] )

    ocmpSym_COMPARE_VAL = ocmpComponent.createLongSymbol("OCMP_OCxR", None)
    ocmpSym_COMPARE_VAL.setLabel("Compare Value")
    ocmpSym_COMPARE_VAL.setDefaultValue(2000)
    ocmpSym_COMPARE_VAL.setMin(0)
    ocmpSym_COMPARE_VAL.setMax(65535)
    ocmpSym_COMPARE_VAL.setDependencies(ocmpCompareMax, ["OCMP_OCxCON_OC32"])

    ocmpSym_SEC_COMPARE_VAL = ocmpComponent.createLongSymbol("OCMP_OCxRS", None)
    ocmpSym_SEC_COMPARE_VAL.setLabel("Secondary Compare Value")
    ocmpSym_SEC_COMPARE_VAL.setDefaultValue(4000)
    ocmpSym_SEC_COMPARE_VAL.setMin(0)
    ocmpSym_SEC_COMPARE_VAL.setMax(65535)
    ocmpSym_SEC_COMPARE_VAL.setVisible(False)
    ocmpSym_SEC_COMPARE_VAL.setDependencies(ocmpSecondaryCompare, ["OCMP_OCxCON_OC32", "OCMP_OCxCON_OCM"])

    ocmpSym_PERIOD_COMMENT = ocmpComponent.createCommentSymbol("OCMP_PERIOD_COMMENT", None)
    ocmpSym_PERIOD_COMMENT.setLabel("**** Configure PWM Period in Selected Timer Source ****")
    ocmpSym_PERIOD_COMMENT.setVisible(False)
    ocmpSym_PERIOD_COMMENT.setDependencies(ocmpCommentVisible, ["OCMP_OCxCON_OCM"])

    ocmpSym_OCxCON_SIDL = ocmpComponent.createBooleanSymbol("OCMP_OCxCON_SIDL", None)
    ocmpSym_OCxCON_SIDL.setLabel("Stop in IDLE")

    #Collect user input to combine into OCxCON register
    ocmpSym_ICM = ocmpComponent.createHexSymbol("OCxCON_VALUE", None)
    ocmpSym_ICM.setDefaultValue(0x1)
    ocmpSym_ICM.setVisible(False)
    depList = ["OCMP_OCxCON_OCM", "OCMP_CFGCON_OCACLK", "OCMP_OCxCON_OCTSEL", "OCMP_OCxCON_OCTSEL_ALT", "OCMP_OCxCON_OC32",
        "OCMP_OCxCON_SIDL"]
    ocmpSym_ICM.setDependencies(combineValues, depList)

    #Calculate the proper interrupt registers for IEC, IFS, IPC, priority shift, and subpriority shift
    ocmpIrq = "OUTPUT_COMPARE_" + str(instanceNum)
    ocmpInterruptVector = ocmpIrq + "_INTERRUPT_ENABLE"
    ocmpInterruptHandler = ocmpIrq + "_INTERRUPT_HANDLER"
    ocmpInterruptHandlerLock = ocmpIrq + "_INTERRUPT_HANDLER_LOCK"
    ocmpInterruptVectorUpdate = ocmpIrq + "_INTERRUPT_ENABLE_UPDATE"
    ocmpIrq_index = int(getIRQIndex(ocmpIrq))

    if ocmpIrq_index == -1:
        ocmpIrq_index = int(getVectorIndex(ocmpIrq))

    enblRegName = _get_enblReg_parms(ocmpIrq_index)
    statRegName = _get_statReg_parms(ocmpIrq_index)

    #IEC_REG
    ocmpIEC = ocmpComponent.createStringSymbol("IEC_REG", None)
    ocmpIEC.setDefaultValue(enblRegName)
    ocmpIEC.setVisible(False)

    #IFS_REG
    ocmpIFS = ocmpComponent.createStringSymbol("IFS_REG", None)
    ocmpIFS.setDefaultValue(statRegName)
    ocmpIFS.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    ocmpSymIntEnComment = ocmpComponent.createCommentSymbol("OCMP_INTRRUPT_ENABLE_COMMENT", None)
    ocmpSymIntEnComment.setLabel("Warning!!! " + ocmpInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    ocmpSymIntEnComment.setVisible(False)
    ocmpSymIntEnComment.setDependencies(updateOCMPInterruptData, ["OCMP_INTERRUPT_ENABLE", "core." + ocmpInterruptVectorUpdate])

    # Clock Warning status
    ocmpSym_ClkEnComment = ocmpComponent.createCommentSymbol("OCMP_CLOCK_ENABLE_COMMENT", None)
    ocmpSym_ClkEnComment.setLabel("Warning!!! " + ocmpInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    ocmpSym_ClkEnComment.setVisible(False)
    ocmpSym_ClkEnComment.setDependencies(updateOCMPClockWarningStatus, ["core." + ocmpInstanceName.getValue() + "_CLOCK_ENABLE"])
    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    ocmpHeaderFile = ocmpComponent.createFileSymbol("OCMP_COMMON_HEADER", None)
    ocmpHeaderFile.setMarkup(True)
    ocmpHeaderFile.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp_common.h")
    ocmpHeaderFile.setOutputName("plib_ocmp_common.h")
    ocmpHeaderFile.setDestPath("peripheral/ocmp/")
    ocmpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpHeaderFile.setType("HEADER")
    ocmpHeaderFile.setOverwrite(True)

    ocmpHeader1File = ocmpComponent.createFileSymbol("OCMP_HEADER1", None)
    ocmpHeader1File.setMarkup(True)
    ocmpHeader1File.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp.h.ftl")
    ocmpHeader1File.setOutputName("plib_" + ocmpInstanceName.getValue().lower() + ".h")
    ocmpHeader1File.setDestPath("peripheral/ocmp/")
    ocmpHeader1File.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpHeader1File.setType("HEADER")
    ocmpHeader1File.setOverwrite(True)

    ocmpSource1File = ocmpComponent.createFileSymbol("OCMP_SOURCE1", None)
    ocmpSource1File.setMarkup(True)
    ocmpSource1File.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp.c.ftl")
    ocmpSource1File.setOutputName("plib_"+ ocmpInstanceName.getValue().lower() + ".c")
    ocmpSource1File.setDestPath("peripheral/ocmp/")
    ocmpSource1File.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpSource1File.setType("SOURCE")
    ocmpSource1File.setOverwrite(True)

    ocmpSystemInitFile = ocmpComponent.createFileSymbol("OCMP_INIT", None)
    ocmpSystemInitFile.setType("STRING")
    ocmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ocmpSystemInitFile.setSourcePath("../peripheral/ocmp_00749/templates/system/initialization.c.ftl")
    ocmpSystemInitFile.setMarkup(True)

    ocmpSystemDefFile = ocmpComponent.createFileSymbol("OCMP_DEF", None)
    ocmpSystemDefFile.setType("STRING")
    ocmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ocmpSystemDefFile.setSourcePath("../peripheral/ocmp_00749/templates/system/definitions.h.ftl")
    ocmpSystemDefFile.setMarkup(True)
