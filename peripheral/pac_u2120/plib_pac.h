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
    PAC_PERIPHERAL_A_PAC = 0,

    /* Interrupt flag for Peripheral bridge A - PM */
    PAC_PERIPHERAL_A_PM = 1,

    /* Interrupt flag for Peripheral bridge A - MCLK */
    PAC_PERIPHERAL_A_MCLK = 2,

    /* Interrupt flag for Peripheral bridge A - RSTC */
    PAC_PERIPHERAL_A_RSTC = 3,

    /* Interrupt flag for Peripheral bridge A - OSCCTRL */
    PAC_PERIPHERAL_A_OSCCTRL = 4,

    /* Interrupt flag for Peripheral bridge A - OSC32KCTRL */
    PAC_PERIPHERAL_A_OSC32KCTRL = 5,

    /* Interrupt flag for Peripheral bridge A - SUPC */
    PAC_PERIPHERAL_A_SUPC = 6,

    /* Interrupt flag for Peripheral bridge A - GCLK */
    PAC_PERIPHERAL_A_GCLK = 7,

    /* Interrupt flag for Peripheral bridge A - WDT */
    PAC_PERIPHERAL_A_WDT = 8,

    /* Interrupt flag for Peripheral bridge A - RTC */
    PAC_PERIPHERAL_A_RTC = 9,

    /* Interrupt flag for Peripheral bridge A - EIC */
    PAC_PERIPHERAL_A_EIC = 10,

    /* Interrupt flag for Peripheral bridge A - FREQM */
    PAC_PERIPHERAL_A_FREQM = 11,

    /* Interrupt flag for Peripheral bridge A - TSENS */
    PAC_PERIPHERAL_A_TSENS = 12,

    /* Interrupt flag for Peripheral bridge B - PORT */
    PAC_PERIPHERAL_B_PORT = 32,

    /* Interrupt flag for Peripheral bridge B - DSU */
    PAC_PERIPHERAL_B_DSU = 33,

    /* Interrupt flag for Peripheral bridge B - NVMCTRL */
    PAC_PERIPHERAL_B_NVMCTRL = 34,

    /* Interrupt flag for Peripheral bridge B - DMAC */
    PAC_PERIPHERAL_B_DMAC = 35,

    /* Interrupt flag for Peripheral bridge B - MTB */
    PAC_PERIPHERAL_B_MTB = 36,

    /* Interrupt flag for Peripheral bridge B - HMATRIXHS */
    PAC_PERIPHERAL_B_HMATRIXHS = 37,

    /* Interrupt flag for Peripheral bridge C - EVSYS */
    PAC_PERIPHERAL_C_EVSYS = 64,

    /* Interrupt flag for Peripheral bridge C - SERCOM0 */
    PAC_PERIPHERAL_C_SERCOM0 = 65,

    /* Interrupt flag for Peripheral bridge C - SERCOM1 */
    PAC_PERIPHERAL_C_SERCOM1 = 66,

    /* Interrupt flag for Peripheral bridge C - SERCOM2 */
    PAC_PERIPHERAL_C_SERCOM2 = 67,

    /* Interrupt flag for Peripheral bridge C - SERCOM3 */
    PAC_PERIPHERAL_C_SERCOM3 = 68,

    /* Interrupt flag for Peripheral bridge C - SERCOM4 */
    PAC_PERIPHERAL_C_SERCOM4 = 69,

    /* Interrupt flag for Peripheral bridge C - SERCOM5 */
    PAC_PERIPHERAL_C_SERCOM5 = 70,

    /* Interrupt flag for Peripheral bridge C - CAN0 */
    PAC_PERIPHERAL_C_CAN0 = 71,

    /* Interrupt flag for Peripheral bridge C - CAN1 */
    PAC_PERIPHERAL_C_CAN1 = 72,

    /* Interrupt flag for Peripheral bridge C - TCC0 */
    PAC_PERIPHERAL_C_TCC0 = 73,

    /* Interrupt flag for Peripheral bridge C - TCC1 */
    PAC_PERIPHERAL_C_TCC1 = 74,

    /* Interrupt flag for Peripheral bridge C - TCC2 */
    PAC_PERIPHERAL_C_TCC2 = 75,

    /* Interrupt flag for Peripheral bridge C - TC0 */
    PAC_PERIPHERAL_C_TC0 = 76,

    /* Interrupt flag for Peripheral bridge C - TC1 */
    PAC_PERIPHERAL_C_TC1 = 77,

    /* Interrupt flag for Peripheral bridge C - TC2 */
    PAC_PERIPHERAL_C_TC2 = 78,

    /* Interrupt flag for Peripheral bridge C - TC3 */
    PAC_PERIPHERAL_C_TC3 = 79,

    /* Interrupt flag for Peripheral bridge C - TC4 */
    PAC_PERIPHERAL_C_TC4 = 80,

    /* Interrupt flag for Peripheral bridge C - ADC0 */
    PAC_PERIPHERAL_C_ADC0 = 81,

    /* Interrupt flag for Peripheral bridge C - ADC1 */
    PAC_PERIPHERAL_C_ADC1 = 82,

    /* Interrupt flag for Peripheral bridge C - SDADC */
    PAC_PERIPHERAL_C_SDADC = 83,

    /* Interrupt flag for Peripheral bridge C - AC */
    PAC_PERIPHERAL_C_AC = 84,

    /* Interrupt flag for Peripheral bridge C - DAC */
    PAC_PERIPHERAL_C_DAC = 85,

    /* Interrupt flag for Peripheral bridge C - PTC */
    PAC_PERIPHERAL_C_PTC = 86,

    /* Interrupt flag for Peripheral bridge C - CCL */
    PAC_PERIPHERAL_C_CCL = 87,

    /* Interrupt flag for Peripheral bridge D - SERCOM6 */
    PAC_PERIPHERAL_D_SERCOM6 = 96,

    /* Interrupt flag for Peripheral bridge D - SERCOM7 */
    PAC_PERIPHERAL_D_SERCOM7 = 97,

    /* Interrupt flag for Peripheral bridge D - TC5 */
    PAC_PERIPHERAL_D_TC5 = 98,

    /* Interrupt flag for Peripheral bridge D - TC6 */
    PAC_PERIPHERAL_D_TC6 = 99,

    /* Interrupt flag for Peripheral bridge D - TC7 */
    PAC_PERIPHERAL_D_TC7 = 100,

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
    void PACx_Initialize( void )

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
        PACx_Initialize();
    </code>

  Remarks:
    None.
*/

void PACx_Initialize( void );

// *****************************************************************************
/* Function:
    void PACx_PeripheralProtectSetup(PAC_PERIPHERAL peripheral,
                                                      PAC_PROTECTION operation)

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
        PACx_Initialize();
        PACx_PeripheralProtectSetup(PAC_PERIPHERAL_B_DSU, PAC_PROTECTION_CLEAR);
    </code>

  Remarks:
    Peripherals protection can be enabled and disabled via MHC. These protection
    settings are applied when the PACx_Initialize() function is called.
*/  

void PACx_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation );

// *****************************************************************************
/* Function:
    void PACx_CallbackRegister( PAC_CALLBACK callback, uintptr_t context )

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

void PACx_CallbackRegister( PAC_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_PACx_H */