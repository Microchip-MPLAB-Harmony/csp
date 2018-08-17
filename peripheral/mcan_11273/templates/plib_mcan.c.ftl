/*******************************************************************************
  Controller Area Network (MCAN) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcan${INDEX?string}.c

  Summary:
    MCAN source file.

  Description:
    None.

  Remarks:
    None.
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

#include "device.h"
#include "plib_mcan${INDEX?string}.h"

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

/* define the constants for this MCAN instance */
#define MCAN${INDEX?string} MCAN${INDEX?string}_REGS

    <#switch MCAN_OPMODE>
    <#default>
    <#case "NORMAL">
    /* MCAN operation is set to normal mode */
#define CONF_MCAN${INDEX?string}_CCCR (MCAN_CCCR_ASM_NORMAL<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_MCAN${INDEX?string}_TEST 0x00
    <#break>
    <#case "CONFIGURATION">
    /* MCAN operation is set to configuration mode */
#define CONF_MCAN${INDEX?string}_CCCR MCAN_CCCR_INIT_ENABLED
#define CONF_MCAN${INDEX?string}_TEST 0x00
    <#break>
    <#case "FD">
    /* MCAN operation is set to FD mode */
#define CONF_MCAN${INDEX?string}_CCCR (MCAN_CCCR_FDOE_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_MCAN${INDEX?string}_TEST 0x00
    <#break>
    <#case "RESTRICTED">
    /* MCAN operation is set to restricted mode */
#define CONF_MCAN${INDEX?string}_CCCR MCAN_CCCR_ASM_RESTRICTED
#define CONF_MCAN${INDEX?string}_TEST 0x00
    <#break>
    <#case "MONITOR">
    /* MCAN operation is set to monitor mode */
#define CONF_MCAN${INDEX?string}_CCCR (MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_MCAN${INDEX?string}_TEST 0x00
    <#break>
    <#case "EXT LOOPBACK">
    /* MCAN operation is set to external loopback mode */
#define CONF_MCAN${INDEX?string}_CCCR (MCAN_CCCR_TEST_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_MCAN${INDEX?string}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    <#case "INT LOOPBACK">
    /* MCAN operation is set to internal loopback mode */
#define CONF_MCAN${INDEX?string}_CCCR (MCAN_CCCR_TEST_ENABLED | MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_MCAN${INDEX?string}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    </#switch>

#define CONF_MCAN${INDEX?string}_GFC (${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | MCAN_GFC_RRFS_REJECT</#if><#if FILTERS_EXT_REJECT> | MCAN_GFC_RRFE_REJECT</#if>)

<#if MCAN_OPMODE =="FD">
/* configure the FD constants */
#define CONF_MCAN${INDEX?string}_FBTP (${FBTP_FSJW} | (${FBTP_FTSEG1} << 8) | (${FBTP_FTSEG2} << 4) | (${FBTP_FBRP} << 16))
</#if>
/* configure the 'Normal' constants */
#define CONF_MCAN${INDEX?string}_BTP  (${BTP_SJW} | (${BTP_TSEG1} << 8) | (${BTP_TSEG2} << 4) | (${BTP_BRP} << 16))
<#if USE_INTERRUPTS == true>

#define CONF_MCAN${INDEX?string}_IE 0x00 \
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

#define CONF_MCAN${INDEX?string}_TSCC (${TIMESTAMP_MODE} | MCAN_TSCC_TCP(${TIMESTAMP_PRESCALER}))
<#if MCAN_TIMEOUT>
#define CONF_MCAN${INDEX?string}_TOCC (${TIMEOUT_SELECT} | MCAN_TOCC_ETOC_TOS_CONTROLLED)
#define CONF_MCAN${INDEX?string}_TOCV MCAN_TOCV_TOC(${TIMEOUT_COUNT})

</#if>
/* Configuration for the bytes in each element of RX FIFOs */
#define CONF_MCAN${INDEX?string}_RXESC (0<#if RXF0_USE> | MCAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | MCAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if>)
<#if RXF0_USE>
<#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
<#if RXF0_BYTES_CFG?number < 5>
  <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
<#else>
  <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
</#if>
#define CONF_MCAN${INDEX?string}_RXF0C (MCAN_RXF0C_F0S(${RXF0_ELEMENTS}) | MCAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | MCAN_RXF0C_F0OM_Msk</#if>)
static uint8_t mcan${INDEX?string}_rx0_fifo[${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if RXF1_USE>
<#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
<#if RXF1_BYTES_CFG?number < 5>
  <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
<#else>
  <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
</#if>

#define CONF_MCAN${INDEX?string}_RXF1C (MCAN_RXF1C_F1S(${RXF1_ELEMENTS}) | MCAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | MCAN_RXF1C_F1OM_Msk</#if>)
static uint8_t mcan${INDEX?string}_rx1_fifo[${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if TX_USE>
<#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
<#if TX_FIFO_BYTES_CFG?number < 5>
  <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
<#else>
  <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
</#if>

#define CONF_MCAN${INDEX?string}_TXESC (MCAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG}))
#define CONF_MCAN${INDEX?string}_TXBC  MCAN_TXBC_TFQS(${TX_FIFO_ELEMENTS})
#define CONF_MCAN${INDEX?string}_TXEFC (MCAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | MCAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}))

static uint8_t mcan${INDEX?string}_tx_fifo[${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}]__attribute__((aligned (4)));
static struct _mcan_tx_event_entry mcan${INDEX?string}_tx_event_fifo[${TX_FIFO_ELEMENTS}]__attribute__((aligned (4)));

</#if>
<#if FILTERS_STD?number gt 0>
#define CONF_MCAN${INDEX?string}_SIDFC_LSS (${FILTERS_STD})
#define CONF_MCAN${INDEX?string}_SIDF  (MCAN_SIDFC_LSS(CONF_MCAN${INDEX?string}_SIDFC_LSS))
<#assign numInstance=FILTERS_STD?number>
__attribute__((aligned (4)))static struct _mcan_standard_message_filter_element
        mcan${INDEX?string}_std_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .S0.val = MCAN_SMF_SFT(${.vars["MCAN${INDEX?string}_STD_FILTER${idx}_TYPE"]}) |
                  MCAN_SMF_SFID1(${.vars["MCAN${INDEX?string}_STD_FILTER${idx}_SFID1"]}) |
                  MCAN_SMF_SFID2(${.vars["MCAN${INDEX?string}_STD_FILTER${idx}_SFID2"]}) |
                  MCAN_SMF_SFEC(${.vars["MCAN${INDEX?string}_STD_FILTER${idx}_CONFIG"]}),
    },
     </#list>
};


</#if>
<#if FILTERS_EXT?number gt 0>
#define CONF_MCAN${INDEX?string}_XIDFC_LSE (${FILTERS_EXT})
#define CONF_MCAN${INDEX?string}_XIDFC (MCAN_XIDFC_LSE(CONF_MCAN${INDEX?string}_XIDFC_LSE))
#define CONF_MCAN${INDEX?string}_XIDAM 0x1FFFFFFF

<#assign numInstance=FILTERS_EXT?number>
__attribute__((aligned (4)))static struct _mcan_extended_message_filter_element
    mcan${INDEX?string}_ext_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .F0.val = MCAN_EFID1(${.vars["MCAN${INDEX?string}_EXT_FILTER${idx}_EFID1"]}) | MCAN_EFEC(${.vars["MCAN${INDEX?string}_EXT_FILTER${idx}_CONFIG"]}),
        .F1.val = MCAN_EFID2(${.vars["MCAN${INDEX?string}_EXT_FILTER${idx}_EFID2"]}) | MCAN_EFT(${.vars["MCAN${INDEX?string}_EXT_FILTER${idx}_TYPE"]}),
    },
     </#list>
};


</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Instance ${INDEX?string} static driver functions
// *****************************************************************************
// *****************************************************************************
void MCAN${INDEX?string}_Initialize(void)
{
    /* set INIT and CCE to get access to configuration registers */
    MCAN${INDEX?string}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((MCAN${INDEX?string}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;

    /* unlock the configuration registers */
    MCAN${INDEX?string}->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

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
<#if MCAN_OPMODE =="FD">

    /* Fast Data Bit Timing and Prescaler Register */
    MCAN${INDEX?string}->MCAN_DBTP = CONF_MCAN${INDEX?string}_FBTP;
</#if>

    /* Nominal Bit timing and Prescaler Register */
    MCAN${INDEX?string}->MCAN_NBTP  = CONF_MCAN${INDEX?string}_BTP;

    /* Timestamp Counter Configuration Register */
    MCAN${INDEX?string}->MCAN_TSCC = CONF_MCAN${INDEX?string}_TSCC;
<#if MCAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    MCAN${INDEX?string}->MCAN_TOCC = CONF_MCAN${INDEX?string}_TOCC;

    /* Timeout Counter Value Register */
    MCAN${INDEX?string}->MCAN_TOCV = CONF_MCAN${INDEX?string}_TOCV;
</#if>
<#if RXF0_USE>

    /* Receive FIFO 0 Configuration Register */
    MCAN${INDEX?string}->MCAN_RXF0C = CONF_MCAN${INDEX?string}_RXF0C |
            (((uint32_t)mcan${INDEX?string}_rx0_fifo) & 0xFFFF);
</#if>
<#if RXF1_USE>

    /* Receive FIFO 1 Configuration Register */
    MCAN${INDEX?string}->MCAN_RXF1C = CONF_MCAN${INDEX?string}_RXF1C |
            (((uint32_t)mcan${INDEX?string}_rx1_fifo) & 0xFFFF);
</#if>
<#if RXF0_USE || RXF1_USE>

    /* Receive Buffer / FIFO Element Size Configuration Register */
    MCAN${INDEX?string}->MCAN_RXESC = CONF_MCAN${INDEX?string}_RXESC;
</#if>
<#if TX_USE>

    /* Transmit Buffer Configuration Register */
    MCAN${INDEX?string}->MCAN_TXBC = CONF_MCAN${INDEX?string}_TXBC |
            (((uint32_t)mcan${INDEX?string}_tx_fifo) & 0xFFFF);

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    MCAN${INDEX?string}->MCAN_TXESC = CONF_MCAN${INDEX?string}_TXESC;

    /* Transmit Event FIFO Configuration Register */
    MCAN${INDEX?string}->MCAN_TXEFC = CONF_MCAN${INDEX?string}_TXEFC |
            (((uint32_t)mcan${INDEX?string}_tx_event_fifo) & 0xFFFF);
</#if>

    /* Global Filter Configuration Register */
    MCAN${INDEX?string}->MCAN_GFC = CONF_MCAN${INDEX?string}_GFC;
<#if FILTERS_STD?number gt 0>

    /* Standard ID Filter Configuration Register */
    MCAN${INDEX?string}->MCAN_SIDFC = CONF_MCAN${INDEX?string}_SIDF |
            (((uint32_t)mcan${INDEX?string}_std_filter) & 0xFFFF);
</#if>
<#if FILTERS_EXT?number gt 0>

    /* Extended ID Filter Configuration Register */
    MCAN${INDEX?string}->MCAN_XIDFC = CONF_MCAN${INDEX?string}_XIDFC |
            (((uint32_t)mcan${INDEX?string}_ext_filter) & 0xFFFF);

    /* Extended ID AND Mask Register */
    MCAN${INDEX?string}->MCAN_XIDAM = CONF_MCAN${INDEX?string}_XIDAM;
</#if>

    /* Set the mode and config state */
    MCAN${INDEX?string}->MCAN_TEST = CONF_MCAN${INDEX?string}_TEST;
    MCAN${INDEX?string}->MCAN_CCCR = CONF_MCAN${INDEX?string}_CCCR;
<#if MCAN_OPMODE != "CONFIGURATION">
    while ((MCAN${INDEX?string}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
<#if USE_INTERRUPTS == true>

    /* Enable the configured interrupts */
    MCAN${INDEX?string}->MCAN_IE = CONF_MCAN${INDEX?string}_IE;
</#if>
}



void MCAN${INDEX?string}_Deinitialize(void)
{
    MCAN${INDEX?string}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
}



void MCAN${INDEX?string}_Open(void)
{
<#if MCAN_OPMODE != "CONFIGURATION">
    MCAN${INDEX?string}->MCAN_CCCR = CONF_MCAN${INDEX?string}_CCCR;
    while ((MCAN${INDEX?string}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
}



void MCAN${INDEX?string}_Close(void)
{
    /* Switch the CAN module OFF */
<#if MCAN_OPMODE != "CONFIGURATION">
    MCAN${INDEX?string}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((MCAN${INDEX?string}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;
</#if>
}



/* returns false on fail, true on success */
bool MCAN${INDEX?string}_ChannelMessageTransmit(MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
{
    (void)channelNum;
<#if !TX_USE>
    (void)address;
    (void)DLC;
    (void)message;
<#else>

    uint32_t tfqpi = MCAN_TXFQS_TFQPI(MCAN${INDEX?string}->MCAN_TXFQS);
    struct _mcan_tx_fifo_entry *fifo =
        (struct _mcan_tx_fifo_entry*) (mcan${INDEX?string}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});

    if (MCAN${INDEX?string}->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk)
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
<#if MCAN_OPMODE =="FD">

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
    MCAN${INDEX?string}->MCAN_TXBAR = 1U << tfqpi;
</#if>

    return 1;
}



/* Channel is which FIFO to use. Only 2 max available */
bool MCAN${INDEX?string}_ChannelMessageReceive(MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
{
<#if RXF0_USE || RXF1_USE>
    uint32_t rxgi;
    struct _mcan_rx_fifo_entry *fifo = NULL;

    /* Read a message from the selected channel */
    switch (channelNum)
    {
        default:
<#if RXF0_USE>
        case 0:
            /* check and return 0 if nothing to be read */
            if ((MCAN${INDEX?string}->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk) == 0) return 0;

            /* read FIFO 0 */
            rxgi = (MCAN${INDEX?string}->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos;
            fifo = (struct _mcan_rx_fifo_entry*) (mcan${INDEX?string}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* ack the fifo position */
            MCAN${INDEX?string}->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            break;
</#if>

<#if RXF1_USE>
        case 1:
            /* check and return 0 if nothing to be read */
            if ((MCAN${INDEX?string}->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk) == 0) return 0;

            /* Read FIFO 1 */
            rxgi = (MCAN${INDEX?string}->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos;
            fifo = (struct _mcan_rx_fifo_entry*) (mcan${INDEX?string}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* ack the fifo position */
            MCAN${INDEX?string}->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
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
/* One Interrupt handler for each MCAN(MCAN) module - default to INT0 */
void MCAN${INDEX?string}_INT0_Handler( void )
{
    uint32_t ir = MCAN${INDEX?string}->MCAN_IR;
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
    MCAN${INDEX?string}->MCAN_IR = ir;
}
</#if>	


/*******************************************************************************
 End of File
*/
