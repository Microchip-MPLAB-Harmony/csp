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
#### Business Logic ####
################################################################################

def updateRingBufferSizeVisibleProperty(symbol, event):
    global flexcomSym_RingBuffer_Enable    
    global flexcomSym_UsartInterrupt
    global flecomRxdmaEnable
    global flecomTxdmaEnable
    
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()

    # Enable RX ring buffer size option if Ring buffer is enabled.
    if symbol.getID() == "USART_RX_RING_BUFFER_SIZE":        
        if (flexcom_mode == "USART"):
            symbol.setVisible(flexcomSym_RingBuffer_Enable.getValue())        
        else:
            symbol.setVisible(False)
    # Enable TX ring buffer size option if Ring buffer is enabled.
    elif symbol.getID() == "USART_TX_RING_BUFFER_SIZE":        
        if (flexcom_mode == "USART"):
            symbol.setVisible(flexcomSym_RingBuffer_Enable.getValue())        
        else:
            symbol.setVisible(False)
    # If Interrupt is enabled, make ring buffer option visible. 
    # Additionally, make interrupt option read-only if ring buffer is enabled.
    # Remove read-only on interrupt if ring buffer is disabled.
    # Hide RX and TX DMA options if ring buffer is enabled. Visible if ring buffer is disabled.
    # Clear RX and TX DMA values if ring buffer is enabled.
    elif symbol.getID() == "USART_RING_BUFFER_ENABLE":     
        if (flexcom_mode == "USART"):
            flexcomSym_UsartInterrupt.setReadOnly(symbol.getValue())                          
            symbol.setVisible(flexcomSym_UsartInterrupt.getValue())
            flecomRxdmaEnable.setVisible(not symbol.getValue())            
            flecomTxdmaEnable.setVisible(not symbol.getValue())
            if (symbol.getValue() == True):
                flecomRxdmaEnable.setReadOnly(True)
                flecomRxdmaEnable.setValue(False)
                flecomRxdmaEnable.setReadOnly(False)            
                flecomTxdmaEnable.setReadOnly(True)
                flecomTxdmaEnable.setValue(False)
                flecomTxdmaEnable.setReadOnly(False)
        else:
            symbol.setVisible(False)
       
# FLEXCOM USART clock source
clock_source = {"Ext_clk_src_Freq" : 1000000}
global baudRateCalc
# Calculates BRG value and Oversampling
def baudRateCalc(clk, baud):

    if (clk >= (16 * baud)):
        brgVal = (clk / (16 * baud))
        overSamp = 0
    elif (clk >= (8 * baud)):
        brgVal = (clk / (8 * baud))
        overSamp = 1
    else:
        brgVal = 0
        overSamp = 0

    # The brgVal must fit into a 16-bit register
    if brgVal > 65535:
        brgVal = 0
        overSamp = 0

    flexcomClockInvalidSym.setVisible((brgVal < 1))

    return [brgVal, overSamp]

def baudRateTrigger(symbol, event):
    if Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x1:
        if Database.getSymbolValue(deviceNamespace, "FLEXCOM_USART_MR_USCLKS") == 0x3:
            clk = Database.getSymbolValue(deviceNamespace, "EXTERNAL_CLOCK_FREQ")
        else:
            clk = Database.getSymbolValue(deviceNamespace, "FLEX_USART_CLOCK_FREQ")

        baud = Database.getSymbolValue(deviceNamespace, "BAUD_RATE")

        brgVal, overSamp = baudRateCalc(clk, baud)

        if symbol.getID() == "BRG_VALUE":
            symbol.setValue(brgVal, 2)
        if symbol.getID() == "FLEXCOM_USART_MR_OVER":
            symbol.setValue(overSamp, 2)

def clockSourceFreq(symbol, event):

    if (event["id"] == "FLEXCOM_USART_MR_USCLKS" or (event["id"] == flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")):
        symbol.setValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

    if (event["id"] == "FLEXCOM_MODE"):
        if event["value"] == 0x1:
            symbol.setVisible(True)
        else :
            symbol.setVisible(False)
    elif event["id"] == "FLEXCOM_USART_MR_USCLKS":
        if event["value"] == 0x3:
            symbol.setVisible(False)
        else :
            symbol.setVisible(True)

def dataWidthLogic(symbol, event):

    if(event["value"] == 4):
        symbol.setValue(True, 2)
    else:
        symbol.setValue(False, 2)

def ExternalClkSymbolVisible(symbol, event):

    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def symbolVisible(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def updateDMASymbolVisiblity(symbol, event):

    if Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x1 and Database.getSymbolValue(deviceNamespace, "USART_INTERRUPT_MODE"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
############################################ FLEXCOM USART ########################################
###################################################################################################
global flexcomSym_RingBuffer_Enable
global flexcomSym_UsartInterrupt
global flecomRxdmaEnable
global flecomTxdmaEnable

flexcomSym_UsartInterrupt = flexcomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", flexcomSym_OperatingMode)
flexcomSym_UsartInterrupt.setLabel("Interrupt Mode (Non-blocking Transfer)")
flexcomSym_UsartInterrupt.setDefaultValue(True)
flexcomSym_UsartInterrupt.setVisible(False)
flexcomSym_UsartInterrupt.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

#Enable Ring buffer?
flexcomSym_RingBuffer_Enable = flexcomComponent.createBooleanSymbol("USART_RING_BUFFER_ENABLE", flexcomSym_OperatingMode)
flexcomSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
flexcomSym_RingBuffer_Enable.setDefaultValue(False)
flexcomSym_RingBuffer_Enable.setVisible(False)
flexcomSym_RingBuffer_Enable.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "USART_INTERRUPT_MODE", "USART_RING_BUFFER_ENABLE"])

flexcomSym_TXRingBuffer_Size = flexcomComponent.createIntegerSymbol("USART_TX_RING_BUFFER_SIZE", flexcomSym_RingBuffer_Enable)
flexcomSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
flexcomSym_TXRingBuffer_Size.setMin(2)
flexcomSym_TXRingBuffer_Size.setMax(65535)
flexcomSym_TXRingBuffer_Size.setDefaultValue(128)
flexcomSym_TXRingBuffer_Size.setVisible(False)
flexcomSym_TXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "USART_RING_BUFFER_ENABLE", "USART_TX_ENABLE"])

flexcomSym_RXRingBuffer_Size = flexcomComponent.createIntegerSymbol("USART_RX_RING_BUFFER_SIZE", flexcomSym_RingBuffer_Enable)
flexcomSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
flexcomSym_RXRingBuffer_Size.setMin(2)
flexcomSym_RXRingBuffer_Size.setMax(65535)
flexcomSym_RXRingBuffer_Size.setDefaultValue(128)
flexcomSym_RXRingBuffer_Size.setVisible(False)
flexcomSym_RXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "USART_RING_BUFFER_ENABLE", "USART_RX_ENABLE"])

flecomRxdmaEnable = flexcomComponent.createBooleanSymbol("USE_USART_RX_DMA", flexcomSym_OperatingMode)
flecomRxdmaEnable.setLabel("Enable DMA for Receive")
flecomRxdmaEnable.setVisible(False)
flecomRxdmaEnable.setDependencies(updateDMASymbolVisiblity, ["FLEXCOM_MODE", "USART_INTERRUPT_MODE"])

flecomTxdmaEnable = flexcomComponent.createBooleanSymbol("USE_USART_TX_DMA", flexcomSym_OperatingMode)
flecomTxdmaEnable.setLabel("Enable DMA for Transmit")
flecomTxdmaEnable.setVisible(False)
flecomTxdmaEnable.setDependencies(updateDMASymbolVisiblity, ["FLEXCOM_MODE", "USART_INTERRUPT_MODE"])

flexcomSym_UsartClkSrc = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_USART_MR_USCLKS", flexcomSym_OperatingMode)
flexcomSym_UsartClkSrc.setLabel("Select Clock Source")
flexcomSym_UsartClkSrc_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"USART\"]/value-group@[name=\"US_MR__USCLKS\"]")
flexcomSym_UsartClkSrc_Values = []
flexcomSym_UsartClkSrc_Values = flexcomSym_UsartClkSrc_Node.getChildren()
for index in range(len(flexcomSym_UsartClkSrc_Values)):
    flexcomSym_UsartClkSrc_Key_Name = flexcomSym_UsartClkSrc_Values[index].getAttribute("name")
    flexcomSym_UsartClkSrc_Key_Value = flexcomSym_UsartClkSrc_Values[index].getAttribute("value")
    flexcomSym_UsartClkSrc_Key_Description = flexcomSym_UsartClkSrc_Values[index].getAttribute("caption")
    flexcomSym_UsartClkSrc.addKey(flexcomSym_UsartClkSrc_Key_Name, flexcomSym_UsartClkSrc_Key_Value, flexcomSym_UsartClkSrc_Key_Description)
flexcomSym_UsartClkSrc.setDisplayMode("Key")
flexcomSym_UsartClkSrc.setOutputMode("Key")
flexcomSym_UsartClkSrc.setDefaultValue(0)
flexcomSym_UsartClkSrc.setVisible(False)
flexcomSym_UsartClkSrc.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_UsartExternalClkValue = flexcomComponent.createIntegerSymbol("EXTERNAL_CLOCK_FREQ", flexcomSym_UsartClkSrc)
flexcomSym_UsartExternalClkValue.setLabel("External Clock Source")
flexcomSym_UsartExternalClkValue.setDefaultValue(clock_source.get("Ext_clk_src_Freq"))
flexcomSym_UsartExternalClkValue.setMin(1)
flexcomSym_UsartExternalClkValue.setMax(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY") / 3))
flexcomSym_UsartExternalClkValue.setVisible(False)
flexcomSym_UsartExternalClkValue.setDependencies(ExternalClkSymbolVisible, ["FLEXCOM_USART_MR_USCLKS"])

flexcomSym_UsartClkValue = flexcomComponent.createIntegerSymbol("FLEX_USART_CLOCK_FREQ", flexcomSym_OperatingMode)
flexcomSym_UsartClkValue.setLabel("Clock Source Value")
flexcomSym_UsartClkValue.setReadOnly(True)
flexcomSym_UsartClkValue.setDefaultValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")))
flexcomSym_UsartClkValue.setVisible(False)
flexcomSym_UsartClkValue.setDependencies(clockSourceFreq, ["FLEXCOM_MODE", "FLEXCOM_USART_MR_USCLKS", "core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

flexcomSym_UsartBaud = flexcomComponent.createIntegerSymbol("BAUD_RATE", flexcomSym_OperatingMode)
flexcomSym_UsartBaud.setLabel("Baud Rate")
flexcomSym_UsartBaud.setDefaultValue(115200)
flexcomSym_UsartBaud.setVisible(False)
flexcomSym_UsartBaud.setMin(1)
flexcomSym_UsartBaud.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

brgVal, overSamp = baudRateCalc(flexcomSym_UsartClkValue.getValue(), flexcomSym_UsartBaud.getValue())
flexcomSym_MR_OVER = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_MR_OVER", flexcomSym_OperatingMode)
flexcomSym_MR_OVER.setVisible(False)
flexcomSym_MR_OVER.setDefaultValue(overSamp)
flexcomSym_MR_OVER.setDependencies(baudRateTrigger, ["BAUD_RATE", "FLEX_USART_CLOCK_FREQ", "EXTERNAL_CLOCK_FREQ"])

flexcomSym_UsartBRGValue = flexcomComponent.createIntegerSymbol("BRG_VALUE", flexcomSym_OperatingMode)
flexcomSym_UsartBRGValue.setVisible(False)
flexcomSym_UsartBRGValue.setDefaultValue(brgVal)
flexcomSym_UsartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "FLEX_USART_CLOCK_FREQ", "EXTERNAL_CLOCK_FREQ"])

flexcomSym_Usart_MR_CHRL = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_CHRL", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL.setLabel("Character Length")
flexcomSym_Usart_MR_CHRL_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"USART\"]/value-group@[name=\"US_MR__CHRL\"]")
flexcomSym_Usart_MR_CHRL_Values = []
flexcomSym_Usart_MR_CHRL_Values = flexcomSym_Usart_MR_CHRL_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_CHRL_Values)):
    flexcomSym_Usart_MR_CHRL_Key_Name = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_CHRL_Key_Value = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_CHRL_Key_Description = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_CHRL.addKey(flexcomSym_Usart_MR_CHRL_Key_Name, flexcomSym_Usart_MR_CHRL_Key_Value, flexcomSym_Usart_MR_CHRL_Key_Description)
# There is no 9 bit available under MR_CHRL, but added here just for menu.
# FLEX_USART_MR_MODE9 will use this value
flexcomSym_Usart_MR_CHRL.addKey("_9_BIT", "4", "Character length is 9 bits")
flexcomSym_Usart_MR_CHRL.setDisplayMode("Description")
flexcomSym_Usart_MR_CHRL.setOutputMode("Key")
flexcomSym_Usart_MR_CHRL.setDefaultValue(3)
flexcomSym_Usart_MR_CHRL.setVisible(False)
flexcomSym_Usart_MR_CHRL.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_Usart_MR_MODE9 = flexcomComponent.createBooleanSymbol("FLEX_USART_MR_MODE9", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_MODE9.setLabel("9 Bit Data Width")
flexcomSym_Usart_MR_MODE9.setVisible(False)
flexcomSym_Usart_MR_MODE9.setDependencies(dataWidthLogic, ["FLEX_USART_MR_CHRL"])

flexcomSym_Usart_MR_PAR = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_PAR", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR.setLabel("Parity Type")
flexcomSym_Usart_MR_PAR_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"USART\"]/value-group@[name=\"US_MR__PAR\"]")
flexcomSym_Usart_MR_PAR_Values = []
flexcomSym_Usart_MR_PAR_Values = flexcomSym_Usart_MR_PAR_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_PAR_Values)):
    flexcomSym_Usart_MR_PAR_Key_Name = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_PAR_Key_Value = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_PAR_Key_Description = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_PAR.addKey(flexcomSym_Usart_MR_PAR_Key_Name, flexcomSym_Usart_MR_PAR_Key_Value, flexcomSym_Usart_MR_PAR_Key_Description)
flexcomSym_Usart_MR_PAR.setDefaultValue(4)
flexcomSym_Usart_MR_PAR.setDisplayMode("Key")
flexcomSym_Usart_MR_PAR.setOutputMode("Key")
flexcomSym_Usart_MR_PAR.setVisible(False)
flexcomSym_Usart_MR_PAR.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_Usart_MR_NBSTOP = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_NBSTOP", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP.setLabel("Stop Bits")
flexcomSym_Usart_MR_NBSTOP_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"USART\"]/value-group@[name=\"US_MR__NBSTOP\"]")
flexcomSym_Usart_MR_NBSTOP_Values = []
flexcomSym_Usart_MR_NBSTOP_Values = flexcomSym_Usart_MR_NBSTOP_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_NBSTOP_Values)):
    flexcomSym_Usart_MR_NBSTOP_Key_Name = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_NBSTOP_Key_Value = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_NBSTOP_Key_Description = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_NBSTOP.addKey(flexcomSym_Usart_MR_NBSTOP_Key_Name, flexcomSym_Usart_MR_NBSTOP_Key_Value, flexcomSym_Usart_MR_NBSTOP_Key_Description)
flexcomSym_Usart_MR_NBSTOP.setDisplayMode("Description")
flexcomSym_Usart_MR_NBSTOP.setOutputMode("Key")
flexcomSym_Usart_MR_NBSTOP.setDefaultValue(0)
flexcomSym_Usart_MR_NBSTOP.setVisible(False)
flexcomSym_Usart_MR_NBSTOP.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#FLEXCOM USART API Prefix
flexcomSym_Usart_API_Prefix = flexcomComponent.createStringSymbol("USART_PLIB_API_PREFIX", flexcomSym_OperatingMode)
flexcomSym_Usart_API_Prefix.setDefaultValue(flexcomInstanceName.getValue() + "_USART")
flexcomSym_Usart_API_Prefix.setVisible(False)

#FLEXCOM USART Character Size 5 Mask
flexcomSym_Usart_MR_CHRL_5_Mask = flexcomComponent.createStringSymbol("USART_DATA_5_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_5_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_CHRL_5_Mask.setVisible(False)

#FLEXCOM USART Character Size 6 Mask
flexcomSym_Usart_MR_CHRL_6_Mask = flexcomComponent.createStringSymbol("USART_DATA_6_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_6_Mask.setDefaultValue("0x40")
flexcomSym_Usart_MR_CHRL_6_Mask.setVisible(False)

#FLEXCOM USART Character Size 7 Mask
flexcomSym_Usart_MR_CHRL_7_Mask = flexcomComponent.createStringSymbol("USART_DATA_7_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_7_Mask.setDefaultValue("0x80")
flexcomSym_Usart_MR_CHRL_7_Mask.setVisible(False)

#FLEXCOM USART Character Size 8 Mask
flexcomSym_Usart_MR_CHRL_8_Mask = flexcomComponent.createStringSymbol("USART_DATA_8_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_8_Mask.setDefaultValue("0xC0")
flexcomSym_Usart_MR_CHRL_8_Mask.setVisible(False)

#FLEXCOM USART Character Size 9 Mask
flexcomSym_Usart_MR_CHRL_9_Mask = flexcomComponent.createStringSymbol("USART_DATA_9_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_9_Mask.setDefaultValue("0x20000")
flexcomSym_Usart_MR_CHRL_9_Mask.setVisible(False)

#FLEXCOM USART EVEN Parity Mask
flexcomSym_Usart_MR_PAR_EVEN_Mask = flexcomComponent.createStringSymbol("USART_PARITY_EVEN_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_PAR_EVEN_Mask.setVisible(False)

#FLEXCOM USART ODD Parity Mask
flexcomSym_Usart_MR_PAR_ODD_Mask = flexcomComponent.createStringSymbol("USART_PARITY_ODD_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_ODD_Mask.setDefaultValue("0x200")
flexcomSym_Usart_MR_PAR_ODD_Mask.setVisible(False)

#FLEXCOM USART SPACE Parity Mask
flexcomSym_Usart_MR_PAR_SPACE_Mask = flexcomComponent.createStringSymbol("USART_PARITY_SPACE_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
flexcomSym_Usart_MR_PAR_SPACE_Mask.setVisible(False)

#FLEXCOM USART MARK Parity Mask
flexcomSym_Usart_MR_PAR_MARK_Mask = flexcomComponent.createStringSymbol("USART_PARITY_MARK_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_MARK_Mask.setDefaultValue("0x600")
flexcomSym_Usart_MR_PAR_MARK_Mask.setVisible(False)

#FLEXCOM USART NO Parity Mask
flexcomSym_Usart_MR_PAR_NO_Mask = flexcomComponent.createStringSymbol("USART_PARITY_NONE_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_NO_Mask.setDefaultValue("0x800")
flexcomSym_Usart_MR_PAR_NO_Mask.setVisible(False)

#FLEXCOM USART MULTIDROP Parity Mask
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask = flexcomComponent.createStringSymbol("USART_PARITY_MULTIDROP_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask.setDefaultValue("0xC00")
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask.setVisible(False)

#FLEXCOM USART Stop 1-bit Mask
flexcomSym_Usart_MR_NBSTOP_1_Mask = flexcomComponent.createStringSymbol("USART_STOP_1_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_1_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_NBSTOP_1_Mask.setVisible(False)

#FLEXCOM USART Stop 1_5-bit Mask
flexcomSym_Usart_MR_NBSTOP_1_5_Mask = flexcomComponent.createStringSymbol("USART_STOP_1_5_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_1_5_Mask.setDefaultValue("0x1000")
flexcomSym_Usart_MR_NBSTOP_1_5_Mask.setVisible(False)

#FLEXCOM USART Stop 2-bit Mask
flexcomSym_Usart_MR_NBSTOP_2_Mask = flexcomComponent.createStringSymbol("USART_STOP_2_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_2_Mask.setDefaultValue("0x2000")
flexcomSym_Usart_MR_NBSTOP_2_Mask.setVisible(False)

#FLEXCOM USART Overrun error Mask
flexcomSym_Usart_CSR_OVRE_Mask = flexcomComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_OVRE_Mask.setDefaultValue("0x20")
flexcomSym_Usart_CSR_OVRE_Mask.setVisible(False)

#FLEXCOM USART parity error Mask
flexcomSym_Usart_CSR_PARE_Mask = flexcomComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_PARE_Mask.setDefaultValue("0x80")
flexcomSym_Usart_CSR_PARE_Mask.setVisible(False)

#FLEXCOM USART framing error Mask
flexcomSym_Usart_CSR_FRAME_Mask = flexcomComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_FRAME_Mask.setDefaultValue("0x40")
flexcomSym_Usart_CSR_FRAME_Mask.setVisible(False)