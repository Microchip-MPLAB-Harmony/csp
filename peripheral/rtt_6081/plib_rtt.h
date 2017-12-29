/*******************************************************************************
 Interface definition of EEFC PLIB.
 
 Company:
	Microchip Technology Inc.
	
 File Name:
	plib_rtt.h
	
 Summary:
	Interface definition of rtt Plib.
	
 Description:
	This file defines the interface for the rtt Plib.
	It allows user to start, stop and configure the on-chip real time timer.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
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
// DOM-IGNORE-END

#ifndef RTT_H    // Guards against multiple inclusion
#define RTT_H
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*  This section lists the other files that are included in this file.
*/
/* This section lists the other files that are included in this file.
*/

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************

typedef enum
{
	RTT_PERIODIC = 0x20000, //Periodic interrupt
	RTT_ALARM	 = 0x10000	// One time Alarm
}RTT_INTERRUPT_TYPE;


/* Callback Function Pointer
 Summary:
	Defines the data type and function signature for the RTT peripheral
	callback function.
 
 Description:
	This data type defines the function signature for the RTT peripheral
	callback function. The RTT peripheral will call back the client's
	function with this signature once the alarm match or periodic interrupt occurs.
 
 Precondition:
	RTT_CallbackRegister must have been called to set the
	function to be called.
 
 Parameters:
	context - Allows the caller to provide a context value (usually a pointer
	to the callers context for multi-instance clients).
	
	type - Reason for the interrupt
 
 Returns:
	None.
*/
typedef void (*RTT_CALLBACK)(uintptr_t context, RTT_INTERRUPT_TYPE type);

typedef struct
{
	RTT_CALLBACK          callback_periodic;
	uintptr_t             context_periodic;
} RTT_OBJECT ;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/* The following functions make up the methods (set of possible operations) of
 this interface.
*/
// *****************************************************************************

/* Function:
	void RTTx_Initialize(void);
	
 Summary:
	Initialize the RTT peripheral
	
 Description:
	This function rests the RTT and initialize the RTT as per MCC
	selection
	
 Precondition:
	None.
	
 Parameters:
	None.
 
 Returns:
	None.
 Example:
	<code>
		RTT0_Initialize();
	</code>

 
*/

void RTTx_Initialize(void);


/* Function:
	void RTTx_Enable(void);
	
 Summary:
	Enables the real Time Timer
	
 Description:
	This API is used to start the real time timer.
	
 Precondition:
	RTT_Initialize must be called in order to configure prescalar and source clock
	
 Parameters:
	None.
 
 Returns:
	None.
 Example:
	<code>
		RTT0_Initialize();
		RTT0_Enable();
	</code>

 
*/

void RTTx_Enable(void);


/* Function:
	void RTTx_Disable( struct tm *time )
	
 Summary:
	Disables the real Time Timer
	
 Description:
	This API is used to stop the real time timer.
	
 Precondition:
	RTT should be running.
	
 Parameters:
	None.
 
 Returns:
	None.
 Example:
	<code>
		void My_callback(uintptr_t context)
		{
			//Interrupt recieved stop RTT
			RTTx_Disable();
		}
		int main(void)
		{
			RTT0_Initialize();
			
			//Enable callback for the periodic interrupt
			RTT0_CallbackRegister(My_callback, RTT_PERIODIC, NULL);
			
			//start RTT
			RTT0_Enable();
		}
	</code>

 
*/

void RTTx_Disable(void);


/* Function:
	void RTTx_PrescalarUpdate(uint16_t prescale);
	
 Summary:
	Updates the prescalar for the RTT peripheral.
	
 Description:
	This function is used to update the prescalar for the RTT peripheral
	
 Precondition:
	None.
	
 Parameters:
	prescale: The prescale value to be loaded.
 
 Returns:
	None.
 Example:
	<code>
		RTT0_PrescalarUpdate(10);
	</code>

 
*/

void RTTx_PrescalarUpdate(uint16_t prescale);


/* Function:
	void RTTx_AlarmValueSet(uint32_t alarm);
	
 Summary:
	Sets the Alarm value for the RTT peripheral.
	
 Description:
	This function updates the Alarm compare value for RTT peripheral.
	
 Precondition:
	None.
	
 Parameters:
	alarm:- The alarm value to be updated
 
 Returns:
	None.
 Example:
	<code>
		RTT0_AlarmValueSet(100);
	</code>

 
*/

void RTTx_AlarmValueSet(uint32_t alarm);


/* Function:
	void RTTx_EnableInterrupt (RTT_INTERRUPT_TYPE type);
	
 Summary:
	Enable RTT interrupts
	
 Description:
	This function is used to enable periodic and alarm interrupts
	
 Precondition:
	None.
	
 Parameters:
	type:- Interrupt to be enabled
 
 Returns:
	None.
 Example:
	<code>
		//Enable Alarm interrupt for RTT
		RTT0_EnableInterrupt(RTT_ALARM);
	</code>
 
*/

void RTTx_EnableInterrupt (RTT_INTERRUPT_TYPE type);


/* Function:
	void RTTx_DisableInterrupt(RTT_INTERRUPT_TYPE type);
	
 Summary:
	Disable RTT interrupts
 
 Description:
	This function is used to disable periodic and alarm interrupts
 
 Precondition:
	 None.
 
 Parameters:
	type:- Interrupt to be disabled
 
 Returns:
	None.
 Example:
	<code>
		//disable Alarm interrupt for RTT
		RTT0_DisableInterrupt(RTT_ALARM);
	</code>
 
 */

void RTTx_DisableInterrupt(RTT_INTERRUPT_TYPE type);


/* Function:
	uint32_t RTTx_TimerValueGet(void);
	
 Summary:
	Returns the current timer value
	
 Description:
	This function is used the counter value of RTT. This value can be
	use to calculate the time elapsed.
	
 Precondition:
	None.
	
 Parameters:
	None.
 
 Returns:
	The current timer count
 Example:
	<code>
		uint32_t frequency = 0;
		uint32_t count = 0;
		uint64_t time_elapsed;
		
		frequency = RTT0_FrequencyGet();
		count = RTT0_TimerValueGet();
		
		time_elapsed = count/frequency;
	</code>
 
*/

uint32_t RTTx_TimerValueGet(void);


/* Function:
	uint32_t RTTx_FrequencyGet(void)
	
 Summary:
	Returns the current RTT frequency
	
 Description:
	This function is used to get the frequncy of the RTT timer
	
 Precondition:
	None.
	
 Parameters:
	None.
 
 Returns:
	Returns the operating frequency of RTT
 Example:
	<code>
		uint32_t frequency = 0;
		frequency = RTT0_FrequencyGet();
	</code>
 
*/

uint32_t RTTx_FrequencyGet(void);

 
/* Function:
	void RTTx_CallbackRegister( RTT_CALLBACK callback, uintptr_t context );
	
 Summary:
	Sets the pointer to the function (and it's context) to be called.
	
 Description:
	This function sets the pointer to a client function to be called "back"
	when the interrupt occurs. It also passes a context value that is passed into the
	function when it is called.
	This function is available only in interrupt mode of operation.
	
 Precondition:
	None.
	
 Parameters:
	callback - A pointer to a function with a calling signature defined
				by the RTT_CALLBACK data type.
	context - A value (usually a pointer) passed (unused) into the function
				identified by the callback parameter.
				
 Returns:
	None.
	
 Example:
	<code>
		void My_callback(uintptr_t context)
		{
			//Interrupt recieved stop RTT
			RTT0_Disable();
		}
		int main(void)
		{
			RTT0_Initialize();
					
			//Enable callback for the periodic interrupt
			RTT0_CallbackRegister(My_callback, RTT_PERIODIC, NULL);
					
			//start RTT
			RTT0_Enable();
		}
	</code>
	
 Remarks:
	The context value may be set to NULL if it is not required. In this case the
	value NULL will be passed to the callback function.
	To disable the callback function, pass a NULL for the callback parameter.
	See the RTCC_CALLBACK type definition for additional information.
*/

void RTTx_CallbackRegister( RTT_CALLBACK callback, uintptr_t context );
 
// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END