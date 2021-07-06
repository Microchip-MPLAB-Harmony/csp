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


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def ccpCaptureVisible(symbol, event):
    if event["value"] == "Capture":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Capture  #############################################
###################################################################################################
global ccpSym_CaptureMenu
ccpSym_CaptureMenu = ccpComponent.createMenuSymbol("CCP_CAPTURE_MENU", ccpSym_OprationMode)
ccpSym_CaptureMenu.setLabel("Capture")
ccpSym_CaptureMenu.setVisible(False)
ccpSym_CaptureMenu.setDependencies(ccpCaptureVisible, ["CCP_OPERATION_MODE"])

#input capture mode
global ccpSym_Cap_CCPCON1_MOD
ccpSym_Cap_CCPCON1_MOD = ccpComponent.createKeyValueSetSymbol("CCP_CAP_CCPCON1_MOD", ccpSym_CaptureMenu)
ccpSym_Cap_CCPCON1_MOD.setLabel("Select Input Capture Mode")
ccpSym_Cap_CCPCON1_MOD.setOutputMode( "Value" )
ccpSym_Cap_CCPCON1_MOD.setDisplayMode( "Description" )
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every rising and falling edge (Edge detect mode)" , "0", "Capture every rising and falling edge (Edge detect mode)"  )
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every rising edge", "1", "Capture every rising edge")
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every falling edge", "2", "Capture every falling edge")
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every rising and falling edge", "3", "Capture every rising and falling edge")
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every 4th rising edge", "4", "Capture every 4th rising edge")
ccpSym_Cap_CCPCON1_MOD.addKey("Capture every 16th rising edge", "5", "Capture every 16th rising edge")
ccpSym_Cap_CCPCON1_MOD.setDefaultValue(0)
ccpSym_Cap_CCPCON1_MOD.setVisible(True)
ccpcon1_depList.append("CCP_CAP_CCPCON1_MOD")

global ccpSym_Cap_CCPCON2_ICS
ccpValGrp_CCPCON2_ICS = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCP\"]/value-group@[name=\"CCP" + str(instanceNum) + "CON2__ICS\"]")

ccpSym_Cap_CCPCON2_ICS = ccpComponent.createKeyValueSetSymbol("CCP_CAP_CCPCON2_ICS", ccpSym_CaptureMenu)
ccpSym_Cap_CCPCON2_ICS.setLabel("Select Input Capture Source")
capture_source = []
_get_bitfield_names(ccpValGrp_CCPCON2_ICS, capture_source)
ccpSym_Cap_CCPCON2_ICS.setOutputMode( "Value" )
ccpSym_Cap_CCPCON2_ICS.setDisplayMode( "Description" )
for ii in capture_source:
    ccpSym_Cap_CCPCON2_ICS.addKey( ii['key'],ii['value'], ii['desc'] )
ccpSym_Cap_CCPCON2_ICS.setDefaultValue(0)
ccpSym_Cap_CCPCON2_ICS.setVisible(True)
ccpcon2_depList.append("CCP_CAP_CCPCON2_ICS")

ccpSym_Cap_Interrupt = ccpComponent.createBooleanSymbol("CCP_CAP_INTERRUPT", ccpSym_CaptureMenu)
ccpSym_Cap_Interrupt.setLabel("Enable Capture Interrupt")