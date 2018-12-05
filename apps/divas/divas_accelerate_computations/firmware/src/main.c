/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    int32_t number;
    uint32_t squareroot;   
    
    number = 144;
    squareroot = DIVAS_SquareRoot(number);
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                SQUARE ROOT CALCULATION                  ");
    printf("\n\r---------------------------------------------------------");
    printf("\n\rInput Number = %lu\r",number);
    printf("\n\rSquare Root = %lu\r",squareroot);
    
    int32_t sign_numerator;
    int32_t sign_denominator;
    int32_t sign_quotient;

    sign_denominator = -2000;
    sign_numerator = 10000;
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                SIGNED INTEGER DIVISION                  ");
    printf("\n\r---------------------------------------------------------");
    printf("\n\rNumerator = %ld, Denominator = %ld\r",sign_numerator,sign_denominator);
    sign_quotient = DIVAS_DivSigned(sign_numerator, sign_denominator);
    printf("\n\rQuotient = %ld\r",sign_quotient);
    
    uint32_t unsign_numerator;
    uint32_t unsign_denominator;
    uint32_t unsign_quotient;

    unsign_denominator = 2000;
    unsign_numerator = 10000;

    printf("\n\r---------------------------------------------------------");
    printf("\n\r                UNSIGNED INTEGER DIVISION                ");
    printf("\n\r---------------------------------------------------------");
    printf("\n\rNumerator = %lu, Denominator = %lu\r",unsign_numerator,unsign_denominator);
    unsign_quotient = DIVAS_DivUnsigned(unsign_numerator,unsign_denominator);
    printf("\n\rQuotient = %lu\r",unsign_quotient);
   
    unsign_denominator = 2000;
    unsign_numerator = 10001;
    uint64_t unsign_quotient2;
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r          UNSIGNED INTEGER DIVISION WITH REMAINDER       ");
    printf("\n\r---------------------------------------------------------");
    unsign_quotient2 = DIVAS_DivmodUnsigned(unsign_numerator,unsign_denominator);
    printf("\n\rNumerator = %lu, Denominator = %lu\r",unsign_numerator,unsign_denominator);
    printf("\n\rQuotient = %lu, Remainder = %lu\n\r",(uint32_t)unsign_quotient2,(uint32_t)(unsign_quotient2 >> 32));
    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

