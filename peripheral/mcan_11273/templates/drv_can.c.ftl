/*******************************************************************************
  CAN Driver Functions for Static Single Instance Driver

  Company:
    Microchip Technology Inc.

  File Name:
    drv_can${INDEX}.c

  Summary:
    CAN driver implementation for the static single instance driver.

  Description:
    The CAN device driver provides a simple interface to manage the CAN
    modules on Microchip microcontrollers.

  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.
    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END
// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include "${__PROCESSOR}.h"
#include "drv_can${INDEX}.h"

<#assign USE_INTERRUPTS = 
    (INT_RXF0_NEW_ENTRY!false) ||
    (INT_RXF0_WATERMARK!false) ||
    (INT_RXF1_NEW_ENTRY!false) ||
    (INT_RXF1_WATERMARK!false) ||
    (INT_TX_COMPLETED!false)   ||
    (INT_TX_FIFO_EMPTY!false)  ||
    (INT_TX_FIFO_WATERMARK!false) ||
    (INT_TIMEOUT!false)
>

/* define the constants for this CAN instance */
#define MCAN${INDEX} MCAN${INDEX}_REGS

    <#switch CAN_OPMODE>
    <#default>
    <#case "NORMAL">
    /* CAN operation is set to normal mode */
#define CONF_CAN${INDEX}_CCCR (MCAN_CCCR_ASM_NORMAL<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_CAN${INDEX}_TEST 0x00
    <#break>
    <#case "CONFIGURATION">
    /* CAN operation is set to configuration mode */
#define CONF_CAN${INDEX}_CCCR MCAN_CCCR_INIT_ENABLED
#define CONF_CAN${INDEX}_TEST 0x00
    <#break>
    <#case "FD">
    /* CAN operation is set to FD mode */
#define CONF_CAN${INDEX}_CCCR (MCAN_CCCR_FDOE_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_CAN${INDEX}_TEST 0x00
    <#break>
    <#case "RESTRICTED">
    /* CAN operation is set to restricted mode */
#define CONF_CAN${INDEX}_CCCR MCAN_CCCR_ASM_RESTRICTED
#define CONF_CAN${INDEX}_TEST 0x00
    <#break>
    <#case "MONITOR">
    /* CAN operation is set to monitor mode */
#define CONF_CAN${INDEX}_CCCR (MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_CAN${INDEX}_TEST 0x00
    <#break>
    <#case "EXT LOOPBACK">
    /* CAN operation is set to external loopback mode */
#define CONF_CAN${INDEX}_CCCR (MCAN_CCCR_TEST_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_CAN${INDEX}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    <#case "INT LOOPBACK">
    /* CAN operation is set to internal loopback mode */
#define CONF_CAN${INDEX}_CCCR (MCAN_CCCR_TEST_ENABLED | MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_CAN${INDEX}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    </#switch>

#define CONF_CAN${INDEX}_GFC (${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | MCAN_GFC_RRFS_REJECT</#if><#if FILTERS_EXT_REJECT> | MCAN_GFC_RRFE_REJECT</#if>)

<#if CAN_OPMODE =="FD">
/* configure the FD constants */
#define CONF_CAN${INDEX}_FBTP (${FBTP_FSJW} | (${FBTP_FTSEG1} << 8) | (${FBTP_FTSEG2} << 4) | (${FBTP_FBRP} << 16))
</#if>
/* configure the 'Normal' constants */
#define CONF_CAN${INDEX}_BTP  (${BTP_SJW} | (${BTP_TSEG1} << 8) | (${BTP_TSEG2} << 4) | (${BTP_BRP} << 16))
<#if USE_INTERRUPTS == true>

#define CONF_CAN${INDEX}_IE 0x00 \
<#if INT_TX_COMPLETED!false>
    | MCAN_IE_TCE_Msk\
</#if>
<#if INT_TX_FIFO_EMPTY!false>
    | MCAN_IE_TFEE_Msk\
</#if>
<#if INT_TX_FIFO_WATERMARK!false>
    | MCAN_IE_TEFWE_Msk\
</#if>
<#if INT_TIMEOUT!false>
    | MCAN_IE_TOOE_Msk\
</#if>
<#if INT_RXF0_NEW_ENTRY!false>
    | MCAN_IE_RF0NE_Msk\
</#if>
<#if INT_RXF0_WATERMARK!false>
    | MCAN_IE_RF0WE_Msk\
</#if>
<#if INT_RXF1_NEW_ENTRY!false>
    | MCAN_IE_RF1NE_Msk\
</#if>
<#if INT_RXF1_WATERMARK!false>
    | MCAN_IE_RF1WE_Msk
</#if>
/* end of IE config */
</#if>

#define CONF_CAN${INDEX}_TSCC (${TIMESTAMP_MODE} | MCAN_TSCC_TCP(${TIMESTAMP_PRESCALER}))
<#if CAN_TIMEOUT>
#define CONF_CAN${INDEX}_TOCC (${TIMEOUT_SELECT} | MCAN_TOCC_ETOC_TOS_CONTROLLED)
#define CONF_CAN${INDEX}_TOCV MCAN_TOCV_TOC(${TIMEOUT_COUNT})

</#if>
/* Configuration for the bytes in each element of RX FIFOs */
#define CONF_CAN${INDEX}_RXESC (0<#if RXF0_USE> | MCAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | MCAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if>)
<#if RXF0_USE>
<#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
<#if RXF0_BYTES_CFG?number < 5>
  <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
<#else>
  <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
</#if>
#define CONF_CAN${INDEX}_RXF0C (MCAN_RXF0C_F0S(${RXF0_ELEMENTS}) | MCAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | MCAN_RXF0C_F0OM_Msk</#if>)
static uint8_t can${INDEX}_rx0_fifo[${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if RXF1_USE>
<#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
<#if RXF1_BYTES_CFG?number < 5>
  <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
<#else>
  <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
</#if>

#define CONF_CAN${INDEX}_RXF1C (MCAN_RXF1C_F1S(${RXF1_ELEMENTS}) | MCAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | MCAN_RXF1C_F1OM_Msk</#if>)
static uint8_t can${INDEX}_rx1_fifo[${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if TX_USE>
<#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
<#if TX_FIFO_BYTES_CFG?number < 5>
  <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
<#else>
  <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
</#if>

#define CONF_CAN${INDEX}_TXESC (MCAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG}))
#define CONF_CAN${INDEX}_TXBC  MCAN_TXBC_TFQS(${TX_FIFO_ELEMENTS})
#define CONF_CAN${INDEX}_TXEFC (MCAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | MCAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}))

static uint8_t can${INDEX}_tx_fifo[${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}]__attribute__((aligned (4)));
static struct _can_tx_event_entry can${INDEX}_tx_event_fifo[${TX_FIFO_ELEMENTS}]__attribute__((aligned (4)));

</#if>
<#if FILTERS_STD?number gt 0>
#define CONF_CAN${INDEX}_SIDFC_LSS (${FILTERS_STD})
#define CONF_CAN${INDEX}_SIDF  (MCAN_SIDFC_LSS(CONF_CAN${INDEX}_SIDFC_LSS))
<#assign numInstance=FILTERS_STD?number>
__attribute__((aligned (4)))static struct _can_standard_message_filter_element
        can${INDEX}_std_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .S0.val = MCAN_SMF_SFT(${.vars["CAN${INDEX}_STD_FILTER${idx}_TYPE"]}) |
                  MCAN_SMF_SFID1(${.vars["CAN${INDEX}_STD_FILTER${idx}_SFID1"]}) |
                  MCAN_SMF_SFID2(${.vars["CAN${INDEX}_STD_FILTER${idx}_SFID2"]}) |
                  MCAN_SMF_SFEC(${.vars["CAN${INDEX}_STD_FILTER${idx}_CONFIG"]}),
    },
     </#list>
};


</#if>
<#if FILTERS_EXT?number gt 0>
#define CONF_CAN${INDEX}_XIDFC_LSE (${FILTERS_EXT})
#define CONF_CAN${INDEX}_XIDFC (MCAN_XIDFC_LSE(CONF_CAN${INDEX}_XIDFC_LSE))
#define CONF_CAN${INDEX}_XIDAM 0x1FFFFFFF

<#assign numInstance=FILTERS_EXT?number>
__attribute__((aligned (4)))static struct _can_extended_message_filter_element
    can${INDEX}_ext_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .F0.val = MCAN_EFID1(${.vars["CAN${INDEX}_EXT_FILTER${idx}_EFID1"]}) | MCAN_EFEC(${.vars["CAN${INDEX}_EXT_FILTER${idx}_CONFIG"]}),
        .F1.val = MCAN_EFID2(${.vars["CAN${INDEX}_EXT_FILTER${idx}_EFID2"]}) | MCAN_EFT(${.vars["CAN${INDEX}_EXT_FILTER${idx}_TYPE"]}),
    },
     </#list>
};


</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Instance ${INDEX} static driver functions
// *****************************************************************************
// *****************************************************************************
void DRV_CAN${INDEX}_Initialize(void)
{
    /* set INIT and CCE to get access to configuration registers */
    MCAN${INDEX}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((MCAN${INDEX}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;

    /* unlock the configuration registers */
    MCAN${INDEX}->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

    /*
    The following registers are cleared when MCAN_CCCR.CCE = 1
    > High Priority Message Status (MCAN_HPMS)
    > Receive FIFO 0 Status (MCAN_RXF0S)
    > Receive FIFO 1 Status (MCAN_RXF1S)
    > Transmit FIFO/Queue Status (MCAN_TXFQS)
    > Transmit Buffer Request Pending (MCAN_TXBRP)
    > Transmit Buffer Transmission Occurred (MCAN_TXBTO)
    > Transmit Buffer Cancellation Finished (MCAN_TXBCF)
    > Transmit Event FIFO Status (MCAN_TXEFS)
    */
<#if CAN_OPMODE =="FD">

    /* Fast Data Bit Timing and Prescaler Register */
    MCAN${INDEX}->MCAN_DBTP = CONF_CAN${INDEX}_FBTP;
</#if>

    /* Nominal Bit timing and Prescaler Register */
    MCAN${INDEX}->MCAN_NBTP  = CONF_CAN${INDEX}_BTP;

    /* Timestamp Counter Configuration Register */
    MCAN${INDEX}->MCAN_TSCC = CONF_CAN${INDEX}_TSCC;
<#if CAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    MCAN${INDEX}->MCAN_TOCC = CONF_CAN${INDEX}_TOCC;

    /* Timeout Counter Value Register */
    MCAN${INDEX}->MCAN_TOCV = CONF_CAN${INDEX}_TOCV;
</#if>
<#if RXF0_USE>

    /* Receive FIFO 0 Configuration Register */
    MCAN${INDEX}->MCAN_RXF0C = CONF_CAN${INDEX}_RXF0C |
            (((uint32_t)can${INDEX}_rx0_fifo) & 0xFFFF);
</#if>
<#if RXF1_USE>

    /* Receive FIFO 1 Configuration Register */
    MCAN${INDEX}->MCAN_RXF1C = CONF_CAN${INDEX}_RXF1C |
            (((uint32_t)can${INDEX}_rx1_fifo) & 0xFFFF);
</#if>
<#if RXF0_USE || RXF1_USE>

    /* Receive Buffer / FIFO Element Size Configuration Register */
    MCAN${INDEX}->MCAN_RXESC = CONF_CAN${INDEX}_RXESC;
</#if>
<#if TX_USE>

    /* Transmit Buffer Configuration Register */
    MCAN${INDEX}->MCAN_TXBC = CONF_CAN${INDEX}_TXBC |
            (((uint32_t)can${INDEX}_tx_fifo) & 0xFFFF);

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    MCAN${INDEX}->MCAN_TXESC = CONF_CAN${INDEX}_TXESC;

    /* Transmit Event FIFO Configuration Register */
    MCAN${INDEX}->MCAN_TXEFC = CONF_CAN${INDEX}_TXEFC |
            (((uint32_t)can${INDEX}_tx_event_fifo) & 0xFFFF);
</#if>

    /* Global Filter Configuration Register */
    MCAN${INDEX}->MCAN_GFC = CONF_CAN${INDEX}_GFC;
<#if FILTERS_STD?number gt 0>

    /* Standard ID Filter Configuration Register */
    MCAN${INDEX}->MCAN_SIDFC = CONF_CAN${INDEX}_SIDF |
            (((uint32_t)can${INDEX}_std_filter) & 0xFFFF);
</#if>
<#if FILTERS_EXT?number gt 0>

    /* Extended ID Filter Configuration Register */
    MCAN${INDEX}->MCAN_XIDFC = CONF_CAN${INDEX}_XIDFC |
            (((uint32_t)can${INDEX}_ext_filter) & 0xFFFF);

    /* Extended ID AND Mask Register */
    MCAN${INDEX}->MCAN_XIDAM = CONF_CAN${INDEX}_XIDAM;
</#if>

    /* Set the mode and config state */
    MCAN${INDEX}->MCAN_TEST = CONF_CAN${INDEX}_TEST;
    MCAN${INDEX}->MCAN_CCCR = CONF_CAN${INDEX}_CCCR;
<#if CAN_OPMODE != "CONFIGURATION">
    while ((MCAN${INDEX}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
<#if USE_INTERRUPTS == true>

    /* Enable the configured interrupts */
    MCAN${INDEX}->MCAN_IE = CONF_CAN${INDEX}_IE;
</#if>
}



void DRV_CAN${INDEX}_Deinitialize(void)
{
    MCAN${INDEX}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
}



void DRV_CAN${INDEX}_Open(void)
{
<#if CAN_OPMODE != "CONFIGURATION">
    MCAN${INDEX}->MCAN_CCCR = CONF_CAN${INDEX}_CCCR;
    while ((MCAN${INDEX}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
}



void DRV_CAN${INDEX}_Close(void)
{
    /* Switch the CAN module OFF */
<#if CAN_OPMODE != "CONFIGURATION">
    MCAN${INDEX}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((MCAN${INDEX}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;
</#if>
}



/* returns false on fail, true on success */
bool DRV_CAN${INDEX}_ChannelMessageTransmit(CAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
{
    (void)channelNum;
<#if !TX_USE>
    (void)address;
    (void)DLC;
    (void)message;
<#else>

    uint32_t tfqpi = MCAN_TXFQS_TFQPI(MCAN${INDEX}->MCAN_TXFQS);
    struct _can_tx_fifo_entry *fifo =
        (struct _can_tx_fifo_entry*) (can${INDEX}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});

    if (MCAN${INDEX}->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk)
    {
        /* The FIFO is full */
        return 0;
    }

    /* if the address is longer than 11 bits, we ASSUME it is extended */
    if (address > 0x7FF)
    {
        /* An extended identifier is stored into ID */
        fifo->T0 = address | MCAN_TXFE_XTD_Msk;
    }
    else
    {
        /* A standard identifier is stored into ID[28:18] */
        fifo->T0 = address << 18;
    }
<#if CAN_OPMODE =="FD">

    /* the length is a weird formula for FD DLC register */
    if (DLC <= 8)
    {
        fifo->T1 = MCAN_TXFE_DLC(DLC);
    }
    else if (DLC <= 12)
    {
        fifo->T1 = MCAN_TXFE_DLC(0x9);
    }
    else if (DLC <= 16)
    {
        fifo->T1 = MCAN_TXFE_DLC(0xA);
    }
    else if (DLC <= 20)
    {
        fifo->T1 = MCAN_TXFE_DLC(0xB);
    }
    else if (DLC <= 24)
    {
        fifo->T1 = MCAN_TXFE_DLC(0xC);
    }
    else if (DLC <= 32)
    {
        fifo->T1 = MCAN_TXFE_DLC(0xD);
    }
    else if (DLC <= 48)
    {
        fifo->T1 = MCAN_TXFE_DLC(0xE);
    }
    else
    {
        if (DLC > 64) DLC = 64;
        fifo->T1 = MCAN_TXFE_DLC(0xF);
    }
<#else>

    /* Limit DLC */
    if (DLC > 8) DLC = 8;
    fifo->T1 = MCAN_TXFE_DLC(DLC);
</#if>

    /* copy the message into the payload */
    memcpy(fifo->data, message, DLC);

    /* request the transmit */
    MCAN${INDEX}->MCAN_TXBAR = 1U << tfqpi;
</#if>

    return 1;
}



/* Channel is which FIFO to use. Only 2 max available */
bool DRV_CAN${INDEX}_ChannelMessageReceive(CAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
{
<#if RXF0_USE || RXF1_USE>
    uint32_t rxgi;
    struct _can_rx_fifo_entry *fifo = NULL;

    /* Read a message from the selected channel */
    switch (channelNum)
    {
        default:
<#if RXF0_USE>
        case 0:
            /* check and return 0 if nothing to be read */
            if ((MCAN${INDEX}->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk) == 0) return 0;

            /* read FIFO 0 */
            rxgi = (MCAN${INDEX}->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos;
            fifo = (struct _can_rx_fifo_entry*) (can${INDEX}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* ack the fifo position */
            MCAN${INDEX}->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            break;
</#if>

<#if RXF1_USE>
        case 1:
            /* check and return 0 if nothing to be read */
            if ((MCAN${INDEX}->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk) == 0) return 0;

            /* Read FIFO 1 */
            rxgi = (MCAN${INDEX}->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos;
            fifo = (struct _can_rx_fifo_entry*) (can${INDEX}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* ack the fifo position */
            MCAN${INDEX}->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
            break;
</#if>
    }

    memcpy(message, fifo->data, DLC);
    return 1;
<#else>
    return 0;
</#if>
}


<#if USE_INTERRUPTS == true>
/* One Interrupt handler for each CAN(MCAN) module - default to INT0 */
void MCAN${INDEX}_INT0_Handler( void )
{
    uint32_t ir = MCAN${INDEX}->MCAN_IR;
    <#if INT_TX_COMPLETED!false>

    /* TX Completed */
    if (ir & MCAN_IR_TC_Msk)
    {
        /* service the TX Completed interrupt here */
    }
    </#if>
    <#if INT_TX_FIFO_EMPTY!false>

    /* TX FIFO is empty */
    if (ir & MCAN_IR_TFE_Msk)
    {
        /* service the TX FIFO empty interrupt here */
    }
    </#if>
    <#if INT_RXF0_NEW_ENTRY!false>

    /* New Message in FIFO 0 */
    if (ir & MCAN_IR_RF0N_Msk)
    {
        /* service the New Entry for RX FIFO 0 here */
    }
    </#if>
    <#if INT_RXF0_WATERMARK!false>

    /* WATERMARK in FIFO 0 reached */
    if (ir & MCAN_IR_RF0W_Msk)
    {
        /* service the Watermark reached interrupt for RX FIFO 0 here */
    }
    </#if>
    <#if INT_RXF1_NEW_ENTRY!false>

    /* New Message in FIFO 1 */
    if (ir & MCAN_IR_RF1N_Msk)
    {
        /* service the New Entry for RX FIFO 1 here */
    }
    </#if>
    <#if INT_RXF1_WATERMARK!false>

    /* WATERMARK in FIFO 1 reached */
    if (ir & MCAN_IR_RF1W_Msk)
    {
        /* service the Watermark reached interrupt for RX FIFO 1 here */
    }
    </#if>
    <#if INT_TIMEOUT!false>

    /* Timeout */
    if (ir & MCAN_IR_TOO_Msk)
    {
        /* service the Timeout */
    }
    </#if>

    /* Clear all of the interrupts */
    MCAN${INDEX}->MCAN_IR = ir;
}
</#if>	


/*******************************************************************************
 End of File
*/
