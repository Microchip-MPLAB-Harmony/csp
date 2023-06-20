# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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
def usartLinVisibility(symbol, event):
    symObj = event["symbol"]
    if symObj.getSelectedKey() == "LIN_MASTER" or symObj.getSelectedKey() == "LIN_SLAVE":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def usartLinInterruptVisibility(symbol, event):
    usartmodeObj = event["source"].getSymbolByID("USART_MODE").getSelectedKey()
    operatingmodeObj = event["source"].getSymbolByID("USART_LIN_OPERATING_MODE").getSelectedKey()
    
    if usartmodeObj == "LIN_SLAVE" or usartmodeObj == "LIN_MASTER":
        if operatingmodeObj == "RING_BUFFER":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)
        
def usartLinSymVisibility(symbol,event):
    symObj = event["source"].getSymbolByID("USART_MODE").getSelectedKey()

    if symbol.getID() == "USART_LIN_LINMR_FSDIS":
        if symObj == "LIN_MASTER":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    elif symbol.getID() == "USART_LIN_LINMR_SYNCDIS":
        if symObj == "LIN_SLAVE":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
            
usartLINSym_Menu = usartComponent.createMenuSymbol("USART_LIN_MENU", None)
usartLINSym_Menu.setLabel ("LIN Configurations")
usartLINSym_Menu.setVisible(False)
usartLINSym_Menu.setDependencies(usartLinVisibility, ["USART_MODE"])
 
usartLINSym_LINMR_PARDIS = usartComponent.createBooleanSymbol("USART_LIN_LINMR_PARDIS", usartLINSym_Menu)
usartLINSym_LINMR_PARDIS.setLabel("Identifier Parity Disable")
usartLINSym_LINMR_PARDIS.setDefaultValue(False)
usartLINSym_LINMR_PARDIS.setVisible(True)

usartLINSym_LINMR_CHKDIS = usartComponent.createBooleanSymbol("USART_LIN_LINMR_CHKDIS", usartLINSym_Menu)
usartLINSym_LINMR_CHKDIS.setLabel("Checksum Disable")
usartLINSym_LINMR_CHKDIS.setDefaultValue(False)
usartLINSym_LINMR_CHKDIS.setVisible(True)

usartLINSym_LINMR_CHKTYP = usartComponent.createKeyValueSetSymbol("USART_LIN_LINMR_CHKTYP", usartLINSym_Menu)
usartLINSym_LINMR_CHKTYP.setLabel("Select Checksum Type")
usartLINSym_LINMR_CHKTYP.addKey("ENHANCED", "0x0", "LIN 2.0 Enhanced Checksum")
usartLINSym_LINMR_CHKTYP.addKey("CLASSIC", "0x1", "LIN 1.3 Classic Checksum")
usartLINSym_LINMR_CHKTYP.setOutputMode("Value")
usartLINSym_LINMR_CHKTYP.setDisplayMode("Description")
usartLINSym_LINMR_CHKTYP.setDefaultValue(0)
usartLINSym_LINMR_CHKTYP.setVisible(True)

usartLINSym_LINMR_DLM = usartComponent.createKeyValueSetSymbol("USART_LIN_LINMR_DLM", usartLINSym_Menu)
usartLINSym_LINMR_DLM.setLabel("Select Data Length Mode")
usartLINSym_LINMR_DLM.addKey("DLC", "0x0", "Data length is defined by DLC")
usartLINSym_LINMR_DLM.addKey("IDCHR", "0x1", "Data length is defined by bits 5 and 6 of the identifier")
usartLINSym_LINMR_DLM.setOutputMode("Value")
usartLINSym_LINMR_DLM.setDisplayMode("Description")
usartLINSym_LINMR_DLM.setDefaultValue(0)
usartLINSym_LINMR_DLM.setVisible(True)

usartLINSym_LINMR_DLC = usartComponent.createIntegerSymbol("USART_LIN_LINMR_DLC", usartLINSym_Menu)
usartLINSym_LINMR_DLC.setLabel("Response Data Length (bytes)")
usartLINSym_LINMR_DLC.setDefaultValue(8)
usartLINSym_LINMR_DLC.setMin(0)
usartLINSym_LINMR_DLC.setMax(255)
usartLINSym_LINMR_DLC.setVisible(False)

usartLINSym_LINMR_FSDIS = usartComponent.createBooleanSymbol("USART_LIN_LINMR_FSDIS", usartLINSym_Menu)
usartLINSym_LINMR_FSDIS.setLabel("Frame Slot Mode Disable")
usartLINSym_LINMR_FSDIS.setDefaultValue(False)
usartLINSym_LINMR_FSDIS.setVisible(True)
usartLINSym_LINMR_FSDIS.setDependencies(usartLinSymVisibility, ["USART_MODE"])

usartLINSym_LINMR_SYNCDIS = usartComponent.createBooleanSymbol("USART_LIN_LINMR_SYNCDIS", usartLINSym_Menu)
usartLINSym_LINMR_SYNCDIS.setLabel("Synchronization Disable")
usartLINSym_LINMR_SYNCDIS.setDefaultValue(False)
usartLINSym_LINMR_SYNCDIS.setVisible(True)
usartLINSym_LINMR_SYNCDIS.setDependencies(usartLinSymVisibility, ["USART_MODE"])

usartLINSym_LINMR_WKUPTYP = usartComponent.createKeyValueSetSymbol("USART_LIN_LINMR_WKUPTYP", usartLINSym_Menu)
usartLINSym_LINMR_WKUPTYP.setLabel("Select Wakeup Signal Type")
usartLINSym_LINMR_WKUPTYP.addKey("LIN2_0", "0x0", "LIN 2.0 Wakeup Signal")
usartLINSym_LINMR_WKUPTYP.addKey("LIN1_3", "0x1", "LIN 1.3 Wakeup Signal")
usartLINSym_LINMR_WKUPTYP.setOutputMode("Value")
usartLINSym_LINMR_WKUPTYP.setDisplayMode("Description")
usartLINSym_LINMR_WKUPTYP.setDefaultValue(0)
usartLINSym_LINMR_WKUPTYP.setVisible(True) 

############################################################################
#### Interrupt Menu ####
############################################################################

usartLINSym_LIN_INTERRUPT_Menu = usartComponent.createMenuSymbol("USART_LIN_INTERRUPT_MENU", usartLINSym_Menu)
usartLINSym_LIN_INTERRUPT_Menu.setLabel ("LIN Interupt Configurations")
usartLINSym_LIN_INTERRUPT_Menu.setVisible(True)
usartLINSym_LIN_INTERRUPT_Menu.setDependencies(usartLinInterruptVisibility, ["USART_LIN_OPERATING_MODE", "USART_MODE"])

usartLINSym_LINIER_LINID_INTERRUPT_ENABLE = usartComponent.createBooleanSymbol("USART_LIN_LINID_INTERRUPT_ENABLE", usartLINSym_LIN_INTERRUPT_Menu)
usartLINSym_LINIER_LINID_INTERRUPT_ENABLE.setLabel("LIN ID Receive/Transmit Interrupt")
usartLINSym_LINIER_LINID_INTERRUPT_ENABLE.setDefaultValue(False)
usartLINSym_LINIER_LINID_INTERRUPT_ENABLE.setVisible(True)

usartLINSym_LINIER_LINTC_INTERRUPT_ENABLE = usartComponent.createBooleanSymbol("USART_LIN_LINTC_INTERRUPT_ENABLE", usartLINSym_LIN_INTERRUPT_Menu)
usartLINSym_LINIER_LINTC_INTERRUPT_ENABLE.setLabel("LIN Data Transfer Complete Interrupt")
usartLINSym_LINIER_LINTC_INTERRUPT_ENABLE.setDefaultValue(False)
usartLINSym_LINIER_LINTC_INTERRUPT_ENABLE.setVisible(True)

usartLINSym_LINIER_LINBK_INTERRUPT_ENABLE = usartComponent.createBooleanSymbol("USART_LIN_LINBK_INTERRUPT_ENABLE", usartLINSym_LIN_INTERRUPT_Menu)
usartLINSym_LINIER_LINBK_INTERRUPT_ENABLE.setLabel("LIN Header-Break Receive/Transmit Interrupt")
usartLINSym_LINIER_LINBK_INTERRUPT_ENABLE.setDefaultValue(False)
usartLINSym_LINIER_LINBK_INTERRUPT_ENABLE.setVisible(True)




