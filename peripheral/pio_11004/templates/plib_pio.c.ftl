/*******************************************************************************
  SYS PORTS Static Functions for PORTS System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.c

  Summary:
    PIO function implementations for the PIO PLIB.

  Description:
    The PIO PLIB provides a simple interface to manage peripheral
    input-output controller.

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

#include "plib_pio.h"

<#compress>
<#if PIO_ENABLE == true>
    <#assign PIO_A_NUM_INT_PINS = 0>
    <#assign PIO_B_NUM_INT_PINS = 0>
    <#assign PIO_C_NUM_INT_PINS = 0>
    <#assign PIO_D_NUM_INT_PINS = 0>
    <#assign PIO_E_NUM_INT_PINS = 0>
    <#list 1..350 as i>
        <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
        <#assign portChannel = "PIN_" + i + "_PIO_CHANNEL">
        <#if .vars[intConfig]?has_content>
            <#if (.vars[intConfig] != "Disabled")>
                <#if (.vars[portChannel] == "A")>
                    <#assign PIO_A_NUM_INT_PINS = PIO_A_NUM_INT_PINS + 1>
                </#if>
                <#if (.vars[portChannel] == "B")>
                    <#assign PIO_B_NUM_INT_PINS = PIO_B_NUM_INT_PINS + 1>
                </#if>
                <#if (.vars[portChannel] == "C")>
                    <#assign PIO_C_NUM_INT_PINS = PIO_C_NUM_INT_PINS + 1>
                </#if>
                <#if (.vars[portChannel] == "D")>
                    <#assign PIO_D_NUM_INT_PINS = PIO_D_NUM_INT_PINS + 1>
                </#if>
                <#if (.vars[portChannel] == "E")>
                    <#assign PIO_E_NUM_INT_PINS = PIO_E_NUM_INT_PINS + 1>
                </#if>
            </#if>
        </#if>
    </#list>    
</#if>

<#macro PIO_INITIALIZE PIO_PORT PIO_DIR PIO_LAT PIO_OD PIO_PU PIO_PD PIO_PER PIO_ABCD1
                       PIO_ABCD2 PIO_INT_TYPE PIO_INT_EDGE PIO_INT_LEVEL PIO_INT_RE_HL PIO_INT_FE_LL PIO_INTERRUPT>
    <#lt>   /************************ PIO ${PIO_PORT} Initialization ************************/
    <#if (PIO_ABCD1 != "0x00000000") | (PIO_ABCD2 != "0x00000000")>
        <#lt>   /* PORT${PIO_PORT} Peripheral Function Selection */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[0]= ${PIO_ABCD1};
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[1]= ${PIO_ABCD2};
    </#if>
    <#if PIO_PER != "0xFFFFFFFF">
        <#lt>   /* PORT${PIO_PORT} PIO Disable and Peripheral Enable*/
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PDR = ~${PIO_PER};
    </#if>
    <#if PIO_LAT != "0x00000000">
        <#lt>   /* PORT${PIO_PORT} Initial state High */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_SODR = ${PIO_LAT};
    </#if>
    <#if PIO_OD != "0x00000000">
        <#lt>   /* PORT${PIO_PORT} Multi Drive or Open Drain Enable */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_MDER = ${PIO_OD};
    </#if>
    <#if PIO_PU != "0x00000000">
        <#lt>   /* PORT${PIO_PORT} Pull Up Enable */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUER = ${PIO_PU};
    </#if>
    <#if PIO_PD != "0x00000000">
        <#lt>   /* PORT${PIO_PORT} Pull Down Enable */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDER = ${PIO_PD};
    </#if>
    <#if PIO_DIR != "0x00000000">
        <#lt>   /* PORT${PIO_PORT} Output Direction Enable */
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OER = ${PIO_DIR};
    </#if>
         <#lt>   /* PORT${PIO_PORT} Output Write Enable */	
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OWER = PIO_OWER_Msk;
    <#if PIO_INTERRUPT == true>
        <#if PIO_INT_TYPE != "0x00000000">
            <#lt>   /* PORT${PIO_PORT} Additional interrupt mode Enable */
            <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_AIMER = ${PIO_INT_TYPE};
        <#else>
        
            <#lt>   /* If PIO Interrupt is selected for both edge, it doesn't need any register
            <#lt>      configuration */
        </#if>
        <#if PIO_INT_LEVEL != "0x00000000">
            <#lt>   /* PORT${PIO_PORT} Level type interrupt Enable */
            <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_LSR = ~${PIO_INT_LEVEL};
        </#if>
        <#if PIO_INT_EDGE != "0x00000000">
            <#lt>   /* PORT${PIO_PORT} Edge type interrupt Enable */
            <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ESR = ${PIO_INT_EDGE};
        </#if>
        <#if PIO_INT_FE_LL != "0x00000000">
            <#lt>   /* PORT${PIO_PORT} Falling Edge or Low Level Interrupt Enable */
            <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_FELLSR = ~${PIO_INT_FE_LL};
        </#if>
        <#if PIO_INT_RE_HL != "0x00000000">
            <#lt>   /* PORT${PIO_PORT} Rising Edge or High Level Interrupt Enable */
            <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_REHLSR = ${PIO_INT_RE_HL};
        </#if>
        <#lt>   /* PORT${PIO_PORT} Interrupt Status Clear */	
        <#lt>   ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ISR;
        
        <#lt>   /* PORT${PIO_PORT} system level interrupt will be enabled by NVIC Manager */
        <#lt>   /* PORT${PIO_PORT} module level Interrupt for every pin has to be enabled by user
        <#lt>      by calling PIO_PinInterruptEnable() API dynamically as and when needed*/
    </#if>
</#macro>

<#macro PIO_INT_CALLBACK PIO_PORT PORT_NUM_INT_PINS PIO_INTERRUPT>
    <#if PIO_INTERRUPT == true>
        <#lt>/* port ${PIO_PORT} current number of callbacks */
        <#lt>uint8_t port${PIO_PORT}CurNumCb = 0;

        <#lt>/* port ${PIO_PORT} maximum number of callbacks */
        <#lt>uint8_t port${PIO_PORT}MaxNumCb = ${PORT_NUM_INT_PINS};
        
        <#lt>/* port ${PIO_PORT} callback objects */
        <#lt>PIO_PIN_CALLBACK_OBJ port${PIO_PORT}PinCbObj[${PORT_NUM_INT_PINS}];
    </#if>
</#macro>


<@PIO_INT_CALLBACK 
    PIO_PORT = "A" 
    PORT_NUM_INT_PINS = "${PIO_A_NUM_INT_PINS}"
    PIO_INTERRUPT = PIO_A_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_PORT = "B" 
    PORT_NUM_INT_PINS = "${PIO_B_NUM_INT_PINS}"
    PIO_INTERRUPT = PIO_B_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_PORT = "C" 
    PORT_NUM_INT_PINS = "${PIO_C_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_C_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_PORT = "D" 
    PORT_NUM_INT_PINS = "${PIO_D_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_D_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_PORT = "E" 
    PORT_NUM_INT_PINS = "${PIO_E_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_E_INTERRUPT_USED
/>
</#compress>


/******************************************************************************
  Function:
    PIO_Initialize ( void )

  Summary:
    Initialize the PIO library.
  
  Description:
    This function initializes the PIO library and all ports & pins configured
    in the MCC Pin Manager.

  Remarks:
    None.
*/
void PIO_Initialize ( void )
{
    <#if PIO_CCFG_SYSIO_VALUE != "0x00000000">
        <#lt>   /* Selected System IO pins are configured as GPIO */
        <#lt>   MATRIX_REGS->CCFG_SYSIO|= ${PIO_CCFG_SYSIO_VALUE};
    </#if>
    <#if PIO_A_USED == true>
        <@PIO_INITIALIZE
            PIO_PORT = "A"
            PIO_DIR = "${PIOA_OER_VALUE}"
            PIO_LAT = "${PIOA_SODR_VALUE}"
            PIO_OD = "${PIOA_MDER_VALUE}"
            PIO_PU = "${PIOA_PUER_VALUE}"
            PIO_PD = "${PIOA_PPDEN_VALUE}"
            PIO_PER = "${PIOA_PER_VALUE}"
            PIO_ABCD1 = "${PIOA_ABCDSR1_VALUE}"
            PIO_ABCD2 = "${PIOA_ABCDSR2_VALUE}"
            PIO_INT_TYPE = "${PIOA_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOA_ESR_VALUE}"
            PIO_INT_LEVEL = "${PIOA_LSR_VALUE}"
            PIO_INT_RE_HL = "${PIOA_REHLSR_VALUE}"
            PIO_INT_FE_LL = "${PIOA_FELLSR_VALUE}"
            PIO_INTERRUPT = PIO_A_INTERRUPT_USED
        />
    </#if>

    <#if PIO_B_USED == true>
        <@PIO_INITIALIZE
            PIO_PORT = "B"
            PIO_DIR = "${PIOB_OER_VALUE}"
            PIO_LAT = "${PIOB_SODR_VALUE}"
            PIO_OD = "${PIOB_MDER_VALUE}"
            PIO_PU = "${PIOB_PUER_VALUE}"
            PIO_PD = "${PIOB_PPDEN_VALUE}"
            PIO_PER = "${PIOB_PER_VALUE}"
            PIO_ABCD1 = "${PIOB_ABCDSR1_VALUE}"
            PIO_ABCD2 = "${PIOB_ABCDSR2_VALUE}"
            PIO_INT_TYPE = "${PIOB_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOB_ESR_VALUE}"
            PIO_INT_LEVEL = "${PIOB_LSR_VALUE}"
            PIO_INT_RE_HL = "${PIOB_REHLSR_VALUE}"
            PIO_INT_FE_LL = "${PIOB_FELLSR_VALUE}"
            PIO_INTERRUPT = PIO_B_INTERRUPT_USED
        />
    </#if>

    <#if PIO_C_USED == true>
        <@PIO_INITIALIZE
            PIO_PORT = "C"
            PIO_DIR = "${PIOC_OER_VALUE}"
            PIO_LAT = "${PIOC_SODR_VALUE}"
            PIO_OD = "${PIOC_MDER_VALUE}"
            PIO_PU = "${PIOC_PUER_VALUE}"
            PIO_PD = "${PIOC_PPDEN_VALUE}"
            PIO_PER = "${PIOC_PER_VALUE}"
            PIO_ABCD1 = "${PIOC_ABCDSR1_VALUE}"
            PIO_ABCD2 = "${PIOC_ABCDSR2_VALUE}"
            PIO_INT_TYPE = "${PIOC_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOC_ESR_VALUE}"
            PIO_INT_LEVEL = "${PIOC_LSR_VALUE}"
            PIO_INT_RE_HL = "${PIOC_REHLSR_VALUE}"
            PIO_INT_FE_LL = "${PIOC_FELLSR_VALUE}"
            PIO_INTERRUPT = PIO_C_INTERRUPT_USED
        />
    </#if>

    <#if PIO_D_USED == true>
        <@PIO_INITIALIZE
            PIO_PORT = "D"
            PIO_DIR = "${PIOD_OER_VALUE}"
            PIO_LAT = "${PIOD_SODR_VALUE}"
            PIO_OD = "${PIOD_MDER_VALUE}"
            PIO_PU = "${PIOD_PUER_VALUE}"
            PIO_PD = "${PIOD_PPDEN_VALUE}"
            PIO_PER = "${PIOD_PER_VALUE}"
            PIO_ABCD1 = "${PIOD_ABCDSR1_VALUE}"
            PIO_ABCD2 = "${PIOD_ABCDSR2_VALUE}"
            PIO_INT_TYPE = "${PIOD_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOD_ESR_VALUE}"
            PIO_INT_LEVEL = "${PIOD_LSR_VALUE}"
            PIO_INT_RE_HL = "${PIOD_REHLSR_VALUE}"
            PIO_INT_FE_LL = "${PIOD_FELLSR_VALUE}"
            PIO_INTERRUPT = PIO_D_INTERRUPT_USED
        />
    </#if>

    <#if PIO_E_USED == true>
        <@PIO_INITIALIZE
            PIO_PORT = "E"
            PIO_DIR = "${PIOE_OER_VALUE}"
            PIO_LAT = "${PIOE_SODR_VALUE}"
            PIO_OD = "${PIOE_MDER_VALUE}"
            PIO_PU = "${PIOE_PUER_VALUE}"
            PIO_PD = "${PIOE_PPDEN_VALUE}"
            PIO_PER = "${PIOE_PER_VALUE}"
            PIO_ABCD1 = "${PIOE_ABCDSR1_VALUE}"
            PIO_ABCD2 = "${PIOE_ABCDSR2_VALUE}"
            PIO_INT_TYPE = "${PIOE_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOE_ESR_VALUE}"
            PIO_INT_LEVEL = "${PIOE_LSR_VALUE}"
            PIO_INT_RE_HL = "${PIOE_REHLSR_VALUE}"
            PIO_INT_FE_LL = "${PIOE_FELLSR_VALUE}"
            PIO_INTERRUPT = PIO_E_INTERRUPT_USED
        />
    </#if>
    <#if (PIO_AFEC0_CHER_VALUE != "0x00000000") | (PIO_AFEC1_CHER_VALUE != "0x00000000") | (PIO_DACC_CHER_VALUE != "0x00000000")>
        <#lt>   /* Analog pins Initialization */
    </#if>
    <#if PIO_AFEC0_CHER_VALUE != "0x00000000">
        <#lt>   AFEC0_REGS->AFEC_CHER = ${PIO_AFEC0_CHER_VALUE};
    </#if>
    <#if PIO_AFEC1_CHER_VALUE != "0x00000000">
        <#lt>   AFEC1_REGS->AFEC_CHER = ${PIO_AFEC1_CHER_VALUE};
    </#if>
    <#if PIO_DACC_CHER_VALUE != "0x00000000">    
        <#lt>   DACC_REGS->DACC_CHER = ${PIO_DACC_CHER_VALUE};
    </#if>
}

// *****************************************************************************
// *****************************************************************************
// Section: PIO APIs which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    uint32_t PIO_PortRead ( PIO_PORT port )

  Summary:
    Read all the I/O lines of the selected port.
  
  Description:
    This function reads the live data values on all the I/O lines of the
    selected port.  Bit values returned in each position indicate corresponding
    pin levels.
    1 = Pin is high.
    0 = Pin is low.
 
    This function reads the value regardless of pin configuration, whether it is
    set as as an input, driven by the PIO Controller, or driven by a peripheral.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will read as
    low (0).
    Implemented pins are Right aligned in the 32-bit return value.
*/
uint32_t PIO_PortRead(PIO_PORT port)
{
    return ((pio_registers_t*)port)->PIO_PDSR;
}

// *****************************************************************************
/* Function:
    void PIO_PortWrite ( PIO_PORT port, uint32_t value );
  
  Summary:
    Write the value on all the I/O lines of the selected port.
  
  Description:
    This function writes the data values driven on all the output lines of the
    selected port.  Bit values in each position indicate corresponding pin
    levels.
    1 = Pin is driven high.
    0 = Pin is driven low.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.
    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortWrite(PIO_PORT port, uint32_t value)
{
    /* Write the desired value */
    ((pio_registers_t*)port)->PIO_ODSR = value;
}

// *****************************************************************************
/* Function:
    uint32_t PIO_PortReadLatch ( PIO_PORT port )
  
  Summary:
    Read the latched value on all the I/O lines of the selected port.
  
  Description:
    This function reads the latched data values on all the I/O lines of the
    selected port.  Bit values returned in each position indicate corresponding
    pin levels.
    1 = Pin is high.
    0 = Pin is low.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will read as
    low (0).
    Implemented pins are Right aligned in the 32-bit return value.
*/
uint32_t PIO_PortReadLatch(PIO_PORT port)
{
    return ((pio_registers_t*)port)->PIO_ODSR;
}

// *****************************************************************************
/* Function:
    void PIO_PortSet ( PIO_PORT port, uint32_t mask )
  
  Summary:
    Set the selected IO pins of a port.
  
  Description:
    This function sets (to '1') the selected IO pins of a port.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.
    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortSet(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_SODR = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortClear ( PIO_PORT port, uint32_t mask )
  
  Summary:
    Clear the selected IO pins of a port.
  
  Description:
    This function clears (to '0') the selected IO pins of a port.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.
    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortClear(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_CODR = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortToggle ( PIO_PORT port, uint32_t mask )
  
  Summary:
    Toggles the selected IO pins of a port.
  
  Description:
    This function toggles (or invert) the selected IO pins of a port.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.
    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortToggle(PIO_PORT port, uint32_t mask)
{
    /* Write into Clr and Set registers */
    ((pio_registers_t*)port)->PIO_ODSR^= mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortInputEnable ( PIO_PORT port, uint32_t mask )
  
  Summary:
    Enables selected IO pins of a port as input.
  
  Description:
    This function enables selected IO pins of a port as input.

  Remarks:
	None.
*/
void PIO_PortInputEnable(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_ODR = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortOutputEnable ( PIO_PORT port, uint32_t mask )
  
  Summary:
    Enables selected IO pins of a port as output(s).
  
  Description:
    This function enables selected IO pins of the given port as output(s).

  Remarks:
	None.
*/
void PIO_PortOutputEnable(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_OER = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Description:
    This function enables IO interrupt on selected IO pins of selected port.

  Remarks:
	None.
*/
void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask)
{   
    ((pio_registers_t*)port)->PIO_IER = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask)

  Summary:
    Disables IO interrupt on selected IO pins of a port.

  Description:
    This function disables IO interrupt on selected IO pins of selected port.

  Remarks:
	None.
*/
void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_IDR = mask;
}

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
// *****************************************************************************
// Section: PIO APIs which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PIO_PinInterruptCallbackRegister(
        PIO_PIN pin, 
        const PIO_PIN_CALLBACK callback,
        void* context
    );

  Summary:
    Allows application to register callback for every pin.

  Description:
    This function allows application to register an event handling function
    for the PLIB to call back when I/O interrupt occurs on the selected pin.

    At any point if application wants to stop the callback, it can call this
    function with "eventHandler" value as NULL.

  Remarks:
    None.
*/
void PIO_PinInterruptCallbackRegister(
    PIO_PIN pin, 
    const PIO_PIN_CALLBACK callback,
    void* context
)
{
    uint8_t portIndex;
    portIndex = pin >> 5;
  
    switch( portIndex )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case 0:
        {
            if( portACurNumCb < portAMaxNumCb )
            {
                portAPinCbObj[ portACurNumCb ].pin   = pin;
                portAPinCbObj[ portACurNumCb ].callback = callback;
                portAPinCbObj[ portACurNumCb ].context  = context;
                portACurNumCb++;
            }
            break;
        }
    </#if>
    <#if PIO_B_INTERRUPT_USED == true>
        case 1:
        {
            if( portBCurNumCb < portBMaxNumCb )
            {
                portBPinCbObj[ portBCurNumCb ].pin   = pin;
                portBPinCbObj[ portBCurNumCb ].callback = callback;
                portBPinCbObj[ portBCurNumCb ].context  = context;
                portBCurNumCb++;
            }
            break;
        }
    </#if>
    <#if PIO_C_INTERRUPT_USED == true>
        case 2:
        {
            if( portCCurNumCb < portCMaxNumCb )
            {
                portCPinCbObj[ portCCurNumCb ].pin   = pin;
                portCPinCbObj[ portCCurNumCb ].callback = callback;
                portCPinCbObj[ portCCurNumCb ].context  = context;
                portCCurNumCb++;
            }
            break;
        }
    </#if>
    <#if PIO_D_INTERRUPT_USED == true>
        case 3:
        {
            if( portDCurNumCb < portDMaxNumCb )
            {
                portDPinCbObj[ portDCurNumCb ].pin   = pin;
                portDPinCbObj[ portDCurNumCb ].callback = callback;
                portDPinCbObj[ portDCurNumCb ].context  = context;
                portDCurNumCb++;
            }
            break;
        }
    </#if>
    <#if PIO_E_INTERRUPT_USED == true>
        case 4:
        {
            if( portECurNumCb < portEMaxNumCb )
            {
                portEPinCbObj[ portECurNumCb ].pin   = pin;
                portEPinCbObj[ portECurNumCb ].callback = callback;
                portEPinCbObj[ portECurNumCb ].context  = context;
                portECurNumCb++;
            }
            break;
        }
    </#if>
        default:
        {
            break;
        }
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: Interrupt Service Routine (ISR) Implementation(s)
// *****************************************************************************
// *****************************************************************************
</#if>

<#if PIO_A_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="A"
    />
</#if>
<#if PIO_B_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="B"
    />
</#if>
<#if PIO_C_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="C"
    />
</#if>
<#if PIO_D_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="D"
    />
</#if>
<#if PIO_E_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="E"
    />
</#if>

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
// *****************************************************************************
// Section: Local Function Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void _PIO_Interrupt_Handler ( PIO_PORT port )

  Summary:
    Interrupt handler for a selected port.

  Description:
    This function defines the Interrupt handler for a selected port.

  Remarks:
	It is an internal function used by the library, user need not call it.
*/
void _PIO_Interrupt_Handler ( PIO_PORT port )
{
    uint32_t status;
    uint32_t i;

    status  = ((pio_registers_t*)port)->PIO_ISR;
    status &= ((pio_registers_t*)port)->PIO_IMR;

    /* Check pending events */
    switch( port )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case PIO_PORT_A:
        {
            for( i = 0; i < portACurNumCb; i++ )
            {
                if( ( status & ( 1 << (portAPinCbObj[i].pin & 0x1F) ) ) &&
                    portAPinCbObj[i].callback != NULL )
                {
                    portAPinCbObj[i].callback ( portAPinCbObj[i].pin, portAPinCbObj[i].context );
                }
            }
            break;
        }
    </#if>
    <#if PIO_B_INTERRUPT_USED == true>
        case PIO_PORT_B:
        {
            for( i = 0; i < portBCurNumCb; i++ )
            {
                if( ( status & ( 1 << (portBPinCbObj[i].pin & 0x1F) ) ) &&
                    portBPinCbObj[i].callback != NULL )
                {
                    portBPinCbObj[i].callback ( portBPinCbObj[i].pin, portBPinCbObj[i].context );
                }
            }
            break;
        }
    </#if>
    <#if PIO_C_INTERRUPT_USED == true>
        case PIO_PORT_C:
        {
            for( i = 0; i < portCCurNumCb; i++ )
            {
                if( ( status & ( 1 << (portCPinCbObj[i].pin & 0x1F) ) ) &&
                    portCPinCbObj[i].callback != NULL )
                {
                    portCPinCbObj[i].callback ( portCPinCbObj[i].pin, portCPinCbObj[i].context );
                }
            }
            break;
        }
    </#if>
    <#if PIO_D_INTERRUPT_USED == true>
        case PIO_PORT_D:
        {
            for( i = 0; i < portDCurNumCb; i++ )
            {
                if( ( status & ( 1 << (portDPinCbObj[i].pin & 0x1F) ) ) &&
                    portDPinCbObj[i].callback != NULL )
                {
                    portDPinCbObj[i].callback ( portDPinCbObj[i].pin, portDPinCbObj[i].context );
                }
            }
            break;
        }
    </#if>
    <#if PIO_E_INTERRUPT_USED == true>
        case PIO_PORT_E:
        {
            for( i = 0; i < portECurNumCb; i++ )
            {
                if( ( status & ( 1 << (portEPinCbObj[i].pin & 0x1F) ) ) &&
                    portEPinCbObj[i].callback != NULL )
                {
                    portEPinCbObj[i].callback ( portEPinCbObj[i].pin, portEPinCbObj[i].context );
                }
            }
            break;
        }
    </#if>
        default:
        {
            break;
        }
    }
}
</#if>

<#macro PIO_ISR_HANDLER PIO_CHANNEL>
// *****************************************************************************
/* Function:
    void PIO${PIO_CHANNEL}_InterruptHandler (void)

  Summary:
    Interrupt handler for PORT${PIO_CHANNEL}.

  Description:
    This function defines the Interrupt service routine for PORT${PIO_CHANNEL}.
    This is the function which by default gets into Interrupt Vector Table.
    
  Remarks:
    User should not call this function.
*/
void PIO${PIO_CHANNEL}_InterruptHandler(void)
{
    /* Local PIO Interrupt Handler */
    _PIO_Interrupt_Handler(PIO_PORT_${PIO_CHANNEL});
}
</#macro>


/*******************************************************************************
 End of File
*/
