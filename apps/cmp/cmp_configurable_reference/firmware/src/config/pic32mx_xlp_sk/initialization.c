/*******************************************************************************
  System Initialization File

  File Name:
    initialization.c

  Summary:
    This file contains source code necessary to initialize the system.

  Description:
    This file contains source code necessary to initialize the system.  It
    implements the "SYS_Initialize" function, defines the configuration bits,
    and allocates any necessary global system resources,
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
#include "definitions.h"
#include "device.h"



// ****************************************************************************
// ****************************************************************************
// Section: Configuration Bits
// ****************************************************************************
// ****************************************************************************

/*** DEVCFG0 ***/
#pragma config DEBUG =      OFF
#pragma config JTAGEN =     OFF
#pragma config ICESEL =     ICS_PGx2
#pragma config PWP =        OFF
#pragma config BWP =        OFF
#pragma config CP =         OFF
#pragma config SMCLR =      MCLR_NORM


/*** DEVCFG1 ***/
#pragma config FNOSC =      SPLL
#pragma config FPBDIV =     DIV_2
#pragma config FSOSCEN =    ON
#pragma config IESO =       ON
#pragma config POSCMOD =    OFF
#pragma config OSCIOFNC =   OFF
#pragma config FCKSM =      CSDCMD
#pragma config WDTPS =      PS1048576
#pragma config WDTSPGM =    ON
#pragma config FWDTEN =     OFF
#pragma config WINDIS =     OFF
#pragma config FWDTWINSZ =  WINSZ_25


/*** DEVCFG2 ***/
#pragma config BOREN =    ON
#pragma config FPLLIDIV =   DIV_2
#pragma config FPLLICLK =   PLL_FRC
#pragma config FPLLMUL =    MUL_18
#pragma config FPLLODIV =   DIV_1
#pragma config DSBOREN =    ON
#pragma config DSWDTPS =    DSPS32
#pragma config DSWDTOSC =   LPRC
#pragma config DSWDTEN =    OFF
#pragma config FDSEN =      ON
#pragma config UPLLEN =     OFF
#pragma config UPLLIDIV =   DIV_3

/*** DEVCFG3 ***/
#pragma config AI2C1 =      OFF
#pragma config AI2C2 =      OFF
#pragma config USERID =     0xffff
#pragma config PMDL1WAY =   ON
#pragma config IOL1WAY =    ON
#pragma config FUSBIDIO =   ON







// *****************************************************************************
// *****************************************************************************
// Section: Driver Initialization Data
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: System Data
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Library/Stack Initialization Data
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: System Initialization
// *****************************************************************************
// *****************************************************************************



/*******************************************************************************
  Function:
    void SYS_Initialize ( void *data )

  Summary:
    Initializes the board, services, drivers, application and other modules.

  Remarks:
 */

void SYS_Initialize ( void* data )
{
    /* Start out with interrupts disabled before configuring any modules */
    __builtin_disable_interrupts();

  
    CLK_Initialize();
	GPIO_Initialize();

    /* Configure KSEG0 as cacheable memory. This is needed for Prefetch Buffer */
    __builtin_mtc0(16, 0,(__builtin_mfc0(16, 0) | 0x3));

    /* Configure Flash Wait States and Prefetch */
    CHECONbits.PFMWS = 3;
    CHECONbits.PREFEN = 3;

    /* Set the SRAM wait states to zero */
    BMXCONbits.BMXWSDRM = 0;




	UART1_Initialize();

	CVR_Initialize();

	CMP_Initialize();





    EVIC_Initialize();

	/* Enable global interrupts */
    __builtin_enable_interrupts();


}


/*******************************************************************************
 End of File
*/
