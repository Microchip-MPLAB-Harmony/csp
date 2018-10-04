/*******************************************************************************
  Controller Area Network (MCAN) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCAN_INSTANCE_NAME?lower_case}.c

  Summary:
    MCAN source file.

  Description:
    None.

  Remarks:
    None.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
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
*******************************************************************************/
//DOM-IGNORE-END
// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${MCAN_INSTANCE_NAME?lower_case}.h"

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
#define ${MCAN_INSTANCE_NAME} ${MCAN_INSTANCE_NAME}_REGS

    <#switch MCAN_OPMODE>
    <#default>
    <#case "NORMAL">
    /* MCAN operation is set to normal mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR (MCAN_CCCR_ASM_NORMAL<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_${MCAN_INSTANCE_NAME}_TEST 0x00
    <#break>
    <#case "CONFIGURATION">
    /* MCAN operation is set to configuration mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR MCAN_CCCR_INIT_ENABLED
#define CONF_${MCAN_INSTANCE_NAME}_TEST 0x00
    <#break>
    <#case "FD">
    /* MCAN operation is set to FD mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR (MCAN_CCCR_FDOE_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_${MCAN_INSTANCE_NAME}_TEST 0x00
    <#break>
    <#case "RESTRICTED">
    /* MCAN operation is set to restricted mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR MCAN_CCCR_ASM_RESTRICTED
#define CONF_${MCAN_INSTANCE_NAME}_TEST 0x00
    <#break>
    <#case "MONITOR">
    /* MCAN operation is set to monitor mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR (MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_${MCAN_INSTANCE_NAME}_TEST 0x00
    <#break>
    <#case "EXT LOOPBACK">
    /* MCAN operation is set to external loopback mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR (MCAN_CCCR_TEST_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_${MCAN_INSTANCE_NAME}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    <#case "INT LOOPBACK">
    /* MCAN operation is set to internal loopback mode */
#define CONF_${MCAN_INSTANCE_NAME}_CCCR (MCAN_CCCR_TEST_ENABLED | MCAN_CCCR_MON_ENABLED<#if TX_PAUSE!false> | MCAN_CCCR_TXP_Msk</#if>)
#define CONF_${MCAN_INSTANCE_NAME}_TEST MCAN_TEST_LBCK_ENABLED
    <#break>
    </#switch>

#define CONF_${MCAN_INSTANCE_NAME}_GFC (${FILTERS_STD_NOMATCH} | ${FILTERS_EXT_NOMATCH}<#if FILTERS_STD_REJECT> | MCAN_GFC_RRFS_REJECT</#if><#if FILTERS_EXT_REJECT> | MCAN_GFC_RRFE_REJECT</#if>)

<#if MCAN_OPMODE =="FD">
/* configure the FD constants */
#define CONF_${MCAN_INSTANCE_NAME}_FBTP (${FBTP_FSJW} | (${FBTP_FTSEG1} << 8) | (${FBTP_FTSEG2} << 4) | (${FBTP_FBRP} << 16))
</#if>
/* configure the 'Normal' constants */
#define CONF_${MCAN_INSTANCE_NAME}_BTP  (${BTP_SJW} | (${BTP_TSEG1} << 8) | (${BTP_TSEG2} << 4) | (${BTP_BRP} << 16))
<#if USE_INTERRUPTS == true>

#define CONF_${MCAN_INSTANCE_NAME}_IE 0x00 \
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

#define CONF_${MCAN_INSTANCE_NAME}_TSCC (${TIMESTAMP_MODE} | MCAN_TSCC_TCP(${TIMESTAMP_PRESCALER}))
<#if MCAN_TIMEOUT>
#define CONF_${MCAN_INSTANCE_NAME}_TOCC (${TIMEOUT_SELECT} | MCAN_TOCC_ETOC_TOS_CONTROLLED)
#define CONF_${MCAN_INSTANCE_NAME}_TOCV MCAN_TOCV_TOC(${TIMEOUT_COUNT})

</#if>
/* Configuration for the bytes in each element of RX FIFOs */
#define CONF_${MCAN_INSTANCE_NAME}_RXESC (0<#if RXF0_USE> | MCAN_RXESC_F0DS(${RXF0_BYTES_CFG!0})</#if><#if RXF1_USE> | MCAN_RXESC_F1DS(${RXF1_BYTES_CFG!0})</#if>)
<#if RXF0_USE>
<#assign RXF0_BYTES_CFG = RXF0_BYTES_CFG!0>
<#if RXF0_BYTES_CFG?number < 5>
  <#assign RXF0_ELEMENT_BYTES = 16 + RXF0_BYTES_CFG?number * 4>
<#else>
  <#assign RXF0_ELEMENT_BYTES = 40 + 16 * (RXF0_BYTES_CFG?number - 5)>
</#if>
#define CONF_${MCAN_INSTANCE_NAME}_RXF0C (MCAN_RXF0C_F0S(${RXF0_ELEMENTS}) | MCAN_RXF0C_F0WM(${RXF0_WATERMARK})<#if RXF0_OVERWRITE> | MCAN_RXF0C_F0OM_Msk</#if>)
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo[${RXF0_ELEMENTS} * ${RXF0_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if RXF1_USE>
<#assign RXF1_BYTES_CFG = RXF1_BYTES_CFG!0>
<#if RXF1_BYTES_CFG?number < 5>
  <#assign RXF1_ELEMENT_BYTES = 16 + RXF1_BYTES_CFG?number * 4>
<#else>
  <#assign RXF1_ELEMENT_BYTES = 40 + 16 * (RXF1_BYTES_CFG?number - 5)>
</#if>

#define CONF_${MCAN_INSTANCE_NAME}_RXF1C (MCAN_RXF1C_F1S(${RXF1_ELEMENTS}) | MCAN_RXF1C_F1WM(${RXF1_WATERMARK})<#if RXF1_OVERWRITE> | MCAN_RXF1C_F1OM_Msk</#if>)
static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo[${RXF1_ELEMENTS} * ${RXF1_ELEMENT_BYTES}]__attribute__((aligned (4)));

</#if>
<#if TX_USE>
<#assign TX_FIFO_BYTES_CFG = TX_FIFO_BYTES_CFG!0>
<#if TX_FIFO_BYTES_CFG?number < 5>
  <#assign TX_ELEMENT_BYTES = 16 + TX_FIFO_BYTES_CFG?number * 4>
<#else>
  <#assign TX_ELEMENT_BYTES = 40 + 16 * (TX_FIFO_BYTES_CFG?number - 5)>
</#if>

#define CONF_${MCAN_INSTANCE_NAME}_TXESC (MCAN_TXESC_TBDS(${TX_FIFO_BYTES_CFG}))
#define CONF_${MCAN_INSTANCE_NAME}_TXBC  MCAN_TXBC_TFQS(${TX_FIFO_ELEMENTS})
#define CONF_${MCAN_INSTANCE_NAME}_TXEFC (MCAN_TXEFC_EFWM(${TX_FIFO_WATERMARK}) | MCAN_TXEFC_EFS(${TX_FIFO_ELEMENTS}))

static uint8_t ${MCAN_INSTANCE_NAME?lower_case}_tx_fifo[${TX_FIFO_ELEMENTS} * ${TX_ELEMENT_BYTES!0}]__attribute__((aligned (4)));
static struct _mcan_tx_event_entry ${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo[${TX_FIFO_ELEMENTS}]__attribute__((aligned (4)));

</#if>
<#if FILTERS_STD?number gt 0>
#define CONF_${MCAN_INSTANCE_NAME}_SIDFC_LSS (${FILTERS_STD})
#define CONF_${MCAN_INSTANCE_NAME}_SIDF  (MCAN_SIDFC_LSS(CONF_${MCAN_INSTANCE_NAME}_SIDFC_LSS))
<#assign numInstance=FILTERS_STD?number>
__attribute__((aligned (4)))static struct _mcan_standard_message_filter_element
        ${MCAN_INSTANCE_NAME?lower_case}_std_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .S0.val = MCAN_SMF_SFT(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_TYPE"]}) |
                  MCAN_SMF_SFID1(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID1"]}) |
                  MCAN_SMF_SFID2(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_SFID2"]}) |
                  MCAN_SMF_SFEC(${.vars["${MCAN_INSTANCE_NAME}_STD_FILTER${idx}_CONFIG"]}),
    },
     </#list>
};


</#if>
<#if FILTERS_EXT?number gt 0>
#define CONF_${MCAN_INSTANCE_NAME}_XIDFC_LSE (${FILTERS_EXT})
#define CONF_${MCAN_INSTANCE_NAME}_XIDFC (MCAN_XIDFC_LSE(CONF_${MCAN_INSTANCE_NAME}_XIDFC_LSE))
#define CONF_${MCAN_INSTANCE_NAME}_XIDAM 0x1FFFFFFF

<#assign numInstance=FILTERS_EXT?number>
__attribute__((aligned (4)))static struct _mcan_extended_message_filter_element
    ${MCAN_INSTANCE_NAME?lower_case}_ext_filter[] =
{
    <#list 1..(numInstance) as idx>
    {
        .F0.val = MCAN_EFID1(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID1"]}) | MCAN_EFEC(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_CONFIG"]}),
        .F1.val = MCAN_EFID2(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_EFID2"]}) | MCAN_EFT(${.vars["${MCAN_INSTANCE_NAME}_EXT_FILTER${idx}_TYPE"]}),
    },
     </#list>
};


</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Instance static driver functions
// *****************************************************************************
// *****************************************************************************
void ${MCAN_INSTANCE_NAME}_Initialize(void)
{
    /* set INIT and CCE to get access to configuration registers */
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((${MCAN_INSTANCE_NAME}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;

    /* unlock the configuration registers */
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR |= MCAN_CCCR_CCE_Msk;

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
    ${MCAN_INSTANCE_NAME}->MCAN_DBTP = CONF_${MCAN_INSTANCE_NAME}_FBTP;
</#if>

    /* Nominal Bit timing and Prescaler Register */
    ${MCAN_INSTANCE_NAME}->MCAN_NBTP  = CONF_${MCAN_INSTANCE_NAME}_BTP;

    /* Timestamp Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TSCC = CONF_${MCAN_INSTANCE_NAME}_TSCC;
<#if MCAN_TIMEOUT>

    /* Timeout Counter Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TOCC = CONF_${MCAN_INSTANCE_NAME}_TOCC;

    /* Timeout Counter Value Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TOCV = CONF_${MCAN_INSTANCE_NAME}_TOCV;
</#if>
<#if RXF0_USE>

    /* Receive FIFO 0 Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_RXF0C = CONF_${MCAN_INSTANCE_NAME}_RXF0C |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo) & 0xFFFF);
</#if>
<#if RXF1_USE>

    /* Receive FIFO 1 Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_RXF1C = CONF_${MCAN_INSTANCE_NAME}_RXF1C |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo) & 0xFFFF);
</#if>
<#if RXF0_USE || RXF1_USE>

    /* Receive Buffer / FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_RXESC = CONF_${MCAN_INSTANCE_NAME}_RXESC;
</#if>
<#if TX_USE>

    /* Transmit Buffer Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TXBC = CONF_${MCAN_INSTANCE_NAME}_TXBC |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_tx_fifo) & 0xFFFF);

    /* Transmit Buffer/FIFO Element Size Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TXESC = CONF_${MCAN_INSTANCE_NAME}_TXESC;

    /* Transmit Event FIFO Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_TXEFC = CONF_${MCAN_INSTANCE_NAME}_TXEFC |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_tx_event_fifo) & 0xFFFF);
</#if>

    /* Global Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_GFC = CONF_${MCAN_INSTANCE_NAME}_GFC;
<#if FILTERS_STD?number gt 0>

    /* Standard ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_SIDFC = CONF_${MCAN_INSTANCE_NAME}_SIDF |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_std_filter) & 0xFFFF);
</#if>
<#if FILTERS_EXT?number gt 0>

    /* Extended ID Filter Configuration Register */
    ${MCAN_INSTANCE_NAME}->MCAN_XIDFC = CONF_${MCAN_INSTANCE_NAME}_XIDFC |
            (((uint32_t)${MCAN_INSTANCE_NAME?lower_case}_ext_filter) & 0xFFFF);

    /* Extended ID AND Mask Register */
    ${MCAN_INSTANCE_NAME}->MCAN_XIDAM = CONF_${MCAN_INSTANCE_NAME}_XIDAM;
</#if>

    /* Set the mode and config state */
    ${MCAN_INSTANCE_NAME}->MCAN_TEST = CONF_${MCAN_INSTANCE_NAME}_TEST;
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR = CONF_${MCAN_INSTANCE_NAME}_CCCR;
<#if MCAN_OPMODE != "CONFIGURATION">
    while ((${MCAN_INSTANCE_NAME}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
<#if USE_INTERRUPTS == true>

    /* Enable the configured interrupts */
    ${MCAN_INSTANCE_NAME}->MCAN_IE = CONF_${MCAN_INSTANCE_NAME}_IE;
</#if>
}



void ${MCAN_INSTANCE_NAME}_Deinitialize(void)
{
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
}



void ${MCAN_INSTANCE_NAME}_Open(void)
{
<#if MCAN_OPMODE != "CONFIGURATION">
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR = CONF_${MCAN_INSTANCE_NAME}_CCCR;
    while ((${MCAN_INSTANCE_NAME}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) == MCAN_CCCR_INIT_Msk)  ;
</#if>
}



void ${MCAN_INSTANCE_NAME}_Close(void)
{
    /* Switch the CAN module OFF */
<#if MCAN_OPMODE != "CONFIGURATION">
    ${MCAN_INSTANCE_NAME}->MCAN_CCCR = MCAN_CCCR_INIT_Msk;
    while ((${MCAN_INSTANCE_NAME}->MCAN_CCCR & MCAN_CCCR_INIT_Msk) != MCAN_CCCR_INIT_Msk)  ;
</#if>
}



/* returns false on fail, true on success */
bool ${MCAN_INSTANCE_NAME}_ChannelMessageTransmit(MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
{
    (void)channelNum;
<#if !TX_USE>
    (void)address;
    (void)DLC;
    (void)message;
<#else>

    uint32_t tfqpi = MCAN_TXFQS_TFQPI(${MCAN_INSTANCE_NAME}->MCAN_TXFQS);
    struct _mcan_tx_fifo_entry *fifo =
        (struct _mcan_tx_fifo_entry*) (${MCAN_INSTANCE_NAME?lower_case}_tx_fifo + tfqpi * ${TX_ELEMENT_BYTES!0});

    if (${MCAN_INSTANCE_NAME}->MCAN_TXFQS & MCAN_TXFQS_TFQF_Msk)
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
    ${MCAN_INSTANCE_NAME}->MCAN_TXBAR = 1U << tfqpi;
</#if>

    return 1;
}



/* Channel is which FIFO to use. Only 2 max available */
bool ${MCAN_INSTANCE_NAME}_ChannelMessageReceive(MCAN_CHANNEL channelNum, int address, uint8_t DLC, uint8_t* message)
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
            if ((${MCAN_INSTANCE_NAME}->MCAN_RXF0S & MCAN_RXF0S_F0FL_Msk) == 0) return 0;

            /* read FIFO 0 */
            rxgi = (${MCAN_INSTANCE_NAME}->MCAN_RXF0S & MCAN_RXF0S_F0GI_Msk) >> MCAN_RXF0S_F0GI_Pos;
            fifo = (struct _mcan_rx_fifo_entry*) (${MCAN_INSTANCE_NAME?lower_case}_rx0_fifo + rxgi * ${RXF0_ELEMENT_BYTES!16});

            /* ack the fifo position */
            ${MCAN_INSTANCE_NAME}->MCAN_RXF0A = MCAN_RXF0A_F0AI(rxgi);
            break;
</#if>

<#if RXF1_USE>
        case 1:
            /* check and return 0 if nothing to be read */
            if ((${MCAN_INSTANCE_NAME}->MCAN_RXF1S & MCAN_RXF1S_F1FL_Msk) == 0) return 0;

            /* Read FIFO 1 */
            rxgi = (${MCAN_INSTANCE_NAME}->MCAN_RXF1S & MCAN_RXF1S_F1GI_Msk) >> MCAN_RXF1S_F1GI_Pos;
            fifo = (struct _mcan_rx_fifo_entry*) (${MCAN_INSTANCE_NAME?lower_case}_rx1_fifo + rxgi * ${RXF1_ELEMENT_BYTES!16});

            /* ack the fifo position */
            ${MCAN_INSTANCE_NAME}->MCAN_RXF1A = MCAN_RXF1A_F1AI(rxgi);
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
void ${MCAN_INSTANCE_NAME}_INT0_InterruptHandler( void )
{
    uint32_t ir = ${MCAN_INSTANCE_NAME}->MCAN_IR;
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
    ${MCAN_INSTANCE_NAME}->MCAN_IR = ir;
}
</#if>	


/*******************************************************************************
 End of File
*/
