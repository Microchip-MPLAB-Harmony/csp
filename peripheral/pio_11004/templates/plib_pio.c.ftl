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
*******************************************************************************/
//DOM-IGNORE-END

#include "plib_pio.h"

<#compress> <#-- To remove unwanted new lines -->

<#-- Find out which all port exists in the device -->
<#assign PORTA_EXISTS = PIO_A_INTERRUPT_USED??>
<#assign PORTB_EXISTS = PIO_B_INTERRUPT_USED??>
<#assign PORTC_EXISTS = PIO_C_INTERRUPT_USED??>
<#assign PORTD_EXISTS = PIO_D_INTERRUPT_USED??>
<#assign PORTE_EXISTS = PIO_E_INTERRUPT_USED??>

<#assign PIO_A_NUM_INT_PINS = 0>
<#assign PIO_B_NUM_INT_PINS = 0>
<#assign PIO_C_NUM_INT_PINS = 0>
<#assign PIO_D_NUM_INT_PINS = 0>
<#assign PIO_E_NUM_INT_PINS = 0>

<#if !PIO_SLEWR_PRESENT>
    <#assign PIOA_SLEWR_VALUE ="">
    <#assign PIOB_SLEWR_VALUE ="">
    <#assign PIOC_SLEWR_VALUE ="">
    <#assign PIOD_SLEWR_VALUE ="">
    <#assign PIOE_SLEWR_VALUE ="">
</#if>

<#if !PIO_DRIVER_PRESENT>
    <#assign PIOA_DRIVER_VALUE ="">
    <#assign PIOB_DRIVER_VALUE ="">
    <#assign PIOC_DRIVER_VALUE ="">
    <#assign PIOD_DRIVER_VALUE ="">
    <#assign PIOE_DRIVER_VALUE ="">
</#if>


<#list 1..PIO_PIN_TOTAL as i>
    <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">
    <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
    <#if .vars[intConfig]?has_content>
        <#if (.vars[intConfig] != "Disabled")>
            <#if (.vars[pinchannel] == "A")>
                <#assign PIO_A_NUM_INT_PINS = PIO_A_NUM_INT_PINS + 1>
            </#if>
            <#if (.vars[pinchannel] == "B")>
                <#assign PIO_B_NUM_INT_PINS = PIO_B_NUM_INT_PINS + 1>
            </#if>
            <#if (.vars[pinchannel] == "C")>
                <#assign PIO_C_NUM_INT_PINS = PIO_C_NUM_INT_PINS + 1>
            </#if>
            <#if (.vars[pinchannel] == "D")>
                <#assign PIO_D_NUM_INT_PINS = PIO_D_NUM_INT_PINS + 1>
            </#if>
            <#if (.vars[pinchannel] == "E")>
                <#assign PIO_E_NUM_INT_PINS = PIO_E_NUM_INT_PINS + 1>
            </#if>
        </#if>
    </#if>
</#list>

</#compress>
<#macro PIO_INITIALIZE PIO_PORT PIO_DIR PIO_LAT_HIGH PIO_OD PIO_PUEN PIO_PDEN PIO_PDR PIO_ABCD1
                       PIO_ABCD2 PIO_INT_TYPE PIO_INT_LEVEL PIO_INT_RE_HL PIO_INTERRUPT PIO_IFER PIO_IFSCER PIO_SCDR PIO_SLEWR PIO_DRIVER>
    <#lt>    /************************ PIO ${PIO_PORT} Initialization ************************/
    <#if (PIO_ABCD1 != "0" ) || (PIO_ABCD2 != "0")>
        <#lt>    /* PORT${PIO_PORT} Peripheral Function Selection */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[0]= 0x${PIO_ABCD1};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ABCDSR[1]= 0x${PIO_ABCD2};
    </#if>
    <#if PIO_PDR != "0">
        <#lt>    /* PORT${PIO_PORT} PIO Disable and Peripheral Enable*/
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PDR = 0x${PIO_PDR};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PER = ~0x${PIO_PDR};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PER = 0xFFFFFFFF;
    </#if>
    <#if PIO_OD != "0">
        <#lt>    /* PORT${PIO_PORT} Multi Drive or Open Drain Enable */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_MDER = 0x${PIO_OD};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_MDDR = ~0x${PIO_OD};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_MDDR = 0xFFFFFFFF;
    </#if>
    <#lt>    /* PORT${PIO_PORT} Pull Up Enable/Disable as per MHC selection */
    <#if PIO_PUEN != "0">
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUDR = ~0x${PIO_PUEN};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUER = 0x${PIO_PUEN};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PUDR = 0xFFFFFFFF;
    </#if>
    <#lt>    /* PORT${PIO_PORT} Pull Down Enable/Disable as per MHC selection */
    <#if PIO_PDEN != "0">
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDDR = ~0x${PIO_PDEN};
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDER = 0x${PIO_PDEN};
    <#else>
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_PPDDR = 0xFFFFFFFF;
    </#if>
    <#lt>    /* PORT${PIO_PORT} Output Write Enable */
    <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OWER = PIO_OWER_Msk;
    <#lt>    /* PORT${PIO_PORT} Output Direction Enable */
    <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_OER = 0x${PIO_DIR};
    <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ODR = ~0x${PIO_DIR};
    <#if PIO_LAT_HIGH != "0">
        <#lt>    /* PORT${PIO_PORT} Initial state High */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_ODSR = 0x${PIO_LAT_HIGH};
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
    <#if PIO_IFER != "0">
        <#lt>    /* PORT${PIO_PORT} Glitch/Debounce Filter Enable */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_IFER = 0x${PIO_IFER};
    </#if>
    <#if PIO_IFSCER != "0">
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_IFSCER = 0x${PIO_IFSCER};
        <#if PIO_SCDR != "0">
            <#lt>    /* PORT${PIO_PORT} Slow Clock Divider */
            <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_SCDR = 0x${PIO_SCDR};
        </#if>
    </#if>
    <#if PIO_SLEWR?has_content>
        <#lt>    /* PORT${PIO_PORT} Slew rate control */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_SLEWR = 0x${PIO_SLEWR};
    </#if>
    <#if PIO_DRIVER?has_content>
        <#lt>    /* PORT${PIO_PORT} drive control */
        <#lt>    ((pio_registers_t*)PIO_PORT_${PIO_PORT})->PIO_DRIVER = 0x${PIO_DRIVER};
    </#if>

</#macro>

<#if INTERRUPT_ACTIVE == true >
#define PIO_MAX_NUM_OF_CHANNELS     5
    <#assign numOfIntInA = PIO_A_NUM_INT_PINS>
    <#assign numOfIntInAB = PIO_A_NUM_INT_PINS + PIO_B_NUM_INT_PINS>
    <#assign numOfIntInABC = PIO_A_NUM_INT_PINS + PIO_B_NUM_INT_PINS + PIO_C_NUM_INT_PINS>
    <#assign numOfIntInABCD = PIO_A_NUM_INT_PINS + PIO_B_NUM_INT_PINS + PIO_C_NUM_INT_PINS + PIO_D_NUM_INT_PINS>
    <#assign numOfIntInABCDE = PIO_A_NUM_INT_PINS + PIO_B_NUM_INT_PINS + PIO_C_NUM_INT_PINS + PIO_D_NUM_INT_PINS + PIO_E_NUM_INT_PINS>

   <#lt>/* Array to store callback objects of each configured interrupt */
    <#lt>PIO_PIN_CALLBACK_OBJ portPinCbObj[${PIO_A_NUM_INT_PINS} + ${PIO_B_NUM_INT_PINS} + ${PIO_C_NUM_INT_PINS} + ${PIO_D_NUM_INT_PINS} + ${PIO_E_NUM_INT_PINS}];

    <#lt>/* Array to store number of interrupts in each PORT Channel + previous interrupt count */
    <#lt>uint8_t portNumCb[PIO_MAX_NUM_OF_CHANNELS + 1] = {0, ${numOfIntInA}, ${numOfIntInAB}, ${numOfIntInABC}, ${numOfIntInABCD}, ${numOfIntInABCDE}};
</#if>

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
    <#if CCFG_SYSIO_PRESENT>
    <#if PIO_CCFG_SYSIO_VALUE != "0">
        <#lt>    /* Selected System IO pins are configured as GPIO */
        <#lt>    MATRIX_REGS->CCFG_SYSIO |= 0x${PIO_CCFG_SYSIO_VALUE};
    </#if>
    </#if>

    <#if PORTA_EXISTS == true>
        <@PIO_INITIALIZE
            PIO_PORT = "A"
            PIO_DIR = PIOA_OER_VALUE
            PIO_LAT_HIGH = PIOA_SODR_VALUE
            PIO_OD = PIOA_MDER_VALUE
            PIO_PUEN = PIOA_PUER_VALUE
            PIO_PDEN = PIOA_PPDEN_VALUE
            PIO_PDR = PIOA_PDR_VALUE
            PIO_ABCD1 = PIOA_ABCDSR1_VALUE
            PIO_ABCD2 = PIOA_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOA_AIMER_VALUE
            PIO_INT_LEVEL = PIOA_LSR_VALUE
            PIO_INT_RE_HL = PIOA_REHLSR_VALUE
            PIO_INTERRUPT = PIO_A_INTERRUPT_USED
            PIO_IFER = PIOA_IFER_VALUE
            PIO_IFSCER = PIOA_IFSCER_VALUE
            PIO_SCDR = PIOA_SCDR_VALUE
            PIO_SLEWR = PIOA_SLEWR_VALUE
            PIO_DRIVER = PIOA_DRIVER_VALUE
        />
    </#if>
    <#if PORTB_EXISTS == true>
        <@PIO_INITIALIZE
            PIO_PORT = "B"
            PIO_DIR = PIOB_OER_VALUE
            PIO_LAT_HIGH = PIOB_SODR_VALUE
            PIO_OD = PIOB_MDER_VALUE
            PIO_PUEN = PIOB_PUER_VALUE
            PIO_PDEN = PIOB_PPDEN_VALUE
            PIO_PDR = PIOB_PDR_VALUE
            PIO_ABCD1 = PIOB_ABCDSR1_VALUE
            PIO_ABCD2 = PIOB_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOB_AIMER_VALUE
            PIO_INT_LEVEL = PIOB_LSR_VALUE
            PIO_INT_RE_HL = PIOB_REHLSR_VALUE
            PIO_INTERRUPT = PIO_B_INTERRUPT_USED
            PIO_IFER = PIOB_IFER_VALUE
            PIO_IFSCER = PIOB_IFSCER_VALUE
            PIO_SCDR = PIOB_SCDR_VALUE
            PIO_SLEWR = PIOB_SLEWR_VALUE
            PIO_DRIVER = PIOB_DRIVER_VALUE
        />
    </#if>
    <#if PORTC_EXISTS == true>
        <@PIO_INITIALIZE
            PIO_PORT = "C"
            PIO_DIR = PIOC_OER_VALUE
            PIO_LAT_HIGH = PIOC_SODR_VALUE
            PIO_OD = PIOC_MDER_VALUE
            PIO_PUEN = PIOC_PUER_VALUE
            PIO_PDEN = PIOC_PPDEN_VALUE
            PIO_PDR = PIOC_PDR_VALUE
            PIO_ABCD1 = PIOC_ABCDSR1_VALUE
            PIO_ABCD2 = PIOC_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOC_AIMER_VALUE
            PIO_INT_LEVEL = PIOC_LSR_VALUE
            PIO_INT_RE_HL = PIOC_REHLSR_VALUE
            PIO_INTERRUPT = PIO_C_INTERRUPT_USED
            PIO_IFER = PIOC_IFER_VALUE
            PIO_IFSCER = PIOC_IFSCER_VALUE
            PIO_SCDR = PIOC_SCDR_VALUE
            PIO_SLEWR = PIOC_SLEWR_VALUE
            PIO_DRIVER = PIOC_DRIVER_VALUE
        />
    </#if>
    <#if PORTD_EXISTS == true>
        <@PIO_INITIALIZE
            PIO_PORT = "D"
            PIO_DIR = PIOD_OER_VALUE
            PIO_LAT_HIGH = PIOD_SODR_VALUE
            PIO_OD = PIOD_MDER_VALUE
            PIO_PUEN = PIOD_PUER_VALUE
            PIO_PDEN = PIOD_PPDEN_VALUE
            PIO_PDR = PIOD_PDR_VALUE
            PIO_ABCD1 = PIOD_ABCDSR1_VALUE
            PIO_ABCD2 = PIOD_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOD_AIMER_VALUE
            PIO_INT_LEVEL = PIOD_LSR_VALUE
            PIO_INT_RE_HL = PIOD_REHLSR_VALUE
            PIO_INTERRUPT = PIO_D_INTERRUPT_USED
            PIO_IFER = PIOD_IFER_VALUE
            PIO_IFSCER = PIOD_IFSCER_VALUE
            PIO_SCDR = PIOD_SCDR_VALUE
            PIO_SLEWR = PIOD_SLEWR_VALUE
            PIO_DRIVER = PIOD_DRIVER_VALUE
            />
    </#if>
    <#if PORTE_EXISTS == true>
        <@PIO_INITIALIZE
            PIO_PORT = "E"
            PIO_DIR = PIOE_OER_VALUE
            PIO_LAT_HIGH = PIOE_SODR_VALUE
            PIO_OD = PIOE_MDER_VALUE
            PIO_PUEN = PIOE_PUER_VALUE
            PIO_PDEN = PIOE_PPDEN_VALUE
            PIO_PDR = PIOE_PDR_VALUE
            PIO_ABCD1 = PIOE_ABCDSR1_VALUE
            PIO_ABCD2 = PIOE_ABCDSR2_VALUE
            PIO_INT_TYPE = PIOE_AIMER_VALUE
            PIO_INT_LEVEL = PIOE_LSR_VALUE
            PIO_INT_RE_HL = PIOE_REHLSR_VALUE
            PIO_INTERRUPT = PIO_E_INTERRUPT_USED
            PIO_IFER = PIOE_IFER_VALUE
            PIO_IFSCER = PIOE_IFSCER_VALUE
            PIO_SCDR = PIOE_SCDR_VALUE
            PIO_SLEWR = PIOE_SLEWR_VALUE
            PIO_DRIVER = PIOE_DRIVER_VALUE
        />
    </#if>
    <#if INTERRUPT_ACTIVE >
    uint32_t i;
    /* Initialize Interrupt Pin data structures */
        <#assign portCurNumCb_A = 0>
        <#assign portCurNumCb_B = 0>
        <#assign portCurNumCb_C = 0>
        <#assign portCurNumCb_D = 0>
        <#assign portCurNumCb_E = 0>
        <#list 1..PIO_PIN_TOTAL as i>
            <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
            <#assign portChannel = "PIN_" + i + "_PIO_CHANNEL">
            <#assign portPosition = "PIN_" + i + "_PIO_PIN">
            <#if .vars[intConfig]?has_content>
                <#if (.vars[intConfig] != "Disabled")>
                    <#if (.vars[portChannel] == "A")>
                        <#lt>    portPinCbObj[${portCurNumCb_A}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                        <#lt>    <#assign portCurNumCb_A = portCurNumCb_A + 1>
                    <#elseif (.vars[portChannel] == "B")>
                        <#lt>    portPinCbObj[${numOfIntInA} + ${portCurNumCb_B}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                        <#lt>    <#assign portCurNumCb_B = portCurNumCb_B + 1>
                    <#elseif (.vars[portChannel] == "C")>
                        <#lt>    portPinCbObj[${numOfIntInAB} + ${portCurNumCb_C}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                        <#lt>    <#assign portCurNumCb_C = portCurNumCb_C + 1>
                    <#elseif (.vars[portChannel] == "D")>
                        <#lt>    portPinCbObj[${numOfIntInABC} + ${portCurNumCb_D}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                        <#lt>    <#assign portCurNumCb_D = portCurNumCb_D + 1>
                    <#elseif (.vars[portChannel] == "E")>
                        <#lt>    portPinCbObj[${numOfIntInABCD} + ${portCurNumCb_E}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                        <#lt>    <#assign portCurNumCb_E = portCurNumCb_E + 1>
                    </#if>
                </#if>
            </#if>
        </#list>
        <#lt>    for(i=0; i<${numOfIntInABCDE}; i++)
        <#lt>    {
        <#lt>        portPinCbObj[i].callback = NULL;
        <#lt>    }
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

<#if INTERRUPT_ACTIVE >
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
    bool PIO_PinInterruptCallbackRegister(
        PIO_PIN pin,
        const PIO_PIN_CALLBACK callback,
        uintptr_t context
    );

  Summary:
    Allows application to register callback for configured pin.

  Remarks:
    See plib_pio.h for more details.
*/
bool PIO_PinInterruptCallbackRegister(
    PIO_PIN pin,
    const PIO_PIN_CALLBACK callback,
    uintptr_t context
)
{
    uint8_t i;
    uint8_t portIndex;

    portIndex = pin >> 5;

    for(i = portNumCb[portIndex]; i < portNumCb[portIndex +1]; i++)
    {
        if (portPinCbObj[i].pin == pin)
        {
            portPinCbObj[i].callback = callback;
            portPinCbObj[i].context  = context;
            return true;
        }
    }
    return false;
}
<#if INTERRUPT_ACTIVE >
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
	It is an internal function used by the library, user should not call it.
*/
void _PIO_Interrupt_Handler ( PIO_PORT port )
{
    uint32_t status;
    uint32_t i, portIndex;

    status  = ((pio_registers_t*)port)->PIO_ISR;
    status &= ((pio_registers_t*)port)->PIO_IMR;

    /* get the index of the port channel: PIO_PORT_A--> 0, PIO_PORT_B--> 1 ... */
    portIndex = (port - PIOA_BASE_ADDRESS) >> 9;

    /* Check pending events and call callback if registered */
    for(i = portNumCb[portIndex]; i < portNumCb[portIndex +1]; i++)
    {
        if((status & (1 << (portPinCbObj[i].pin & 0x1F))) && (portPinCbObj[i].callback != NULL))
        {
            portPinCbObj[i].callback (portPinCbObj[i].pin, portPinCbObj[i].context);
        }
    }

}
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Interrupt Service Routine (ISR) Implementation(s)
// *****************************************************************************
// *****************************************************************************
</#if>
<#if PIO_A_INTERRUPT_USED??>
<#if PIO_A_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="A"
    />
</#if>
</#if>
<#if PIO_B_INTERRUPT_USED??>
<#if PIO_B_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="B"
    />
</#if>
</#if>

<#if PIO_C_INTERRUPT_USED??>
<#if PIO_C_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="C"
    />
</#if>
</#if>

<#if PIO_C_INTERRUPT_USED??>
<#if PIO_D_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="D"
    />
</#if>
</#if>

<#if PIO_E_INTERRUPT_USED??>
<#if PIO_E_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER
        PIO_CHANNEL="E"
    />
</#if>
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
