/*******************************************************************************
  Analog Comparator Controller(ACC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    acc.h

  Summary
    ACC peripheral library interface.

  Description
    This library provides documentation of all the interfaces which can be used
    to interact with an instance of a Analog Comparator Controller (ACC).
    This file must not be included in any MPLAB Project.
	
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_ACCx_H    // Guards against multiple inclusion
#define PLIB_ACCx_H

// *****************************************************************************
// *****************************************************************************
// Section: Data types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* ACC comparison status
   
   Summary:
    Identifies ACC Comparison status

   Description:
    This enumeration identifies the ACC Comparison status either from Comparison
	edge or synchronized comparator output.

   Remarks:
    None.
*/
typedef enum
{
    /* ACC synchronized comparator output */
    ACC_STATUS_SOURCE_COMPARATOR_OUTPUT,      

    /* ACC comparison edge */
    ACC_STATUS_SOURCE_COMPARISON_EDGE,

} ACC_STATUS_SOURCE;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ACCx_Initialize (void);

   Summary:
     Initializes ACC x module of the device

   Description:
    This function initializes ACC x module of the device with the values
    configured in MHC GUI. Once the peripheral is initialized, Status API can be
	used to get the comparison status.

   Precondition:
     MHC GUI should be configured with the right values.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        ACC0_Initialize ();
    </code>

   Remarks:
     This function must be called only once and before any other ACC function is
     called.
*/

void ACCx_Initialize (void);

// *****************************************************************************
/* Function:
    bool ACCx_StatusGet (ACC_STATUS_SOURCE status);

  Summary:
    Returns comparison status of the ACC x

  Description:
    This function returns the current comparison status based on input parameter
	either comparison edge or synchronized comparator output of ACC x module.

  Precondition:
    None.

  Parameters:
    status   Data structure of type ACC_STATUS_SOURCE which has the list of 
	         elements of Comparison status.
             
  Returns:
    Returns the comparison status based on input parameter.

  Example:
    <code>
        bool status;
        status = ACC0_StatusGet(ACC_STATUS_SOURCE_COMPARATOR_OUTPUT);
        if (status)
        {
            // Application related tasks     
        }
    </code>

  Remarks:
    None.

*/
bool ACCx_StatusGet (ACC_STATUS_SOURCE status);

// *****************************************************************************
/* ACC Callback Function pointer
    typedef void (*ACC_CALLBACK) (uintptr_t context);

  Summary:
    Pointer to a ACC callback function

  Description:
    This data type defines the required function signature for the ACC callback
	function. Application must register a pointer to a callback function whose
	function signature (parameter and return value types) match the types 
	specified by this function pointer in order to receive callback from the 
	PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context   Value identifying the context of the application that registered
              the callback function.

  Returns:
    None.

   Example:
    <code>
        ACC0_CallbackRegister (&APP_ACC_CallbackFunction, NULL);
        void APP_ACC_CallbackFunction (uintptr_t context)
        {
            //Application related tasks
        }
    </code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the callback function was registered using the
    ACCx_CallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context or instance  of the client that made the data transfer
    request.

    The callback function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/
typedef void (*ACC_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* Function:
    void ACCx_CallbackRegister (ACC_CALLBACK callback, uintptr_t context);
	
  Summary:
     Allows application to register callback with PLIB

  Description:
    This function allows application to register a callback function for the 
	PLIB to call back when interrupt occurred.
	
    At any point if application wants to stop the callback, it can call this 
	function with "callback" value as NULL.

  Precondition:
    The ACCx_Initialize function must have been called.

  Parameters:
    callback - Pointer to the callback function implemented by the user.
	
    context  - The value of parameter will be passed back to the application
               unchanged, when the callback function is called. It can be used
			   to identify any application specific value that identifies the 
			   instance of the client module (for example, it may be a pointer
			   to the client module's state structure).

  Returns:
    None.

  Example:
    <code>
        MY_APP_OBJ myAppObj;
    
        void APP_ACC_CallbackFunction (uintptr_t context)
        {  
            // The context was set to an application specific object.
            // It is now retrievable easily in Callback function.
               MY_APP_OBJ myAppObj = (MY_APP_OBJ *) context;
            //Application related tasks
        }
                      
        ACC0_CallbackRegister (APP_ACC_CallbackFunction, (uintptr_t)&myAppObj);  
    </code>

  Remarks:
    None.

*/
void ACCx_CallbackRegister (ACC_CALLBACK callback, uintptr_t context);

#endif // PLIB_ACCx_H
