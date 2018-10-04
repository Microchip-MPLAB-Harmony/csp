/*******************************************************************************
  Divide Square Root Accelerator (${DIVAS_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DIVAS_INSTANCE_NAME?lower_case}.h

  Summary:
    ${DIVAS_INSTANCE_NAME} PLIB Header File

  Description:
    This file defines the interface to the DIVAS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

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

// DOM-IGNORE-BEGIN
#ifndef PLIB_${DIVAS_INSTANCE_NAME}_H
#define PLIB_${DIVAS_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C"
{
#endif

// DOM-IGNORE-END

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
    void ${DIVAS_INSTANCE_NAME}_Initialize(void);

  Summary:
    Initializes ${DIVAS_INSTANCE_NAME} module of the device.

  Description:
    This function initializes ${DIVAS_INSTANCE_NAME} module of the device with the
    values configured in MCC GUI. Once the peripheral is initialized, signed,
    unsigned division and square root functions can be used.

  Precondition:
    MCC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        ${DIVAS_INSTANCE_NAME}_Initialize();
    </code>

  Remarks:
    This function must be called before any other DIVAS function is called.
    This function should only be called once during system initialization.
*/

void ${DIVAS_INSTANCE_NAME}_Initialize(void);

// *****************************************************************************
/* Function:
    bool ${DIVAS_INSTANCE_NAME}_DivideSigned ( int32_t divisor, int32_t dividend,
                                    int32_t * quotient, int32_t * remainder );

Summary:
    This function uses the DIVAS peripheral to performs a signed 32-bit
    division.

  Description:
    This function uses the DIVAS peripheral to perform a signed 32-bit division.
    The function takes a signed divisor and dividend and returns the quotient
    and remainder. If the library is configured (in MHC) with the Leading Zero
    optimization option enabled, a division operation takes 2-16 cycles. If the
    option is disabled, the option always takes 16 cycles. The latter option is
    recommended if deterministic operation is desired.

  Precondition:
    The peripheral should have been initialized by calling the
    ${DIVAS_INSTANCE_NAME}_Initialize() function once. The AHB clock to the DIVAS
    Peripheral should have been enabled.

  Parameters:
    divisor - This should contain the signed divisor.

    dividend - This should contain the signed dividend.

    quotient - This is a pointer to a output parameter which will contain the
    quotient of the division operation. This value is valid if the division
    operation was successful.

    remainder - This is a pointer to a output parameter which will contain the
    remainder of the division operation. This value is valid if the division
    operation was successful.

  Returns:
    true - if the division operation was successful.
    false - if a divide-by-zero error has occurred.

  Example:
    <code>
        int32_t divisor;
        int32_t dividend;
        int32_t quotient;
        int32_t remainder;

        divisor = -2000;
        dividend = 10000;

        if (true == ${DIVAS_INSTANCE_NAME}_DivideSigned(divisor, dividend,
                                                    &quotient, &remainder ))
        {
            // quotient and remainder will have valid values.
        }
    </code>

  Remarks:
    None.
*/

bool ${DIVAS_INSTANCE_NAME}_DivideSigned( int32_t divisor, int32_t dividend, int32_t * quotient, int32_t * remainder );

// *****************************************************************************
/* Function:
    bool ${DIVAS_INSTANCE_NAME}_DivideUnsigned ( uint32_t divisor,
                uint32_t dividend, uint32_t * quotient, uint32_t * remainder );

 Summary:
    This function uses the DIVAS peripheral to performs a unsigned 32-bit
    division.

  Description:
    This function uses the DIVAS peripheral to perform unsigned 32-bit division.
    The function takes a unsigned divisor and dividend and returns the quotient
    and remainder. If the library is configured (in MHC) with the Leading Zero
    optimization option enabled, a division operation takes 2-16 cycles. If the
    option is disabled, the option always takes 16 cycles. The latter option is
    recommended if deterministic operation is desired.

  Precondition:
    The peripheral should have been initialized by calling the
    ${DIVAS_INSTANCE_NAME}_Initialize() function once. The AHB clock to the DIVAS
    peripheral should have been enabled.

  Parameters:
    divisor - This should contain the unsigned divisor.

    dividend - This should contain the unsigned dividend.

    quotient - This is a pointer to a output parameter which will contain the
    quotient of the division operation. This value is valid if the division
    operation was successful.

    remainder - This is a pointer to a output parameter which will contain the
    remainder of the division operation. This value is valid if the division
    operation was successful.

  Returns:
    true - if the division operation was successful.
    false - if a divide-by-zero error has occurred.

  Example:
    <code>
        uint32_t divisor;
        uint32_t dividend;
        uint32_t quotient;
        uint32_t remainder;

        divisor = 2000;
        dividend = 10000;

        if (true == ${DIVAS_INSTANCE_NAME}_DivideUnsigned(divisor, dividend,
                                                    &quotient, &remainder ))
        {
            // quotient and remainder will have valid values.
        }
    </code>

  Remarks:
    None.
*/

bool ${DIVAS_INSTANCE_NAME}_DivideUnsigned( uint32_t divisor, uint32_t dividend, uint32_t * quotient, uint32_t * remainder );

// *****************************************************************************
/* Function:
    uint32_t ${DIVAS_INSTANCE_NAME}_SquareRoot ( uint32_t number ,
                                            uint32_t * remainder);

  Summary:
    This function uses the DIVAS peripheral to perform a square root operation.

  Description:
    This function uses the DIVAS peripheral to perform a square root operation.
    The function will return the square root of the number contained in number.
    The remainder output parameter will contain a remainder if the square root
    was not perfect.

  Precondition:
    The peripheral should have been initialized by calling the
    DIVASx_Initialize() function once. The AHB clock to the DIVAS peripheral
    should have been enabled.

  Parameters:
    number - unsigned number whose square root needs to be obtained.

    remainder - pointer to an output parameter which will contain the remainder
    of the square root operation (in case of a imperfect square root operation).

  Returns:
    The function returns the square root of the value contained in the number
    parameter.

  Example:
    <code>
        uint32_t number;
        uint32_t remainder;
        uint32_t squareRoot;

        number = 144;
        squareRoot = ${DIVAS_INSTANCE_NAME}_SquareRoot (number, &remainder);

    </code>

  Remarks:
    None.
*/

uint32_t ${DIVAS_INSTANCE_NAME}_SquareRoot ( uint32_t number , uint32_t * remainder);

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif /* PLIB_${DIVAS_INSTANCE_NAME}_H */
