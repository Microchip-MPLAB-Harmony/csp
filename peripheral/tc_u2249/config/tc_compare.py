# coding: utf-8
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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateCompareMenuVisibleProperty(symbol, event):
    if event["value"] == "Compare":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateCompareMaxValue(symbol, event):
    if event["value"] == 0x1:
        symbol.setMax(255)
    elif event["value"] == 0x0:
        symbol.setMax(65535)
    elif event["value"] == 0x2:
        symbol.setMax(4294967295)

def updateCompareDuty(symbol, event):
    if event["id"] == "TC_COMPARE_PERIOD":
        symbol.setMax(event["value"])

    #hide compare value for Match frequency waveform mode
    if event["id"] == "TC_COMPARE_WAVE_WAVEGEN":
        print (str(event["value"]))
        if event["value"] == 1:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

###################################################################################################
####################################### Compare Mode ##############################################
###################################################################################################

#compare menu
tcSym_CompareMenu = tcComponent.createMenuSymbol("TC_COMPARE_MENU", tcSym_OperationMode)
tcSym_CompareMenu.setLabel("Compare")
tcSym_CompareMenu.setVisible(False)
tcSym_CompareMenu.setDependencies(updateCompareMenuVisibleProperty, ["TC_OPERATION_MODE"])

#waveform mode
tcSym_Compare_WAVE_WAVEGEN = tcComponent.createKeyValueSetSymbol("TC_COMPARE_WAVE_WAVEGEN", tcSym_CompareMenu)
tcSym_Compare_WAVE_WAVEGEN.setLabel("Waveform Mode")
tcSym_Compare_WAVE_WAVEGEN.addKey("MFRQ", "1", "Match Frequency")
tcSym_Compare_WAVE_WAVEGEN.addKey("MPWM", "3", "Match PWM")
tcSym_Compare_WAVE_WAVEGEN.setDefaultValue(1)
tcSym_Compare_WAVE_WAVEGEN.setOutputMode("Key")
tcSym_Compare_WAVE_WAVEGEN.setDisplayMode("Description")

#compare direction
tcSym_Compare_CTRLBSET_DIR = tcComponent.createKeyValueSetSymbol("TC_COMPARE_CTRLBSET_DIR", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_DIR.setLabel("Counter Direction")
tcSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_UP", "0", "UP Count")
tcSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_DOWN", "1", "DOWN Count")
tcSym_Compare_CTRLBSET_DIR.setDefaultValue(0)
tcSym_Compare_CTRLBSET_DIR.setOutputMode("Value")
tcSym_Compare_CTRLBSET_DIR.setDisplayMode("Description")

#compare period
tcSym_ComparePeriod = tcComponent.createLongSymbol("TC_COMPARE_PERIOD", tcSym_CompareMenu)
tcSym_ComparePeriod.setLabel("Period Value")
tcSym_ComparePeriod.setDefaultValue(48)
tcSym_ComparePeriod.setMin(0)
tcSym_ComparePeriod.setMax(65535)
tcSym_ComparePeriod.setDependencies(updateCompareMaxValue, ["TC_CTRLA_MODE"])

#period time in us
tcSym_ComparePeriod_Comment = tcComponent.createCommentSymbol("TC_COMPARE_PERIOD_COMMENT", tcSym_CompareMenu)
tcSym_ComparePeriod_Comment.setLabel("**** Timer Period is 1 us ****")

#compare value
tcSym_CompareDuty = tcComponent.createLongSymbol("TC_COMPARE_CC1", tcSym_CompareMenu)
tcSym_CompareDuty.setLabel("Compare Value")
tcSym_CompareDuty.setDefaultValue(24)
tcSym_CompareDuty.setMin(0)
tcSym_CompareDuty.setMax(tcSym_ComparePeriod.getValue())
tcSym_CompareDuty.setDependencies(updateCompareDuty, ["TC_COMPARE_WAVE_WAVEGEN", "TC_COMPARE_PERIOD"])

#compare one shot mode
tcSym_Compare_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLBSET_ONESHOT", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

#double buffering
tcSym_Compare_CTRLBSET_LUPD = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLBSET_LUPD", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_LUPD.setLabel("Enable Double Buffering")
tcSym_Compare_CTRLBSET_LUPD.setDefaultValue(True)

#compare channel counter/compare interrupt
global tcSym_Compare_INTENSET_OVF
tcSym_Compare_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_COMPARE_INTENSET_OVF", tcSym_CompareMenu)
tcSym_Compare_INTENSET_OVF.setLabel("Enable Period Interrupt")
tcSym_Compare_INTENSET_OVF.setDefaultValue(False)