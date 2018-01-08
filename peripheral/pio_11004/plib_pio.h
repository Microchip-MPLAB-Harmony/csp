/*******************************************************************************
  PIO Plib

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.h

  Summary:
    PIO Plib Header File

  Description:
    This library provides an interface to control and interact with Parallel
    Input/Output controller (PIO) module.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef _PLIB_PIO_H
#define _PLIB_PIO_H

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* PIO Channel

  Summary:
    Identifies the available Ports channels.

  Description:
    This enumeration identifies the available Ports channels.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all channels are available on all devices.  Refer to the specific
    device data sheet to determine which channels are supported.
*/

typedef enum
{
    /* Port A */
    PIO_CHANNEL_A = _PORTA_BASE_ADDRESS,
    
    /* Port B */
    PIO_CHANNEL_B = _PORTB_BASE_ADDRESS,

    /* Port C */
    PIO_CHANNEL_C = _PORTC_BASE_ADDRESS,

    /* Port D */
    PIO_CHANNEL_D = _PORTD_BASE_ADDRESS,

    /* Port E */
    PIO_CHANNEL_E = _PORTE_BASE_ADDRESS  

} PIO_CHANNEL;

// *****************************************************************************
/* PIO Pins

  Summary:
    Identifies the available Ports pins.

  Description:
    This enumeration identifies the available Ports pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/

typedef enum
{
    /* PA0 pin */
    PIO_PIN_PA0,
    
    /* PA1 pin */
    PIO_PIN_PA1,

    /* PA2 pin */
    PIO_PIN_PA2,

    /* PA3 pin */
    PIO_PIN_PA3,

    /* PA4 pin */
    PIO_PIN_PA4,  

    /* PA5 pin */
    PIO_PIN_PA5,
    
    /* PA6 pin */
    PIO_PIN_PA6,

    /* PA7 pin */
    PIO_PIN_PA7,

    /* PA8 pin */
    PIO_PIN_PA8,

    /* PA9 pin */
    PIO_PIN_PA9,
 
    /* PA10 pin */
    PIO_PIN_PA10,
    
    /* PA11 pin */
    PIO_PIN_PA11,

    /* PA12 pin */
    PIO_PIN_PA12,

    /* PA13 pin */
    PIO_PIN_PA13,

    /* PA14 pin */
    PIO_PIN_PA14,  

    /* PA15 pin */
    PIO_PIN_PA15,
    
    /* PA16 pin */
    PIO_PIN_PA16,

    /* PA17 pin */
    PIO_PIN_PA17,

    /* PA18 pin */
    PIO_PIN_PA18,

    /* PA19 pin */
    PIO_PIN_PA19,
    
    /* PA20 pin */
    PIO_PIN_PA20,
    
    /* PA21 pin */
    PIO_PIN_PA21,

    /* PA22 pin */
    PIO_PIN_PA22,

    /* PA23 pin */
    PIO_PIN_PA23,

    /* PA24 pin */
    PIO_PIN_PA24,  

    /* PA25 pin */
    PIO_PIN_PA25,
    
    /* PA26 pin */
    PIO_PIN_PA26,

    /* PA27 pin */
    PIO_PIN_PA27,

    /* PA28 pin */
    PIO_PIN_PA28,

    /* PA29 pin */
    PIO_PIN_PA29,
  
    /* PA30 pin */
    PIO_PIN_PA30,

    /* PA31 pin */
    PIO_PIN_PA31,
  
    /* PB0 pin */
    PIO_PIN_PB0,
    
    /* PB1 pin */
    PIO_PIN_PB1,

    /* PB2 pin */
    PIO_PIN_PB2,

    /* PB3 pin */
    PIO_PIN_PB3,

    /* PB4 pin */
    PIO_PIN_PB4,  

    /* PB5 pin */
    PIO_PIN_PB5,
    
    /* PB6 pin */
    PIO_PIN_PB6,

    /* PB7 pin */
    PIO_PIN_PB7,

    /* PB8 pin */
    PIO_PIN_PB8,

    /* PB9 pin */
    PIO_PIN_PB9,
 
    /* PB10 pin */
    PIO_PIN_PB10,
    
    /* PB11 pin */
    PIO_PIN_PB11,

    /* PB12 pin */
    PIO_PIN_PB12,

    /* PB13 pin */
    PIO_PIN_PB13,

    /* PB14 pin */
    PIO_PIN_PB14,  

    /* PB15 pin */
    PIO_PIN_PB15,
    
    /* PB16 pin */
    PIO_PIN_PB16,

    /* PB17 pin */
    PIO_PIN_PB17,

    /* PB18 pin */
    PIO_PIN_PB18,

    /* PB19 pin */
    PIO_PIN_PB19,
    
    /* PB20 pin */
    PIO_PIN_PB20,
    
    /* PB21 pin */
    PIO_PIN_PB21,

    /* PB22 pin */
    PIO_PIN_PB22,

    /* PB23 pin */
    PIO_PIN_PB23,

    /* PB24 pin */
    PIO_PIN_PB24,  

    /* PB25 pin */
    PIO_PIN_PB25,
    
    /* PB26 pin */
    PIO_PIN_PB26,

    /* PB27 pin */
    PIO_PIN_PB27,

    /* PB28 pin */
    PIO_PIN_PB28,

    /* PB29 pin */
    PIO_PIN_PB29,
  
    /* PB30 pin */
    PIO_PIN_PB30,

    /* PB31 pin */
    PIO_PIN_PB31,
 
    /* PC0 pin */
    PIO_PIN_PC0,
    
    /* PC1 pin */
    PIO_PIN_PC1,

    /* PC2 pin */
    PIO_PIN_PC2,

    /* PC3 pin */
    PIO_PIN_PC3,

    /* PC4 pin */
    PIO_PIN_PC4,  

    /* PC5 pin */
    PIO_PIN_PC5,
    
    /* PC6 pin */
    PIO_PIN_PC6,

    /* PC7 pin */
    PIO_PIN_PC7,

    /* PC8 pin */
    PIO_PIN_PC8,

    /* PC9 pin */
    PIO_PIN_PC9,
 
    /* PC10 pin */
    PIO_PIN_PC10,
    
    /* PC11 pin */
    PIO_PIN_PC11,

    /* PC12 pin */
    PIO_PIN_PC12,

    /* PC13 pin */
    PIO_PIN_PC13,

    /* PC14 pin */
    PIO_PIN_PC14,  

    /* PC15 pin */
    PIO_PIN_PC15,
    
    /* PC16 pin */
    PIO_PIN_PC16,

    /* PC17 pin */
    PIO_PIN_PC17,

    /* PC18 pin */
    PIO_PIN_PC18,

    /* PC19 pin */
    PIO_PIN_PC19,
    
    /* PC20 pin */
    PIO_PIN_PC20,
    
    /* PC21 pin */
    PIO_PIN_PC21,

    /* PC22 pin */
    PIO_PIN_PC22,

    /* PC23 pin */
    PIO_PIN_PC23,

    /* PC24 pin */
    PIO_PIN_PC24,  

    /* PC25 pin */
    PIO_PIN_PC25,
    
    /* PC26 pin */
    PIO_PIN_PC26,

    /* PC27 pin */
    PIO_PIN_PC27,

    /* PC28 pin */
    PIO_PIN_PC28,

    /* PC29 pin */
    PIO_PIN_PC29,
  
    /* PC30 pin */
    PIO_PIN_PC30,

    /* PC31 pin */
    PIO_PIN_PC31,
 
    /* PD0 pin */
    PIO_PIN_PD0,
    
    /* PD1 pin */
    PIO_PIN_PD1,

    /* PD2 pin */
    PIO_PIN_PD2,

    /* PD3 pin */
    PIO_PIN_PD3,

    /* PD4 pin */
    PIO_PIN_PD4,  

    /* PD5 pin */
    PIO_PIN_PD5,
    
    /* PD6 pin */
    PIO_PIN_PD6,

    /* PD7 pin */
    PIO_PIN_PD7,

    /* PD8 pin */
    PIO_PIN_PD8,

    /* PD9 pin */
    PIO_PIN_PD9,
 
    /* PD10 pin */
    PIO_PIN_PD10,
    
    /* PD11 pin */
    PIO_PIN_PD11,

    /* PD12 pin */
    PIO_PIN_PD12,

    /* PD13 pin */
    PIO_PIN_PD13,

    /* PD14 pin */
    PIO_PIN_PD14,  

    /* PD15 pin */
    PIO_PIN_PD15,
    
    /* PD16 pin */
    PIO_PIN_PD16,

    /* PD17 pin */
    PIO_PIN_PD17,

    /* PD18 pin */
    PIO_PIN_PD18,

    /* PD19 pin */
    PIO_PIN_PD19,
    
    /* PD20 pin */
    PIO_PIN_PD20,
    
    /* PD21 pin */
    PIO_PIN_PD21,

    /* PD22 pin */
    PIO_PIN_PD22,

    /* PD23 pin */
    PIO_PIN_PD23,

    /* PD24 pin */
    PIO_PIN_PD24,  

    /* PD25 pin */
    PIO_PIN_PD25,
    
    /* PD26 pin */
    PIO_PIN_PD26,

    /* PD27 pin */
    PIO_PIN_PD27,

    /* PD28 pin */
    PIO_PIN_PD28,

    /* PD29 pin */
    PIO_PIN_PD29,
  
    /* PD30 pin */
    PIO_PIN_PD30,

    /* PD31 pin */
    PIO_PIN_PD31,
 
    /* PE0 pin */
    PIO_PIN_PE0,
    
    /* PE1 pin */
    PIO_PIN_PE1,

    /* PE2 pin */
    PIO_PIN_PE2,

    /* PE3 pin */
    PIO_PIN_PE3,

    /* PE4 pin */
    PIO_PIN_PE4,  

    /* PE5 pin */
    PIO_PIN_PE5,
    
    /* PE6 pin */
    PIO_PIN_PE6,

    /* PE7 pin */
    PIO_PIN_PE7,

    /* PE8 pin */
    PIO_PIN_PE8,

    /* PE9 pin */
    PIO_PIN_PE9,
 
    /* PE10 pin */
    PIO_PIN_PE10,
    
    /* PE11 pin */
    PIO_PIN_PE11,

    /* PE12 pin */
    PIO_PIN_PE12,

    /* PE13 pin */
    PIO_PIN_PE13,

    /* PE14 pin */
    PIO_PIN_PE14,  

    /* PE15 pin */
    PIO_PIN_PE15,
    
    /* PE16 pin */
    PIO_PIN_PE16,

    /* PE17 pin */
    PIO_PIN_PE17,

    /* PE18 pin */
    PIO_PIN_PE18,

    /* PE19 pin */
    PIO_PIN_PE19,
    
    /* PE20 pin */
    PIO_PIN_PE20,
    
    /* PE21 pin */
    PIO_PIN_PE21,

    /* PE22 pin */
    PIO_PIN_PE22,

    /* PE23 pin */
    PIO_PIN_PE23,

    /* PE24 pin */
    PIO_PIN_PE24,  

    /* PE25 pin */
    PIO_PIN_PE25,
    
    /* PE26 pin */
    PIO_PIN_PE26,

    /* PE27 pin */
    PIO_PIN_PE27,

    /* PE28 pin */
    PIO_PIN_PE28,

    /* PE29 pin */
    PIO_PIN_PE29,
  
    /* PE30 pin */
    PIO_PIN_PE30,

    /* PE31 pin */
    PIO_PIN_PE31
  
} PIO_PIN;

// *****************************************************************************
/* PIO Interrupt Type

  Summary:
    Identifies the type of PIO Interrupt.

  Description:
    This enumeration identifies the possible type of PIO Interrupts.

  Remarks:
    None.
*/

typedef enum {
    
    /* PIO Interrupt can occur on any edge detection */
    PIO_INTERRUPT_BOTH_EDGE,
    
    /* PIO Interrupt can occur on rising edge detection */
    PIO_INTERRUPT_RISING_EDGE,
    
    /* PIO Interrupt can occur on falling edge detection */
    PIO_INTERRUPT_FALLING_EDGE,
    
    /* PIO Interrupt can occur on high-level detection */
    PIO_INTERRUPT_HIGH_LEVEL,
    
    /* PIO Interrupt can occur on low-level detection */
    PIO_INTERRUPT_LOW_LEVEL

} PIO_INTERRUPT_TYPE;

// *****************************************************************************
/* PIO Event Handler Function Pointer

   Summary:
    Pointer to a PIO Event handler function.

   Description:
    This data type defines the required function signature for the 
    PIO event handling callback function. Application must register
    a pointer to an event handling function whose function signature (parameter
    and return value types) match the types specified by this function pointer
    in order to receive event calls back from the PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    pin             - One of the IO pins from the enum PIO_PIN

    context         - Value identifying the context of the application that
                      registered the event handling function

  Returns:
    None.

  Example:
    <code>
    PIO_PinCallbackRegister(PIO_PIN_PA5, &APP_PIOInterruptHandler, NULL);
    void APP_PIOInterruptHandler(PIO_PIN pin, uintptr_t contextHandle)
    {
        // Do Something
    }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the event handling function was  registered using the
    PIO_PinCallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context.

    The event handler function executes in the PLIB's interrupt
    context. It is recommended of the application to not perform process
    intensive or blocking operations with in this function.
*/
typedef  void (*PIO_EVENT_HANDLER) (PIO_PIN pin,  void* context);

// *****************************************************************************
// *****************************************************************************
// Section: Generated API based on pin configurations done in Pin Manager
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PIO_Initialize(void)

  Summary:
    Initialize the Pin Manager.

  Description:
    This function Initializes all port channels/pins with the configurations
    selected in the Pin Manager.

  Precondition:
    None.

  Parameters:
    None.
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_Initialize();
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: Generated APIs based on custom name selected in Pin Manager
// *****************************************************************************
// *****************************************************************************

// Sets the pin by name <custom name>. The pin name is configured in Pin Manager.
void <custom name>_Set(void);

// Clears the pin by name <custom name>. The pin name is configured in Pin Manager.
void <custom name>_Clear(void);

// Toggles the pin by name <custom name>. The pin name is configured in Pin Manager.
void <custom name>_Toggle(void);

// Get/Read the pin by name <custom name>. The pin name is configured in Pin Manager.
bool <custom name>_Get(void);

// Enable I/O interrupt for the pin by name <custom name>. The pin name is configured in Pin Manager.
void <custom name>_InterruptEnable(void);

// Disable I/O interrupt for the pin by name <custom name>. The pin name is configured in Pin Manager.
void <custom name>_InterruptDisable(void);

// Make the pin by name <custom name> as Input. The pin name is configured in Pin Manager.
void <custom name>_InputEnable(void);

// Make the pin by name <custom name> as Output. The pin name is configured in Pin Manager.
void <custom name>_OutputEnable(void);

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

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    value     - value to be written on the selected pin
    
  Returns:
    None.

  Example:
    <code>   
        bool value = true;
        PIO_PinWrite(PIO_PIN_PB3, value);                                                              
    </code>

  Remarks:
	None.
*/
void PIO_PinWrite(PIO_PIN pin, bool value);

// *****************************************************************************
/* Function:
    bool PIO_PinRead(PIO_PIN pin)

  Summary:
    Read the selected pin value.

  Description:
    This function reads the selected pin value.
    it reads the value regardless of pin configuration, whether uniquely as an
    input, or driven by the PIO Controller, or driven by peripheral.

  Precondition:
    Reading the I/O line levels requires the clock of the PIO Controller to be
    enabled, otherwise this API reads the levels present on the I/O line at the
    time the clock was disabled.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    Returns the read value of the selected I/O pin.

  Example:
    <code>
    
    bool value;
    value = PIO_PinRead(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	To read the latched value on this pin, PIO_PinLatchRead API should be used.
*/
bool PIO_PinRead(PIO_PIN pin);

// *****************************************************************************
/* Function:
    bool PIO_PinLatchRead(PIO_PIN pin)

  Summary:
    Read the value driven on the selected pin.

  Description:
    This function reads the data driven on the selected I/O line/pin.
    Whatever data is written/driven on I/O line by using any of the PIO PLIB
    APIs, will be read by this API.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    Returns the value driven on the selected I/O pin.

  Example:
    <code>
    
    bool value;
    value = PIO_PinLatchRead(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	To read actual pin value, PIO_PinRead API should be used.
*/
bool PIO_PinLatchRead(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinToggle(PIO_PIN pin)

  Summary:
    Toggles the selected pin.

  Description:
    This function toggles/inverts the value on the selected I/O line/pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinToggle(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinToggle(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinSet(PIO_PIN pin)

  Summary:
    Sets the selected pin.

  Description:
    This function drives '1' on the selected I/O line/pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinSet(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinSet(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinClear(PIO_PIN pin)

  Summary:
    Clears the selected pin.

  Description:
    This function drives '0' on the selected I/O line/pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinClear(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinClear(PIO_PIN pin);

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

  Precondition:
    The PIO_Initialize function must have been called.

  Parameters:
    pin          - One of the IO pins from the enum PIO_PIN
    eventHandler - Pointer to the event handler function implemented by the user

    context      - The value of parameter will be passed back to the application
                   unchanged, when the eventHandler function is called. It can
                   be used to identify any application specific value.

  Returns:
    None.

  Example:
    <code>
    
    PIO_PinCallbackRegister(PIO_PIN_PB3, &APP_PinHandler, NULL);

    </code>

  Remarks:
    None.
*/
void PIO_PinCallbackRegister(
    PIO_PIN pin, 
    PIO_EVENT_HANDLER callback,
    void* context
);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptEnable(PIO_PIN pin, PIO_INTERRUPT_TYPE interruptType)

  Summary:
    Enables IO interrupt on selected IO pin.

  Description:
    This function enables selected type of IO interrupt on selected IO pin.

  Precondition:
    None.

  Parameters:
    pin           - One of the IO pins from the enum PIO_PIN
    interruptType - One of the interrupt types from the enum PIO_INTERRUPT_TYPE
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinInterruptEnable(PIO_PIN_PB3, PIO_INTERRUPT_RISING_EDGE);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinInterruptEnable(PIO_PIN pin, PIO_INTERRUPT_TYPE interruptType);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptDisable(PIO_PIN pin)

  Summary:
    Disables IO interrupt on selected IO pin.

  Description:
    This function disables IO interrupt on selected IO pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinInterruptDisable(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinInterruptDisable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as input.

  Description:
    This function enables selected IO pin as input.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinInputEnable(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinInputEnable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinOutputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as output.

  Description:
    This function enables selected IO pin as output.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    
  Returns:
    None.

  Example:
    <code>
    
    PIO_PinOutputEnable(PIO_PIN_PB3);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PinOutputEnable(PIO_PIN pin);

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

  Precondition:
    Reading the I/O line levels requires the clock of the PIO Controller to be
    enabled, otherwise this API reads the levels present on the I/O line at the
    time the clock was disabled.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL

  Returns:
    Returns the read value of all the I/O lines of the selected port channel.

  Example:
    <code>
    
    uint32_t value;
    value = PIO_PortRead(PIO_CHANNEL_C);
                                                                
    </code>

  Remarks:
	None.
*/
uint32_t PIO_PortRead(PIO_CHANNEL channel);

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

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL

  Returns:
    Returns the data driven on all the I/O lines of the selected port channel.

  Example:
    <code>
    
    uint32_t value;
    value = PIO_PortLatchRead(PIO_CHANNEL_C);
                                                                
    </code>

  Remarks:
	None.
*/
uint32_t PIO_PortLatchRead(PIO_CHANNEL channel);

// *****************************************************************************
/* Function:
    void PIO_PortWrite(PIO_CHANNEL channel, uint32_t value);

  Summary:
    Write the value on all the I/O lines of the selected port channel.

  Description:
    This function writes/drives the value on all the I/O lines of the selected
    port channel.

  Precondition:
    The I/O lines of the selected channel must be made to work as output.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    value         - 32bit value which has to be written/driven on all the I/O
                    lines of the selected channel.
  Returns:
    None.

  Example:
    <code>
    
    PIO_PortWrite(PIO_CHANNEL_C, 0x7563D45F);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortWrite(PIO_CHANNEL channel, uint32_t value);

// *****************************************************************************
/* Function:
    void PIO_PortSet(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Set the selected IO pins of a channel.

  Description:
    This function sets (to '1') the selected IO pins of a channel.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will be set. 
                    The bit positions of mask value which are set as 1,
                    corresponding IO pin of the selected channel will be set
                    (to '1').
                    The bit positions of mask value which are set as 0,
                    corresponding IO pin of the selected channel will remain
                    unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Set PC5 and PC7 pins to 1
    PIO_PortSet(PIO_CHANNEL_C, 0x00A0);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortSet(PIO_CHANNEL channel, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortClear(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Clear the selected IO pins of a channel.

  Description:
    This function clears (to '0') the selected IO pins of a channel.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will be cleared. 
                    The bit positions of mask value which are set as 1,
                    corresponding IO pin of the selected channel will be cleared
                    (to '0').
                    The bit positions of mask value which are set as 0,
                    corresponding IO pin of the selected channel will remain
                    unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Clear PC5 and PC7 pins to 0
    PIO_PortClear(PIO_CHANNEL_C, 0x00A0);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortClear(PIO_CHANNEL channel, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortToggle(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Toggles the selected IO pins of a channel.

  Description:
    This function toggles (or invert) the selected IO pins of a channel.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will be toggled. 
                    The bit positions of mask value which are set as 1,
                    corresponding IO pin of the selected channel will be toggled.
                    The bit positions of mask value which are set as 0,
                    corresponding IO pin of the selected channel will remain
                    unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Toggles PC5 and PC7 pins
    PIO_PortToggle(PIO_CHANNEL_C, 0x00A0);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortToggle(PIO_CHANNEL channel, uint32_t mask);
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
    This function enables selected type of IO interrupt on selected IO pins of
    selected channel.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will have interrupt
                    enabled. 
                    The bit positions of mask value which are set as 1, IO
                    interrupt of corresponding IO pin of the selected channel
                    will be enabled.
                    The bit positions of mask value which are set as 0, IO
                    interrupt of corresponding IO pin of the selected channel
                    will remain unchanged.
    interruptType - One of the interrupt types from the enum PIO_INTERRUPT_TYPE
    
  Returns:
    None.

  Example:
    <code>
    
    // Enable IO interrupt on Rising edge for PC5 and PC7 pins
    PIO_PortInterruptEnable(PIO_CHANNEL_C, 0x00A0, PIO_INTERRUPT_RISING_EDGE);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortInterruptEnable(
        PIO_CHANNEL channel,
        uint32_t mask,
        PIO_INTERRUPT_TYPE interruptType
        );

// *****************************************************************************
/* Function:
    void PIO_PortInterruptDisable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Disables IO interrupt on selected IO pins of a channel.

  Description:
    This function disables IO interrupt on selected IO pins of selected channel.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will have interrupt
                    disabled. 
                    The bit positions of mask value which are set as 1, IO
                    interrupt of corresponding IO pin of the selected channel
                    will be disabled.
                    The bit positions of mask value which are set as 0, IO
                    interrupt of corresponding IO pin of the selected channel
                    will remain unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Disable IO interrupt for PB9 and PB1 pins
    PIO_PortInterruptDisable(PIO_CHANNEL_C, 0x0202);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortInterruptDisable(PIO_CHANNEL channel, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortInputEnable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Enables selected IO pins of a channel as input.

  Description:
    This function enables selected IO pins of a channel as input.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will be input. 
                    The bit positions of mask value which are set as 1,
                    direction of corresponding IO pins of the selected channel
                    will be input.
                    The bit positions of mask value which are set as 0,
                    direction of corresponding IO pins of the selected channel
                    will remain unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Make PC5 and PC7 pins as input
    PIO_PortInputEnable(PIO_CHANNEL_C, 0x00A0);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortInputEnable(PIO_CHANNEL channel, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortOutputEnable(PIO_CHANNEL channel, uint32_t mask)

  Summary:
    Enables selected IO pins of a channel as output.

  Description:
    This function enables selected IO pins of a channel as output.

  Precondition:
    None.

  Parameters:
    channel       - One of the IO channels from the enum PIO_CHANNEL
    mask          - It is a 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected channel will be output. 
                    The bit positions of mask value which are set as 1,
                    direction of corresponding IO pins of the selected channel
                    will be output.
                    The bit positions of mask value which are set as 0,
                    direction of corresponding IO pins of the selected channel
                    will remain unchanged.
  Returns:
    None.

  Example:
    <code>
    
    // Make PC5 and PC7 pins as output
    PIO_PortOutputEnable(PIO_CHANNEL_C, 0x00A0);
                                                                
    </code>

  Remarks:
	None.
*/
void PIO_PortOutputEnable(PIO_CHANNEL channel, uint32_t mask);



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // _PLIB_PIO_H