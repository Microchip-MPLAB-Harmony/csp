/*******************************************************************************
  Divide Square Root Accelerator (DIVAS) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DIVAS_INSTANCE_NAME?lower_case}.c

  Summary:
    DIVAS PLIB Implementation File

  Description:
    This file defines the interface to the DIVAS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

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


#include "plib_${DIVAS_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${DIVAS_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${DIVAS_INSTANCE_NAME}_Initialize(void)
{
    <#if DIVAS_DLZ == false>
    /* Disable Leading Zero optimization*/
    DIVAS_REGS->DIVAS_CTRLA |= DIVAS_CTRLA_DLZ_Msk;
    <#else>
    /* Leading Zero optimization is by default enabled*/
    </#if>
}


bool ${DIVAS_INSTANCE_NAME}_DivideSigned ( int32_t divisor, int32_t dividend, int32_t * quotient, int32_t * remainder )
{
    bool statusValue = false;
    uint32_t quo = 0;
    uint32_t rem = 0;

    if(divisor != 0)
    {
        if(dividend == 0)
        {
            statusValue = true;
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


            statusValue = true;
            quo = DIVAS_REGS->DIVAS_RESULT;
            rem = DIVAS_REGS->DIVAS_REM;
        }
        if(quotient != NULL)
        {
            *quotient = quo;
        }
        if(remainder != NULL)
        {
            *remainder = rem;
        }
    }
    return statusValue;
}



bool ${DIVAS_INSTANCE_NAME}_DivideUnsigned( uint32_t divisor, uint32_t dividend, uint32_t * quotient, uint32_t * remainder )
{
    bool statusValue = false;
    uint32_t quo = 0;
    uint32_t rem = 0;
    
    if(divisor != 0)
    {
        if(dividend == 0)
        {
            statusValue = true;
        }
        else
        {
            /* Selection of the unsigned division */
            DIVAS_REGS->DIVAS_CTRLA &= ~DIVAS_CTRLA_SIGNED_Msk;
            
            /* Writing the dividend to DIVIDEND register */
            DIVAS_REGS->DIVAS_DIVIDEND = dividend;
            
            /* Writing the divisor to DIVISOR register */
            DIVAS_REGS->DIVAS_DIVISOR = divisor;
            
            statusValue = true;
            quo = DIVAS_REGS->DIVAS_RESULT;
            rem = DIVAS_REGS->DIVAS_REM;
        }

        if( quotient != NULL)
        {
            *quotient = quo;
        }

        if( remainder != NULL)
        {
            *remainder = rem;

        }
    }
    return statusValue;
}


uint32_t ${DIVAS_INSTANCE_NAME}_SquareRoot ( uint32_t number , uint32_t * remainder)
{
    uint32_t squareRootResult = 0;

    DIVAS_REGS->DIVAS_SQRNUM = number;

    while((DIVAS_REGS->DIVAS_STATUS & DIVAS_STATUS_BUSY_Msk) == DIVAS_STATUS_BUSY_Msk)
    {
        /* Wait for the square root to complete */
    }

    squareRootResult = DIVAS_REGS->DIVAS_RESULT;

    if(remainder != NULL)
    {
        *remainder = DIVAS_REGS->DIVAS_REM;
    }

    return squareRootResult;
}
