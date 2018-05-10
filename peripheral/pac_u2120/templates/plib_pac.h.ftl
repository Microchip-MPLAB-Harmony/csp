/*******************************************************************************
  Peripheral Access Controller(PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pac${PAC_INDEX}.h

  Summary
    PAC PLIB Header File.

  Description
    This file defines the interface to the PAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
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

/* Guards against multiple inclusion */
#ifndef PLIB_PAC${PAC_INDEX}_H
#define PLIB_PAC${PAC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include "device.h"
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* AHB Slave Buses Identifier enumeration

  Summary:
    List of available AHB Slave Buses on which errors will be detected.

  Description:
    This enumeration identifies the available AHB Slave Buses on which the PAC
    module will detect errors. 

  Remarks:
    None.
*/
 
typedef enum
{
    /* Interrupt flag for SLAVE FLASH */
    PAC_AHB_SLAVE_FLASH = 0x1,
    
    /* Interrupt flag for SLAVE HSRAMCMOP */
    PAC_AHB_SLAVE_HSRAMCM0P = 0x2,
    
    /* Interrupt flag for SLAVE HSRAMDSU */
    PAC_AHB_SLAVE_HSRAMDSU = 0x4,
    
    /* Interrupt flag for SLAVE HPB1 */
    PAC_AHB_SLAVE_HPB1 = 0x8,
    
    /* Interrupt flag for SLAVE HPB0 */
    PAC_AHB_SLAVE_HPB0 = 0x10,
    
    /* Interrupt flag for SLAVE HPB2 */
    PAC_AHB_SLAVE_HPB2 = 0x20,
    
    /* Interrupt flag for SLAVE LPRAMDMAC */
    PAC_AHB_SLAVE_LPRAMDMAC = 0x40,
    
    /* Interrupt flag for SLAVE DIVAS */
    PAC_AHB_SLAVE_DIVAS = 0x80, 
    
    /* Interrupt flag for SLAVE HPB3 */
    PAC_AHB_SLAVE_HPB3 = 0x100,
    
    /* Interrupt flag for all SLAVES */
    PAC_AHB_SLAVE_ANY = 0xFFFFFFFF     
    
} PAC_AHB_SLAVE;
 
// *****************************************************************************
/* Peripheral module Identifier enumeration

  Summary:
    List of available Peripheral module on which errors will be detected.

  Description:
    This enumeration identifies all the Peripheral modules used on which access
    errors will be detected.

  Remarks:
    None.
*/

typedef enum
{
<#list 0..PAC_BRIDGE_COUNT as i>
    <#assign PAC_BRIDGE = "PAC_" + i + "_BRIDGE">
    <#assign PAC_BRIDGE_PERI_COUNT = "PAC_BRIDGE_" + i + "_PERI_COUNT">
        <#if .vars[PAC_BRIDGE_PERI_COUNT]?has_content>
            <#assign PAC_PERI_COUNT = .vars[PAC_BRIDGE_PERI_COUNT]>
            <#list 0..PAC_PERI_COUNT as j>
                <#assign PAC_REG_PROTECT = "PAC_BRIDGE_" + i + "_PERI_" + j + "_REG_PROTECT">
                <#assign PAC_BRIDGE_PERI_NAME = "PAC_BRIDGE_" + i + "_PERI_" + j + "_NAME">
                    <#if .vars[PAC_REG_PROTECT]?has_content>
    <#lt>    /* Interrupt flag for Peripheral bridge ${.vars[PAC_BRIDGE]} - ${.vars[PAC_BRIDGE_PERI_NAME]} */
    <#lt>    PAC_PERIPHERAL_${.vars[PAC_BRIDGE]}_${.vars[PAC_BRIDGE_PERI_NAME]} = ((${i} * 32 ) + ${j}),

                    </#if>
            </#list>
        </#if>
</#list>

    /* Interrupt flag for all Peripheral bridges */
    PAC_PERIPHERAL_ANY = 0xFFFFFFFF
  
} PAC_PERIPHERAL;

// *****************************************************************************
/* Peripheral Access Control Keys enumeration

  Summary:
    List of available Peripheral Access Control Operations.

  Description:
    This enum identifies the possible PAC operation. This data type is used
    along with the PAC${PAC_INDEX}_PeripheralProtect() function and specifies 
    the type of access operation that needs to be peformed

  Remarks:
    None.
*/

typedef enum
{
    /* No Action */
    PAC_PROTECTION_OFF,
        
    /* Clear the peripheral write control protection */
    PAC_PROTECTION_CLEAR,
    
    /* Set the peripheral write control protection */
    PAC_PROTECTION_SET,
    
    /* Set and lock the peripheral write control until the next hardware reset */
    PAC_PROTECTION_SET_AND_LOCK,
 
} PAC_PROTECTION;

// *****************************************************************************
/* Callback function Pointer

  Summary:
    Defines the data type and function signature for the PAC peripheral
    callback function.

  Description:
    This data type defines the function signature for the PAC peripheral
    callback function. The PAC peripheral will call back the function with 
    this signature when a access violation has been detected.

  Function:
    void (*PAC_CALLBACK)( uintptr_t context )

  Precondition:
    None.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void APP_PACErrorCallback( uintptr_t context )
      {
            // Identify the error.
            if(PAC${PAC_INDEX}_PeripheralErrorOccurred())
            {
                // Call the PAC${PAC_INDEX}_PeripheralErrorGet() function to 
                // identify the error.
            }
            else if(PAC${PAC_INDEX}_AHBSlaveErrorOccurred())
            {
                // Call the PAC${PAC_INDEX}_AHBSlaveErrorGet() function to 
                // identify the error.
            }
      }

      PAC${PAC_INDEX}_CallbackRegister(APP_PACErrorCallback, NULL);

    </code>

  Remarks:
    The callback feature is only available when the library was generated with
    interrupt option (in MHC) enabled. The function will execute within an
    interrupt context. Avoid calling computationally intensive or blocking
    functions from within the callback function.
*/

typedef void (*PAC_CALLBACK)( uintptr_t context );


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
    void PAC${PAC_INDEX}_Initialize (void);

  Summary:
    Initializes given instance of PAC peripheral.

  Description:
    This function initializes given instance of PAC peripheral of the device 
    with the values configured in MCC GUI.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        PAC${PAC_INDEX}_Initialize ();
    </code>

  Remarks:
     None.
*/

void PAC${PAC_INDEX}_Initialize( void );

// *****************************************************************************
/* Function:
    bool PAC${PAC_INDEX}_PeripheralIsProtected (PAC_PERIPHERAL peripheral)

  Summary:
    Gets write protect status for the given interface module

  Description:
    This function returns true if the specified peripheral is write protected.
    It returns false otherwise.

  Precondition:
    None.

  Parameters:
    peripheral - peripheral to be checked.

  Returns:
    true - Peripheral is write protected

    false - Peripheral is not write protected

  Example:
    <code>
    if(!PAC${PAC_INDEX}_PeripheralIsProtected(PAC_PERIPHERAL_A_PM))
    {
        PAC${PAC_INDEX}_PeripheralProtect(PAC_PERIPHERAL_A_PM, PAC_PROTECTION_SET);
    };
    </code>

  Remarks:
    None.
*/
    
bool PAC${PAC_INDEX}_PeripheralIsProtected (PAC_PERIPHERAL peripheral);

// *****************************************************************************
/* Function:
    void PAC${PAC_INDEX}_PeripheralProtect (PAC_PERIPHERAL peripheral,
                                            PAC_PROTECTION operation);

  Summary:
    This function performs a PAC protection operation on the specified
    peripheral.

  Description:
    This function performs a PAC protection operation on the specified
    peripheral. The function can be called to disable the protection
    (PAC_PROTECTION_CLEAR), to set write protection which can be disabled via a
    clear operation (PAC_PROTECTION_SET) and to set write protection that cannot
    be cleared (PAC_PROTECTION_SET_AND_LOCK).

  Precondition:
    The PAC${PAC_INDEX}_Initialize() function should have been called once. 

  Parameters:
    peripheral - Peripheral to be operated on.

    operation - PAC operation to be performed. Refer to the description of the
    PAC_PROTECTION enumeration for possible operations.

  Returns:
    None.
    
  Example:
    <code>

    // Refer to the description of PAC${PAC_INDEX}_PeripheralIsProtected() 
    // function for example usage of the PAC${PAC_INDEX}_PeripheralProtect API.
    
    </code>

  Remarks:
    Peripherals protection can be enabled and disabled via MHC. These protection
    settings are applied when the PAC${PAC_INDEX}_Initialize() function is called.
*/  

void PAC${PAC_INDEX}_PeripheralProtect (PAC_PERIPHERAL peripheral, PAC_PROTECTION operation);

// *****************************************************************************
/* Function:
    bool PAC${PAC_INDEX}_PeripheralErrorOccurred (void)

  Summary:
    Returns true if any Peripheral Access Error has occurred.

  Description:
    This function returns true if any peripheral access error has occurred. The
    application can then call the PAC${PAC_INDEX}_PeripheralErrorGet() function 
    to identify the peripheral on which the error has occurred.

  Precondition:
    The PAC${PAC_INDEX}_Initialize() function should have been called once. 

  Parameters:
    None.

  Returns:
    true - atleast one peripheral is reporting a PAC error.

    false - no peripherals are reporting PAC errors.
    
  Example:
    <code>

    PAC_PERIPHERAL peripheral;

    // Process and clear all peripheral errors.
    while(PAC${PAC_INDEX}_PeripheralErrorOccurred())
    {
        peripheral = PAC${PAC_INDEX}_PeripheralErrorGet();
        
        // Assuming that some application function has processed the error, we
        // can clear the error.

        PAC${PAC_INDEX}_PeripheralErrorClear(peripheral);
    }

    </code>

  Remarks:
    None.
*/

bool PAC${PAC_INDEX}_PeripheralErrorOccurred (void);

// *****************************************************************************
/* Function:
    PAC_PERIPHERAL PAC${PAC_INDEX}_PeripheralErrorGet (void);

  Summary:
    Returns the first peripheral that is reporting an access error.

  Description:
    This function returns the first peripheral that is reporting an access
    error. The application can call this function to identify the peripheral
    that is a reporting an access error. In case where multiple peripherals are
    reporting access errors, the application must call this function multiple
    times. The application can use the PAC${PAC_INDEX}_PeripheralErrorOccurred() 
    function to check if a peripheral access error is active. The application 
    must use the PAC${PAC_INDEX}_PeripheralErrorClear() function to clear the 
    error before calling the PAC${PAC_INDEX}_PeripheralErrorGet() function 
    again. Not clearing the error will cause the function to continue reporting 
    the error on the same peripheral.

    In a case where the peripheral is experiencing repeated access errors, it is
    possible that this function will return the same peripheral ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application implement a convenient break mechanism to prevent a blocking
    loop.
   
  Precondition:
    PAC${PAC_INDEX}_Initialize() function should have been called once. The
    PAC${PAC_INDEX}_PeripheralErrorOccurred() have returned true.

  Parameters:
    None.

  Returns:
    Returns the first peripheral that is reporting an access error.

  Example:
    <code>
    // Refer to the description of the PAC${PAC_INDEX}_PeripheralErrorOccurred() 
    // for example usage of this function.
    </code>

  Remarks:
    None.
*/

PAC_PERIPHERAL PAC${PAC_INDEX}_PeripheralErrorGet (void);

// *****************************************************************************
/* Function:     
    void PAC${PAC_INDEX}_PeripheralErrorClear (PAC_PERIPHERAL peripheral)

  Summary:
    Clear the peripheral access error flag.

  Description:
    Calling this function will cause the peripheral access error flag to be
    cleared. This will then cause the PAC${PAC_INDEX}_PeripheralErrorGet() 
    function to identify the next peripheral that is reporting an error. If 
    after calling this function, there are no peripheral errors active, the
    PAC${PAC_INDEX}_PeripheralErrorOccurred() function will return false. 
    The application must call this function to clear the error on the peripheral 
    that was identified by the last call of the 
    PAC${PAC_INDEX}_PeripheralErrorGet() function.

  Precondition:
    The PAC${PAC_INDEX}_Initialize() function should have been called once.

  Parameters:
    peripheral - Peripheral ID of peripheral for which the peripheral error
    needs to be cleared. Specifying PAC_PERIPHERAL_ANY will clear all errors.

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the PAC${PAC_INDEX}_PeripheralErrorOccurred() function
    // for example usage.
    </code>

  Remarks:
    None.
*/

void PAC${PAC_INDEX}_PeripheralErrorClear (PAC_PERIPHERAL peripheral);

// *****************************************************************************
/* Function:
    bool PAC${PAC_INDEX}_AHBSlaveErrorOccurred (void)

  Summary:
    Returns true if an error has occurred on any of the AHB slaves.

  Description:
    This function returns true if any AHB Slave error has occurred. The
    application can then call the PAC${PAC_INDEX}_AHBSlaveErrorGet() function 
    to identify the AHB Slave on which the error has occurred.

  Precondition:
    The PAC${PAC_INDEX}_Initialize() function should have been called once. 

  Parameters:
    None.

  Returns:
    true - atleast one AHB Slave is reporting an access error.

    false - no AHB Slave is reporting access errors.
    
  Example:
    <code>

    PAC_AHB_SLAVE ahbSlave;

    // Process and clear all AHB Slave errors.
    while(PAC${PAC_INDEX}_AHBSlaveErrorOccurred())
    {
        ahbSlave = PAC${PAC_INDEX}_AHBSlaveErrorGet();
        
        // Assuming that some application function has processed the error, we
        // can clear the error.

        PAC${PAC_INDEX}_AHBSlaveErrorClear(ahbSlave);
    }

    </code>

  Remarks:
    None.
*/

bool PAC${PAC_INDEX}_AHBSlaveErrorOccurred (void);

// *****************************************************************************
/* Function:
    AHB_SLAVE PAC${PAC_INDEX}_AHBSlaveErrorGet (void);

  Summary:
    Returns the first AHB Slave that is reporting an access error.

  Description:
    This function returns the first AHB Slave that is reporting an access
    error. The application can call this function to identify the AHB Slave
    that is a reporting an access error. In case where multiple AHB Slaves are
    reporting access errors, the application must call this function multiple
    times. The application can use the PAC${PAC_INDEX}_AHBSlaveErrorOccurred() 
    function to check if a AHB Slave access error is active. The application 
    must use the PAC${PAC_INDEX}_AHBSlaveErrorClear() function to clear the 
    error before calling the PAC${PAC_INDEX}_AHBSlaveErrorGet() function again. 
    Not clearing the error will cause the function to continue reporting the 
    error on the same AHB Slave.

    In a case where the AHB Slave is experiencing repeated access errors, it is
    possible that this function will return the same AHB Slave ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application in implement a convenient break mechanism to prevent a 
    blocking loop.
   
  Precondition:
    PAC${PAC_INDEX}_Initialize() function should have been called once. The
    PAC${PAC_INDEX}_AHBSlaveErrorOccurred() have returned true.

  Parameters:
    None.

  Returns:
    Returns the first AHB Slave that is reporting an access error.

  Example:
    <code>
    // Refer to the description of the PAC${PAC_INDEX}_AHBSlaveErrorOccurred() 
    // for example usage of this function.
    </code>

  Remarks:
    None.
*/

PAC_AHB_SLAVE PAC${PAC_INDEX}_AHBSlaveErrorGet (void);

// *****************************************************************************
/* Function:     
    void PAC${PAC_INDEX}_AHBSlaveErrorClear (PAC_AHB_SLAVE AHB Slave)

  Summary:
    Clear the AHB Slave access error flag.

  Description:
    Calling this function will cause the AHB Slave access error flag to be
    cleared. This will then cause the PAC${PAC_INDEX}_AHBSlaveErrorGet() 
    function to identify the next AHB Slave that is reporting an error. If after 
    calling this function, there are no AHB Slave errors active, the
    PAC${PAC_INDEX}_AHBSlaveErrorOccurred() function will return false. The 
    application must call this function to clear the error on the AHB Slave that 
    was identified by the last call of the PAC${PAC_INDEX}_AHBSlaveErrorGet() 
    function.

  Precondition:
    The PAC${PAC_INDEX}_Initialize() function should have been called once.

  Parameters:
    AHB Slave - AHB Slave ID of AHB Slave for which the AHB Slave error needs to
    be cleared. Specifying PAC_AHB_SLAVE_ANY will clear all errors.

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the PAC${PAC_INDEX}_AHBSlaveErrorOccurred() 
    // function for example usage.
    </code>

  Remarks:
     None.
*/

void PAC${PAC_INDEX}_AHBSlaveErrorClear (PAC_AHB_SLAVE ahbSlave);

<#if PAC_INTERRRUPT_MODE = true>

// *****************************************************************************
/* Function:
    void PAC${PAC_INDEX}_CallbackRegister(PAC_CALLBACK callback,uintptr_t context)

  Summary:
    Registers the function to be called when a PAC error has occurred.

  Description
    This function registers the callback function to be called when a PAC error
    has occurred. The function is available only when the module interrupt is
    enabled in MHC.

  Precondition:
    PAC${PAC_INDEX}_Initialize() function should have beeb called once. 
    Interrupt option in MHC should have been enabled.

  Parameters:
    callback - callback function pointer. Setting this to NULL will disable the
    callback feature.

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the PAC_CALLBACK function pointer type for
    // example usage.
    </code>

  Remarks:
    Context value can be set to NULL if this is not required.
*/

void PAC${PAC_INDEX}_CallbackRegister (PAC_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    void PAC${PAC_INDEX}_InterruptHandler ( void )

  Summary:
    PAC Interrupt Handler.

  Description
    This PAC Interrupt handler function handles PAC interrupts

  Precondition:
    PAC${PAC_INDEX}_Initialize() function should have beeb called once. 
    Interrupt option in MHC should have been enabled.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        PAC${PAC_INDEX}_InterruptHandler ();
    </code>

  Remarks:
    Context value can be set to NULL if this is not required.
*/

void PAC${PAC_INDEX}_InterruptHandler (void);

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_PAC${PAC_INDEX}_H */