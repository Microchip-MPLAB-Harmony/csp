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

""" This module will instantiate and setup TC component """

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateTimerMenuVisibleProperty(symbol, event):
    if event["value"] == "Timer":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTimerPeriodMaxValue(symbol, event):
    if event["value"] == 0x1:
        symbol.setMax(255)
    elif event["value"] == 0x0:
        symbol.setMax(65535)
    elif event["value"] == 0x2:
        symbol.setMax(4294967295)

###################################################################################################
######################################### Timer Mode ##############################################
###################################################################################################

#timer menu
tcSym_TimerMenu = tcComponent.createMenuSymbol("TC_TIMER_MENU", tcSym_OperationMode)
tcSym_TimerMenu.setLabel("Timer")
tcSym_TimerMenu.setDependencies(updateTimerMenuVisibleProperty, ["TC_OPERATION_MODE"])

#timer one shot mode
tcSym_Timer_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_TIMER_CTRLBSET_ONESHOT", tcSym_TimerMenu)
tcSym_Timer_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

#timer 8-bit period
tcSym_TimerPeriod = tcComponent.createLongSymbol("TC_TIMER_PERIOD", tcSym_TimerMenu)
tcSym_TimerPeriod.setLabel("Timer Period")
tcSym_TimerPeriod.setDefaultValue(48)
tcSym_TimerPeriod.setMin(0)
tcSym_TimerPeriod.setMax(65535)
tcSym_TimerPeriod.setDependencies(updateTimerPeriodMaxValue, ["TC_CTRLA_MODE"])

#period time in us
tcSym_TimerPeriod_Comment = tcComponent.createCommentSymbol("TC_TIMER_PERIOD_COMMENT", tcSym_TimerMenu)
tcSym_TimerPeriod_Comment.setLabel("**** Timer Period is 1 us ****")

#timer interrupt mode
global tcSym_Timer_INTENSET
tcSym_Timer_INTENSET = tcComponent.createBooleanSymbol("TC_TIMER_INTERRUPT_MODE", tcSym_TimerMenu)
tcSym_Timer_INTENSET.setLabel("Enable Timer Period Interrupt")
tcSym_Timer_INTENSET.setDefaultValue(True)
