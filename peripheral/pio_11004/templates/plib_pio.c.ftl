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
#include "plib_pio_local.h"

<#if PIO_ENABLE == true>
    <#assign PIO_A_NUM_INT_PINS = 0>
    <#assign PIO_B_NUM_INT_PINS = 0>
    <#assign PIO_C_NUM_INT_PINS = 0>
    <#assign PIO_D_NUM_INT_PINS = 0>
    <#assign PIO_E_NUM_INT_PINS = 0>
    <#list 1..350 as i>
    <#assign intConfig = "BSP_PIN_" + i + "_PIO_INTERRUPT">
    <#assign portChannel = "BSP_PIN_" + i + "_PIO_CHANNEL">
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

<#macro PIO_INITIALIZE PIO_CHANNEL PIO_DIR PIO_LAT PIO_OD PIO_PU PIO_PD PIO_PER PIO_ABCD1
          PIO_ABCD2 PIO_INT PIO_INT_TYPE PIO_INT_EDGE PIO_INT_RE_HL PIO_INTERRUPT>
    /* PORT${PIO_CHANNEL} ABCD 1 */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_ABCDSR[0].w = ${PIO_ABCD1};
    /* PORT${PIO_CHANNEL} ABCD 2 */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_ABCDSR[1].w = ${PIO_ABCD2};
    /* PORT${PIO_CHANNEL} Pio enable */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PDR.w = ~${PIO_PER};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PER.w = ${PIO_PER};
    /* PORT${PIO_CHANNEL} Active state */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_CODR.w = ~${PIO_LAT};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_SODR.w = ${PIO_LAT};
    /* PORT${PIO_CHANNEL} Open drain state */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_MDDR.w = ~${PIO_OD};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_MDER.w = ${PIO_OD};
    /* PORT${PIO_CHANNEL} Pull Up */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PUDR.w = ~${PIO_PU};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PUER.w = ${PIO_PU};
    /* PORT${PIO_CHANNEL} Pull Down */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PPDDR.w = ~${PIO_PD};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_PPDER.w = ${PIO_PD};
    /* PORT${PIO_CHANNEL} Direction */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_ODR.w = ~${PIO_DIR};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_OER.w = ${PIO_DIR};
<#if PIO_INTERRUPT == true>
    /* PORT${PIO_CHANNEL} system level interrupt enable */
    SYS_INT_SourceEnable(PORT${PIO_CHANNEL}_IRQn);
    /* PORT${PIO_CHANNEL} Type of interrupt(alternate) */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_AIMDR.w = ~${PIO_INT_TYPE};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_AIMER.w = ${PIO_INT_TYPE};
    /* PORT${PIO_CHANNEL} If edge, type of edge */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_ESR.w = ~${PIO_INT_EDGE};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_ESR.w = ${PIO_INT_EDGE};
    /* PORT${PIO_CHANNEL} Rising/high level */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_FELLSR.w = ~${PIO_INT_RE_HL};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_REHLSR.w = ${PIO_INT_RE_HL};
    /* PORT${PIO_CHANNEL} module level Interrupt enable */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_IDR.w = ~${PIO_INT};
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_IER.w = ${PIO_INT};
<#else>
    /* PORT${PIO_CHANNEL} module level Interrupt disable */
    VCAST(port_registers_t, PIO_CHANNEL_${PIO_CHANNEL})->PORT_IDR.w = ~${PIO_INT};
</#if>
</#macro>

<#macro PIO_INT_CALLBACK PIO_CHANNEL PORT_NUM_INT_PINS PIO_INTERRUPT>
    <#if PIO_INTERRUPT == true>
/* port ${PIO_CHANNEL} current number of callbacks */
uint32_t port${PIO_CHANNEL}CurNumCb = 0;

/* port ${PIO_CHANNEL} maximum number of callbacks */
uint32_t port${PIO_CHANNEL}MaxNumCb = ${PORT_NUM_INT_PINS};

/* port ${PIO_CHANNEL} callback objects */
PIO_PIN_CALLBACK_OBJ port${PIO_CHANNEL}PinCbObj[${PORT_NUM_INT_PINS}];

    </#if>
</#macro>

<@PIO_INT_CALLBACK 
    PIO_CHANNEL = "A" 
    PORT_NUM_INT_PINS = "${PIO_A_NUM_INT_PINS}"
    PIO_INTERRUPT = PIO_A_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_CHANNEL = "B" 
    PORT_NUM_INT_PINS = "${PIO_B_NUM_INT_PINS}"
    PIO_INTERRUPT = PIO_B_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_CHANNEL = "C" 
    PORT_NUM_INT_PINS = "${PIO_C_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_C_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_CHANNEL = "D" 
    PORT_NUM_INT_PINS = "${PIO_D_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_D_INTERRUPT_USED
/>
<@PIO_INT_CALLBACK 
    PIO_CHANNEL = "E" 
    PORT_NUM_INT_PINS = "${PIO_E_NUM_INT_PINS}" 
    PIO_INTERRUPT = PIO_E_INTERRUPT_USED
/>

/******************************************************************************
  Function:
    PIO_Initialize ( void )

  Summary:
    Initializes Ports System Service

  Description:
    This function initializes different port pins/channels to the desired state.
    It also remaps the pins to the desired specific function.

  Remarks:
    None.
*/
void PIO_Initialize ( void )
{
<#if PIO_CCFG_SYSIO_VALUE?has_content>
    /* Initialize the Debug pins as GPIO pins */
    _MATRIX_REGS->CCFG_SYSIO.w |= ${PIO_CCFG_SYSIO_VALUE};
</#if>

    <#if PIO_INST_IDX0 == true>
    /********** PORT A Initialization **********/
        <@PIO_INITIALIZE
            PIO_CHANNEL = "A"
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

    <#if PIO_INST_IDX1 == true>
    /********** PORT B Initialization **********/
        <@PIO_INITIALIZE
            PIO_CHANNEL = "B"
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

    <#if PIO_INST_IDX2 == true>
    /********** PORT C Initialization **********/
        <@PIO_INITIALIZE
            PIO_CHANNEL = "C"
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

    <#if PIO_INST_IDX3 == true>
    /********** PORT D Initialization **********/
        <@PIO_INITIALIZE
            PIO_CHANNEL = "D"
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

    <#if PIO_INST_IDX4 == true>
    /********** PORT E Initialization **********/
        <@PIO_INITIALIZE
            PIO_CHANNEL = "E"
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
    uint32_t channelIndex, channel, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    if (value == false)
    {
        VCAST(port_registers_t, channel)->PORT_CODR.w = 1 << bitPos;
    }
    else
    {
        VCAST(port_registers_t, channel)->PORT_SODR.w = 1 << bitPos;
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
	To read the latched value on this pin, PIO_PinLatchRead API should be used.
*/
bool PIO_PinRead(PIO_PIN pin)
{
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    return (bool)((VCAST(port_registers_t, channel)->PORT_PDSR.w >> bitPos) & 0x00000001);
}

// *****************************************************************************
/* Function:
    bool PIO_PinLatchRead(PIO_PIN pin)

  Summary:
    Read the value driven on the selected pin.

  Description:
    This function reads the data driven on the selected I/O line/pin.
    Whatever data is written/driven on I/O line by using any of the PIO PLIB
    APIs, will be read by this API.

  Remarks:
	To read actual pin value, PIO_PinRead API should be used.
*/
bool PIO_PinLatchRead(PIO_PIN pin)
{
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    return (bool)((VCAST(port_registers_t, channel)->PORT_ODSR.w >> bitPos) & 0x00000001);
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    if ( ((VCAST(port_registers_t, channel)->PORT_ODSR.w >> bitPos) & 1) == 1 )
    {
        VCAST(port_registers_t, channel)->PORT_CODR.w = 1 << bitPos;
    }
    else
    {
        VCAST(port_registers_t, channel)->PORT_SODR.w = 1 << bitPos;
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    VCAST(port_registers_t, channel)->PORT_SODR.w = 1 << bitPos;
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    VCAST(port_registers_t, channel)->PORT_CODR.w = 1 << bitPos;
}

// *****************************************************************************
/* Function:
    void PIO_PinCallbackRegister(
        PIO_PIN pin, 
        PIO_EVENT_HANDLER callback,
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
    PIO_EVENT_HANDLER callback,
    void* context
)
{
    uint32_t channelIndex;
    PIO_CHANNEL channel;
    
    channelIndex = pin >> 5;
    channel = (PIO_CHANNEL)(_PORTA_BASE_ADDRESS + (0x200 * channelIndex));
    
<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
    switch( channel )
    {
<#if PIO_A_INTERRUPT_USED == true>
        case PIO_CHANNEL_A:
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
        case PIO_CHANNEL_B:
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
        case PIO_CHANNEL_C:
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
        case PIO_CHANNEL_D:
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
        case PIO_CHANNEL_E:
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
<#else>
    SYS_ASSERT(false, "Interrupt for the pin to be enabled from the PIO Interrupt tab of Pin Settings in MHC.");
</#if>

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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    switch (interruptType)
    {
        case PIO_INTERRUPT_RISING_EDGE:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_ESR.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_REHLSR.w = 1 << bitPos;
            break;

        case PIO_INTERRUPT_FALLING_EDGE:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_ESR.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_FELLSR.w = 1 << bitPos;
            break;

        case PIO_INTERRUPT_HIGH_LEVEL:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_LSR.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_REHLSR.w = 1 << bitPos;
            break;

        case PIO_INTERRUPT_LOW_LEVEL:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_LSR.w = 1 << bitPos;
            VCAST(port_registers_t, channel)->PORT_FELLSR.w = 1 << bitPos;
            break;
            
        case PIO_INTERRUPT_BOTH_EDGE:
            /* For both the edge interrupts, we have to disable additional interrupt */
            VCAST(port_registers_t, channel)->PORT_AIMDR.w = 1 << bitPos;
            break;
        default:
            break;
    }
    
    VCAST(port_registers_t, channel)->PORT_IER.w = 1 << bitPos;
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    VCAST(port_registers_t, channel)->PORT_IDR.w = 1 << bitPos;
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    VCAST(port_registers_t, channel)->PORT_ODR.w = 1 << bitPos;
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
    uint32_t channel, channelIndex, bitPos;

    channelIndex = pin >> 5;
    bitPos = pin & 0x1F;
    channel = _PORTA_BASE_ADDRESS + (0x200 * channelIndex);
    
    VCAST(port_registers_t, channel)->PORT_OER.w = 1 << bitPos;
}

// *****************************************************************************
// *****************************************************************************
// Section: PIO APIs which operates on multiple pins of a channel
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    uint32_t PIO_PortRead(PIO_CHANNEL channel)

  Summary:
    Read all the I/O lines of the selected port channel.

  Description:
    This function reads all the I/O lines of the selected port channel.
    it reads the value regardless of pin configuration, whether uniquely as an
    input, or driven by the PIO Controller, or driven by peripheral.

  Remarks:
	None.
*/
uint32_t PIO_PortRead(PIO_CHANNEL channel)
{
    return VCAST(port_registers_t, channel)->PORT_PDSR.w;
}

// *****************************************************************************
/* Function:
    void PIO_PortWrite(PIO_CHANNEL channel, uint32_t value);

  Summary:
    Write the value on all the I/O lines of the selected port channel.

  Description:
    This function writes/drives the value on all the I/O lines of the selected
    port channel.

  Remarks:
	None.
*/
void PIO_PortWrite(PIO_CHANNEL channel, uint32_t value)
{
    /* Enable write to the selected port */
    VCAST(port_registers_t, channel)->PORT_OWER.w = PORT_OWER_Msk;

    /* Write the desired value */
    VCAST(port_registers_t, channel)->PORT_ODSR.w = value;
}

// *****************************************************************************
/* Function:
    uint32_t PIO_PortLatchRead(PIO_CHANNEL channel)

  Summary:
    Read the data driven on all the I/O lines of the selected port channel.

  Description:
    This function reads the data driven on all the I/O lines of the selected
    port channel.
    Whatever data is written/driven on I/O lines by using any of the PIO PLIB
    APIs, will be read by this API.

  Remarks:
	None.
*/
uint32_t PIO_PortLatchRead(PIO_CHANNEL channel)
{
    return VCAST(port_registers_t, channel)->PORT_ODSR.w;
}

// *****************************************************************************
/* Function:
    void PIO_PortSet(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Set the selected IO pins of a channel.

  Description:
    This function sets (to '1') the selected IO pins of a channel.

  Remarks:
	None.
*/
void PIO_PortSet(PIO_CHANNEL channel, uint32_t mask)
{
    VCAST(port_registers_t, channel)->PORT_SODR.w = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortClear(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Clear the selected IO pins of a channel.

  Description:
    This function clears (to '0') the selected IO pins of a channel.

  Remarks:
	None.
*/
void PIO_PortClear(PIO_CHANNEL channel, uint32_t mask)
{
    VCAST(port_registers_t, channel)->PORT_CODR.w = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortToggle(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Toggles the selected IO pins of a channel.

  Description:
    This function toggles (or invert) the selected IO pins of a channel.

  Remarks:
	None.
*/
void PIO_PortToggle(PIO_CHANNEL channel, uint32_t mask)
{
    uint32_t statusReg = 0;

    statusReg = VCAST(port_registers_t, channel)->PORT_ODSR.w;

    /* Write into Clr and Set registers */
    VCAST(port_registers_t, channel)->PORT_CODR.w = ( mask & (statusReg));
    VCAST(port_registers_t, channel)->PORT_SODR.w = ( mask & (~statusReg));
}

// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(
        PIO_CHANNEL channel,
        uint32_t mask,
        PIO_INTERRUPT_TYPE interruptType
        )

  Summary:
    Enables IO interrupt on selected IO pins of a channel.

  Description:
    This function enables IO interrupt on selected IO pins of selected channel.

  Remarks:
	None.
*/
void PIO_PortInterruptEnable(
    PIO_CHANNEL channel,
    uint32_t mask,
    PIO_INTERRUPT_TYPE interruptType
    )
{
    switch (interruptType)
    {
        case PIO_INTERRUPT_RISING_EDGE:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = mask;
            VCAST(port_registers_t, channel)->PORT_ESR.w = mask;
            VCAST(port_registers_t, channel)->PORT_REHLSR.w = mask;
            break;

        case PIO_INTERRUPT_FALLING_EDGE:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = mask;
            VCAST(port_registers_t, channel)->PORT_ESR.w = mask;
            VCAST(port_registers_t, channel)->PORT_FELLSR.w = mask;
            break;

        case PIO_INTERRUPT_HIGH_LEVEL:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = mask;
            VCAST(port_registers_t, channel)->PORT_LSR.w = mask;
            VCAST(port_registers_t, channel)->PORT_REHLSR.w = mask;
            break;

        case PIO_INTERRUPT_LOW_LEVEL:
            VCAST(port_registers_t, channel)->PORT_AIMER.w = mask;
            VCAST(port_registers_t, channel)->PORT_LSR.w = mask;
            VCAST(port_registers_t, channel)->PORT_FELLSR.w = mask;
            break;
            
        case PIO_INTERRUPT_BOTH_EDGE:
            /* For both the edge interrupts, we have to disable additional interrupt */
            VCAST(port_registers_t, channel)->PORT_AIMDR.w = mask;
            break;
        default:
            break;
    }
    
    VCAST(port_registers_t, channel)->PORT_IER.w = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortInterruptDisable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Disables IO interrupt on selected IO pins of a channel.

  Description:
    This function disables IO interrupt on selected IO pins of selected channel.

  Remarks:
	None.
*/
void PIO_PortInterruptDisable(PIO_CHANNEL channel, uint32_t mask)
{
    VCAST(port_registers_t, channel)->PORT_IDR.w = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortInputEnable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Enables selected IO pins of a channel as input.

  Description:
    This function enables selected IO pins of a channel as input.

  Remarks:
	None.
*/
void PIO_PortInputEnable(PIO_CHANNEL channel, uint32_t mask)
{
    VCAST(port_registers_t, channel)->PORT_ODR.w = mask;
}

// *****************************************************************************
/* Function:
    void PIO_PortOutputEnable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Enables selected IO pins of a channel as output.

  Description:
    This function enables selected IO pins of a channel as output.

  Remarks:
	None.
*/
void PIO_PortOutputEnable(PIO_CHANNEL channel, uint32_t mask)
{
    VCAST(port_registers_t, channel)->PORT_OER.w = mask;
}

// *****************************************************************************
/* Function:
    void _PIO_Interrupt_Handler ( PIO_CHANNEL channel )

  Summary:
    Interrupt handler for a selected channel.

  Description:
    This function defines the Interrupt handler for a selected channel.

  Remarks:
	It is an internal function used by the library, user need not call it.
*/
void _PIO_Interrupt_Handler ( PIO_CHANNEL channel )
{
<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
    uint32_t status;
    uint32_t i;

    status  = VCAST(port_registers_t, channel)->PORT_ISR.w;
    status &= VCAST(port_registers_t, channel)->PORT_IMR.w;

    /* Check pending events */
    switch( channel )
    {
    <#if PIO_A_INTERRUPT_USED == true>
        case PIO_CHANNEL_A:
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
        case PIO_CHANNEL_B:
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
        case PIO_CHANNEL_C:
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
        case PIO_CHANNEL_D:
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
        case PIO_CHANNEL_E:
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
<#else>
    ;
</#if>
}

/*******************************************************************************
 End of File
*/
