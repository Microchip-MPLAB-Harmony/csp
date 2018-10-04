/*******************************************************************************
  Peripheral Access Controller(PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pacx.h

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
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

/* Guards against multiple inclusion */
#ifndef PLIB_PACx_H
#define PLIB_PACx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

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
    /* Interrupt flag for Peripheral bridge A - PAC */
    PAC_PERIPHERAL_A_PAC = ((0 * 32 ) + 0),

    /* Interrupt flag for Peripheral bridge A - PM */
    PAC_PERIPHERAL_A_PM = ((0 * 32 ) + 1),

    /* Interrupt flag for Peripheral bridge A - MCLK */
    PAC_PERIPHERAL_A_MCLK = ((0 * 32 ) + 2),

    /* Interrupt flag for Peripheral bridge A - RSTC */
    PAC_PERIPHERAL_A_RSTC = ((0 * 32 ) + 3),

    /* Interrupt flag for Peripheral bridge A - OSCCTRL */
    PAC_PERIPHERAL_A_OSCCTRL = ((0 * 32 ) + 4),

    /* Interrupt flag for Peripheral bridge A - OSC32KCTRL */
    PAC_PERIPHERAL_A_OSC32KCTRL = ((0 * 32 ) + 5),

    /* Interrupt flag for Peripheral bridge A - SUPC */
    PAC_PERIPHERAL_A_SUPC = ((0 * 32 ) + 6),

    /* Interrupt flag for Peripheral bridge A - GCLK */
    PAC_PERIPHERAL_A_GCLK = ((0 * 32 ) + 7),

    /* Interrupt flag for Peripheral bridge A - WDT */
    PAC_PERIPHERAL_A_WDT = ((0 * 32 ) + 8),

    /* Interrupt flag for Peripheral bridge A - RTC */
    PAC_PERIPHERAL_A_RTC = ((0 * 32 ) + 9),

    /* Interrupt flag for Peripheral bridge A - EIC */
    PAC_PERIPHERAL_A_EIC = ((0 * 32 ) + 10),

    /* Interrupt flag for Peripheral bridge A - FREQM */
    PAC_PERIPHERAL_A_FREQM = ((0 * 32 ) + 11),

    /* Interrupt flag for Peripheral bridge A - TSENS */
    PAC_PERIPHERAL_A_TSENS = ((0 * 32 ) + 12),

    /* Interrupt flag for Peripheral bridge B - PORT */
    PAC_PERIPHERAL_B_PORT = ((1 * 32 ) + 0),

    /* Interrupt flag for Peripheral bridge B - DSU */
    PAC_PERIPHERAL_B_DSU = ((1 * 32 ) + 1),

    /* Interrupt flag for Peripheral bridge B - NVMCTRL */
    PAC_PERIPHERAL_B_NVMCTRL = ((1 * 32 ) + 2),

    /* Interrupt flag for Peripheral bridge B - DMAC */
    PAC_PERIPHERAL_B_DMAC = ((1 * 32 ) + 3),

    /* Interrupt flag for Peripheral bridge B - MTB */
    PAC_PERIPHERAL_B_MTB = ((1 * 32 ) + 4),

    /* Interrupt flag for Peripheral bridge B - HMATRIXHS */
    PAC_PERIPHERAL_B_HMATRIXHS = ((1 * 32 ) + 5),

    /* Interrupt flag for Peripheral bridge C - EVSYS */
    PAC_PERIPHERAL_C_EVSYS = ((2 * 32 ) + 0),

    /* Interrupt flag for Peripheral bridge C - SERCOM0 */
    PAC_PERIPHERAL_C_SERCOM0 = ((2 * 32 ) + 1),

    /* Interrupt flag for Peripheral bridge C - SERCOM1 */
    PAC_PERIPHERAL_C_SERCOM1 = ((2 * 32 ) + 2),

    /* Interrupt flag for Peripheral bridge C - SERCOM2 */
    PAC_PERIPHERAL_C_SERCOM2 = ((2 * 32 ) + 3),

    /* Interrupt flag for Peripheral bridge C - SERCOM3 */
    PAC_PERIPHERAL_C_SERCOM3 = ((2 * 32 ) + 4),

    /* Interrupt flag for Peripheral bridge C - SERCOM4 */
    PAC_PERIPHERAL_C_SERCOM4 = ((2 * 32 ) + 5),

    /* Interrupt flag for Peripheral bridge C - SERCOM5 */
    PAC_PERIPHERAL_C_SERCOM5 = ((2 * 32 ) + 6),

    /* Interrupt flag for Peripheral bridge C - CAN0 */
    PAC_PERIPHERAL_C_CAN0 = ((2 * 32 ) + 7),

    /* Interrupt flag for Peripheral bridge C - CAN1 */
    PAC_PERIPHERAL_C_CAN1 = ((2 * 32 ) + 8),

    /* Interrupt flag for Peripheral bridge C - TCC0 */
    PAC_PERIPHERAL_C_TCC0 = ((2 * 32 ) + 9),

    /* Interrupt flag for Peripheral bridge C - TCC1 */
    PAC_PERIPHERAL_C_TCC1 = ((2 * 32 ) + 10),

    /* Interrupt flag for Peripheral bridge C - TCC2 */
    PAC_PERIPHERAL_C_TCC2 = ((2 * 32 ) + 11),

    /* Interrupt flag for Peripheral bridge C - TC0 */
    PAC_PERIPHERAL_C_TC0 = ((2 * 32 ) + 12),

    /* Interrupt flag for Peripheral bridge C - TC1 */
    PAC_PERIPHERAL_C_TC1 = ((2 * 32 ) + 13),

    /* Interrupt flag for Peripheral bridge C - TC2 */
    PAC_PERIPHERAL_C_TC2 = ((2 * 32 ) + 14),

    /* Interrupt flag for Peripheral bridge C - TC3 */
    PAC_PERIPHERAL_C_TC3 = ((2 * 32 ) + 15),

    /* Interrupt flag for Peripheral bridge C - TC4 */
    PAC_PERIPHERAL_C_TC4 = ((2 * 32 ) + 16),

    /* Interrupt flag for Peripheral bridge C - ADC0 */
    PAC_PERIPHERAL_C_ADC0 = ((2 * 32 ) + 17),

    /* Interrupt flag for Peripheral bridge C - ADC1 */
    PAC_PERIPHERAL_C_ADC1 = ((2 * 32 ) + 18),

    /* Interrupt flag for Peripheral bridge C - SDADC */
    PAC_PERIPHERAL_C_SDADC = ((2 * 32 ) + 19),

    /* Interrupt flag for Peripheral bridge C - AC */
    PAC_PERIPHERAL_C_AC = ((2 * 32 ) + 20),

    /* Interrupt flag for Peripheral bridge C - DAC */
    PAC_PERIPHERAL_C_DAC = ((2 * 32 ) + 21),

    /* Interrupt flag for Peripheral bridge C - PTC */
    PAC_PERIPHERAL_C_PTC = ((2 * 32 ) + 22),

    /* Interrupt flag for Peripheral bridge C - CCL */
    PAC_PERIPHERAL_C_CCL = ((2 * 32 ) + 23),

    /* Interrupt flag for Peripheral bridge C - TAL */
    PAC_PERIPHERAL_C_TAL = ((2 * 32 ) + 24),

    /* Interrupt flag for Peripheral bridge D - SERCOM6 */
    PAC_PERIPHERAL_D_SERCOM6 = ((3 * 32 ) + 0),

    /* Interrupt flag for Peripheral bridge D - SERCOM7 */
    PAC_PERIPHERAL_D_SERCOM7 = ((3 * 32 ) + 1),

    /* Interrupt flag for Peripheral bridge D - TC5 */
    PAC_PERIPHERAL_D_TC5 = ((3 * 32 ) + 2),

    /* Interrupt flag for Peripheral bridge D - TC6 */
    PAC_PERIPHERAL_D_TC6 = ((3 * 32 ) + 3),

    /* Interrupt flag for Peripheral bridge D - TC7 */
    PAC_PERIPHERAL_D_TC7 = ((3 * 32 ) + 4),


    /* Interrupt flag for all Peripheral bridges */
    PAC_PERIPHERAL_ANY = 0xFFFFFFFF
  
} PAC_PERIPHERAL;

// *****************************************************************************
/* Peripheral Access Control Keys enumeration

  Summary:
    List of available Peripheral Access Control Operations.

  Description:
    This enum identifies the possible PAC operation. This data type is used
    along with the PACx_PeripheralProtect() function and specifies 
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
            if(PACx_PeripheralErrorOccurred())
            {
                // Call the PACx_PeripheralErrorGet() function to 
                // identify the error.
            }
            else if(PACx_AHBSlaveErrorOccurred())
            {
                // Call the PACx_AHBSlaveErrorGet() function to 
                // identify the error.
            }
      }

      PACx_CallbackRegister(APP_PACErrorCallback, NULL);

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
    void PACx_Initialize (void);

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
        PACx_Initialize ();
    </code>

  Remarks:
     None.
*/

void PACx_Initialize( void );

// *****************************************************************************
/* Function:
    bool PACx_PeripheralIsProtected (PAC_PERIPHERAL peripheral)

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
    if(!PACx_PeripheralIsProtected(PAC_PERIPHERAL_A_PM))
    {
        PACx_PeripheralProtect(PAC_PERIPHERAL_A_PM, PAC_PROTECTION_SET);
    };
    </code>

  Remarks:
    None.
*/
    
bool PACx_PeripheralIsProtected (PAC_PERIPHERAL peripheral);

// *****************************************************************************
/* Function:
    void PACx_PeripheralProtect (PAC_PERIPHERAL peripheral,
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
    The PACx_Initialize() function should have been called once. 

  Parameters:
    peripheral - Peripheral to be operated on.

    operation - PAC operation to be performed. Refer to the description of the
    PAC_PROTECTION enumeration for possible operations.

  Returns:
    None.
    
  Example:
    <code>

    // Refer to the description of PACx_PeripheralIsProtected() 
    // function for example usage of the PACx_PeripheralProtect API.
    
    </code>

  Remarks:
    Peripherals protection can be enabled and disabled via MHC. These protection
    settings are applied when the PACx_Initialize() function is called.
*/  

void PACx_PeripheralProtect (PAC_PERIPHERAL peripheral, PAC_PROTECTION operation);

// *****************************************************************************
/* Function:
    bool PACx_PeripheralErrorOccurred (void)

  Summary:
    Returns true if any Peripheral Access Error has occurred.

  Description:
    This function returns true if any peripheral access error has occurred. The
    application can then call the PACx_PeripheralErrorGet() function 
    to identify the peripheral on which the error has occurred.

  Precondition:
    The PACx_Initialize() function should have been called once. 

  Parameters:
    None.

  Returns:
    true - atleast one peripheral is reporting a PAC error.

    false - no peripherals are reporting PAC errors.
    
  Example:
    <code>

    PAC_PERIPHERAL peripheral;

    // Process and clear all peripheral errors.
    while(PACx_PeripheralErrorOccurred())
    {
        peripheral = PACx_PeripheralErrorGet();
        
        // Assuming that some application function has processed the error, we
        // can clear the error.

        PACx_PeripheralErrorClear(peripheral);
    }

    </code>

  Remarks:
    None.
*/

bool PACx_PeripheralErrorOccurred (void);

// *****************************************************************************
/* Function:
    PAC_PERIPHERAL PACx_PeripheralErrorGet (void);

  Summary:
    Returns the first peripheral that is reporting an access error.

  Description:
    This function returns the first peripheral that is reporting an access
    error. The application can call this function to identify the peripheral
    that is a reporting an access error. In case where multiple peripherals are
    reporting access errors, the application must call this function multiple
    times. The application can use the PACx_PeripheralErrorOccurred() 
    function to check if a peripheral access error is active. The application 
    must use the PACx_PeripheralErrorClear() function to clear the 
    error before calling the PACx_PeripheralErrorGet() function 
    again. Not clearing the error will cause the function to continue reporting 
    the error on the same peripheral.

    In a case where the peripheral is experiencing repeated access errors, it is
    possible that this function will return the same peripheral ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application implement a convenient break mechanism to prevent a blocking
    loop.
   
  Precondition:
    PACx_Initialize() function should have been called once. The
    PACx_PeripheralErrorOccurred() have returned true.

  Parameters:
    None.

  Returns:
    Returns the first peripheral that is reporting an access error.

  Example:
    <code>
    // Refer to the description of the PACx_PeripheralErrorOccurred() 
    // for example usage of this function.
    </code>

  Remarks:
    None.
*/

PAC_PERIPHERAL PACx_PeripheralErrorGet (void);

// *****************************************************************************
/* Function:     
    void PACx_PeripheralErrorClear (PAC_PERIPHERAL peripheral)

  Summary:
    Clear the peripheral access error flag.

  Description:
    Calling this function will cause the peripheral access error flag to be
    cleared. This will then cause the PACx_PeripheralErrorGet() 
    function to identify the next peripheral that is reporting an error. If 
    after calling this function, there are no peripheral errors active, the
    PACx_PeripheralErrorOccurred() function will return false. 
    The application must call this function to clear the error on the peripheral 
    that was identified by the last call of the 
    PACx_PeripheralErrorGet() function.

  Precondition:
    The PACx_Initialize() function should have been called once.

  Parameters:
    peripheral - Peripheral ID of peripheral for which the peripheral error
    needs to be cleared. Specifying PAC_PERIPHERAL_ANY will clear all errors.

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the PACx_PeripheralErrorOccurred() function
    // for example usage.
    </code>

  Remarks:
    None.
*/

void PACx_PeripheralErrorClear (PAC_PERIPHERAL peripheral);

// *****************************************************************************
/* Function:
    bool PACx_AHBSlaveErrorOccurred (void)

  Summary:
    Returns true if an error has occurred on any of the AHB slaves.

  Description:
    This function returns true if any AHB Slave error has occurred. The
    application can then call the PACx_AHBSlaveErrorGet() function 
    to identify the AHB Slave on which the error has occurred.

  Precondition:
    The PACx_Initialize() function should have been called once. 

  Parameters:
    None.

  Returns:
    true - atleast one AHB Slave is reporting an access error.

    false - no AHB Slave is reporting access errors.
    
  Example:
    <code>

    PAC_AHB_SLAVE ahbSlave;

    // Process and clear all AHB Slave errors.
    while(PACx_AHBSlaveErrorOccurred())
    {
        ahbSlave = PACx_AHBSlaveErrorGet();
        
        // Assuming that some application function has processed the error, we
        // can clear the error.

        PACx_AHBSlaveErrorClear(ahbSlave);
    }

    </code>

  Remarks:
    None.
*/

bool PACx_AHBSlaveErrorOccurred (void);

// *****************************************************************************
/* Function:
    AHB_SLAVE PACx_AHBSlaveErrorGet (void);

  Summary:
    Returns the first AHB Slave that is reporting an access error.

  Description:
    This function returns the first AHB Slave that is reporting an access
    error. The application can call this function to identify the AHB Slave
    that is a reporting an access error. In case where multiple AHB Slaves are
    reporting access errors, the application must call this function multiple
    times. The application can use the PACx_AHBSlaveErrorOccurred() 
    function to check if a AHB Slave access error is active. The application 
    must use the PACx_AHBSlaveErrorClear() function to clear the 
    error before calling the PACx_AHBSlaveErrorGet() function again. 
    Not clearing the error will cause the function to continue reporting the 
    error on the same AHB Slave.

    In a case where the AHB Slave is experiencing repeated access errors, it is
    possible that this function will return the same AHB Slave ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application in implement a convenient break mechanism to prevent a 
    blocking loop.
   
  Precondition:
    PACx_Initialize() function should have been called once. The
    PACx_AHBSlaveErrorOccurred() have returned true.

  Parameters:
    None.

  Returns:
    Returns the first AHB Slave that is reporting an access error.

  Example:
    <code>
    // Refer to the description of the PACx_AHBSlaveErrorOccurred() 
    // for example usage of this function.
    </code>

  Remarks:
    None.
*/

PAC_AHB_SLAVE PACx_AHBSlaveErrorGet (void);

// *****************************************************************************
/* Function:     
    void PACx_AHBSlaveErrorClear (PAC_AHB_SLAVE AHB Slave)

  Summary:
    Clear the AHB Slave access error flag.

  Description:
    Calling this function will cause the AHB Slave access error flag to be
    cleared. This will then cause the PACx_AHBSlaveErrorGet() 
    function to identify the next AHB Slave that is reporting an error. If after 
    calling this function, there are no AHB Slave errors active, the
    PACx_AHBSlaveErrorOccurred() function will return false. The 
    application must call this function to clear the error on the AHB Slave that 
    was identified by the last call of the PACx_AHBSlaveErrorGet() 
    function.

  Precondition:
    The PACx_Initialize() function should have been called once.

  Parameters:
    AHB Slave - AHB Slave ID of AHB Slave for which the AHB Slave error needs to
    be cleared. Specifying PAC_AHB_SLAVE_ANY will clear all errors.

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the PACx_AHBSlaveErrorOccurred() 
    // function for example usage.
    </code>

  Remarks:
     None.
*/

void PACx_AHBSlaveErrorClear (PAC_AHB_SLAVE ahbSlave);


// *****************************************************************************
/* Function:
    void PACx_CallbackRegister(PAC_CALLBACK callback,uintptr_t context)

  Summary:
    Registers the function to be called when a PAC error has occurred.

  Description
    This function registers the callback function to be called when a PAC error
    has occurred. The function is available only when the module interrupt is
    enabled in MHC.

  Precondition:
    PACx_Initialize() function should have beeb called once. 
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

void PACx_CallbackRegister (PAC_CALLBACK callback, uintptr_t context);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_PACx_H */