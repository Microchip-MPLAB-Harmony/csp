/*******************************************************************************
  Divide Square Root Accelerator (DIVAS) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_divas${DIVAS_INDEX}.c

  Summary:
    DIVAS PLIB Implementation File

  Description:
    This file defines the interface to the DIVAS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_divas${DIVAS_INDEX}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: DIVAS${DIVAS_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void DIVAS${DIVAS_INDEX}_Initialize(void);

  Summary:
    Initializes DIVAS ${DIVAS_INDEX} module of the device.

  Description:
    This function initializes DIVAS${DIVAS_INDEX} module of the device with the
    values configured in MCC GUI. Once the peripheral is initialized, signed,
    unsigned division and square root functions can be used.

  Remarks:
    Refer plib_divas${DIVAS_INDEX}.h file for more information.
*/

void DIVAS${DIVAS_INDEX}_Initialize(void)
{
    /* 
     * Enable/Disable Leading Zero optimization ,
     * If enabled,  32 bit divisions = 2-16 cycles
     * If disabled, 32 bit divisions = 16 cycles
     */
    DIVAS_REGS->DIVAS_CTRLA |= DIVAS_CTRLA_RESETVALUE ${DIVAS_DLZ?then(' ', '| DIVAS_CTRLA_DLZ_Msk')};
}

// *****************************************************************************
/* Function:
    bool DIVAS${DIVAS_INDEX}_DivideSigned ( int32_t divisor, int32_t dividend,
                                int32_t * quotient, int32_t * remainder );

 Summary:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to performs a
    unsigned 32-bit division.

  Description:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to perform unsigned
    32-bit division.

    The function takes a unsigned divisor and dividend and returns the quotient
    and remainder. If the library is configured (in MHC) with the Leading Zero
    optimization option enabled, a division operation takes 2-16 cycles. If the
    option is disabled, the option always takes 16 cycles. The latter option is
    recommended if deterministic operation is desired.

  Remarks:
    Refer plib_divas${DIVAS_INDEX}.h for more information.
*/

bool DIVAS${DIVAS_INDEX}_DivideSigned ( int32_t divisor, int32_t dividend, int32_t * quotient, int32_t * remainder )
{
    bool statusValue = false;

    if(divisor != 0)
    {
        if(dividend == 0)
        {
            statusValue = true;
            
            /* Handle the trivial case. This does not require hardware */
            if(quotient != NULL)
            {
                *quotient = 0;
            }

            if(remainder != NULL)
            {
                *remainder = 0;
            }
        }
        else
        {
            /* Selection of the signed division */
            DIVAS_REGS->DIVAS_CTRLA |= DIVAS_CTRLA_SIGNED_Msk;

            /* Writing the dividend to DIVIDEND register */
            DIVAS_REGS->DIVAS_DIVIDEND = dividend;

            /* Writing the divisor to DIVISOR register */
            DIVAS_REGS->DIVAS_DIVISOR = divisor;

            while((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_BUSY_Msk) == DIVAS_STATUS_BUSY_Msk)
            {
                /* Wait for the division to complete */
            }

            if ((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_DBZ_Msk) != DIVAS_STATUS_DBZ_Msk)
            {
                statusValue = true;

                if( quotient != NULL)
                {
                    /* Reading the resultant Division value from the RESULT register */
                    *quotient = DIVAS_REGS->DIVAS_RESULT;
                }

                if( remainder != NULL)
                {
                    /* Reading the resultant remainder value from the REM register */
                    *remainder = DIVAS_REGS->DIVAS_REM;
                }
            }
        }
    }

    return statusValue;
}

// *****************************************************************************
/* Function:
    bool DIVAS${DIVAS_INDEX}_DivideUnsigned ( uint32_t divisor,
                uint32_t dividend, uint32_t * quotient, uint32_t * remainder );

 Summary:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to performs a
    unsigned 32-bit division.

  Description:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to perform unsigned
    32-bit division.

    The function takes a unsigned divisor and dividend and returns the quotient
    and remainder. If the library is configured (in MHC) with the Leading Zero
    optimization option enabled, a division operation takes 2-16 cycles. If the
    option is disabled, the option always takes 16 cycles. The latter option is
    recommended if deterministic operation is desired.

  Remarks:
    Refer plib_divas${DIVAS_INDEX}.h for more information.
*/

bool DIVAS${DIVAS_INDEX}_DivideUnsigned( uint32_t divisor, uint32_t dividend, uint32_t * quotient, uint32_t * remainder )
{
    bool statusValue = false;
    if(divisor != 0)
    {
        if(dividend == 0)
        {
            statusValue = true;
            
            /* Handle the trivial case. This does not require hardware */
            if(quotient != NULL)
            {
                *quotient = 0;
            }

            if(remainder != NULL)
            {
                *remainder = 0;
            }
        }
        else
        {
            /* Selection of the unsigned division */
            DIVAS_REGS->DIVAS_CTRLA &= ~DIVAS_CTRLA_SIGNED_Msk;

           /* Writing the dividend to DIVIDEND register */
            DIVAS_REGS->DIVAS_DIVIDEND = dividend;

            /* Writing the divisor to DIVISOR register */
            DIVAS_REGS->DIVAS_DIVISOR = divisor;

            while((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_BUSY_Msk) == DIVAS_STATUS_BUSY_Msk)
            {
                /* Wait for the division to complete */
            }

            if ((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_DBZ_Msk) != DIVAS_STATUS_DBZ_Msk)
            {
                statusValue = true;
                
                if( quotient != NULL)
                {
                    /* Reading the resultant Division value from the RESULT register */
                    *quotient = DIVAS_REGS->DIVAS_RESULT;
                }

                if( remainder != NULL)
                {
                    /* Reading the resultant remainder value from the REM register */
                    *remainder = DIVAS_REGS->DIVAS_REM;

                }
            }
        }
    }

    return statusValue;
}


// *****************************************************************************
/* Function:
    uint32_t DIVAS${DIVAS_INDEX}_SquareRoot ( uint32_t number ,
                                              uint32_t * remainder);

  Summary:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to perform a
    square root operation.

  Description:
    This function uses the DIVAS${DIVAS_INDEX} peripheral to perform a square
    root operation.

    The function will return the square root of the number contained in number.
    The remainder output parameter will contain a remainder if the square root
    was not perfect.

  Remarks:
    Refer plib_divas${DIVAS_INDEX}.h for more information.
*/

uint32_t DIVAS${DIVAS_INDEX}_SquareRoot ( uint32_t number , uint32_t * remainder)
{
    uint32_t squareRootResult = 0;

    /* Writing the number to SQRNUM register */
    DIVAS_REGS->DIVAS_SQRNUM = number;

    while((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_BUSY_Msk) == DIVAS_STATUS_BUSY_Msk)
    {
        /* Wait for the square root to complete */
    }

    /* Reading the resultant square root value from the RESULT register */
    squareRootResult = DIVAS_REGS->DIVAS_RESULT;

    if(remainder != NULL)
    {
        /* Reading the resultant remainder value from the REM register */
        *remainder = DIVAS_REGS->DIVAS_REM;
    }

    return squareRootResult;
}
