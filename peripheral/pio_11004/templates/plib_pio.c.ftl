/*******************************************************************************
  SYS PORTS Static Functions for PORTS System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.c

  Summary:
    PIO function implementations for the Ports plib.

  Description:
    The PIO Plib provides a simple interface to manage peripheral
    input-output controller.

*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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
                       PIO_ABCD2 PIO_INT PIO_INT_TYPE PIO_INT_EDGE PIO_INT_RE_HL PIO_INTERRUPT>
    /* PORT${PIO_PORT} ABCD 1 */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_ABCDSR[0].w = ${PIO_ABCD1};
    /* PORT${PIO_PORT} ABCD 2 */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_ABCDSR[1].w = ${PIO_ABCD2};
    /* PORT${PIO_PORT} Pio enable */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PDR.w = ~${PIO_PER};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PER.w = ${PIO_PER};
    /* PORT${PIO_PORT} Active state */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_CODR.w = ~${PIO_LAT};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_SODR.w = ${PIO_LAT};
    /* PORT${PIO_PORT} Open drain state */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_MDDR.w = ~${PIO_OD};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_MDER.w = ${PIO_OD};
    /* PORT${PIO_PORT} Pull Up */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PUDR.w = ~${PIO_PU};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PUER.w = ${PIO_PU};
    /* PORT${PIO_PORT} Pull Down */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PPDDR.w = ~${PIO_PD};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_PPDER.w = ${PIO_PD};
    /* PORT${PIO_PORT} Direction */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_ODR.w = ~${PIO_DIR};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_OER.w = ${PIO_DIR};
<#if PIO_INTERRUPT == true>
    /* PORT${PIO_PORT} system level interrupt enable */
    SYS_INT_SourceEnable(PORT${PIO_PORT}_IRQn);
    /* PORT${PIO_PORT} Type of interrupt(alternate) */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_AIMDR.w = ~${PIO_INT_TYPE};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_AIMER.w = ${PIO_INT_TYPE};
    /* PORT${PIO_PORT} If edge, type of edge */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_LSR.w = ~${PIO_INT_EDGE};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_ESR.w = ${PIO_INT_EDGE};
    /* PORT${PIO_PORT} Rising/high level */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_FELLSR.w = ~${PIO_INT_RE_HL};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_REHLSR.w = ${PIO_INT_RE_HL};
    /* PORT${PIO_PORT} module level Interrupt enable */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_IDR.w = ~${PIO_INT};
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_IER.w = ${PIO_INT};
<#else>
    /* PORT${PIO_PORT} module level Interrupt disable */
    ((port_registers_t*)PIO_PORT_${PIO_PORT})->PORT_IDR.w = ~${PIO_INT};
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

/******************************************************************************
  Function:
    PIO_Initialize ( void )

  Summary:
    Initialize the PIO library.
  
  Description:
    This function initializes the PIO library and all ports and pins configured
    in the MCC Pin Manager.

  Remarks:
    None.
*/
void PIO_Initialize ( void )
{
    <#if PIO_CCFG_SYSIO_VALUE?has_content>
        <#lt>   /* Initialize the Debug pins as GPIO pins */
        <#lt>   _MATRIX_REGS->CCFG_SYSIO.w |= ${PIO_CCFG_SYSIO_VALUE};
    </#if>

    <#if PIO_A_USED == true>
        <#lt>   /********** PORT A Initialization **********/
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
            PIO_INT = "${PIOA_IER_VALUE}"
            PIO_INT_TYPE = "${PIOA_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOA_ESR_VALUE}"
            PIO_INT_RE_HL = "${PIOA_REHLSR_VALUE}"
            PIO_INTERRUPT = PIO_A_INTERRUPT_USED
        />
    </#if>

    <#if PIO_B_USED == true>
        <#lt>   /********** PORT B Initialization **********/
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
            PIO_INT = "${PIOB_IER_VALUE}"
            PIO_INT_TYPE = "${PIOB_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOB_ESR_VALUE}"
            PIO_INT_RE_HL = "${PIOB_REHLSR_VALUE}"
            PIO_INTERRUPT = PIO_B_INTERRUPT_USED
        />
    </#if>

    <#if PIO_C_USED == true>
        <#lt>   /********** PORT C Initialization **********/
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
            PIO_INT = "${PIOC_IER_VALUE}"
            PIO_INT_TYPE = "${PIOC_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOC_ESR_VALUE}"
            PIO_INT_RE_HL = "${PIOC_REHLSR_VALUE}"
            PIO_INTERRUPT = PIO_C_INTERRUPT_USED
        />
    </#if>

    <#if PIO_D_USED == true>
        <#lt>   /********** PORT D Initialization **********/
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
            PIO_INT = "${PIOD_IER_VALUE}"
            PIO_INT_TYPE = "${PIOD_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOD_ESR_VALUE}"
            PIO_INT_RE_HL = "${PIOD_REHLSR_VALUE}"
            PIO_INTERRUPT = PIO_D_INTERRUPT_USED
        />
    </#if>

    <#if PIO_E_USED == true>
        <#lt>   /********** PORT E Initialization **********/
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
            PIO_INT = "${PIOE_IER_VALUE}"
            PIO_INT_TYPE = "${PIOE_AIMER_VALUE}"
            PIO_INT_EDGE = "${PIOE_ESR_VALUE}"
            PIO_INT_RE_HL = "${PIOE_REHLSR_VALUE}"
            PIO_INTERRUPT = PIO_E_INTERRUPT_USED
        />
    </#if>

    /* Analog pins Initialization */
    _AFEC0_REGS->AFEC_CHER.w = ${PIO_AFEC0_CHER_VALUE};
    _AFEC1_REGS->AFEC_CHER.w = ${PIO_AFEC1_CHER_VALUE};
    _DACC_REGS->DACC_CHER.w = ${PIO_DACC_CHER_VALUE};
}

// *****************************************************************************
// *****************************************************************************
// Section: PIO APIs which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PIO_PinWrite(PIO_PIN pin, bool value)

  Summary:
    Writes the selected pin.
  
  Description:
    This function writes/drives the "value" on the selected I/O line/pin.
  
  Remarks:
	None.
*/
void PIO_PinWrite(PIO_PIN pin, bool value)
{
    uint32_t portIndex, port, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    if (value == false)
    {
        ((port_registers_t*)port)->PORT_CODR.w = 1 << bitPos;
    }
    else
    {
        ((port_registers_t*)port)->PORT_SODR.w = 1 << bitPos;
    }
}

// *****************************************************************************
/* Function:
    bool PIO_PinRead(PIO_PIN pin)

  Summary:
    Read the selected pin value.
  
  Description:
    This function reads the selected pin value.
    it reads the value regardless of pin configuration, whether uniquely as an
    input, or driven by the PIO Controller, or driven by peripheral.

  Remarks:
	To read the latched value on this pin, PIO_PinReadLatch API should be used.
*/
bool PIO_PinRead(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    return (bool)((((port_registers_t*)port)->PORT_PDSR.w >> bitPos) & 0x00000001);
}

// *****************************************************************************
/* Function:
    bool PIO_PinReadLatch ( PIO_PIN pin )
  
  Summary:
    Read the value driven on the selected pin.
  
  Description:
    This function reads the data driven on the selected I/O line/pin.
    Whatever data is written/driven on I/O line by using any of the PIO PLIB
    APIs, will be read by this API.

  Remarks:
	To read actual pin value, PIO_PinRead API should be used.
*/
bool PIO_PinReadLatch(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    return (bool)((((port_registers_t*)port)->PORT_ODSR.w >> bitPos) & 0x00000001);
}

// *****************************************************************************
/* Function:
    void PIO_PinToggle(PIO_PIN pin)

  Summary:
    Toggles the selected pin.

  Description:
    This function toggles/inverts the value on the selected I/O line/pin.

  Remarks:
	None.
*/
void PIO_PinToggle(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    if ( ((((port_registers_t*)port)->PORT_ODSR.w >> bitPos) & 1) == 1 )
    {
        ((port_registers_t*)port)->PORT_CODR.w = 1 << bitPos;
    }
    else
    {
        ((port_registers_t*)port)->PORT_SODR.w = 1 << bitPos;
    }
}

// *****************************************************************************
/* Function:
    void PIO_PinSet(PIO_PIN pin)

  Summary:
    Sets the selected pin.

  Description:
    This function drives '1' on the selected I/O line/pin.

  Remarks:
	None.
*/
void PIO_PinSet(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    ((port_registers_t*)port)->PORT_SODR.w = 1 << bitPos;
}

// *****************************************************************************
/* Function:
    void PIO_PinClear(PIO_PIN pin)

  Summary:
    Clears the selected pin.

  Description:
    This function drives '0' on the selected I/O line/pin.

  Remarks:
	None.
*/
void PIO_PinClear(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    ((port_registers_t*)port)->PORT_CODR.w = 1 << bitPos;
}

// *****************************************************************************
/* Function:
    void PIO_PinInterruptEnable(PIO_PIN pin, PIO_INTERRUPT_TYPE interruptType)

  Summary:
    Enables IO interrupt on selected IO pin.

  Description:
    This function enables selected type of IO interrupt on selected IO pin.

  Remarks:
	None.
*/
void PIO_PinInterruptEnable(PIO_PIN pin, PIO_INTERRUPT_TYPE interruptType)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    PIO_PortInterruptEnable(port, 1 << bitPos, interruptType);
}

// *****************************************************************************
/* Function:
    void PIO_PinInterruptDisable(PIO_PIN pin)

  Summary:
    Disables IO interrupt on selected IO pin.     

  Description:
    This function disables IO interrupt on selected IO pin.

  Remarks:
	None.
*/
void PIO_PinInterruptDisable(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    ((port_registers_t*)port)->PORT_IDR.w = 1 << bitPos;
}

// *****************************************************************************
/* Function:
    void PIO_PinInputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as input.

  Description:
    This function enables selected IO pin as input.

  Remarks:
	None.
*/
void PIO_PinInputEnable(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    ((port_registers_t*)port)->PORT_ODR.w = 1 << bitPos;
}

// *****************************************************************************
/* Function:
    void PIO_PinOutputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as output.

  Description:
    This function enables selected IO pin as output.

  Remarks:
	None.
*/
void PIO_PinOutputEnable(PIO_PIN pin)
{
    uint32_t port, portIndex, bitPos;

    portIndex = pin >> 5;
    bitPos = pin & 0x1F;
    port = _PORTA_BASE_ADDRESS + (0x200 * portIndex);
    
    ((port_registers_t*)port)->PORT_OER.w = 1 << bitPos;
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
    Read all the I/O lines of the selected port port.
  
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
    return ((port_registers_t*)port)->PORT_PDSR.w;
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
    /* Enable write to the selected port */
    ((port_registers_t*)port)->PORT_OWER.w = PORT_OWER_Msk;

    /* Write the desired value */
    ((port_registers_t*)port)->PORT_ODSR.w = value;
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
    return ((port_registers_t*)port)->PORT_ODSR.w;
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
    ((port_registers_t*)port)->PORT_SODR.w = mask;
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
    ((port_registers_t*)port)->PORT_CODR.w = mask;
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
    uint32_t statusReg = 0;

    statusReg = ((port_registers_t*)port)->PORT_ODSR.w;

    /* Write into Clr and Set registers */
    ((port_registers_t*)port)->PORT_CODR.w = ( mask & (statusReg));
    ((port_registers_t*)port)->PORT_SODR.w = ( mask & (~statusReg));
}

// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(
        PIO_PORT port,
        uint32_t mask,
        PIO_INTERRUPT_TYPE interruptType
        )

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Description:
    This function enables IO interrupt on selected IO pins of selected port.

  Remarks:
	None.
*/
void PIO_PortInterruptEnable(
    PIO_PORT port,
    uint32_t mask,
    PIO_INTERRUPT_TYPE interruptType
    )
{
    switch (interruptType)
    {
        case PIO_INTERRUPT_RISING_EDGE:
            ((port_registers_t*)port)->PORT_AIMER.w = mask;
            ((port_registers_t*)port)->PORT_ESR.w = mask;
            ((port_registers_t*)port)->PORT_REHLSR.w = mask;
            break;

        case PIO_INTERRUPT_FALLING_EDGE:
            ((port_registers_t*)port)->PORT_AIMER.w = mask;
            ((port_registers_t*)port)->PORT_ESR.w = mask;
            ((port_registers_t*)port)->PORT_FELLSR.w = mask;
            break;

        case PIO_INTERRUPT_HIGH_LEVEL:
            ((port_registers_t*)port)->PORT_AIMER.w = mask;
            ((port_registers_t*)port)->PORT_LSR.w = mask;
            ((port_registers_t*)port)->PORT_REHLSR.w = mask;
            break;

        case PIO_INTERRUPT_LOW_LEVEL:
            ((port_registers_t*)port)->PORT_AIMER.w = mask;
            ((port_registers_t*)port)->PORT_LSR.w = mask;
            ((port_registers_t*)port)->PORT_FELLSR.w = mask;
            break;
            
        case PIO_INTERRUPT_BOTH_EDGE:
            /* For both the edge interrupts, we have to disable additional interrupt */
            ((port_registers_t*)port)->PORT_AIMDR.w = mask;
            break;
        default:
            break;
    }
    
    ((port_registers_t*)port)->PORT_IER.w = mask;
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
    ((port_registers_t*)port)->PORT_IDR.w = mask;
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
    ((port_registers_t*)port)->PORT_ODR.w = mask;
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
    ((port_registers_t*)port)->PORT_OER.w = mask;
}

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >

// *****************************************************************************
/* Function:
    void PIO_PinCallbackRegister(
        PIO_PIN pin, 
        const PIO_EVENT_HANDLER_PIN callback,
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
void PIO_PinCallbackRegister(
    PIO_PIN pin, 
    const PIO_EVENT_HANDLER_PIN callback,
    void* context
)
{
    uint32_t portIndex;
    uint8_t  bitPosition;
    
    portIndex = pin >> 5;
    bitPosition = (uint8_t) (pin & 0x1F);
    
    switch( portIndex )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case 0:
        {
            if( portACurNumCb < portAMaxNumCb )
            {
                portAPinCbObj[ portACurNumCb ].bitPosition   = bitPosition;
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
                portBPinCbObj[ portBCurNumCb ].bitPosition   = bitPosition;
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
                portCPinCbObj[ portCCurNumCb ].bitPosition   = bitPosition;
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
                portDPinCbObj[ portDCurNumCb ].bitPosition   = bitPosition;
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
                portEPinCbObj[ portECurNumCb ].bitPosition   = bitPosition;
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

    status  = ((port_registers_t*)port)->PORT_ISR.w;
    status &= ((port_registers_t*)port)->PORT_IMR.w;

    /* Check pending events */
    switch( port )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case PIO_PORT_A:
        {
            for( i = 0; i < portACurNumCb; i++ )
            {
                if( ( status & ( 1 << (portAPinCbObj[i].bitPosition) ) ) &&
                    portAPinCbObj[i].callback != NULL )
                {
                    portAPinCbObj[i].callback ( portAPinCbObj[i].context );
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
                if( ( status & ( 1 << (portBPinCbObj[i].bitPosition) ) ) &&
                    portBPinCbObj[i].callback != NULL )
                {
                    portBPinCbObj[i].callback ( portBPinCbObj[i].context );
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
                if( ( status & ( 1 << (portCPinCbObj[i].bitPosition) ) ) &&
                    portCPinCbObj[i].callback != NULL )
                {
                    portCPinCbObj[i].callback ( portCPinCbObj[i].context );
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
                if( ( status & ( 1 << (portDPinCbObj[i].bitPosition) ) ) &&
                    portDPinCbObj[i].callback != NULL )
                {
                    portDPinCbObj[i].callback ( portDPinCbObj[i].context );
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
                if( ( status & ( 1 << (portEPinCbObj[i].bitPosition) ) ) &&
                    portEPinCbObj[i].callback != NULL )
                {
                    portEPinCbObj[i].callback ( portEPinCbObj[i].context );
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
/*******************************************************************************
 End of File
*/
