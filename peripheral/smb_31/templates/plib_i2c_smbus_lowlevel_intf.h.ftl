/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_i2c_smbus_lowlevel_intf.h

  Summary:
    I2C PLIB Master-Slave Mode Common Header file

  Description:
    This file defines the interface to the I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_SMB_LOWLEVEL_INTF_H
#define PLIB_SMB_LOWLEVEL_INTF_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
//----------------------------------------------------------------------

#define I2CSMB_BUS_SPEED_100KHZ 0
#define I2CSMB_BUS_SPEED_400KHZ 1
#define I2CSMB_BUS_SPEED_1MHZ 2

typedef uint32_t I2CSMB_BUS_SPEED;

// SMBUS TIMING Values
//-----------------------------------------------------------------------------------------
//SMBus Baud Clock configuration

#define I2CSMB_BAUD_CLK_8MHZ 0
#define I2CSMB_BAUD_CLK_10MHZ 1
#define I2CSMB_BAUD_CLK_16MHZ 2

//Define and enable the actual baud clock option as per hardware
#define I2CSMB_BAUD_CLK I2CSMB_BAUD_CLK_16MHZ
//#define I2CSMB_BAUD_CLK I2CSMB_BAUD_CLK_10MHZ
//#define I2CSMB_BAUD_CLK I2CSMB_BAUD_CLK_8MHZ


//-----------------------------------------------------------------------------------------
// SMBUS TIMING Values

#if (I2CSMB_BAUD_CLK == I2CSMB_BAUD_CLK_16MHZ)
    /* SMBus Timing values for 1MHz Speed */
    #define SPD_1MHZ_BUS_CLOCK 0x0509
    #define SPD_1MHZ_DATA_TIMING 0x06060601     //As per 16 MHz Baud Clock
    #define SPD_1MHZ_DATA_TIMING_2 0x06
    #define SPD_1MHZ_IDLE_SCALING 0x01000050    //As per 16 MHz Baud Clock
    #define SPD_1MHZ_TIMEOUT_SCALING 0x149CC2C7

    //Add Values for 100Khz and 400Khz as per 16Mhz baud clock
    #define SPD_400KHZ_BUS_CLOCK 0x0F17
    #define SPD_400KHZ_DATA_TIMING 0x040A0A06     //As per 16 MHz Baud Clock
    #define SPD_400KHZ_DATA_TIMING_2 0x0A
    #define SPD_400KHZ_IDLE_SCALING 0x01000050    //As per 16 MHz Baud Clock
    #define SPD_400KHZ_TIMEOUT_SCALING 0x159CC2C7

    #define SPD_100KHZ_BUS_CLOCK 0x4F4F
    #define SPD_100KHZ_DATA_TIMING 0x0C4D5006     //As per 16 MHz Baud Clock
    #define SPD_100KHZ_DATA_TIMING_2 0x4D
    #define SPD_100KHZ_IDLE_SCALING 0x01FC01ED    //As per 16 MHz Baud Clock
    #define SPD_100KHZ_TIMEOUT_SCALING 0x4B9CC2C7

#elif (I2CSMB_BAUD_CLK == SMB_BAUD_CLK_10MHZ)

    #define SPD_400KHZ_BUS_CLOCK 0x0A0D
    #define SPD_400KHZ_DATA_TIMING 0x03080804     //As per 10 MHz Baud Clock
    #define SPD_400KHZ_IDLE_SCALING 0x00A00032    //As per 10 MHz Baud Clock
    #define SPD_400KHZ_TIMEOUT_SCALING 0x0A9DC4C8
    #define SPD_400KHZ_DATA_TIMING_2 0x07

    #define SPD_100KHZ_BUS_CLOCK 0x3131
    #define SPD_100KHZ_DATA_TIMING 0x072A3104      //As per 10 MHz Baud Clock
    #define SPD_100KHZ_IDLE_SCALING 0x01400136     //As per 10 MHz Baud Clock
    #define SPD_100KHZ_TIMEOUT_SCALING 0x30C6F5FB
    #define SPD_100KHZ_DATA_TIMING_2 0x2B

#else //(I2CSMB_BAUD_CLK == SMB_BAUD_CLK_8MHZ)
    /* For 8MHz baud clock, set the high & low period to 10,
     * therefore 8M/(10+10) = 400khz */
    #define SPD_400KHZ_BUS_CLOCK 0x080a
    #define SPD_400KHZ_DATA_TIMING 0x02060603      //As per 8 MHz Baud Clock
    /* T_Idle_Delay = 17us, T_Idle_Window = 6us */
    #define SPD_400KHZ_IDLE_SCALING 0x0084002A     //As per 8 MHz Baud Clock
    #define SPD_400KHZ_TIMEOUT_SCALING 0x0A9DC4C8
    #define SPD_400KHZ_DATA_TIMING_2 0x05

    /* For 8MHz baud clock, set the high & low period to 40,
     * therefore 8M/(40+40) = 100khz */
    #define SPD_100KHZ_BUS_CLOCK 0x2727
    #define SPD_100KHZ_DATA_TIMING 0x05222703      //As per 8 MHz Baud Clock
    /* T_Idle_Delay = 32us, T_Idle_Window = 31us */
    #define SPD_100KHZ_IDLE_SCALING 0x010000F8     //As per 8 MHz Baud Clock

    /* Bus Idle Min(Byte3 of Time-Out Scaling Register) = 4.7us
     * Master Cum Time Out(Byte2 of Time-Out Scaling Register) = 10ms
     * Slave Cum Time Out(Byte1 of Time-Out Scaling Register) = 25ms
     * Clock High Time Out(Byte 0 of Time-Out Scaling Register) = 50us
     */
    #define SPD_100KHZ_TIMEOUT_SCALING 0x269DC4C8
#endif

typedef enum
{
<#list 0..I2C_NUM_SMBUS_INSTANCES-1 as i>
    SMB_INSTANCE${i} = ${i},
</#list>
} SMB_INSTANCE;

/*
 * The following functions make up the methods (set of possible operations) of
 * this interface.
 */
void I2CSMBx_Reset(SMB_INSTANCE smbInstance);
void I2CSMBx_Enable(SMB_INSTANCE smbInstance, const uint16_t ownAddress, const uint8_t port, const uint8_t speed, const bool fairnessEnableFlag);
void I2CSMBx_StartSlave(SMB_INSTANCE smbInstance, const uint8_t read_count, const uint8_t write_count, const bool pecFlag);
void I2CSMBx_TimingInit(SMB_INSTANCE smbInstance, const uint8_t speed, const bool fairnessEnable);
void I2CSMBx_FlushHwTxRxBuffers(SMB_INSTANCE smbInstance);
void I2CSMBx_StartMaster(SMB_INSTANCE smbInstance, const uint32_t master_command);
void I2CSMBx_MasterCmdRegReadCntSet(SMB_INSTANCE smbInstance, const uint8_t readCount);
void I2CSMBx_MasterCmdRegWriteCntSet(SMB_INSTANCE smbInstance, const uint8_t writeCount);
void I2CSMBx_MasterProceed(SMB_INSTANCE smbInstance);
void I2CSMBx_MasterRun(SMB_INSTANCE smbInstance);
void I2CSMBx_MasterCmdSet(SMB_INSTANCE smbInstance, const uint8_t cmdValue);
void I2CSMBx_MdoneEnable(SMB_INSTANCE smbInstance);
void I2CSMBx_MdoneDisable(SMB_INSTANCE smbInstance);
void I2CSMBx_SdoneEnable(SMB_INSTANCE smbInstance);
void I2CSMBx_SdoneDisable(SMB_INSTANCE smbInstance);
void I2CSMBx_OwnSlaveAddrSet(SMB_INSTANCE smbInstance, const uint16_t value);
void I2CSMBx_ClkValueSet(SMB_INSTANCE smbInstance, const uint16_t value);
void I2CSMBx_TimeoutScalingValueSet(SMB_INSTANCE smbInstance, const uint32_t value);
void I2CSMBx_RepeatedStartHoldTimeValSet(SMB_INSTANCE smbInstance, const uint32_t value);
void I2CSMBx_TimeoutsEnable(SMB_INSTANCE smbInstance, const uint8_t timeoutsFlag);
void I2CSMBx_PortSet(SMB_INSTANCE smbInstance, const uint8_t port);
uint8_t I2CSMBx_PortGet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsBusErrorSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsMdoneSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsSdoneSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsLABSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsMNAKXSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsSNAKRSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsSTRSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsRepeatWriteSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsRepeatReadSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsMTRSet(SMB_INSTANCE smbInstance);
bool I2CSMBx_IsTimerErrorSet(SMB_INSTANCE smbInstance);
void I2CSMBx_MRUNSet(SMB_INSTANCE smbInstance);
void I2CSMBx_MRUNClr(SMB_INSTANCE smbInstance);
void I2CSMBx_SRUNSet(SMB_INSTANCE smbInstance);
void I2CSMBx_SRUNClr(SMB_INSTANCE smbInstance);
void I2CSMBx_ClrAllCompletionStatus(SMB_INSTANCE smbInstance);
void I2CSMBx_ClrMasterCompletionStatus(SMB_INSTANCE smbInstance);
void I2CSMBx_ClrLABCompletionStatus(SMB_INSTANCE smbInstance);
void I2CSMBx_ClrSlaveCompletionStatus(SMB_INSTANCE smbInstance);
void I2CSMBx_ClrBERStatus(SMB_INSTANCE smbInstance);
void I2CSMBx_SlaveTxBufferFlush(SMB_INSTANCE smbInstance);
void I2CSMBx_SlaveRxBufferFlush(SMB_INSTANCE smbInstance);
void I2CSMBx_MasterTxBufferFlush(SMB_INSTANCE smbInstance);
void I2CSMBx_MasterRxBufferFlush(SMB_INSTANCE smbInstance);
uint8_t I2CSMBx_SlaveReadCountGet(SMB_INSTANCE smbInstance);
uint8_t I2CSMBx_MasterWriteCountGet(SMB_INSTANCE smbInstance);
uint8_t I2CSMBx_MasterReadCountGet(SMB_INSTANCE smbInstance);
uint32_t I2CSMBx_SlaveRxBufferAddrGet(SMB_INSTANCE smbInstance);
uint32_t I2CSMBx_SlaveTxBufferAddrGet(SMB_INSTANCE smbInstance);
uint32_t I2CSMBx_MasterRxBufferAddrGet(SMB_INSTANCE smbInstance);
uint32_t I2CSMBx_MasterTxBufferAddrGet(SMB_INSTANCE smbInstance);






// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SMB_LOWLEVEL_INTF_H */