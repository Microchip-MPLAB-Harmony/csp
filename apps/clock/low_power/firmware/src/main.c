/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include <string.h>

static void enter_idle(void);
static void ramcode_init(void);
void enter_idle_sram(void);
void enter_ulp0(void);
void enter_ulp0_sram(void);
void really_enter_ulp0_sram(void);


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
void pit_callback(uintptr_t context)
{
    int *timer_count = (int *)context;
    (*timer_count)++;
    if (*timer_count == 5) {
        LED_BLUE_Toggle();
        *timer_count = 0;
    }
}

void print_menu(void)
{
    printf(" ------------------------------------------\n\r"
            " Select an option :\n\r"
            " 0 -> Enter Idle mode\n\r"
            " 1 -> Enter Ultra Low Power mode 0\n\r"
            " =>");

}

int main ( void )
{
    char c = 0;
    int timer_count = 0;
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    LED_BLUE_Set();
    PIT_TimerCallbackSet(pit_callback, (uintptr_t)&timer_count);
    ramcode_init();

    while ( true )
    {
        print_menu();
        c = getchar();
        switch (c) {
            case '0':
                printf("\n\r");
                enter_idle();
                break;
            case '1':
                printf("\n\r");
                enter_ulp0();
                break;
            default:
                printf("\n\r");
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
   

#pragma section = ".ramcode_section"
#pragma section = ".ramcode_section_init"                                                                                                                 
#pragma section = ".ramdata_section"
#pragma section = ".ramdata_section_init" 

static void ramcode_init(void)
{
    memcpy(__section_begin(".ramcode_section"),
        __section_begin(".ramcode_section_init"),
        __section_size(".ramcode_section_init"));
    memcpy(__section_begin(".ramdata_section"),
        __section_begin(".ramdata_section_init"),
        __section_size(".ramdata_section_init"));
    DCACHE_CLEAN_INVALIDATE_ALL();
    L1_ICACHE_INVALIDATE_ALL();
}

void enter_idle(void)
{
    struct tm time;
    /* configure RTC alarm */
    RTC_TimeGet(&time);
    if (time.tm_sec < 30) {
        time.tm_sec += 30;
    } else {
        time.tm_sec += 30;
        time.tm_sec = time.tm_sec % 60;
    }
    RTC_AlarmSet(&time, RTC_ALARM_MASK_SS);
    RTC_InterruptEnable(RTC_INT_ALARM);

    /* disbale PIT since we don't want it as a wake-up source */
    PIT_TimerStop();
    
    printf(" ------------------------------------------\n\r"
           "Entering Idle Mode for 30 seconds\n\r");

    enter_idle_sram();
    
    printf(" ------------------------------------------\n\r"
           "Leaving Idle Mode\n\r");

    /* enable PIT */
    PIT_TimerStart();
    /* disable RTC alarm */
    RTC_InterruptDisable(RTC_INT_ALARM);
}

#pragma location=".ramcode_section" 
void enter_idle_sram(void)
{
  
    PMC_REGS->PMC_SCDR = PMC_SCDR_PCK_Msk;
    
    asm("dsb" ::: "memory");
    asm("wfi" ::: "memory");
}

void enter_ulp0(void)
{
    struct tm time;
    /* configure RTC alarm */
    RTC_TimeGet(&time);
    time.tm_sec += 30;
    time.tm_sec %= 60;
    RTC_AlarmSet(&time, RTC_ALARM_MASK_SS);
    RTC_InterruptEnable(RTC_INT_ALARM);

    /* disbale PIT since we don't want it as a wake-up source */
    PIT_TimerStop();
    
    printf(" ------------------------------------------\n\r"
           "Entering ULP0 Mode for 30 seconds\n\r");

    enter_ulp0_sram();


    UART1_Initialize();
    
    printf(" ------------------------------------------\n\r"
           "Leaving ULP0 Mode\n\r");

    /* enable PIT */
    PIT_TimerStart();
    /* disable RTC alarm */
    RTC_InterruptDisable(RTC_INT_ALARM);

}

_Pragma("location=\".ramdata_section\"") int tmp_stack[256];
#pragma location=".ramcode_section" 
void enter_ulp0_sram(void)
{
    /* set up new stack in sram since ddr will be unavailable */
    uint32_t sp = (uint32_t)&tmp_stack[256];
    asm("mov r3, %0" : : "r"(sp));
    asm("mov r0, sp");
    asm("mov sp, r3");
    asm("push {r0}");

    /* broken up like this so we can use stack variables */
    really_enter_ulp0_sram();


    /* use original ddr based stack */
    asm("pop {r0}");
    asm("mov sp, r0");
}

#pragma location=".ramcode_section" 
void really_enter_ulp0_sram(void)
{
    struct clock_cfg {
        uint32_t scsr;
        uint32_t pcsr0;
        uint32_t pcsr1;
        uint32_t mckr;
        uint32_t mor;
    } clock_cfg;
    clock_cfg.scsr = PMC_REGS->PMC_SCSR;
    clock_cfg.pcsr0 = PMC_REGS->PMC_PCSR0;
    clock_cfg.pcsr1 = PMC_REGS->PMC_PCSR1;
    clock_cfg.mckr = PMC_REGS->PMC_MCKR;
    clock_cfg.mor = PMC_REGS->CKGR_MOR;

    /* set DDR in self-refresh mode */
    MPDDRC_REGS->MPDDRC_LPR = (MPDDRC_REGS->MPDDRC_LPR & ~MPDDRC_LPR_LPCB_Msk) | MPDDRC_LPR_LPCB_SELFREFRESH;
    while (!(MPDDRC_REGS->MPDDRC_LPR & MPDDRC_LPR_SELF_DONE_Msk));

    /* disable all unused peripheral clocks */
    PMC_REGS->PMC_PCDR0 = 0xFFFFFFFF;
    PMC_REGS->PMC_PCDR1 = 0xFFFFFFFF;
    PMC_REGS->PMC_SCDR = 0xFFFFFFFF;    

    /* switch to slow clock */
    PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_SLOW_CLK;
    while (!(PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk));
    
    /* disable main clock */
    PMC_REGS->CKGR_MOR &= ~(CKGR_MOR_MOSCXTEN_Msk | CKGR_MOR_MOSCRCEN_Msk) | CKGR_MOR_KEY_PASSWD | CKGR_MOR_ONE_Msk;

    /* enter ULP0 */
    asm("cpsid if");
    asm("dsb" ::: "memory");
    asm("wfi" ::: "memory");

    /* enable main clock */
    PMC_REGS->CKGR_MOR = clock_cfg.mor |  CKGR_MOR_KEY_PASSWD | CKGR_MOR_ONE_Msk;
    if (clock_cfg.mor & CKGR_MOR_MOSCSEL_Msk == 1)
        while (!(PMC_REGS->PMC_SR & PMC_SR_MOSCXTS_Msk));

    /* wait for pll lock */
    while (!(PMC_REGS->PMC_SR & PMC_SR_LOCKA_Msk));

    /* switch master clock to pll */
    PMC_REGS->PMC_MCKR = clock_cfg.mckr;
    while (!(PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk));

    PMC_REGS->PMC_SCER = clock_cfg.scsr;
    PMC_REGS->PMC_PCER0 = clock_cfg.pcsr0;
    PMC_REGS->PMC_PCER1 = clock_cfg.pcsr1;

    asm("cpsie if");
}
