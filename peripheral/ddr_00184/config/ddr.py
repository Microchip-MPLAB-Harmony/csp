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

################################################################################
#### Register Information ####
################################################################################
ddrValGrp_DDRSCLCFG1_DBLREFDLY = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DDR_PHY"]/value-group@[name="DDRSCLCFG1__DBLREFDLY"]')
ddrValGrp_DDRPHYPADCON_PREAMBDLY = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DDR_PHY"]/value-group@[name="DDRPHYPADCON__PREAMBDLY"]')
ddrValGrp_DDRPHYPADCON_ADDCDRVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DDR_PHY"]/value-group@[name="DDRPHYPADCON__ADDCDRVSEL"]')
ddrValGrp_DDRPHYPADCON_DATDRVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DDR_PHY"]/value-group@[name="DDRPHYPADCON__DATDRVSEL"]')
ddrValGrp_DDRPHYPADCON_ODTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DDR_PHY"]/value-group@[name="DDRPHYPADCON__ODTSEL"]')
##
##cmpBitFld_CM2CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CCH"]')
##cmpBitFld_CM2CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CREF"]')
##cmpBitFld_CM2CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="EVPOL"]')
##cmpBitFld_CM2CON_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CPOL"]')
##cmpBitFld_CM2CON_COE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="COE"]')

################################################################################
#### Global Variables ####
################################################################################
global ddrInstanceName

################################################################################
#### Business Logic ####
################################################################################

def _get_bitfield_names(node, outputList):
    valueNodes = node.getChildren()
    for ii in reversed(valueNodes):
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)
            outputList.append(dict)        
    
################################################################################
#### Component ####
################################################################################
def instantiateComponent(ddrComponent):
    global ddrInstanceName

    ddrInstanceName = ddrComponent.createStringSymbol("DDR_INSTANCE_NAME", None)
    ddrInstanceName.setVisible(False)
    ddrInstanceName.setDefaultValue(ddrComponent.getID().upper())
    print("Running " + ddrInstanceName.getValue())

    #DDR Type
    ddrSym_DDR_TYPE = ddrComponent.createKeyValueSetSymbol("DDR_TYPE", None)
    ddrSym_DDR_TYPE.setLabel("DDR Type")
    ddrSym_DDR_TYPE.setDefaultValue(0)
    ddrSym_DDR_TYPE.setOutputMode("Value")
    ddrSym_DDR_TYPE.setDisplayMode("Description")
    ddrSym_DDR_TYPE.addKey( 'Internal', 'Internal', 'Internal')
    ddrSym_DDR_TYPE.addKey( 'Micron MT47H64M16', 'Micron MT47H64M16', 'Micron MT47H64M16')
    ddrSym_DDR_TYPE.addKey( 'Custom', 'Custom', 'Custom')    
    ddrSym_DDR_TYPE.setVisible(True)     
    #DDR Size (MB) 
    ddrSym_DDRsize = ddrComponent.createIntegerSymbol("DDR_SIZE_MB", None)
    ddrSym_DDRsize.setLabel("DDR Size (MB)")
    ddrSym_DDRsize.setDefaultValue(32)
    ddrSym_DDRsize.setMin(0)
    ddrSym_DDRsize.setMax(256)
    ddrSym_DDRsize.setVisible(True)  
    #Arbiter
    ddrSym_ARBITER_STRING = ddrComponent.createCommentSymbol("ARBITER", None)
    ddrSym_ARBITER_STRING.setLabel("Arbiter")
    ddrSym_ARBITER_STRING.setVisible(True)
    #Target 0 Minimum Burst Limit - hex field
    ddrSym_DDRMINLIM_MINLIM0 = ddrComponent.createHexSymbol("DDR_MINLIM_TGT0", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINLIM_MINLIM0.setLabel("Target 0 Minimum Burst Limit")
    ddrSym_DDRMINLIM_MINLIM0.setDefaultValue(31)
    ddrSym_DDRMINLIM_MINLIM0.setMin(0)
    ddrSym_DDRMINLIM_MINLIM0.setMax(31)
    ddrSym_DDRMINLIM_MINLIM0.setVisible(True)    
    #Target 0 Request Period - hex field
    ddrSym_DDRRQPER_RQPER0 = ddrComponent.createHexSymbol("DDR_REQPER_TGT0", ddrSym_ARBITER_STRING)
    ddrSym_DDRRQPER_RQPER0.setLabel("Target 0 Request Period")
    ddrSym_DDRRQPER_RQPER0.setDefaultValue(255)
    ddrSym_DDRRQPER_RQPER0.setMin(0)
    ddrSym_DDRRQPER_RQPER0.setMax(255)
    ddrSym_DDRRQPER_RQPER0.setVisible(True)      
    #Target 0 Minimum Command - hex field
    ddrSym_DDRMINCMD_MINCMD0 = ddrComponent.createHexSymbol("DDR_MINCMD_TGT0", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINCMD_MINCMD0.setLabel("Target 0 Minimum Command")
    ddrSym_DDRMINCMD_MINCMD0.setDefaultValue(4)
    ddrSym_DDRMINCMD_MINCMD0.setMin(0)
    ddrSym_DDRMINCMD_MINCMD0.setMax(255)
    ddrSym_DDRMINCMD_MINCMD0.setVisible(True)    
    #Target 1 Minimum Burst Limit - hex field
    ddrSym_DDRMINLIM_MINLIM1 = ddrComponent.createHexSymbol("DDR_MINLIM_TGT1", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINLIM_MINLIM1.setLabel("Target 1 Minimum Burst Limit")
    ddrSym_DDRMINLIM_MINLIM1.setDefaultValue(31)
    ddrSym_DDRMINLIM_MINLIM1.setMin(0)
    ddrSym_DDRMINLIM_MINLIM1.setMax(31)
    ddrSym_DDRMINLIM_MINLIM1.setVisible(True)        
    #Target 1 Request Period - hex field
    ddrSym_DDRRQPER_RQPER1 = ddrComponent.createHexSymbol("DDR_REQPER_TGT1", ddrSym_ARBITER_STRING)
    ddrSym_DDRRQPER_RQPER1.setLabel("Target 1 Request Period")
    ddrSym_DDRRQPER_RQPER1.setDefaultValue(255)
    ddrSym_DDRRQPER_RQPER1.setMin(0)
    ddrSym_DDRRQPER_RQPER1.setMax(255)
    ddrSym_DDRRQPER_RQPER1.setVisible(True)      
    #Target 1 Minimum Command - hex field
    ddrSym_DDRMINCMD_MINCMD1 = ddrComponent.createHexSymbol("DDR_MINCMD_TGT1", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINCMD_MINCMD1.setLabel("Target 1 Minimum Command")
    ddrSym_DDRMINCMD_MINCMD1.setDefaultValue(16)
    ddrSym_DDRMINCMD_MINCMD1.setMin(0)
    ddrSym_DDRMINCMD_MINCMD1.setMax(255)
    ddrSym_DDRMINCMD_MINCMD1.setVisible(True)        
    #Target 2 Minimum Burst Limit - hex field
    ddrSym_DDRMINLIM_MINLIM2 = ddrComponent.createHexSymbol("DDR_MINLIM_TGT2", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINLIM_MINLIM2.setLabel("Target 2 Minimum Burst Limit")
    ddrSym_DDRMINLIM_MINLIM2.setDefaultValue(31)
    ddrSym_DDRMINLIM_MINLIM2.setMin(0)
    ddrSym_DDRMINLIM_MINLIM2.setMax(31)
    ddrSym_DDRMINLIM_MINLIM2.setVisible(True)        
    #Target 2 Request Period - hex field
    ddrSym_DDRRQPER_RQPER2 = ddrComponent.createHexSymbol("DDR_REQPER_TGT2", ddrSym_ARBITER_STRING)
    ddrSym_DDRRQPER_RQPER2.setLabel("Target 2 Request Period")
    ddrSym_DDRRQPER_RQPER2.setDefaultValue(255)
    ddrSym_DDRRQPER_RQPER2.setMin(0)
    ddrSym_DDRRQPER_RQPER2.setMax(255)
    ddrSym_DDRRQPER_RQPER2.setVisible(True)      
    #Target 2 Minimum Command - hex field
    ddrSym_DDRMINCMD_MINCMD2 = ddrComponent.createHexSymbol("DDR_MINCMD_TGT2", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINCMD_MINCMD2.setLabel("Target 2 Minimum Command")
    ddrSym_DDRMINCMD_MINCMD2.setDefaultValue(16)
    ddrSym_DDRMINCMD_MINCMD2.setMin(0)
    ddrSym_DDRMINCMD_MINCMD2.setMax(255)
    ddrSym_DDRMINCMD_MINCMD2.setVisible(True)        
    #Target 3 Minimum Burst Limit - hex field
    ddrSym_DDRMINLIM_MINLIM3 = ddrComponent.createHexSymbol("DDR_MINLIM_TGT3", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINLIM_MINLIM3.setLabel("Target 3 Minimum Burst Limit")
    ddrSym_DDRMINLIM_MINLIM3.setDefaultValue(4)
    ddrSym_DDRMINLIM_MINLIM3.setMin(0)
    ddrSym_DDRMINLIM_MINLIM3.setMax(31)
    ddrSym_DDRMINLIM_MINLIM3.setVisible(True)        
    #Target 3 Request Period - hex field
    ddrSym_DDRRQPER_RQPER3 = ddrComponent.createHexSymbol("DDR_REQPER_TGT3", ddrSym_ARBITER_STRING)
    ddrSym_DDRRQPER_RQPER3.setLabel("Target 3 Request Period")
    ddrSym_DDRRQPER_RQPER3.setDefaultValue(255)
    ddrSym_DDRRQPER_RQPER3.setMin(0)
    ddrSym_DDRRQPER_RQPER3.setMax(255)
    ddrSym_DDRRQPER_RQPER3.setVisible(True)      
    #Target 3 Minimum Command - hex field
    ddrSym_DDRMINCMD_MINCMD3 = ddrComponent.createHexSymbol("DDR_MINCMD_TGT3", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINCMD_MINCMD3.setLabel("Target 3 Minimum Command")
    ddrSym_DDRMINCMD_MINCMD3.setDefaultValue(4)
    ddrSym_DDRMINCMD_MINCMD3.setMin(0)
    ddrSym_DDRMINCMD_MINCMD3.setMax(255)
    ddrSym_DDRMINCMD_MINCMD3.setVisible(True)        
    #Target 4 Minimum Burst Limit - hex field
    ddrSym_DDRMINLIM_MINLIM4 = ddrComponent.createHexSymbol("DDR_MINLIM_TGT4", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINLIM_MINLIM4.setLabel("Target 4 Minimum Burst Limit")    
    ddrSym_DDRMINLIM_MINLIM4.setDefaultValue(4)
    ddrSym_DDRMINLIM_MINLIM4.setMin(0)
    ddrSym_DDRMINLIM_MINLIM4.setMax(31)
    ddrSym_DDRMINLIM_MINLIM4.setVisible(True)        
    #Target 4 Request Period - hex field
    ddrSym_DDRRQPER_RQPER4 = ddrComponent.createHexSymbol("DDR_REQPER_TGT4", ddrSym_ARBITER_STRING)
    ddrSym_DDRRQPER_RQPER4.setLabel("Target 4 Request Period")
    ddrSym_DDRRQPER_RQPER4.setDefaultValue(255)
    ddrSym_DDRRQPER_RQPER4.setMin(0)
    ddrSym_DDRRQPER_RQPER4.setMax(255)
    ddrSym_DDRRQPER_RQPER4.setVisible(True)      
    #Target 4 Minimum Command - hex field
    ddrSym_DDRMINCMD_MINCMD4 = ddrComponent.createHexSymbol("DDR_MINCMD_TGT4", ddrSym_ARBITER_STRING)
    ddrSym_DDRMINCMD_MINCMD4.setLabel("Target 4 Minimum Command")
    ddrSym_DDRMINCMD_MINCMD4.setDefaultValue(4)
    ddrSym_DDRMINCMD_MINCMD4.setMin(0)
    ddrSym_DDRMINCMD_MINCMD4.setMax(255)
    ddrSym_DDRMINCMD_MINCMD4.setVisible(True)        

    #Addressing
    ddrSym_ADDRESSING_STRING = ddrComponent.createCommentSymbol("ADDRESSING", None)
    ddrSym_ADDRESSING_STRING.setLabel("Addressing")
    ddrSym_ADDRESSING_STRING.setVisible(True)
    #Number of Column Bits - number field
    ddrSym_ColumnBits = ddrComponent.createIntegerSymbol("DDR_COL_BITS", ddrSym_ADDRESSING_STRING)
    ddrSym_ColumnBits.setLabel("Number of Column Bits")
    ddrSym_ColumnBits.setDefaultValue(9)
    ddrSym_ColumnBits.setMin(0)
    ddrSym_ColumnBits.setMax(31)
    ddrSym_ColumnBits.setVisible(True)    
    #Number of Row Bits - number field
    ddrSym_RowBits = ddrComponent.createIntegerSymbol("DDR_ROW_BITS", ddrSym_ADDRESSING_STRING)
    ddrSym_RowBits.setLabel("Number of Row Bits")
    ddrSym_RowBits.setDefaultValue(13)
    ddrSym_RowBits.setMin(0)
    ddrSym_RowBits.setMax(31)
    ddrSym_RowBits.setVisible(True)     
    #Number of Bank Bits - number field
    ddrSym_BankBits = ddrComponent.createIntegerSymbol("DDR_BANK_BITS", ddrSym_ADDRESSING_STRING)
    ddrSym_BankBits.setLabel("Number of Bank Bits")
    ddrSym_BankBits.setDefaultValue(2)
    ddrSym_BankBits.setMin(0)
    ddrSym_BankBits.setMax(31)
    ddrSym_BankBits.setVisible(True)     

    #Timing
    ddrSym_TIMING_STRING = ddrComponent.createCommentSymbol("TIMING", None)
    ddrSym_TIMING_STRING.setLabel("Timing")
    ddrSym_TIMING_STRING.setVisible(True)
    #DDR Clock Period (psec)
    ddrSym_ClockPeriod = ddrComponent.createIntegerSymbol("DDR_CLK_PER", ddrSym_TIMING_STRING)
    ddrSym_ClockPeriod.setLabel("DDR Clock Period (psec)")
    ddrSym_ClockPeriod.setDefaultValue(2500)
    #ddrSym_ClockPeriod.setMin(0)
    #ddrSym_ClockPeriod.setMax(31)
    ddrSym_ClockPeriod.setVisible(True) 
    #Burst Length (BL) 
    ddrSym_BurstLength = ddrComponent.createIntegerSymbol("DDR_BRST_LEN", ddrSym_TIMING_STRING)
    ddrSym_BurstLength.setLabel("Burst Length (BL)")
    ddrSym_BurstLength.setDefaultValue(2)
    #ddrSym_BurstLength.setMin(0)
    #ddrSym_BurstLength.setMax(31)
    ddrSym_BurstLength.setVisible(True)     
    #Read Latency (CAS, clock cycles)
    ddrSym_ReadLatency = ddrComponent.createIntegerSymbol("DDR_CAS_LAT", ddrSym_TIMING_STRING)
    ddrSym_ReadLatency.setLabel("Read Latency (CAS, clock cycles)")
    ddrSym_ReadLatency.setDefaultValue(5)
    #ddrSym_ReadLatency.setMin(0)
    #ddrSym_ReadLatency.setMax(31)
    ddrSym_ReadLatency.setVisible(True)     
    #Write Latency (WL, clock cycles)
    ddrSym_WriteLatency = ddrComponent.createIntegerSymbol("DDR_WR_LAT", ddrSym_TIMING_STRING)
    ddrSym_WriteLatency.setLabel("Write Latency (WL, clock cycles)")
    ddrSym_WriteLatency.setDefaultValue(4)
    #ddrSym_WriteLatency.setMin(0)
    #ddrSym_WriteLatency.setMax(31)
    ddrSym_WriteLatency.setVisible(True)     
    #Refresh Cycle Time (tRFC, psec)
    ddrSym_RefreshCycTime = ddrComponent.createIntegerSymbol("DDR_TRFC", ddrSym_TIMING_STRING)
    ddrSym_RefreshCycTime.setLabel("Refresh Cycle Time (tRFC, psec)")
    ddrSym_RefreshCycTime.setDefaultValue(127500)
    #ddrSym_RefreshCycTime.setMin(0)
    #ddrSym_RefreshCycTime.setMax(31)
    ddrSym_RefreshCycTime.setVisible(True)     
    #Refresh Interval (tRFI, clock cycles)
    ddrSym_RefreshInterval = ddrComponent.createIntegerSymbol("DDR_TRFI", ddrSym_TIMING_STRING)
    ddrSym_RefreshInterval.setLabel("Refresh Interval (tRFI, clock cycles)")
    ddrSym_RefreshInterval.setDefaultValue(7800000)
    #ddrSym_RefreshInterval.setMin(0)
    #ddrSym_RefreshInterval.setMax(31)
    ddrSym_RefreshInterval.setVisible(True)     
    #Maximum Number of Pending Refreshes
    ddrSym_MaxPendRefresh = ddrComponent.createIntegerSymbol("DDR_MAX_PEND_REFS", ddrSym_TIMING_STRING)
    ddrSym_MaxPendRefresh.setLabel("Maximum Number of Pending Refreshes")
    ddrSym_MaxPendRefresh.setDefaultValue(7)
    #ddrSym_MaxPendRefresh.setMin(0)
    #ddrSym_MaxPendRefresh.setMax(31)
    ddrSym_MaxPendRefresh.setVisible(True)     
    #Write Recovery Time (tWR, psec)
    ddrSym_WriteRecTime = ddrComponent.createIntegerSymbol("DDR_TWR", ddrSym_TIMING_STRING)
    ddrSym_WriteRecTime.setLabel("Write Recovery Time (tWR, psec)")
    ddrSym_WriteRecTime.setDefaultValue(15000)
    #ddrSym_WriteRecTime.setMin(0)
    #ddrSym_WriteRecTime.setMax(31)
    ddrSym_WriteRecTime.setVisible(True)     
    #RAS Precharge Time (tRP, psec)
    ddrSym_RAS_PrecharTime = ddrComponent.createIntegerSymbol("DDR_TRP", ddrSym_TIMING_STRING)
    ddrSym_RAS_PrecharTime.setLabel("RAS Precharge Time (tRP, psec)")
    ddrSym_RAS_PrecharTime.setDefaultValue(12500)
    #ddrSym_RAS_PrecharTime.setMin(0)
    #ddrSym_RAS_PrecharTime.setMax(31)
    ddrSym_RAS_PrecharTime.setVisible(True)     
    #RAS to CAS Delay Time (tRCD, psec)
    ddrSym_RAS_CAS_Delay = ddrComponent.createIntegerSymbol("DDR_TRCD", ddrSym_TIMING_STRING)
    ddrSym_RAS_CAS_Delay.setLabel("RAS to CAS Delay Time (tRCD, psec)")
    ddrSym_RAS_CAS_Delay.setDefaultValue(12500)
    #ddrSym_RAS_CAS_Delay.setMin(0)
    #ddrSym_RAS_CAS_Delay.setMax(31)
    ddrSym_RAS_CAS_Delay.setVisible(True)     
    #Activate to Activate Delay Time (tWTR, psec)
    ddrSym_Act_Act_Delay = ddrComponent.createIntegerSymbol("DDR_TRRD", ddrSym_TIMING_STRING)
    ddrSym_Act_Act_Delay.setLabel("Activate to Activate Delay Time (tRRD, psec)")
    ddrSym_Act_Act_Delay.setDefaultValue(7500)
    #ddrSym_Act_Act_Delay.setMin(0)
    #ddrSym_Act_Act_Delay.setMax(31)
    ddrSym_Act_Act_Delay.setVisible(True)     
    #Write to Read Command Delay Time (tWTR, psec)
    ddrSym_Write_ReadCmdDelay = ddrComponent.createIntegerSymbol("DDR_TWTR", ddrSym_TIMING_STRING)
    ddrSym_Write_ReadCmdDelay.setLabel("Write to Read Command Delay Time (tWTR, psec)")
    ddrSym_Write_ReadCmdDelay.setDefaultValue(7500)
    #ddrSym_Write_ReadCmdDelay.setMin(0)
    #ddrSym_Write_ReadCmdDelay.setMax(31)
    ddrSym_Write_ReadCmdDelay.setVisible(True)     
    #Read to Precharge Delay Time (tRTP, psec)
    ddrSym_Read_Precharg_Delay = ddrComponent.createIntegerSymbol("DDR_TRTP", ddrSym_TIMING_STRING)
    ddrSym_Read_Precharg_Delay.setLabel("Read to Precharge Delay Time (tRTP, psec)")
    ddrSym_Read_Precharg_Delay.setDefaultValue(7500)
    #ddrSym_Read_Precharg_Delay.setMin(0)
    #ddrSym_Read_Precharg_Delay.setMax(31)
    ddrSym_Read_Precharg_Delay.setVisible(True)     
    #Active to Precharge Delay Time (tRAS, psec)
    ddrSym_Act_Precharg_Delay = ddrComponent.createIntegerSymbol("DDR_TRAS", ddrSym_TIMING_STRING)
    ddrSym_Act_Precharg_Delay.setLabel("Active to Precharge Delay Time (tRAS, psec)")
    ddrSym_Act_Precharg_Delay.setDefaultValue(45000)
    #ddrSym_Act_Precharg_Delay.setMin(0)
    #ddrSym_Act_Precharg_Delay.setMax(31)
    ddrSym_Act_Precharg_Delay.setVisible(True)     
    #Row Cycle Time (tRC, psec)
    ddrSym_RowCycleTime = ddrComponent.createIntegerSymbol("DDR_TRC", ddrSym_TIMING_STRING)
    ddrSym_RowCycleTime.setLabel("Row Cycle Time (tRC, psec)")
    ddrSym_RowCycleTime.setDefaultValue(57500)
    #ddrSym_RowCycleTime.setMin(0)
    #ddrSym_RowCycleTime.setMax(31)
    ddrSym_RowCycleTime.setVisible(True)     
    #Four Bank Activate Window (tFAW, psec)
    #default 45000 if SYS_MEMORY_DDR_TYPE = "Micron MT47H64M16"
    #default 35000 if SYS_MEMORY_DDR_TYPE = "Internal"
    #default 0
    ddrSym_FourBankActWin = ddrComponent.createIntegerSymbol("DDR_TFAW", ddrSym_TIMING_STRING)
    ddrSym_FourBankActWin.setLabel("Four Bank Activate Window (tFAW, psec)")
    ddrSym_FourBankActWin.setDefaultValue(35000)
    #ddrSym_FourBankActWin.setMin(0)
    #ddrSym_FourBankActWin.setMax(31)
    ddrSym_FourBankActWin.setVisible(True)     
    #Exit Precharge Power Down to Any Command Time (tXP, clock cycles)
    ddrSym_ExitPregchargPwrDwn = ddrComponent.createIntegerSymbol("DDR_TXP", ddrSym_TIMING_STRING)
    ddrSym_ExitPregchargPwrDwn.setLabel("Exit Precharge Power Down to Any Command Time (tXP, clock cycles)")
    ddrSym_ExitPregchargPwrDwn.setDefaultValue(2)
    #ddrSym_ExitPregchargPwrDwn.setMin(0)
    #ddrSym_ExitPregchargPwrDwn.setMax(31)
    ddrSym_ExitPregchargPwrDwn.setVisible(True)     
    #CKE Minimum High/Low Time (tCKE, clock cycles)
    ddrSym_CKE_MinHLTime = ddrComponent.createIntegerSymbol("DDR_TCKE", ddrSym_TIMING_STRING)
    ddrSym_CKE_MinHLTime.setLabel("CKE Minimum High/Low Time (tCKE, clock cycles)")
    ddrSym_CKE_MinHLTime.setDefaultValue(3)
    #ddrSym_CKE_MinHLTime.setMin(0)
    #ddrSym_CKE_MinHLTime.setMax(31)
    ddrSym_CKE_MinHLTime.setVisible(True)     
    #Mode Register Set Command Cycle Time (tMRD, clock cycles)
    ddrSym_ModeRegSetCmdCycTime = ddrComponent.createIntegerSymbol("DDR_TMRD", ddrSym_TIMING_STRING)
    ddrSym_ModeRegSetCmdCycTime.setLabel("Mode Register Set Command Cycle Time (tMRD, clock cycles)")
    ddrSym_ModeRegSetCmdCycTime.setDefaultValue(2)
    #ddrSym_ModeRegSetCmdCycTime.setMin(0)
    #ddrSym_ModeRegSetCmdCycTime.setMax(31)
    ddrSym_ModeRegSetCmdCycTime.setVisible(True)     
    #DLL Lock Time (number of clocks)
    ddrSym_DLL_LockTime = ddrComponent.createIntegerSymbol("DDR_TDLLK", ddrSym_TIMING_STRING)
    ddrSym_DLL_LockTime.setLabel("DLL Lock Time (number of clocks)")
    ddrSym_DLL_LockTime.setDefaultValue(200)
    #ddrSym_DLL_LockTime.setMin(0)
    #ddrSym_DLL_LockTime.setMax(31)
    ddrSym_DLL_LockTime.setVisible(True)     

    #Power Control
    ddrSym_PWRCONTROL_STRING = ddrComponent.createCommentSymbol("PWRCONTROL", None)
    ddrSym_PWRCONTROL_STRING.setLabel("Power Control")
    ddrSym_PWRCONTROL_STRING.setVisible(True)
    #Enable Auto Power Down? 
    ddrSym_DDRPWRCFG_APWRDNEN = ddrComponent.createBooleanSymbol("DDR_AUTO_PWR_DOWN", ddrSym_PWRCONTROL_STRING)
    ddrSym_DDRPWRCFG_APWRDNEN.setLabel("Enable Automatic Power Down")
    ddrSym_DDRPWRCFG_APWRDNEN.setDefaultValue(False)
    ddrSym_DDRPWRCFG_APWRDNEN.setVisible(True)
    #Enable Auto Self Refresh  - Bool ****************************NOT IN H2****************
##    ddrSym_DDRPWRCFG_ASLFREFEN = ddrComponent.createBooleanSymbol("ASLFREFEN", ddrSym_PWRCONTROL_STRING)
##    ddrSym_DDRPWRCFG_ASLFREFEN.setLabel("Automatic Self Refresh Enable bit")
##    ddrSym_DDRPWRCFG_ASLFREFEN.setDefaultValue(False)
##    ddrSym_DDRPWRCFG_ASLFREFEN.setVisible(True)     
    #Enable Auto Precharge?
    ddrSym_DDRMEMCFG0_APCHRGEN = ddrComponent.createBooleanSymbol("DDR_AUTO_PCHRG", ddrSym_PWRCONTROL_STRING)
    ddrSym_DDRMEMCFG0_APCHRGEN.setLabel("Enable Auto Precharge")
    ddrSym_DDRMEMCFG0_APCHRGEN.setDefaultValue(False)
    ddrSym_DDRMEMCFG0_APCHRGEN.setVisible(True)        
    #Enable Auto Precharge Power Down?
    ddrSym_DDRPWRCFG_PCHRGPWDN = ddrComponent.createBooleanSymbol("DDR_AUTO_PCHRG_PWR_DOWN", ddrSym_PWRCONTROL_STRING)
    ddrSym_DDRPWRCFG_PCHRGPWDN.setLabel("Enable Auto Precharge Power Down")
    ddrSym_DDRPWRCFG_PCHRGPWDN.setDefaultValue(False)
    ddrSym_DDRPWRCFG_PCHRGPWDN.setVisible(True)        
    #Self Refresh Delay
    ddrSym_DDRPWRCFG_SLFREFDLY = ddrComponent.createIntegerSymbol("DDR_SELF_REFRESH_DELAY", ddrSym_PWRCONTROL_STRING)
    ddrSym_DDRPWRCFG_SLFREFDLY.setLabel("Self Refresh Delay")
    ddrSym_DDRPWRCFG_SLFREFDLY.setDefaultValue(17)
    #ddrSym_DDRPWRCFG_SLFREFDLY.setMin(0)
    #ddrSym_DDRPWRCFG_SLFREFDLY.setMax(31)
    ddrSym_DDRPWRCFG_SLFREFDLY.setVisible(True)     
    #Power Down Delay
    ddrSym_DDRPWRCFG_PWRDNDLY = ddrComponent.createIntegerSymbol("DDR_PWR_DOWN_DELAY", ddrSym_PWRCONTROL_STRING)
    ddrSym_DDRPWRCFG_PWRDNDLY.setLabel("Power Down Delay")
    ddrSym_DDRPWRCFG_PWRDNDLY.setDefaultValue(8)
    #ddrSym_DDRPWRCFG_PWRDNDLY.setMin(0)
    #ddrSym_DDRPWRCFG_PWRDNDLY.setMax(31)
    ddrSym_DDRPWRCFG_PWRDNDLY.setVisible(True)     

    #Host Commands
    ddrSym_HOSTCMD_STRING = ddrComponent.createCommentSymbol("HOSTCMD", None)
    ddrSym_HOSTCMD_STRING.setLabel("Host Commands")
    ddrSym_HOSTCMD_STRING.setVisible(True)
    #Number of Host Commands
    ddrSym_DDRCMDISSUE_NUMHOSTCMDS = ddrComponent.createHexSymbol("DDR_NUM_CMDS", ddrSym_HOSTCMD_STRING)
    ddrSym_DDRCMDISSUE_NUMHOSTCMDS.setLabel("Number of Host Commands")
    ddrSym_DDRCMDISSUE_NUMHOSTCMDS.setDefaultValue(12-1)
    ddrSym_DDRCMDISSUE_NUMHOSTCMDS.setVisible(True)
    
    #On-Die Termination
    ddrSym_TERMINATION_STRING = ddrComponent.createCommentSymbol("TERMINATION", None)
    ddrSym_TERMINATION_STRING.setLabel("On-Die Termination")
    ddrSym_TERMINATION_STRING.setVisible(True)
    
    #Enable ODT for Reads
    ddrSym_DDRODTENCFG_ODTREN = ddrComponent.createBooleanSymbol("DDR_ODT_READ_ENABLE", ddrSym_TERMINATION_STRING)
    ddrSym_DDRODTENCFG_ODTREN.setLabel("Enable On-Die Termination for Reads")
    ddrSym_DDRODTENCFG_ODTREN.setDefaultValue(False)
    ddrSym_DDRODTENCFG_ODTREN.setVisible(True)      
        #Number of Clocks ODT is Turned on for Reads
    ddrSym_DDRODTCFG_ODTRLEN = ddrComponent.createIntegerSymbol("DDR_ODT_READ_CLOCKS", ddrSym_DDRODTENCFG_ODTREN)
    ddrSym_DDRODTCFG_ODTRLEN.setLabel("On-Die Termination Read Length bits")
    ddrSym_DDRODTCFG_ODTRLEN.setDefaultValue(2)
    #ddrSym_DDRODTCFG_ODTRLEN.setMin(0)
    #ddrSym_DDRODTCFG_ODTRLEN.setMax(31)
    ddrSym_DDRODTCFG_ODTRLEN.setVisible(True) 
        #Number of Clocks After Write Command Before Turning on ODT
    ddrSym_DDRODTCFG_ODTRDLY = ddrComponent.createIntegerSymbol("DDR_ODT_READ_DLY", ddrSym_DDRODTENCFG_ODTREN)
    ddrSym_DDRODTCFG_ODTRDLY.setLabel("On-Die Termination Read Delay bits")
    ddrSym_DDRODTCFG_ODTRDLY.setDefaultValue(4)
    #ddrSym_DDRODTCFG_ODTRDLY.setMin(0)
    #ddrSym_DDRODTCFG_ODTRDLY.setMax(31)
    ddrSym_DDRODTCFG_ODTRDLY.setVisible(True)
    
    #Enable ODT for Writes?
    ddrSym_DDRODTENCFG_ODTWEN = ddrComponent.createBooleanSymbol("DDR_ODT_WRITE_ENABLE", ddrSym_TERMINATION_STRING)
    ddrSym_DDRODTENCFG_ODTWEN.setLabel("Enable On-Die Termination for Writes")
    ddrSym_DDRODTENCFG_ODTWEN.setDefaultValue(True)
    ddrSym_DDRODTENCFG_ODTWEN.setVisible(True)     
        #Number of Clocks ODT is Turned on for Writes
    ddrSym_DDRODTCFG_ODTWLEN = ddrComponent.createIntegerSymbol("DDR_ODT_WRITE_CLOCKS", ddrSym_DDRODTENCFG_ODTWEN)
    ddrSym_DDRODTCFG_ODTWLEN.setLabel("On-Die Termination Write Length bits")
    ddrSym_DDRODTCFG_ODTWLEN.setDefaultValue(3)
    #ddrSym_DDRODTCFG_ODTWLEN.setMin(0)
    #ddrSym_DDRODTCFG_ODTWLEN.setMax(31)
    ddrSym_DDRODTCFG_ODTWLEN.setVisible(True)     
        #Number of Clocks After Write Command Before turning on ODT
    ddrSym_DDRODTCFG_ODTWDLY = ddrComponent.createIntegerSymbol("DDR_ODT_WRITE_DLY", ddrSym_DDRODTENCFG_ODTWEN)
    ddrSym_DDRODTCFG_ODTWDLY.setLabel("On-Die Termination Write Delay bits")
    ddrSym_DDRODTCFG_ODTWDLY.setDefaultValue(1)
    #ddrSym_DDRODTCFG_ODTWDLY.setMin(0)
    #ddrSym_DDRODTCFG_ODTWDLY.setMax(31)
    ddrSym_DDRODTCFG_ODTWDLY.setVisible(True)      

    #DDR PHY Configuration Parameters
    ddrSym_PHYCONFIG_STRING = ddrComponent.createCommentSymbol("PHYCONFIG", None)
    ddrSym_PHYCONFIG_STRING.setLabel("DDR PHY Configuration Parameters")
    ddrSym_PHYCONFIG_STRING.setVisible(True)        
    #Enable PHY ODT - Boolean
    ddrSym_DDRPHYPADCON_ODTEN = ddrComponent.createBooleanSymbol("DDR_PHY_ODT_ENABLE", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_ODTEN.setLabel("On-Die Termination Enable bit")
    ddrSym_DDRPHYPADCON_ODTEN.setDefaultValue(True)
    ddrSym_DDRPHYPADCON_ODTEN.setVisible(True)
    #ODTSEL On-Die Termination Select bit
    ddrODTSEL_names = []
    _get_bitfield_names(ddrValGrp_DDRPHYPADCON_ODTSEL, ddrODTSEL_names)
    ddrSym_DDRPHYPADCON_ODTSEL = ddrComponent.createKeyValueSetSymbol("DDR_PHY_ODT_VALUE", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_ODTSEL.setLabel("PHY On-Die Termination Value")
    ddrSym_DDRPHYPADCON_ODTSEL.setDefaultValue(1)
    ddrSym_DDRPHYPADCON_ODTSEL.setOutputMode("Value")
    ddrSym_DDRPHYPADCON_ODTSEL.setDisplayMode("Description")
    for ii in ddrODTSEL_names:
        ddrSym_DDRPHYPADCON_ODTSEL.addKey( ii['desc'], ii['value'], ii['key'] )    
    ddrSym_DDRPHYPADCON_ODTSEL.setVisible(True) 
    #PHY Drive Strength for Data Pads
    ddrDATDRVSEL_names = []
    _get_bitfield_names(ddrValGrp_DDRPHYPADCON_DATDRVSEL, ddrDATDRVSEL_names)
    ddrSym_DDRPHYPADCON_DATDRVSEL = ddrComponent.createKeyValueSetSymbol("DDR_PHY_SYS_MEMORY_STRENGTH_DATA", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_DATDRVSEL.setLabel("Data Pad Drive Strength Select bit")
    ddrSym_DDRPHYPADCON_DATDRVSEL.setDefaultValue(0)
    ddrSym_DDRPHYPADCON_DATDRVSEL.setOutputMode("Value")
    ddrSym_DDRPHYPADCON_DATDRVSEL.setDisplayMode("Description")
    for ii in ddrDATDRVSEL_names:
        ddrSym_DDRPHYPADCON_DATDRVSEL.addKey( ii['desc'], ii['value'], ii['key'] )    
    ddrSym_DDRPHYPADCON_DATDRVSEL.setVisible(True)    
    #PHY Drive Strength for Address and Control Pads
    ddrADDCDRVSEL_names = []
    _get_bitfield_names(ddrValGrp_DDRPHYPADCON_ADDCDRVSEL, ddrADDCDRVSEL_names)
    ddrSym_DDRPHYPADCON_ADDCDRVSEL = ddrComponent.createKeyValueSetSymbol("DDR_PHY_SYS_MEMORY_STRENGTH_ADDC", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_ADDCDRVSEL.setLabel("Data Pad Drive Strength Select bit")
    ddrSym_DDRPHYPADCON_ADDCDRVSEL.setDefaultValue(0)
    ddrSym_DDRPHYPADCON_ADDCDRVSEL.setOutputMode("Value")
    ddrSym_DDRPHYPADCON_ADDCDRVSEL.setDisplayMode("Description")
    for ii in ddrDATDRVSEL_names:
        ddrSym_DDRPHYPADCON_ADDCDRVSEL.addKey( ii['desc'], ii['value'], ii['key'] )    
    ddrSym_DDRPHYPADCON_ADDCDRVSEL.setVisible(True)     
    #PHY ODT Pull-Up Calibration Value (0-3)
    ddrSym_DDRPHYPADCON_ODTPUCAL = ddrComponent.createIntegerSymbol("DDR_PHY_ODT_PU_CAL", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_ODTPUCAL.setLabel("On-Die Termination Pull-Up Calibration bits")
    ddrSym_DDRPHYPADCON_ODTPUCAL.setDefaultValue(3)
    ddrSym_DDRPHYPADCON_ODTPUCAL.setMin(0)
    ddrSym_DDRPHYPADCON_ODTPUCAL.setMax(3)
    ddrSym_DDRPHYPADCON_ODTPUCAL.setVisible(True)       
    #PHY ODT Pull-Up Calibration Value (0-3)
    ddrSym_DDRPHYPADCON_ODTPDCAL = ddrComponent.createIntegerSymbol("DDR_PHY_ODT_PD_CAL", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_ODTPDCAL.setLabel("On-Die Termination Pull-Down Calibration bits")
    ddrSym_DDRPHYPADCON_ODTPDCAL.setDefaultValue(2)
    ddrSym_DDRPHYPADCON_ODTPDCAL.setMin(0)
    ddrSym_DDRPHYPADCON_ODTPDCAL.setMax(3)
    ddrSym_DDRPHYPADCON_ODTPDCAL.setVisible(True)       
    #PHY Drive Strength (NFET) Calibration Value (0-15)
    ddrSym_DDRPHYPADCON_DRVSTRNFET = ddrComponent.createIntegerSymbol("DDR_PHY_SYS_MEMORY_STR_NFET_CAL", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_DRVSTRNFET.setLabel("NFET Drive Strength bits")
    ddrSym_DDRPHYPADCON_DRVSTRNFET.setDefaultValue(14)
    ddrSym_DDRPHYPADCON_DRVSTRNFET.setMin(0)
    ddrSym_DDRPHYPADCON_DRVSTRNFET.setMax(15)
    ddrSym_DDRPHYPADCON_DRVSTRNFET.setVisible(True)    
    #PHY Drive Strength (PFET) Calibration Value (0-15)
    ddrSym_DDRPHYPADCON_DRVSTRPFET = ddrComponent.createIntegerSymbol("DDR_PHY_SYS_MEMORY_STR_PFET_CAL", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_DRVSTRPFET.setLabel("PFET Drive Strength bits")
    ddrSym_DDRPHYPADCON_DRVSTRPFET.setDefaultValue(14)
    ddrSym_DDRPHYPADCON_DRVSTRPFET.setMin(0)
    ddrSym_DDRPHYPADCON_DRVSTRPFET.setMax(15)
    ddrSym_DDRPHYPADCON_DRVSTRPFET.setVisible(True)    
    #Enable Drive Pad for an Extra Clock After Write Burst
    ddrSym_DDRPHYPADCON_EOENCLKCYC = ddrComponent.createBooleanSymbol("DDR_PHY_EXTRA_CLK", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_EOENCLKCYC.setLabel("Extra Output Enable bit")
    ddrSym_DDRPHYPADCON_EOENCLKCYC.setDefaultValue(False)
    ddrSym_DDRPHYPADCON_EOENCLKCYC.setVisible(True)

    #DDR_PHY_DLL - Visable in H2 but fixed as 'Internal'
    
    #Enable Pad Receivers on Bidirectional I/Os?
    ddrSym_DDRPHYPADCON_RCVREN = ddrComponent.createBooleanSymbol("DDR_PHY_RCVREN", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_RCVREN.setLabel("Receiver Enable bit")
    ddrSym_DDRPHYPADCON_RCVREN.setDefaultValue(True)
    ddrSym_DDRPHYPADCON_RCVREN.setVisible(True)     
    #Enable Pad Write Command Delay?
    ddrSym_DDRPHYPADCON_WRCMDDLY = ddrComponent.createBooleanSymbol("DDR_PHY_WR_CMD_DLY", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_WRCMDDLY.setLabel("Write Command Delay bit")
    ddrSym_DDRPHYPADCON_WRCMDDLY.setDefaultValue(True)
    ddrSym_DDRPHYPADCON_WRCMDDLY.setVisible(True)     
    #Preamble Delay for Writes 
    ddrPREAMBDLY_names = []
    _get_bitfield_names(ddrValGrp_DDRPHYPADCON_PREAMBDLY, ddrPREAMBDLY_names)
    ddrSym_DDRPHYPADCON_PREAMBDLY = ddrComponent.createKeyValueSetSymbol("DDR_PHY_PRE_DLY", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYPADCON_PREAMBDLY.setLabel("Preamble Delay bits")
    ddrSym_DDRPHYPADCON_PREAMBDLY.setDefaultValue(2)
    ddrSym_DDRPHYPADCON_PREAMBDLY.setOutputMode("Value")
    ddrSym_DDRPHYPADCON_PREAMBDLY.setDisplayMode("Description")
    for ii in ddrPREAMBDLY_names:
        ddrSym_DDRPHYPADCON_PREAMBDLY.addKey( ii['desc'], ii['value'], ii['key'] )    
    ddrSym_DDRPHYPADCON_PREAMBDLY.setVisible(True)     
    #Enable DLL Recalibration 
    ddrSym_DDRPHYDLLR_DISRECALIB = ddrComponent.createBooleanSymbol("DDR_PHY_RECALIB_EN", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DISRECALIB.setLabel("Disable Recalibration bit")
    ddrSym_DDRPHYDLLR_DISRECALIB.setDefaultValue(True)
    ddrSym_DDRPHYDLLR_DISRECALIB.setVisible(True)     
        #DLL Recalibraion Count 
    ddrSym_DDRPHYDLLR_RECALIBCNT = ddrComponent.createIntegerSymbol("DDR_PHY_RECALIB_COUNT", ddrSym_DDRPHYDLLR_DISRECALIB)
    ddrSym_DDRPHYDLLR_RECALIBCNT.setLabel("Recalibration Count bits")
    ddrSym_DDRPHYDLLR_RECALIBCNT.setDefaultValue(16)
    ddrSym_DDRPHYDLLR_RECALIBCNT.setMin(0)
    ddrSym_DDRPHYDLLR_RECALIBCNT.setMax(262143)
    ddrSym_DDRPHYDLLR_RECALIBCNT.setVisible(True)     
    #Start Value of the DLL Master Delay Line
    ddrSym_DDRPHYDLLR_DLYSTVAL = ddrComponent.createIntegerSymbol("DDR_PHY_DLL_MASTER_DELAY_START", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setLabel("Delay Start Value bits")
    ddrSym_DDRPHYDLLR_DLYSTVAL.setDefaultValue(3)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMin(0)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMax(15)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setVisible(True)     
    #PHY SCL Capture Clock Delay 
    ddrSym_DDRPHYDLLR_DLYSTVAL = ddrComponent.createIntegerSymbol("DDR_PHY_SCL_CAP_CLK_DELAY", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setLabel("PHY SCL Capture Clock Delay ")
    ddrSym_DDRPHYDLLR_DLYSTVAL.setDefaultValue(3)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMin(0)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMax(15)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setVisible(True)     
    #PHY SCL Main Clock Delay
    ddrSym_DDRPHYDLLR_DLYSTVAL = ddrComponent.createIntegerSymbol("DDR_PHY_SCL_MAIN_CLK_DELAY", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setLabel("PHY SCL Main Clock Delay")
    ddrSym_DDRPHYDLLR_DLYSTVAL.setDefaultValue(4)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMin(0)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setMax(15)
    ddrSym_DDRPHYDLLR_DLYSTVAL.setVisible(True)     
    #SCL Burst Mode - text field - DDR_PHY_SCL_BURST_MODE
    ddrSym_burstString = ddrComponent.createStringSymbol("DDR_PHY_SCL_BURST_MODE", ddrSym_PHYCONFIG_STRING)
    ddrSym_burstString.setLabel("SCL Burst Mode")
    ddrSym_burstString.setDefaultValue("DDR_PHY_SCL_BURST_MODE_8")
    ddrSym_burstString.setVisible(True)        
    #DDR Type (for PHY configuration) - text field - DDR_PHY_DDR_TYPE
    ddrSym_burstString = ddrComponent.createStringSymbol("DDR_PHY_DDR_TYPE", ddrSym_PHYCONFIG_STRING)
    ddrSym_burstString.setLabel("DDR Type (for PHY configuration)")
    ddrSym_burstString.setDefaultValue("DDR_PHY_DDR_TYPE_DDR2")
    ddrSym_burstString.setVisible(True)      
    #Enable ODT on Chip Select Line While Running SCL?
    ddrSym_DDRPHYDLLR_DISRECALIB = ddrComponent.createBooleanSymbol("DDR_PHY_ODT_CS_EN", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DISRECALIB.setLabel("Enable ODT on Chip Select Line While Running SCL?")
    ddrSym_DDRPHYDLLR_DISRECALIB.setDefaultValue(True)
    ddrSym_DDRPHYDLLR_DISRECALIB.setVisible(True)    
    #SCL Reference Delay 
    ddrDBLREFDLY_names = []
    _get_bitfield_names(ddrValGrp_DDRSCLCFG1_DBLREFDLY, ddrDBLREFDLY_names)
    ddrSym_DDRSCLCFG1_DBLREFDLY = ddrComponent.createKeyValueSetSymbol("DDR_PHY_SCL_DLY", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRSCLCFG1_DBLREFDLY.setLabel("SCL Reference Delay ")
    ddrSym_DDRSCLCFG1_DBLREFDLY.setDefaultValue(0)
    ddrSym_DDRSCLCFG1_DBLREFDLY.setOutputMode("Value")
    ddrSym_DDRSCLCFG1_DBLREFDLY.setDisplayMode("Description")
    for ii in ddrDBLREFDLY_names:
        ddrSym_DDRSCLCFG1_DBLREFDLY.addKey( ii['desc'], ii['value'], ii['key'] )    
    ddrSym_DDRSCLCFG1_DBLREFDLY.setVisible(True)     
    #Enable SCL on Chip Select 0
    ddrSym_DDRPHYDLLR_DISRECALIB = ddrComponent.createBooleanSymbol("DDR_SCL_CS_EN", ddrSym_PHYCONFIG_STRING)
    ddrSym_DDRPHYDLLR_DISRECALIB.setLabel("Enable SCL on Chip Select 0")
    ddrSym_DDRPHYDLLR_DISRECALIB.setDefaultValue(True)
    ddrSym_DDRPHYDLLR_DISRECALIB.setVisible(True)     

############################################################################
#### Dependency ####
############################################################################
  
############################################################################
#### Code Generation ####
############################################################################
    
    configName = Variables.get("__CONFIGURATION_NAME")

    ddrHeader1File = ddrComponent.createFileSymbol("DDR_HEADER1", None)
    ddrHeader1File.setMarkup(True)
    ddrHeader1File.setSourcePath("../peripheral/ddr_00184/templates/plib_ddr.h.ftl")
    ddrHeader1File.setOutputName("plib_"+ ddrInstanceName.getValue().lower()+ ".h")
    ddrHeader1File.setDestPath("peripheral/ddr/")
    ddrHeader1File.setProjectPath("config/" + configName + "/peripheral/ddr/")
    ddrHeader1File.setType("HEADER")
    ddrHeader1File.setOverwrite(True)

    ddrSource1File = ddrComponent.createFileSymbol("DDR_SOURCE1", None)
    ddrSource1File.setMarkup(True)
    ddrSource1File.setSourcePath("../peripheral/ddr_00184/templates/plib_ddr.c.ftl")
    ddrSource1File.setOutputName("plib_"+ddrInstanceName.getValue().lower() + ".c")
    ddrSource1File.setDestPath("peripheral/ddr/")
    ddrSource1File.setProjectPath("config/" + configName + "/peripheral/ddr/")
    ddrSource1File.setType("SOURCE")
    ddrSource1File.setOverwrite(True)

    ddrSystemInitFile = ddrComponent.createFileSymbol("DDR_INIT", None)
    ddrSystemInitFile.setType("STRING")
    ddrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ddrSystemInitFile.setSourcePath("../peripheral/ddr_00184/templates/system/initialization.c.ftl")
    ddrSystemInitFile.setMarkup(True)

    ddrSystemDefFile = ddrComponent.createFileSymbol("DDR_DEF", None)
    ddrSystemDefFile.setType("STRING")
    ddrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ddrSystemDefFile.setSourcePath("../peripheral/ddr_00184/templates/system/definitions.h.ftl")
    ddrSystemDefFile.setMarkup(True)

