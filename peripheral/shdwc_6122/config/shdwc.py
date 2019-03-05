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

def mrUpdate(eventsSym, event):
    events = eventsSym.getValue()
    if event['value'] == True:
        if event['id'] not in events:
            events = events +" "+ event['id']
    else:
        if event['id'] in events:
            events.replace(event['id'],"",)
    eventsSym.setValue(events,0)

def instantiateComponent(shdwcComponent):

    mrReg = Register.getRegisterModule("SHDWC").getRegisterGroup("SHDWC").getRegister("SHDW_MR")
    wuiReg = Register.getRegisterModule("SHDWC").getRegisterGroup("SHDWC").getRegister("SHDW_WUIR")

    instanceName = shdwcComponent.createStringSymbol("SHDWC_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(shdwcComponent.getID().upper());

    events = []
    for bitfieldName in mrReg.getBitfieldNames():
        if "EN" not in bitfieldName:
            continue
        bitfield = mrReg.getBitfield(bitfieldName)
        eventSym = shdwcComponent.createBooleanSymbol(bitfieldName, None)
        eventSym.setLabel(bitfieldName)
        eventSym.setDescription(bitfield.getDescription())
        eventSym.setDefaultValue(False)
        events.append(bitfieldName)

    eventsSym = shdwcComponent.createStringSymbol("EVENT_LIST", None)
    eventsSym.setVisible(False)
    eventsSym.setDependencies(mrUpdate, events)

    debounceValueGroup = Register.getRegisterModule("SHDWC").getValueGroup(mrReg.getBitfield("WKUPDBC").getValueGroupName())
    debounce = shdwcComponent.createKeyValueSetSymbol("WKUPDBC", None)
    for name in debounceValueGroup.getValueNames():
        value = debounceValueGroup.getValue(name)
        debounce.addKey(value.getName(), value.getValue(), value.getDescription())
    debounce.setOutputMode("Value")
    debounce.setDisplayMode("Key")


    bitfieldNames = wuiReg.getBitfieldNames()
    bitfieldNames = sorted(bitfieldNames)

    pins = []
    for i in range(0,len(bitfieldNames)):
        if "EN" not in bitfieldNames[i]:
            continue
        bitfield = wuiReg.getBitfield(bitfieldNames[i])
        eventSym = shdwcComponent.createBooleanSymbol(bitfieldNames[i], None)
        eventSym.setLabel(bitfield.getName())
        eventSym.setDescription(bitfield.getDescription())
        eventSym.setDefaultValue(False)
        TypeSym = shdwcComponent.createComboSymbol(bitfieldNames[i].split("EN")[0]+"T"+str(i), eventSym, ["LOW", "HIGH"])
        pins.append(bitfieldNames[i])

    pinsSym = shdwcComponent.createStringSymbol("PINS_LIST", None)
    pinsSym.setVisible(False)
    pinsSym.setDependencies(mrUpdate, pins)

    configName = Variables.get("__CONFIGURATION_NAME")

    srcFile = shdwcComponent.createFileSymbol(None, None)
    srcFile.setSourcePath("../peripheral/shdwc_6122/templates/plib_shdwc.c.ftl")
    srcFile.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    srcFile.setDestPath("/peripheral/shdwc/")
    srcFile.setProjectPath("config/"+configName+"/peripheral/shdwc/")
    srcFile.setType("SOURCE")
    srcFile.setOverwrite(True)
    srcFile.setMarkup(True)

    hdrFile = shdwcComponent.createFileSymbol(None, None)
    hdrFile.setSourcePath("../peripheral/shdwc_6122/templates/plib_shdwc.h.ftl")
    hdrFile.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    hdrFile.setDestPath("/peripheral/shdwc/")
    hdrFile.setProjectPath("config/"+configName+"/peripheral/shdwc/")
    hdrFile.setType("HEADER")
    hdrFile.setOverwrite(True)
    hdrFile.setMarkup(True)

    shdwcSystemInitFile = shdwcComponent.createFileSymbol(None, None)
    shdwcSystemInitFile.setType("STRING")
    shdwcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    shdwcSystemInitFile.setSourcePath("../peripheral/shdwc_6122/templates/system/initialization.c.ftl")
    shdwcSystemInitFile.setMarkup(True)

    shdwcSystemDefFile = shdwcComponent.createFileSymbol(None, None)
    shdwcSystemDefFile.setType("STRING")
    shdwcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    shdwcSystemDefFile.setSourcePath("../peripheral/shdwc_6122/templates/system/definitions.h.ftl")
    shdwcSystemDefFile.setMarkup(True)
