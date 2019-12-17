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

<#-- Initialize variables -->
<#assign TOTAL_NUM_OF_INT_USED = 0>
<#assign portNumCbList = [0]>

<#list 0..PORT_CHANNEL_TOTAL-1 as i>
  <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
  <@"<#assign PORT_${.vars[channel]}_NUM_INT_PINS = 0>"?interpret />
</#list>

<#list 1..PIO_PIN_TOTAL as i>
    <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">
    <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
    <#if .vars[intConfig]?has_content>
        <#if (.vars[intConfig] != "Disabled")>
          <@"<#assign PORT_${.vars[pinchannel]}_NUM_INT_PINS = PORT_${.vars[pinchannel]}_NUM_INT_PINS + 1>"?interpret />
        </#if>
    </#if>
</#list>

<#-- count total number of active interrupts and save it in variable -->
<#list 0..PORT_CHANNEL_TOTAL-1 as i>
    <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
    <@"<#assign TOTAL_NUM_OF_INT_USED = TOTAL_NUM_OF_INT_USED + PORT_${.vars[channel]}_NUM_INT_PINS>"?interpret />
    <@"<#assign port${.vars[channel]}IndexStart = 0>"?interpret />
</#list>
</#compress>
<#-- Create a list of indexes and use it as initialization values for portNumCb array -->
<#if TOTAL_NUM_OF_INT_USED gt 0 >
    <#list 1..PORT_CHANNEL_TOTAL-1 as i>
        <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
        <#assign prevChannel = "PORT_CHANNEL_" + (i - 1) + "_NAME">
        <#if .vars[channel]?has_content>
            <@"<#assign port${.vars[channel]}IndexStart = port${.vars[prevChannel]}IndexStart + PORT_${.vars[prevChannel]}_NUM_INT_PINS>"?interpret />
            <@"<#assign portNumCbList = portNumCbList + [port${.vars[channel]}IndexStart]>"?interpret />
        </#if>
    </#list>
    <#assign portNumCbList = portNumCbList + [TOTAL_NUM_OF_INT_USED] >

    <#lt>/* Array to store callback objects of each configured interrupt */
    <#lt>PIO_PIN_CALLBACK_OBJ portPinCbObj[${TOTAL_NUM_OF_INT_USED}];

    <#lt>/* Array to store number of interrupts in each PORT Channel + previous interrupt count */
    <@compress single_line=true>
        <#lt>uint8_t portNumCb[${PORT_CHANNEL_TOTAL} + 1] = {
                                                                <#list portNumCbList as i>
                                                                    ${i},
                                                                </#list>
                                                            };
    </@compress>

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
<#assign PORT = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] >
<#assign PERFUNC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "GPIO"] >
<#list PORT as port>
	<#list PERFUNC as func>
	<#assign PORT_MSKR = "PORT_" + port + "_MSKR_Value" + func >
	<#assign PORT_CFGR = "FUNC_" + func + "_CFGR_Value">  
	<#if .vars[PORT_MSKR] != '0x0' && .vars[PORT_MSKR] != '0x0L'>
	<#lt> /* Port ${port} Peripheral function ${func} configuration */
	<#lt>	PIO${port}_REGS->PIO_MSKR = ${.vars[PORT_MSKR]};
	<#lt>	PIO${port}_REGS->PIO_CFGR = ${.vars[PORT_CFGR]};
	
	</#if>   
	</#list>
	<#list 0..31 as pin>
	<#assign PORT_MSKR = "PORT_" + port + "_MSKR_Value" + pin >
	<#assign PORT_CFGR = "PORT_" + port + "_CFGR_Value" + pin > 
	<#if .vars[PORT_CFGR] != '0x0'>
	<#lt> /* Port ${port} Pin ${pin} configuration */
	<#lt>	PIO${port}_REGS->PIO_MSKR = ${.vars[PORT_MSKR]};
	<#lt>	PIO${port}_REGS->PIO_CFGR = (PIO${port}_REGS->PIO_CFGR & (PIO_CFGR_FUNC_Msk)) | ${.vars[PORT_CFGR]};
	
	</#if>   
	</#list>
	<#assign PORT_LATCH = "PORT_" + port + "_LATCH" >
	<#if .vars[PORT_LATCH] != '0x0'>
	<#lt> /* Port ${port} Latch configuration */
	<#lt>	PIO${port}_REGS->PIO_SODR = ${.vars[PORT_LATCH]};
	
	</#if>
	<#assign PORT_SLCK = "PORT_" + port + "_SCLK_DIV" >
	<#if .vars[PORT_SLCK] != 0>
	<#lt> /* Port ${port} Slow clock Divider configuration */
	<#lt>	PIO${port}_REGS->PIO_SCDR = ${.vars[PORT_SLCK]};
	
	</#if>

	<#assign PORT_ISR = "PORT_" + port + "_NUM_INT_PINS" >
	<#if .vars[PORT_ISR] != 0>
    /* Clear the ISR register */ 
	<#lt>	(uint32_t)PIO${port}_REGS->PIO_ISR;
  </#if>	
</#list>

<#if TOTAL_NUM_OF_INT_USED gt 0>
    uint32_t i;
    /* Initialize Interrupt Pin data structures */
    <#list 0..PORT_CHANNEL_TOTAL-1 as i>
        <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
        <#if .vars[channel]?has_content>
            <@"<#assign portCurNumCb_${.vars[channel]} = 0>"?interpret />
        </#if>
    </#list>
    <#list 1..PIO_PIN_TOTAL as i>
        <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
        <#assign portChannel = "PIN_" + i + "_PIO_CHANNEL">
        <#assign portPosition = "PIN_" + i + "_PIO_PIN">
        <#if .vars[intConfig]?has_content>
            <#if (.vars[intConfig] != "Disabled")>
                <#lt>    portPinCbObj[${.vars["port${.vars[portChannel]}IndexStart"]} + ${.vars["portCurNumCb_${.vars[portChannel]}"]}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                <#lt>    <@"<#assign portCurNumCb_${.vars[portChannel]} = portCurNumCb_${.vars[portChannel]} + 1>"?interpret />
            </#if>
        </#if>
    </#list>
    <#lt>    for(i=0; i<${TOTAL_NUM_OF_INT_USED}; i++)
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
    return ((pio_group_registers_t*)port)->PIO_PDSR;
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
    ((pio_group_registers_t*)port)->PIO_MSKR = mask;
    ((pio_group_registers_t*)port)->PIO_ODSR = value;
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
    return ((pio_group_registers_t*)port)->PIO_ODSR;
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
    ((pio_group_registers_t*)port)->PIO_SODR = mask;
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
    ((pio_group_registers_t*)port)->PIO_CODR = mask;
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
    ((pio_group_registers_t*)port)->PIO_MSKR = mask;
    ((pio_group_registers_t*)port)->PIO_ODSR ^= mask;
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
    ((pio_group_registers_t*)port)->PIO_MSKR = mask;
    ((pio_group_registers_t*)port)->PIO_CFGR &= ~(1 << PIO_CFGR_DIR_Pos);	
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
    ((pio_group_registers_t*)port)->PIO_MSKR = mask;
    ((pio_group_registers_t*)port)->PIO_CFGR |= (1 << PIO_CFGR_DIR_Pos);
}
<#if PORT_A_INTERRUPT_USED == true ||
     PORT_B_INTERRUPT_USED == true ||
     PORT_C_INTERRUPT_USED == true ||
     PORT_D_INTERRUPT_USED == true ||
     PORT_E_INTERRUPT_USED == true ||
     PORT_F_INTERRUPT_USED == true ||
     PORT_G_INTERRUPT_USED == true >
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
    ((pio_group_registers_t*)port)->PIO_IER = mask;
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
    ((pio_group_registers_t*)port)->PIO_IDR = mask;
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
    Allows application to register callback for every pin.

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

// *****************************************************************************
// *****************************************************************************
// Section: Interrupt Service Routine (ISR) Implementation(s)
// *****************************************************************************
// *****************************************************************************
</#if>

<#list 0..PORT_CHANNEL_TOTAL-1 as i>
    <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if .vars["PORT_${.vars[channel]}_INTERRUPT_USED"] == true>
// *****************************************************************************
/* Function:
    void PIO${.vars[channel]}_InterruptHandler (void)

  Summary:
    Interrupt handler for PORT${.vars[channel]}.

  Description:
    This function defines the Interrupt service routine for PORT${.vars[channel]}.
    This is the function which by default gets into Interrupt Vector Table.

  Remarks:
    User should not call this function.
*/
void PIO${.vars[channel]}_InterruptHandler(void)
{
    uint32_t status;
    uint8_t j;

    status  = PIO${.vars[channel]}_REGS->PIO_ISR;
    status &= PIO${.vars[channel]}_REGS->PIO_IMR;
	
	for( j = ${portNumCbList[i]}; j < ${portNumCbList[i+1]}; j++ )
	{
		if((status & ( 1 << (portPinCbObj[j].pin & 0x1F) ) ) && (portPinCbObj[j].callback != NULL))
		{
			portPinCbObj[j].callback ( portPinCbObj[j].pin, portPinCbObj[j].context );
		}
	}   
}
        </#if>
    </#if>
</#list>

/*******************************************************************************
 End of File
*/
