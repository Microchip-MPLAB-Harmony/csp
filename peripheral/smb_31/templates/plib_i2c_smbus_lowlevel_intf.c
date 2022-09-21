/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_i2c_smbus_lowlevel_intf.c

  Summary:
    I2C PLIB Master-Slave Mode Common Implementation file

  Description:
    This file defines the interface to the I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "device.h"
#include "plib_i2c_smbus_lowlevel_intf.h"

#define NOP() asm("nop")

static smb_registers_t* smbInstanceGet(SMB_INSTANCE instanceNum)
{
    return (smb_registers_t*)(SMB0_BASE_ADDRESS + (((uint32_t)instanceNum) * 0x400U));
}

/******************************************************************************/
/** I2CSMBx_Reset function.
 * This function resets the smb controller
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_Reset(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_RST_Msk;
    NOP();NOP();NOP();NOP();
    smb_regs->SMB_CFG[0] &= ~SMB_CFG_RST_Msk;
}

/******************************************************************************/
/** I2CSMBx_Enable function.
 * This function enables the smbus hardware controller
 * @param ownAddress - smb address to program in own address register
 * @param port - the port to configure
 * @param speed - smbus speed to configure - SMBUS_SPEED_400KHZ/SMBUS_SPEED_100KHZ
 * @param fairnessEnableFlag - flag to indicate if fairness needs to be enabled
 * @return None
*******************************************************************************/
void I2CSMBx_Enable(SMB_INSTANCE smbInstance, const uint16_t ownAddress, const uint8_t port, const uint8_t speed, const bool fairnessEnableFlag)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    I2CSMBx_Reset(smbInstance);

    /* PIN =1 */
    smb_regs->SMB_WCTRL = SMB_WCTRL_PIN_Msk;

    /* Enable Smbus Controller and assign the port */
    smb_regs->SMB_CFG[0] = (SMB_CFG_GC_DIS_Msk |
                           SMB_CFG_EN_Msk | SMB_CFG_PECEN_Msk |
                           SMB_CFG_FEN_Msk | port);

    /* Configure speed and other timing parameters */
    I2CSMBx_TimingInit(smbInstance, speed, fairnessEnableFlag);

    /* Program the own address register */
    I2CSMBx_OwnSlaveAddrSet(smbInstance, ownAddress);

    /* PIN(Bit7 of Control Register) =1, ESO(Bit6 of Control Register)=1,
     * ACK(Bit0 of Control Register) =1 */
    smb_regs->SMB_WCTRL = (SMB_WCTRL_PIN_Msk | SMB_WCTRL_ESO_Msk | SMB_WCTRL_ACK_Msk);
}

/******************************************************************************/
/** HW_SMB::start_slave function.
 * This function starts the slave state machine by programming the slave command
 * register
 * @param read_count - slave read count
 * @param write_count - slave write count
 * @param pecFlag - flag to indicate if PEC needs to be enabled
 * @return None
*******************************************************************************/
void I2CSMBx_StartSlave(SMB_INSTANCE smbInstance, const uint8_t read_count, const uint8_t write_count, const bool pecFlag)
{
    uint32_t slaveCommandRegValue;
    uint8_t pec_bit=0;
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    if (pecFlag)
    {
        pec_bit = 1;
    }

    slaveCommandRegValue = (uint32_t)(((uint32_t)read_count << 16) | ((uint32_t)write_count << 8)
                            | ((uint32_t)pec_bit << 2));

    smb_regs->SMB_SCMD[0] = slaveCommandRegValue;

    /* Need to set SProceed bit in SMB Slave Commnad reg. */
    smb_regs->SMB_SCMD[0] |= SMB_SCMD_SPROCEED_Msk;

    /* Run the Slave State Machine */
    smb_regs->SMB_SCMD[0] |= SMB_SCMD_SRUN_Msk;
}

/******************************************************************************/
/** HW_SMB::timing_init function.
 * This function programs the bus clock, data timing, fairness and
 * timeout scaling registers
 * @param speed - speed to configure SMBUS_SPEED_1MHZ/SMBUS_SPEED_400KHZ/SMBUS_SPEED_100KHZ
 * @param fairnessEnableFlag - flag to indicate if fairness needs to be enabled
 * @return None
*******************************************************************************/
void I2CSMBx_TimingInit(SMB_INSTANCE smbInstance, const uint8_t speed, const bool fairnessEnable)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    if ((uint8_t)I2CSMB_BUS_SPEED_400KHZ == speed)
    {
        /* For 8MHz baud clock, set the high & low period to 10,
         * therefore 8M/(10+10) = 400khz */

        smb_regs->SMB_BUSCLK = SPD_400KHZ_BUS_CLOCK;
        smb_regs->SMB_DATATM = SPD_400KHZ_DATA_TIMING;
        smb_regs->SMB_TMOUTSC = SPD_400KHZ_TIMEOUT_SCALING;
        smb_regs->SMB_RSHTM = SPD_400KHZ_DATA_TIMING_2;
        if (fairnessEnable)
        {
            smb_regs->SMB_CFG[0] |= SMB_CFG_FAIR_Msk;
            smb_regs->SMB_IDLSC = SPD_400KHZ_IDLE_SCALING;
        }
    }
    else
    {
        if ((uint8_t)I2CSMB_BUS_SPEED_100KHZ == speed)
        {
            /* For 8MHz baud clock, set the high & low period to 40,
             * therefore 8M/(40+40) = 100khz */
            smb_regs->SMB_BUSCLK = SPD_100KHZ_BUS_CLOCK;
            smb_regs->SMB_DATATM = SPD_100KHZ_DATA_TIMING;
            smb_regs->SMB_TMOUTSC = SPD_100KHZ_TIMEOUT_SCALING;
            smb_regs->SMB_RSHTM = SPD_100KHZ_DATA_TIMING_2;
            if (fairnessEnable)
            {
                smb_regs->SMB_CFG[0] |= SMB_CFG_FAIR_Msk;
                smb_regs->SMB_IDLSC = SPD_100KHZ_IDLE_SCALING;
            }
        }
        else if ((uint8_t)I2CSMB_BUS_SPEED_1MHZ == speed)
        {
            smb_regs->SMB_BUSCLK = SPD_1MHZ_BUS_CLOCK;
            smb_regs->SMB_DATATM = SPD_1MHZ_DATA_TIMING;
            smb_regs->SMB_TMOUTSC = SPD_1MHZ_TIMEOUT_SCALING;
            smb_regs->SMB_RSHTM = SPD_1MHZ_DATA_TIMING_2;
            if (fairnessEnable)
            {
                smb_regs->SMB_CFG[0] |= SMB_CFG_FAIR_Msk;
                smb_regs->SMB_IDLSC = SPD_1MHZ_IDLE_SCALING;
            }
        }

        else
        {
            //smb_timing_init: Invalid speed configuration
        }
    }
}

/******************************************************************************/
/** I2CSMBx_FlushHwTxRxBuffers function.
 * This function clears the master/slave tx and rx buffers
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_FlushHwTxRxBuffers(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Flush Master Xmit and Rx Buffers */
    smb_regs->SMB_CFG[0] |= (SMB_CFG_FLUSH_MXBUF_Msk | SMB_CFG_FLUSH_MRBUF_Msk);

    /* Flush Slave Xmit and Rx Buffers */
    smb_regs->SMB_CFG[0] |= (SMB_CFG_FLUSH_SXBUF_Msk | SMB_CFG_FLUSH_SRBUF_Msk);
}

/******************************************************************************/
/** I2CSMBx_StartMaster function.
 * This function starts the master state machine
 * @return master_command - master command value
 * @param None
*******************************************************************************/
void I2CSMBx_StartMaster(SMB_INSTANCE smbInstance, const uint32_t master_command)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Program the Master Command Register */
    smb_regs->SMB_MCMD[0] = (master_command | SMB_MCMD_MPROCEED_Msk | SMB_MCMD_MRUN_Msk);
}/* I2CSMBx_StartMaster */

/******************************************************************************/
/** I2CSMBx_MasterCmdRegReadCntSet function.
 * This function programs the readcount in the master command register
 * @return readCount - readcount value
 * @param None
*******************************************************************************/
void I2CSMBx_MasterCmdRegReadCntSet(SMB_INSTANCE smbInstance, const uint8_t readCount)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Program the Read count in the Master Command Register */
    smb_regs->SMB_MCMD[0] |= (smb_regs->SMB_MCMD[0] & ~SMB_MCMD_RD_CNT_Msk) | SMB_MCMD_RD_CNT(readCount);

}/* I2CSMBx_MasterCmdRegReadCntSet */

/******************************************************************************/
/** I2CSMBx_MasterCmdRegWriteCntSet function.
 * This function programs the writeCount in the master command register
 * @return writeCount - writeCount value
 * @param None
*******************************************************************************/
void I2CSMBx_MasterCmdRegWriteCntSet(SMB_INSTANCE smbInstance, const uint8_t writeCount)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Program the Write count in the Master Command Register */
    smb_regs->SMB_MCMD[0] |= (smb_regs->SMB_MCMD[0] & ~SMB_MCMD_WR_CNT_Msk) | SMB_MCMD_WR_CNT(writeCount);

}/* I2CSMBx_MasterCmdRegWriteCntSet */

/******************************************************************************/
/** I2CSMBx_MasterProceed function.
 * This function sets the PROCEED bit in master command register
 * @param None
 * @return None
*******************************************************************************/
void I2CSMBx_MasterProceed(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Set the Proceed bit in the Master Command Register */
    smb_regs->SMB_MCMD[0] |= SMB_MCMD_MPROCEED_Msk;
}/* I2CSMBx_MasterProceed */

/******************************************************************************/
/** I2CSMBx_MasterRun function.
 * This function sets the PROCEED bit and MRUN in master command register
 * @param None
 * @return None
*******************************************************************************/
void I2CSMBx_MasterRun(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_MCMD[0] |= SMB_MCMD_MRUN_Msk;
}/* I2CSMBx_MasterRun  */

/******************************************************************************/
/** I2CSMBx_MasterCmdSet function.
 * This function programs the master command register value
 * @param cmdValue Master command value
 * @return None
*******************************************************************************/
void I2CSMBx_MasterCmdSet(SMB_INSTANCE smbInstance, const uint8_t cmdValue)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_MCMD[0] = cmdValue;
}/* I2CSMBx_MasterCmdSet */

/******************************************************************************/
/** I2CSMBx_MdoneEnable function.
 * This function enables MDONE interrupt
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MdoneEnable(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_ENMI_Msk;
}/* I2CSMBx_MdoneEnable */

/******************************************************************************/
/** I2CSMBx_MdoneDisable function.
 * This function disables MDONE interrupt
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MdoneDisable(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] &= ~SMB_CFG_ENMI_Msk;
}/* I2CSMBx_MdoneDisable */

/** I2CSMBx_SdoneEnable function.
 * This function enables SDONE interrupt
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SdoneEnable(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_ENSI_Msk;
}/* I2CSMBx_SdoneEnable  */

/******************************************************************************/
/** I2CSMBx_SdoneDisable function.
 * This function disables SDONE interrupt
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SdoneDisable(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] &= ~SMB_CFG_ENSI_Msk;
}/* I2CSMBx_SdoneDisable */

/******************************************************************************/
/** I2CSMBx_OwnSlaveAddrSet function.
 * This function sets the own address in the own address register
 * @param value - the own address value
 * @return None
*******************************************************************************/
void I2CSMBx_OwnSlaveAddrSet(SMB_INSTANCE smbInstance, const uint16_t value)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_OWN_ADDR = value;
}/* I2CSMBx_OwnSlaveAddrSet */

/******************************************************************************/
/** I2CSMBx_ClkValueSet function.
 * This function sets the clock value in the Bus clk register
 * @param value - the clock value
 * @return None
*******************************************************************************/
void I2CSMBx_ClkValueSet(SMB_INSTANCE smbInstance, const uint16_t value)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_BUSCLK = value;
}/* I2CSMBx_ClkValueSet */

/******************************************************************************/
/** I2CSMBx_TimeoutScalingValueSet function.
 * This function sets the value in the Timeout Scaling Register
 * @param value - the timeout Scaling value
 * @return None
*******************************************************************************/
void I2CSMBx_TimeoutScalingValueSet(SMB_INSTANCE smbInstance, const uint32_t value)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_TMOUTSC = value;
}/* I2CSMBx_TimeoutScalingValueSet */

/******************************************************************************/
/** I2CSMBx_RepeatedStartHoldTimeValSet function.
 * This function sets the value in the Data Timing 2 Register
 * @param value - the timeout Scaling value
 * @return None
*******************************************************************************/
void I2CSMBx_RepeatedStartHoldTimeValSet(SMB_INSTANCE smbInstance, const uint32_t value)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_RSHTM = value;
}/* I2CSMBx_RepeatedStartHoldTimeValSet */

/******************************************************************************/
/** I2CSMBx_TimeoutsEnable function.
 * This function enables timeouts
 * @param None
 * @return None
*******************************************************************************/
void I2CSMBx_TimeoutsEnable(SMB_INSTANCE smbInstance, const uint8_t timeoutsFlag)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_COMPL[0] = (smb_regs->SMB_COMPL[0] & 0xFFFFFF00U) | timeoutsFlag;
    smb_regs->SMB_CFG[0] |= SMB_CFG_TCEN_Msk;
}

/******************************************************************************/
/** I2CSMBx_PortSet function.
 * This function sets the smbus port
 * @param port the port to configure
 * @return None
*******************************************************************************/
void I2CSMBx_PortSet(SMB_INSTANCE smbInstance, const uint8_t port)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] = (smb_regs->SMB_CFG[0] & ~SMB_CFG_PORT_SEL_Msk) | SMB_CFG_PORT_SEL(port);
}/* I2CSMBx_PortSet */

/******************************************************************************/
/** I2CSMBx_PortGet function.
 * This function returns the port that is configured
 * @param None
 * @return port - port that is configured
*******************************************************************************/
uint8_t I2CSMBx_PortGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint8_t)(smb_regs->SMB_CFG[0] & SMB_CFG_PORT_SEL_Msk);

}/* I2CSMBx_PortGet */


/******************************************************************************/
/** I2CSMBx_IsBusErrorSet function.
 * This function returns TRUE if BER bit is set, else FALSE
 * @param None
 * @return TRUE/FALSE
*******************************************************************************/
bool I2CSMBx_IsBusErrorSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_BER_Msk) > 0U);

}/* I2CSMBx_IsBusErrorSet */

/******************************************************************************/
/** I2CSMBx_IsMdoneSet function.
 * This function return TRUE if MDONE is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsMdoneSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (((smb_regs->SMB_CFG[0] & SMB_CFG_ENMI_Msk) != 0U) && ((smb_regs->SMB_COMPL[0] & SMB_COMPL_MDONE_Msk) != 0U));

}/* I2CSMBx_IsMdoneSet */

/******************************************************************************/
/** I2CSMBx_IsSdoneSet function.
 * This function returns TRUE if SDONE bit is set, else FALSE
 * @return None
 * @param None
*******************************************************************************/
bool I2CSMBx_IsSdoneSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (((smb_regs->SMB_CFG[0] & SMB_CFG_ENSI_Msk) != 0U) && ((smb_regs->SMB_COMPL[0] & SMB_COMPL_SDONE_Msk) != 0U));

}/* I2CSMBx_IsSdoneSet  */

/******************************************************************************/
/** I2CSMBx_IsLABSet function.
 * This function returns TRUE if LAB bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsLABSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_LAB_Msk) > 0U);
}/* I2CSMBx_IsLABSet */

/******************************************************************************/
/** I2CSMBx_IsMNAKXSet function.
 * This function returns TRUE if MNAKX (master nack) bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsMNAKXSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_MNAKX_Msk) > 0U);
}/* I2CSMBx_IsMNAKXSet */

/******************************************************************************/
/** I2CSMBx_IsSNAKRSet function.
 * This function returns TRUE if SNAKR (slave nack) bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsSNAKRSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_SNAKR_Msk) > 0U);

}/* I2CSMBx_IsSNAKRSet */

/******************************************************************************/
/** I2CSMBx_IsSTRSet function.
 * This function returns TRUE if STR bit is set, else FALSE
 * @return None
 * @param None
*******************************************************************************/
bool I2CSMBx_IsSTRSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_STR_Msk) > 0U);

}/* I2CSMBx_IsSTRSet */

 /******************************************************************************/
/** I2CSMBx_IsRepeatWriteSet function.
 * This function returns TRUE if REPEAT_WRITE bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsRepeatWriteSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_REP_WR_Msk) > 0U);

}/* I2CSMBx_IsRepeatWriteSet */

/******************************************************************************/
/** I2CSMBx_IsRepeatReadSet function.
 * This function returns TRUE if REPEAT_READ bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsRepeatReadSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_REP_RD_Msk) > 0U);

}/* I2CSMBx_IsRepeatReadSet */

/******************************************************************************/
/** I2CSMBx_IsMTRSet function.
 * This function returns TRUE if MTR (master xmit) bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsMTRSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_MTR_Msk) > 0U);

}/* I2CSMBx_IsMTRSet */

/******************************************************************************/
/** I2CSMBx_IsTimerErrorSet function.
 * This function returns TRUE if TIMERR bit is set, else FALSE
 * @return TRUE/FALSE
 * @param None
*******************************************************************************/
bool I2CSMBx_IsTimerErrorSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return ((smb_regs->SMB_COMPL[0] & SMB_COMPL_TIMERR_Msk) > 0U);

}/* I2CSMBx_IsTimerErrorSet */


/******************************************************************************/
/** I2CSMBx_MRUNSet function.
 * This function sets the MRUN bit
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MRUNSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_MCMD[0] |= SMB_MCMD_MRUN_Msk;
}/* I2CSMBx_MRUNSet */

/******************************************************************************/
/** I2CSMBx_MRUNClr function.
 * This function clears MRUN bit
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MRUNClr(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_MCMD[0] &= ~SMB_MCMD_MRUN_Msk;
}/* I2CSMBx_MRUNClr */

/******************************************************************************/
/** I2CSMBx_SRUNSet function.
 * This function sets SRUN bit
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SRUNSet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_SCMD[0] |= SMB_SCMD_SRUN_Msk;
}/* I2CSMBx_SRUNSet */

/******************************************************************************/
/** I2CSMBx_SRUNClr function.
 * This function clears the SRUN bit
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SRUNClr(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_SCMD[0] &= ~SMB_SCMD_SRUN_Msk;
}/* I2CSMBx_SRUNClr */

/******************************************************************************/
/** I2CSMBx_ClrAllCompletionStatus function.
 * This function initializes the smbus base
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_ClrAllCompletionStatus(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    /* Clear LAB and BER status */
    smb_regs->SMB_COMPL[0] = (SMB_COMPL_LAB_Msk | SMB_COMPL_BER_Msk);
    /* clr_master_completion_status() */
    smb_regs->SMB_COMPL[0] = (SMB_COMPL_MDONE_Msk | SMB_COMPL_MNAKX_Msk);
    /* clr_slave_completion_status() */
    smb_regs->SMB_COMPL[0] = (SMB_COMPL_SDONE_Msk | SMB_COMPL_SNAKR_Msk | SMB_COMPL_SPROT_Msk | SMB_COMPL_REP_RD_Msk | SMB_COMPL_REP_WR_Msk);

}/* I2CSMBx_ClrAllCompletionStatus */

/******************************************************************************/
/** I2CSMBx_ClrMasterCompletionStatus function.
 * This function clears the master completion status bits
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_ClrMasterCompletionStatus(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_COMPL[0] = (SMB_COMPL_MDONE_Msk | SMB_COMPL_MNAKX_Msk);
}/* I2CSMBx_ClrMasterCompletionStatus */

/*****************************************************************************/
/** I2CSMBx_ClrLABCompletionStatus function.
 * This function clears the LAB bit in the completion register
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_ClrLABCompletionStatus(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_COMPL[0] = SMB_COMPL_LAB_Msk;
}/* I2CSMBx_ClrLABCompletionStatus */

/******************************************************************************/
/** I2CSMBx_ClrSlaveCompletionStatus function.
 * This function clears all slave completion status
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_ClrSlaveCompletionStatus(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_COMPL[0] = (SMB_COMPL_SDONE_Msk | SMB_COMPL_SNAKR_Msk | SMB_COMPL_SPROT_Msk | SMB_COMPL_REP_RD_Msk | SMB_COMPL_REP_WR_Msk);
}/* I2CSMBx_ClrSlaveCompletionStatus */

/******************************************************************************/
/** I2CSMBx_ClrBERStatus function.
 * This function clears BER status bit in completion register
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_ClrBERStatus(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_COMPL[0] = SMB_COMPL_BER_Msk;
}/* I2CSMBx_ClrBERStatus */

/******************************************************************************/
/** I2CSMBx_SlaveTxBufferFlush function.
 * This function clears the slave tx buffer
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SlaveTxBufferFlush(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_FLUSH_SXBUF_Msk;
}/* I2CSMBx_SlaveTxBufferFlush */

/******************************************************************************/
/** I2CSMBx_SlaveRxBufferFlush function.
 * This function clears the slave rx buffer
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_SlaveRxBufferFlush(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_FLUSH_SRBUF_Msk;
}/* I2CSMBx_SlaveRxBufferFlush */

/******************************************************************************/
/** I2CSMBx_MasterTxBufferFlush function.
 * This function clears the master tx buffer
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MasterTxBufferFlush(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_FLUSH_MXBUF_Msk;
}/* I2CSMBx_MasterTxBufferFlush */

/******************************************************************************/
/** I2CSMBx_MasterRxBufferFlush function.
 * This function clears the master rx buffer
 * @return None
 * @param None
*******************************************************************************/
void I2CSMBx_MasterRxBufferFlush(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    smb_regs->SMB_CFG[0] |= SMB_CFG_FLUSH_MRBUF_Msk;

}/* I2CSMBx_MasterRxBufferFlush */

/******************************************************************************/
/** I2CSMBx_SlaveReadCountGet function.
 * This function return read count programmed in slave command register
 * @return None
 * @param None
*******************************************************************************/
uint8_t I2CSMBx_SlaveReadCountGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint8_t)((smb_regs->SMB_SCMD[0] & SMB_SCMD_RD_CNT_Msk) >> SMB_SCMD_RD_CNT_Pos);
}/* I2CSMBx_SlaveReadCountGet */

/******************************************************************************/
/** I2CSMBx_MasterWriteCountGet function.
 * This function returns the write count programmed in the master command register
 * @return None
 * @param None
*******************************************************************************/
uint8_t I2CSMBx_MasterWriteCountGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint8_t)((smb_regs->SMB_MCMD[0] & SMB_MCMD_WR_CNT_Msk) >> SMB_MCMD_WR_CNT_Pos);
}/* I2CSMBx_MasterWriteCountGet */

/******************************************************************************/
/** I2CSMBx_MasterReadCountGet function.
 * This function returns the read count programmed in the master command register
 * @return None
 * @param None
*******************************************************************************/
uint8_t I2CSMBx_MasterReadCountGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint8_t)((smb_regs->SMB_MCMD[0] & SMB_MCMD_RD_CNT_Msk) >> SMB_MCMD_RD_CNT_Pos);
}/* I2CSMBx_MasterReadCountGet  */

/******************************************************************************/
/** I2CSMBx_SlaveRxBufferAddrGet function.
 * This function returns the address of slave rx buffer
 * @return None
 * @param None
*******************************************************************************/
uint32_t I2CSMBx_SlaveRxBufferAddrGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint32_t)(&smb_regs->SMB_SLV_RXB);
}/* I2CSMBx_SlaveRxBufferAddrGet  */

/******************************************************************************/
/** I2CSMBx_SlaveTxBufferAddrGet function.
 * This function returns the address of slave tx buffer
 * @return None
 * @param None
*******************************************************************************/
uint32_t I2CSMBx_SlaveTxBufferAddrGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint32_t)(&smb_regs->SMB_SLV_TXB);
}/* I2CSMBx_SlaveTxBufferAddrGet */

/******************************************************************************/
/** I2CSMBx_MasterRxBufferAddrGet function.
 * This function returns the address of master rx buffer
 * @return None
 * @param None
*******************************************************************************/
uint32_t I2CSMBx_MasterRxBufferAddrGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint32_t)(&smb_regs->SMB_MTR_RXB);
}/* I2CSMBx_MasterRxBufferAddrGet */

/******************************************************************************/
/** I2CSMBx_MasterTxBufferAddrGet function.
 * This function returns the address of master tx buffer
 * @return None
 * @param None
*******************************************************************************/
uint32_t I2CSMBx_MasterTxBufferAddrGet(SMB_INSTANCE smbInstance)
{
    smb_registers_t* smb_regs = smbInstanceGet(smbInstance);

    return (uint32_t)(&smb_regs->SMB_MTR_TXB);
}/* I2CSMBx_MasterTxBufferAddrGet */


