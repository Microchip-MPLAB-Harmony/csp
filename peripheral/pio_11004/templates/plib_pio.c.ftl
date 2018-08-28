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

<#macro PIO_INITIALIZE PIO_PORT PIO_DIR PIO_LAT_HIGH PIO_LAT_LOW PIO_OD PIO_PU PIO_PD PIO_PDR PIO_ABCD1
                       PIO_ABCD2 PIO_INT_TYPE PIO_INT_LEVEL PIO_INT_RE_HL PIO_INTERRUPT>
    <#lt>    /************************ PIO ${PIO_PORT} Initialization ************************/
    <#if (PIO_ABCD1 != "0" ) || (PIO_ABCD2 != "0")>
        <#lt>    /* PORT${PIO_PORT} Peripheral Function Selection */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[0]= 0x${PIO_ABCD1};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[1]= 0x${PIO_ABCD2};
    </#if>
    <#if PIO_PDR != "0">
        <#lt>    /* PORT${PIO_PORT} PIO Disable and Peripheral Enable*/
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PDR = 0x${PIO_PDR};
    </#if>

    <#if PIO_OD != "0">
        <#lt>    /* PORT${PIO_PORT} Multi Drive or Open Drain Enable */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_MDER = 0x${PIO_OD};
    </#if>

    <#lt>    /* PORT${PIO_PORT} Pull Up Enable/Disable as per MHC selection */
    <#if PIO_PU != "0">
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUDR = ~0x${PIO_PU};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDDR = 0x${PIO_PU};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUER = 0x${PIO_PU};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUDR = ~0x${PIO_PU};
    </#if>

    <#lt>    /* PORT${PIO_PORT} Pull Down Enable/Disable as per MHC selection */
    <#if PIO_PD != "0">
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDDR = ~0x${PIO_PD};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUDR = 0x${PIO_PD};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDER = 0x${PIO_PD};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDDR = ~0x${PIO_PD};
    </#if>

    <#lt>    /* PORT${PIO_PORT} Output Write Enable */
    <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OWER = PIO_OWER_Msk;

    <#if PIO_DIR != "0">
        <#if PIO_LAT_HIGH != "0">
            <#lt>    /* PORT${PIO_PORT} Initial state High */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_SODR = 0x${PIO_LAT_HIGH};
        </#if>
        <#if PIO_LAT_LOW != "0">
            <#lt>    /* PORT${PIO_PORT} Initial state Low */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_CODR = 0x${PIO_LAT_LOW};
        </#if>

        <#lt>    /* PORT${PIO_PORT} Output Direction Enable */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OER = 0x${PIO_DIR};
    </#if>

    <#if PIO_INTERRUPT == true>
        <#if PIO_INT_TYPE != "0">
            <#lt>    /* PORT${PIO_PORT} Additional interrupt mode Enable */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_AIMER = 0x${PIO_INT_TYPE};
        <#else>

            <#lt>    /* If PIO Interrupt is selected for both edge, it doesn't need any register
            <#lt>       configuration */
        </#if>
        <#if PIO_INT_LEVEL != "0">
            <#lt>    /* PORT${PIO_PORT} Level type interrupt Enable */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_LSR = 0x${PIO_INT_LEVEL};
        </#if>
        <#if PIO_INT_RE_HL != "0">
            <#lt>    /* PORT${PIO_PORT} Rising Edge or High Level Interrupt Enable */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_REHLSR = 0x${PIO_INT_RE_HL};
        </#if>
        <#lt>    /* PORT${PIO_PORT} Interrupt Status Clear */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ISR;

        <#lt>    /* PORT${PIO_PORT} system level interrupt will be enabled by NVIC Manager */
        <#lt>    /* PORT${PIO_PORT} module level Interrupt for every pin has to be enabled by user
        <#lt>       by calling PIO_PinInterruptEnable() API dynamically as and when needed*/
    </#if>
</#macro>

<#macro PIO_INT_CALLBACK PIO_PORT PORT_NUM_INT_PINS PIO_INTERRUPT>
    <#if PIO_INTERRUPT == true>
        <#lt>/* port ${PIO_PORT} current number of callbacks */
        <#lt>uint8_t port${PIO_PORT}CurNumCb = 0;

        <#lt>/* port ${PIO_PORT} callback objects */
        <#lt>PIO_PIN_CALLBACK_OBJ port${PIO_PORT}PinCbObj[${PORT_NUM_INT_PINS}];
    </#if>
</#macro>


<@PIO_INT_CALLBACK
    PIO_PORT = "A"
    PORT_NUM_INT_PINS = PIO_A_NUM_OF_INT_PINS_USED
    PIO_INTERRUPT = PIO_A_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK
    PIO_PORT = "B"
    PORT_NUM_INT_PINS = PIO_B_NUM_OF_INT_PINS_USED
    PIO_INTERRUPT = PIO_B_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK
    PIO_PORT = "C"
    PORT_NUM_INT_PINS = PIO_C_NUM_OF_INT_PINS_USED
    PIO_INTERRUPT = PIO_C_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK
    PIO_PORT = "D"
    PORT_NUM_INT_PINS = PIO_D_NUM_OF_INT_PINS_USED
    PIO_INTERRUPT = PIO_D_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK
    PIO_PORT = "E"
    PORT_NUM_INT_PINS = PIO_E_NUM_OF_INT_PINS_USED
    PIO_INTERRUPT = PIO_E_INTERRUPT_USED
/>
</#compress>


/******************************************************************************
  Function:
    PIO_Initialize ( void )

  Summary:
    Initialize the PIO library.

  Remarks:
    See plib_pio.h for more details.
*/
void PIO_Initialize ( void )
{
    <#if PIO_CCFG_SYSIO_VALUE != "20400000">
        <#lt>    /* Selected System IO pins are configured as GPIO */
        <#lt>    MATRIX_REGS->CCFG_SYSIO|= 0x${PIO_CCFG_SYSIO_VALUE};
    </#if>

        <@PIO_INITIALIZE
            PIO_PORT = "A"
            PIO_DIR = PIOA_OER_VALUE
            PIO_LAT_HIGH = PIOA_SODR_VALUE
            PIO_LAT_LOW = PIOA_CODR_VALUE
            PIO_OD = PIOA_MDER_VALUE
            PIO_PU = PIOA_PUER_VALUE
            PIO_PD = PIOA_PPDEN_VALUE
            PIO_PDR = PIOA_PDR_VALUE
            PIO_ABCD1 = PIOA_ABCDSR1_VALUE
            PIO_ABCD2 = PIOA_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOA_AIMER_VALUE
            PIO_INT_LEVEL = PIOA_LSR_VALUE
            PIO_INT_RE_HL = PIOA_REHLSR_VALUE
            PIO_INTERRUPT = PIO_A_INTERRUPT_USED
        />

        <@PIO_INITIALIZE
            PIO_PORT = "B"
            PIO_DIR = PIOB_OER_VALUE
            PIO_LAT_HIGH = PIOB_SODR_VALUE
            PIO_LAT_LOW = PIOB_CODR_VALUE
            PIO_OD = PIOB_MDER_VALUE
            PIO_PU = PIOB_PUER_VALUE
            PIO_PD = PIOB_PPDEN_VALUE
            PIO_PDR = PIOB_PDR_VALUE
            PIO_ABCD1 = PIOB_ABCDSR1_VALUE
            PIO_ABCD2 = PIOB_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOB_AIMER_VALUE
            PIO_INT_LEVEL = PIOB_LSR_VALUE
            PIO_INT_RE_HL = PIOB_REHLSR_VALUE
            PIO_INTERRUPT = PIO_B_INTERRUPT_USED
        />


        <@PIO_INITIALIZE
            PIO_PORT = "C"
            PIO_DIR = PIOC_OER_VALUE
            PIO_LAT_HIGH = PIOC_SODR_VALUE
            PIO_LAT_LOW = PIOC_CODR_VALUE
            PIO_OD = PIOC_MDER_VALUE
            PIO_PU = PIOC_PUER_VALUE
            PIO_PD = PIOC_PPDEN_VALUE
            PIO_PDR = PIOC_PDR_VALUE
            PIO_ABCD1 = PIOC_ABCDSR1_VALUE
            PIO_ABCD2 = PIOC_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOC_AIMER_VALUE
            PIO_INT_LEVEL = PIOC_LSR_VALUE
            PIO_INT_RE_HL = PIOC_REHLSR_VALUE
            PIO_INTERRUPT = PIO_C_INTERRUPT_USED
        />


        <@PIO_INITIALIZE
            PIO_PORT = "D"
            PIO_DIR = PIOD_OER_VALUE
            PIO_LAT_HIGH = PIOD_SODR_VALUE
            PIO_LAT_LOW = PIOD_CODR_VALUE
            PIO_OD = PIOD_MDER_VALUE
            PIO_PU = PIOD_PUER_VALUE
            PIO_PD = PIOD_PPDEN_VALUE
            PIO_PDR = PIOD_PDR_VALUE
            PIO_ABCD1 = PIOD_ABCDSR1_VALUE
            PIO_ABCD2 = PIOD_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOD_AIMER_VALUE
            PIO_INT_LEVEL = PIOD_LSR_VALUE
            PIO_INT_RE_HL = PIOD_REHLSR_VALUE
            PIO_INTERRUPT = PIO_D_INTERRUPT_USED
        />


        <@PIO_INITIALIZE
            PIO_PORT = "E"
            PIO_DIR = PIOE_OER_VALUE
            PIO_LAT_HIGH = PIOE_SODR_VALUE
            PIO_LAT_LOW = PIOE_CODR_VALUE
            PIO_OD = PIOE_MDER_VALUE
            PIO_PU = PIOE_PUER_VALUE
            PIO_PD = PIOE_PPDEN_VALUE
            PIO_PDR = PIOE_PDR_VALUE
            PIO_ABCD1 = PIOE_ABCDSR1_VALUE
            PIO_ABCD2 = PIOE_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOE_AIMER_VALUE
            PIO_INT_LEVEL = PIOE_LSR_VALUE
            PIO_INT_RE_HL = PIOE_REHLSR_VALUE
            PIO_INTERRUPT = PIO_E_INTERRUPT_USED
        />

    <#if (PIO_A_INTERRUPT_USED == true) || (PIO_B_INTERRUPT_USED == true) || (PIO_C_INTERRUPT_USED == true) || (PIO_D_INTERRUPT_USED == true) || (PIO_E_INTERRUPT_USED == true) >
    /* Initialize Interrupt Pin data structures */
        <#list 1..PIO_PIN_TOTAL as i>
            <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
            <#assign portChannel = "PIN_" + i + "_PIO_CHANNEL">
            <#assign portPosition = "PIN_" + i + "_PIO_PIN">
            <#if .vars[intConfig]?has_content>
                <#if (.vars[intConfig] != "Disabled")>
                    <#lt>    port${.vars[portChannel]}PinCbObj[port${.vars[portChannel]}CurNumCb].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                    <#lt>    port${.vars[portChannel]}PinCbObj[port${.vars[portChannel]}CurNumCb].callback = NULL;
                    <#lt>    port${.vars[portChannel]}CurNumCb++;
                </#if>
            </#if>
        </#list>
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
    void PIO_PortWrite (PIO_PORT port, uint32_t mask, uint32_t value);

  Summary:
    Write the value on the masked I/O lines of the selected port.

  Remarks:
    See plib_pio.h for more details.
*/
void PIO_PortWrite(PIO_PORT port, uint32_t mask, uint32_t value)
{
    ((pio_registers_t*)port)->PIO_ODSR = (((pio_registers_t*)port)->PIO_ODSR & (~mask)) | (mask & value);
}

// *****************************************************************************
/* Function:
    uint32_t PIO_PortLatchRead ( PIO_PORT port )

  Summary:
    Read the latched value on all the I/O lines of the selected port.

  Remarks:
    See plib_pio.h for more details.
*/
uint32_t PIO_PortLatchRead(PIO_PORT port)
{
    return ((pio_registers_t*)port)->PIO_ODSR;
}

// *****************************************************************************
/* Function:
    void PIO_PortSet ( PIO_PORT port, uint32_t mask )

  Summary:
    Set the selected IO pins of a port.

  Remarks:
    See plib_pio.h for more details.
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

  Remarks:
    See plib_pio.h for more details.
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

  Remarks:
    See plib_pio.h for more details.
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

  Remarks:
    See plib_pio.h for more details.
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

  Remarks:
    See plib_pio.h for more details.
*/
void PIO_PortOutputEnable(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_OER = mask;
}

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Remarks:
    See plib_pio.h for more details.
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

  Remarks:
    See plib_pio.h for more details.
*/
void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask)
{
    ((pio_registers_t*)port)->PIO_IDR = mask;
}

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
        uintptr_t context
    );

  Summary:
    Allows application to register callback for every pin.

  Remarks:
    See plib_pio.h for more details.
*/
void PIO_PinInterruptCallbackRegister(
    PIO_PIN pin,
    const PIO_PIN_CALLBACK callback,
    uintptr_t context
)
{
    uint8_t i;
    uint8_t portIndex;
    portIndex = pin >> 5;

    switch( portIndex )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case 0:
        {
            for(i=0; i<portACurNumCb; i++)
            {
                if (portAPinCbObj[i].pin == pin)
                {
                    portAPinCbObj[i].callback = callback;
                    portAPinCbObj[i].context  = context;
                    break;
                }
            }
            break;
        }
    </#if>
    <#if PIO_B_INTERRUPT_USED == true>
        case 1:
        {
            for(i=0; i<portBCurNumCb; i++)
            {
                if (portBPinCbObj[i].pin == pin)
                {
                    portBPinCbObj[i].callback = callback;
                    portBPinCbObj[i].context  = context;
                    break;
                }
            }
            break;
        }
    </#if>
    <#if PIO_C_INTERRUPT_USED == true>
        case 2:
        {
            for(i=0; i<portCCurNumCb; i++)
            {
                if (portCPinCbObj[i].pin == pin)
                {
                    portCPinCbObj[i].callback = callback;
                    portCPinCbObj[i].context  = context;
                    break;
                }
            }
            break;
        }
    </#if>
    <#if PIO_D_INTERRUPT_USED == true>
        case 3:
        {
            for(i=0; i<portDCurNumCb; i++)
            {
                if (portDPinCbObj[i].pin == pin)
                {
                    portDPinCbObj[i].callback = callback;
                    portDPinCbObj[i].context  = context;
                    break;
                }
            }
            break;
        }
    </#if>
    <#if PIO_E_INTERRUPT_USED == true>
        case 4:
        {
            for(i=0; i<portECurNumCb; i++)
            {
                if (portEPinCbObj[i].pin == pin)
                {
                    portEPinCbObj[i].callback = callback;
                    portEPinCbObj[i].context  = context;
                    break;
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
