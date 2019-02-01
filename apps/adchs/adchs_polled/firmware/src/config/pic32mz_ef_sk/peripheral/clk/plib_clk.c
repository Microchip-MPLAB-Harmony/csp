
 /*******************************************************************************
  SYS CLK Static Functions for Clock System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clk.c.ftl

  Summary:
    SYS CLK static function implementations for the Clock System Service.

  Description:
    The Clock System Service provides a simple interface to manage the oscillators
    on Microchip microcontrollers. This file defines the static implementation for the 
    Clock System Service.
    
  Remarks:
    Static functions incorporate all system clock configuration settings as
    determined by the user via the Microchip Harmony Configurator GUI.  It provides 
    static version of the routines, eliminating the need for an object ID or 
    object handle.
    
    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/
// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_clk.h"

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Functions
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    void CLK_Initialize ( void )

  Summary:
    Initializes hardware and internal data structure of the System Clock.

  Description:
    This function initializes the hardware and internal data structure of System
    Clock Service.

  Remarks:
    This is configuration values for the static version of the Clock System Service 
    module is determined by the user via the Microchip Harmony Configurator GUI.

    The objective is to eliminate the user's need to be knowledgeable in the function of
    the 'configuration bits' to configure the system oscillators. 
*/

void CLK_Initialize( void )
{
    bool int_flag = false;
    volatile uint32_t *reg;
    uint8_t ii;
    
    int_flag = (bool)__builtin_disable_interrupts();
    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    if (int_flag)
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001)); /* enable interrupts */
    }
    
    OSCCONbits.FRCDIV = 0;
    
    /* Enable Secondary Oscillator */
    OSCCONSET = _OSCCON_SOSCEN_MASK;


    /* Enable Peripheral Bus 1 */
    /* PBDIV = 2-1 */
    *(volatile uint32_t *)(&PB1DIV) = 0x1;


    /* Enable Peripheral Bus 2 */
    /* PBDIV = 2-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB2DIV) = 0x8001;


    /* Enable Peripheral Bus 3 */
    /* PBDIV = 2-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB3DIV) = 0x8001;




    /* Enable Peripheral Bus 4 */
    /* PBDIV = 2-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB4DIV) = 0x8001;



    /* Enable Peripheral Bus 5 */
    /* PBDIV = 2-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB5DIV) = 0x8001;


    /* Enable Peripheral Bus 7 */
    /* PBDIV = 1-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB7DIV) = 0x8000;


    /* Enable Peripheral Bus 8 */
    /* PBDIV = 2-1 */
    /* ON = 1                             */
    *(volatile uint32_t *)(&PB8DIV) = 0x8001;



    /* Set up Reference Clock 1 */
    /* REFO1CON register */        
    /* ROSEL =  9 */
    /* DIVSWEN = 1 */
    /* RODIV = 0 */
    *(volatile uint32_t *)(&REFO1CON) = 0x209;
    
    /* REFO1TRIM register */
    /* ROTRIM = 0 */
    *(volatile uint32_t *)(&REFO1TRIM) = 0x0;

    /* ON - enable oscillator */
    *(volatile uint32_t *)(&REFO1CONSET) = 0x00008000;
    /* Clear Output Enable bit, OE */
    *(volatile uint32_t *)(&REFO1CONCLR) = 0x00001000;


    /* Set up Reference Clock 2 */
    /* REFO2CON register */        
    /* ROSEL =  9 */
    /* DIVSWEN = 1 */
    /* RODIV = 0 */
    *(volatile uint32_t *)(&REFO2CON) = 0x209;
    
    /* REFO2TRIM register */
    /* ROTRIM = 0 */
    *(volatile uint32_t *)(&REFO2TRIM) = 0x0;

    /* ON - enable oscillator */
    *(volatile uint32_t *)(&REFO2CONSET) = 0x00008000;
    /* Clear Output Enable bit, OE */
    *(volatile uint32_t *)(&REFO2CONCLR) = 0x00001000;


    /* Set up Reference Clock 3 */
    /* REFO3CON register */        
    /* ROSEL =  9 */
    /* DIVSWEN = 1 */
    /* RODIV = 0 */
    *(volatile uint32_t *)(&REFO3CON) = 0x209;
    
    /* REFO3TRIM register */
    /* ROTRIM = 0 */
    *(volatile uint32_t *)(&REFO3TRIM) = 0x0;

    /* ON - enable oscillator */
    *(volatile uint32_t *)(&REFO3CONSET) = 0x00008000;
    /* Clear Output Enable bit, OE */
    *(volatile uint32_t *)(&REFO3CONCLR) = 0x00001000;


    /* Set up Reference Clock 4 */
    /* REFO4CON register */        
    /* ROSEL =  9 */
    /* DIVSWEN = 1 */
    /* RODIV = 0 */
    *(volatile uint32_t *)(&REFO4CON) = 0x209;
    
    /* REFO4TRIM register */
    /* ROTRIM = 0 */
    *(volatile uint32_t *)(&REFO4TRIM) = 0x0;

    /* ON - enable oscillator */
    *(volatile uint32_t *)(&REFO4CONSET) = 0x00008000;
    /* Clear Output Enable bit, OE */
    *(volatile uint32_t *)(&REFO4CONCLR) = 0x00001000;
  
    /* Lock system since done with clock configuration */
    int_flag = (bool)__builtin_disable_interrupts();
    SYSKEY = 0x33333333;  
    if (int_flag) /* if interrupts originally were enabled, re-enable them */
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001));
    }
}

 
 
 
