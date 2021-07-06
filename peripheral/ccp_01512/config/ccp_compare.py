"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

ccpBitField_CCPCON2_OENSYNC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CCP"]/register-group@[name="CCP"]/register@[name="CCP1CON2"]/bitfield@[name="OENSYNC"]')
ccpValGrp_CCPCON2_OENSYNC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCP\"]/value-group@[name=\"CCP1CON2__OENSYNC\"]")

ccpBitField_CCPCON3_POLACE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CCP"]/register-group@[name="CCP"]/register@[name="CCP1CON3"]/bitfield@[name="POLACE"]')
ccpValGrp_CCPCON3_POLACE = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCP\"]/value-group@[name=\"CCP1CON3__POLACE\"]")

ccpBitField_CCPCON2_OENSYNC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CCP"]/register-group@[name="CCP"]/register@[name="CCP1CON2"]/bitfield@[name="OENSYNC"]')
ccpValGrp_CCPCON2_OENSYNC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCP\"]/value-group@[name=\"CCP1CON2__OENSYNC\"]")

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def ccpCompICSVisible(symbol, event):
    symObj = event["symbol"]
    if symObj.getSelectedValue() == "15":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def ccpCompMaxValue(symbol, event):
    if event["value"] == True:
        symbol.setMax(pow(2,32) - 1)
    else:
        symbol.setMax(pow(2,16) - 1)

def ccpCompareVisible(symbol, event):
    if event["value"] == "Compare":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)        
###################################################################################################
########################################## Capture  #############################################
###################################################################################################

ccpSym_CompareMenu = ccpComponent.createMenuSymbol("CCP_COMPARE_MENU", ccpSym_OprationMode)
ccpSym_CompareMenu.setLabel("Compare")
ccpSym_CompareMenu.setVisible(False)
ccpSym_CompareMenu.setDependencies(ccpCompareVisible, ["CCP_OPERATION_MODE"])

global ccpSym_Comp_CCPCON1_MOD
ccpSym_Comp_CCPCON1_MOD = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON1_MOD", ccpSym_CompareMenu)
ccpSym_Comp_CCPCON1_MOD.setLabel("Select Output Compare Mode")
ccpSym_Comp_CCPCON1_MOD.addKey("16-Bit/32-Bit Single Edge mode: Drives output high on compare match", "1", "16-Bit/32-Bit Single Edge mode: Drives output high on compare match")
ccpSym_Comp_CCPCON1_MOD.addKey("16-Bit/32-Bit Single Edge mode: Drives output low on compare match", "2", "16-Bit/32-Bit Single Edge mode: Drives output low on compare match")
ccpSym_Comp_CCPCON1_MOD.addKey("16-Bit/32-Bit Single Edge mode: Toggles output on compare match", "3", "16-Bit/32-Bit Single Edge mode: Toggles output on compare match")
ccpSym_Comp_CCPCON1_MOD.addKey("Dual Edge Compare mode", "4", "Dual Edge Compare mode")
ccpSym_Comp_CCPCON1_MOD.addKey("Dual Edge Compare mode, buffered", "5", "Dual Edge Compare mode, buffered")
ccpSym_Comp_CCPCON1_MOD.addKey("Center-Aligned Pulse Compare mode, buffered", "6", "Center-Aligned Pulse Compare mode, buffered")
ccpSym_Comp_CCPCON1_MOD.addKey("Variable Frequency Pulse mode", "7", "Variable Frequency Pulse mode")
ccpSym_Comp_CCPCON1_MOD.addKey("External Input mode: Pulse generator is disabled, source is selected by ICS<2:0>", "15", "External Input mode: Pulse generator is disabled, source is selected by ICS<2:0>")
ccpSym_Comp_CCPCON1_MOD.setDefaultValue(0)
ccpSym_Comp_CCPCON1_MOD.setOutputMode( "Value" )
ccpSym_Comp_CCPCON1_MOD.setDisplayMode( "Description" )
ccpcon1_depList.append("CCP_COMP_CCPCON1_MOD")

#ICS source
global ccpSym_Comp_CCPCON2_ICS
ccpSym_Comp_CCPCON2_ICS = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON2_ICS", ccpSym_Comp_CCPCON1_MOD)
ccpSym_Comp_CCPCON2_ICS.setLabel("Select Input Capture Source")
capture_source = []
_get_bitfield_names(ccpValGrp_CCPCON1_SYNC, capture_source)
ccpSym_Comp_CCPCON2_ICS.setOutputMode( "Value" )
ccpSym_Comp_CCPCON2_ICS.setDisplayMode( "Description" )
for ii in capture_source:
    ccpSym_Comp_CCPCON2_ICS.addKey( ii['key'],ii['value'], ii['desc'] )
ccpSym_Comp_CCPCON2_ICS.setDefaultValue(0)
ccpSym_Comp_CCPCON2_ICS.setVisible(False)
ccpSym_Comp_CCPCON2_ICS.setDependencies(ccpCompICSVisible, ["CCP_COMP_CCPCON1_MOD"])
ccpcon2_depList.append("CCP_COMP_CCPCON2_ICS")


#period value
ccpSym_Comp_CCPPR = ccpComponent.createLongSymbol("CCP_COMP_CCPPR", ccpSym_CompareMenu)
ccpSym_Comp_CCPPR.setLabel("Period Value")
ccpSym_Comp_CCPPR.setDefaultValue(4000)
ccpSym_Comp_CCPPR.setMin(0)
ccpSym_Comp_CCPPR.setMax(65535)
ccpSym_Comp_CCPPR.setDependencies(ccpCompMaxValue, ["CCP_CCPCON1_T32"])

#Compare value RA
ccspSym_Comp_CCPRA = ccpComponent.createLongSymbol("CCP_COMP_CCPRA", ccpSym_CompareMenu)
ccspSym_Comp_CCPRA.setLabel("Compare A Value")
ccspSym_Comp_CCPRA.setDefaultValue(500)
ccspSym_Comp_CCPRA.setMin(0)
ccspSym_Comp_CCPRA.setMax(65535)
ccspSym_Comp_CCPRA.setDependencies(ccpCompMaxValue, ["CCP_CCPCON1_T32"])

#Compare value RB
ccspSym_Comp_CCPRB = ccpComponent.createLongSymbol("CCP_COMP_CCPRB", ccpSym_CompareMenu)
ccspSym_Comp_CCPRB.setLabel("Compare B Value")
ccspSym_Comp_CCPRB.setDefaultValue(1000)
ccspSym_Comp_CCPRB.setMin(0)
ccspSym_Comp_CCPRB.setMax(65535)
ccspSym_Comp_CCPRB.setDependencies(ccpCompMaxValue, ["CCP_CCPCON1_T32"])

#MCCP ONLY
if mccpPresent.getValue() == True:
    global ccpSym_Comp_CCPCON3_OUTM
    #PWM output mode
    ccpSym_Comp_CCPCON3_OUTM = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON3_OUTM", ccpSym_CompareMenu)
    ccpSym_Comp_CCPCON3_OUTM.setLabel("PWM Output Mode Control")
    ccpSym_Comp_CCPCON3_OUTM.setOutputMode( "Value" )
    ccpSym_Comp_CCPCON3_OUTM.setDisplayMode( "Description" )
    ccpSym_Comp_CCPCON3_OUTM.addKey("Steerable single output mode", "0", "Steerable single output mode")
    ccpSym_Comp_CCPCON3_OUTM.addKey("Push Pull output mode", "1", "Push Pull output mode")
    ccpSym_Comp_CCPCON3_OUTM.addKey("Half Bridge output mode", "2", "Half Bridge output mode")
    ccpSym_Comp_CCPCON3_OUTM.addKey("Brush DC output mode (reverse)", "4", "Brush DC output mode (reverse)")
    ccpSym_Comp_CCPCON3_OUTM.addKey("Brush DC output mode (forward)", "5", "Brush DC output mode (forward)")
    ccpSym_Comp_CCPCON3_OUTM.addKey("Output Scan mode", "7", "Output  Scan mode")
    ccpSym_Comp_CCPCON3_OUTM.setDefaultValue(0)
    ccpcon3_depList.append("CCP_COMP_CCPCON3_OUTM")

    #dead-time
    ccpSym_Comp_CCPCON3_DT = ccpComponent.createIntegerSymbol("CCP_COMP_CCPCON3_DT", ccpSym_CompareMenu)
    ccpSym_Comp_CCPCON3_DT.setLabel("PWM Dead-Time")
    ccpSym_Comp_CCPCON3_DT.setMin(0)
    ccpSym_Comp_CCPCON3_DT.setMax(63)
    ccpcon3_depList.append("CCP_COMP_CCPCON3_DT")
    
ccpSym_Comp_Interrupt = ccpComponent.createBooleanSymbol("CCP_COMP_INTERRUPT", ccpSym_CompareMenu)
ccpSym_Comp_Interrupt.setLabel("Enable Compare Interrupt")

ccpSym_OutputsMenu = ccpComponent.createMenuSymbol("CCP_COMP_OUTPUTS_MENU", ccpSym_CompareMenu)
ccpSym_OutputsMenu.setLabel("Outputs")

#output pin enable
ccpSym_Comp_CCPCON2_OCAEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCAEN", ccpSym_OutputsMenu)
ccpSym_Comp_CCPCON2_OCAEN.setLabel("Enable Output Pin A")
ccpcon2_depList.append("CCP_COMP_CCPCON2_OCAEN")

if mccpPresent.getValue() == True:
    ccpSym_Comp_CCPCON2_OCBEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCBEN", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON2_OCBEN.setLabel("Enable Output Pin B")
    ccpcon2_depList.append("CCP_COMP_CCPCON2_OCBEN")

    ccpSym_Comp_CCPCON2_OCCEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCCEN", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON2_OCCEN.setLabel("Enable Output Pin C")
    ccpcon2_depList.append("CCP_COMP_CCPCON2_OCCEN")

    ccpSym_Comp_CCPCON2_OCDEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCDEN", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON2_OCDEN.setLabel("Enable Output Pin D")
    ccpcon2_depList.append("CCP_COMP_CCPCON2_OCDEN")

    ccpSym_Comp_CCPCON2_OCEEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCEEN", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON2_OCEEN.setLabel("Enable Output Pin E")
    ccpcon2_depList.append("CCP_COMP_CCPCON2_OCEEN")

    ccpSym_Comp_CCPCON2_OCFEN = ccpComponent.createBooleanSymbol("CCP_COMP_CCPCON2_OCFEN", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON2_OCFEN.setLabel("Enable Output Pin F")
    ccpcon2_depList.append("CCP_COMP_CCPCON2_OCFEN")

global ccpSym_Comp_CCPCON2_OENSYNC
ccpSym_Comp_CCPCON2_OENSYNC = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON2_OENSYNC", ccpSym_OutputsMenu)
ccpSym_Comp_CCPCON2_OENSYNC.setLabel("Output Enable Synchronization")
sync_source = []
_get_bitfield_names(ccpValGrp_CCPCON2_OENSYNC, sync_source)
ccpSym_Comp_CCPCON2_OENSYNC.setOutputMode( "Value" )
ccpSym_Comp_CCPCON2_OENSYNC.setDisplayMode( "Description" )
for ii in sync_source:
    ccpSym_Comp_CCPCON2_OENSYNC.addKey( ii['key'],ii['value'], ii['desc'] )
ccpSym_Comp_CCPCON2_OENSYNC.setDefaultValue(0)
ccpcon2_depList.append("CCP_COMP_CCPCON2_OENSYNC")

#output polarity for high side output pins
global ccpSym_Comp_CCPCON3_POLACE
ccpSym_Comp_CCPCON3_POLACE = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON3_POLACE", ccpSym_OutputsMenu)
ccpSym_Comp_CCPCON3_POLACE.setLabel("Output Polarity for High Side Outputs")
polarity_source = []
_get_bitfield_names(ccpValGrp_CCPCON3_POLACE, polarity_source)
ccpSym_Comp_CCPCON3_POLACE.setOutputMode( "Value" )
ccpSym_Comp_CCPCON3_POLACE.setDisplayMode( "Description" )
for ii in polarity_source:
    ccpSym_Comp_CCPCON3_POLACE.addKey( ii['key'],ii['value'], ii['desc'] )
ccpSym_Comp_CCPCON3_POLACE.setDefaultValue(0)
ccpcon3_depList.append("CCP_COMP_CCPCON3_POLACE")

if mccpPresent.getValue() == True:
    global ccpSym_Comp_CCPCON3_POLBDF
    #output polarity for low side output pins
    ccpSym_Comp_CCPCON3_POLBDF = ccpComponent.createKeyValueSetSymbol("CCP_COMP_CCPCON3_POLBDF", ccpSym_OutputsMenu)
    ccpSym_Comp_CCPCON3_POLBDF.setLabel("Output Polarity for Low Side Outputs")
    ccpSym_Comp_CCPCON3_POLBDF.setOutputMode( "Value" )
    ccpSym_Comp_CCPCON3_POLBDF.setDisplayMode( "Description" )
    for ii in polarity_source:
        ccpSym_Comp_CCPCON3_POLBDF.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_Comp_CCPCON3_POLBDF.setDefaultValue(0)
    ccpcon3_depList.append("CCP_COMP_CCPCON3_POLBDF")





