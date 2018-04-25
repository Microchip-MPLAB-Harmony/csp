/*******************************************************************************
 CLOCK PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clock.c

  Summary:
    CLOCK PLIB Implementation File.

  Description:
    None

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

#include "plib_clock.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACRO DEFINATIONS
// *****************************************************************************
// *****************************************************************************

//****************************      GCLK      **********************************
/* GCLK Generator's Division Factor and Division Selection Values */

<#if GCLK_INST_NUM0 = true>
#define CONF_GCLK_GEN_0_DIV ${GCLK_0_DIV}
#define GCLK_GEN_0_DIV_SEL (${GCLK_0_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM1 = true>
#define CONF_GCLK_GEN_1_DIV ${GCLK_1_DIV}
#define GCLK_GEN_1_DIV_SEL (${GCLK_1_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM2 = true>
#define CONF_GCLK_GEN_2_DIV ${GCLK_2_DIV}
#define GCLK_GEN_2_DIV_SEL (${GCLK_2_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM3 = true>
#define CONF_GCLK_GEN_3_DIV ${GCLK_3_DIV}
#define GCLK_GEN_3_DIV_SEL (${GCLK_3_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM4 = true>
#define CONF_GCLK_GEN_4_DIV ${GCLK_4_DIV}
#define GCLK_GEN_4_DIV_SEL (${GCLK_4_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM5 = true>
#define CONF_GCLK_GEN_5_DIV ${GCLK_5_DIV}
#define GCLK_GEN_5_DIV_SEL (${GCLK_5_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM6 = true>
#define CONF_GCLK_GEN_6_DIV ${GCLK_6_DIV}
#define GCLK_GEN_6_DIV_SEL (${GCLK_6_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM7 = true>
#define CONF_GCLK_GEN_7_DIV ${GCLK_7_DIV}
#define GCLK_GEN_7_DIV_SEL (${GCLK_7_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>
<#if GCLK_INST_NUM8 = true>
#define CONF_GCLK_GEN_8_DIV ${GCLK_8_DIV}
#define GCLK_GEN_8_DIV_SEL (${GCLK_8_DIVSEL} << GCLK_GENCTRL_DIVSEL_Pos)
</#if>

#define MCLK_AHB_CLOCK_INITIAL_VALUE  (${MCLK_AHB_INITIAL_VALUE})

#define MCLK_APBA_CLOCK_INITIAL_VALUE  (${MCLK_APBA_INITIAL_VALUE})

#define MCLK_APBB_CLOCK_INITIAL_VALUE  (${MCLK_APBB_INITIAL_VALUE})

#define MCLK_APBC_CLOCK_INITIAL_VALUE  (${MCLK_APBC_INITIAL_VALUE})

#define MCLK_APBD_CLOCK_INITIAL_VALUE  (${MCLK_APBD_INITIAL_VALUE})
<#if XOSC_INTERRUPT_MODE = true || DPLL_INTERRUPT_MODE = true>

// *****************************************************************************
/*OSCCTRL Object

  Summary:
    Defines the data type for the data structures used for Oscillator controller
    operations.

  Description:
    This may be for used for OSCCTRL operations.

  Remarks:
    None.
*/
typedef struct
{

    /* OSCCTRL callback Handler */
    OSCCTRL_CALLBACK   callback;

    /* client context*/
    uintptr_t        context;

}OSCCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSCCTRL_OBJECT oscctrlObj;

</#if>
<#if XOSC32K_INTERRUPT_MODE = true >
// *****************************************************************************
/*OSC32KCTRL Object

  Summary:
    Defines the data type for the data structures used for 32KHz Oscillator
    Controller Operations.

  Description:
    This may be for used for OSC32KCTRL operations.

  Remarks:
    None.
*/
typedef struct
{

    /* OSC32KCTRL Callback Handler */
    OSC32KCTRL_CFD_CALLBACK   callback;

    /* client context*/
    uintptr_t        context;

}OSC32KCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSC32KCTRL_OBJECT osc32kctrlObj;

</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Function Prototypes
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void OSCCTRL_Initialize (void);

  Summary:
    Initializes all the modules related to the Oscillator Control.

  Description:
    This function initializes the Internal 48MHz Internal Oscillator , External
    Crystal Oscillator and Digital Phase Locked Loop modules

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        OSCCTRL_Initialize();
    </code>

  Remarks:
    This function should only be called once during system
    initialization.
*/

void OSCCTRL_Initialize(void);

// *****************************************************************************
/* Function:
    void OSC32KCTRL_Initialize (void);

  Summary:
    Initializes all the modules related to the 32KHz Oscillator Control.

  Description:
    This function initializes the 32KHz Internal Oscillator and 32KHz External
    Crystal Oscillator.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        OSC32KCTRL_Initialize();
    </code>

  Remarks:
    This function should only be called once during system
    initialization.
*/

void OSC32KCTRL_Initialize(void);

// *****************************************************************************
/* Function:
    void CLOCK_Initialize (void);

  Summary:
    Initializes all the modules related to the system clock.

  Description:
    This function initializes the clock as defined by the MHC and Clock Manager
    selections. The function will configure the NVM Flash Wait states based on
    the configured CPU operational frequency. It will then configure the
    oscillators.

    For each of the clock sources (External Oscillator, Digital Phase Locked
    Loop, Internal 48MHz Oscillator, External 32KHz oscillator and the Internal
    32KHz oscillator) enabled in MHC, the function will configure the clock
    settings and will then wait till the clock is ready. In case of DPLL, the
    function will wait till a lock is obtained.

    The function will then configure the Generic clock generators based on MHC
    configurations. If a Generic Clock is enabled in MHC, this will be enabled
    in the CLOCK_Initialize() function. The function will apply the CPU clock
    divider and will wait for the Main Clock module to get ready. If the Main
    Clock to the Peripheral APB and AHB interfaces was enabled in MHC, these
    will be enabled in the CLOCK_Initialize() function. If the Peripheral Clock
    Channels and mclk clocks were enabled in MHC, these will be enabled in the
    CLOCK_Initialize() function.

    The peripheral AHB and APB main clock and peripheral channel clocks will be
    enabled when the peripheral specific initialize functions are called. This
    will override the setting in MHC. The Generic Clock Generator source for
    desired peripheral channel must be configured in MHC.

   Remarks:
    Refer plib_clock.h file for more information.
*/
void CLOCK_Initialize (void)
{
    /* NVM Wait States */
    NVMCTRL_REGS->CTRLB |= NVMCTRL_CTRLB_RWS(NVMCTRL_CTRLB_RWS_SINGLE_Val);

    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();

    <#if CONFIG_CLOCK_OSCULP32K_CALIB_ENABLE = true >
    /* User Selection of the Calibration Value */
    OSC32KCTRL_REGS->OSCULP32K = OSC32KCTRL_OSCULP32K_CALIB(${OSCULP32K_CALIB_VALUE});
    </#if>

    /* selection of the CPU clock Division */
    MCLK_REGS->CPUDIV |= MCLK_CPUDIV_CPUDIV(${CONF_CPU_CLOCK_DIVIDER});

    while((MCLK_REGS->INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }

    /* Turn on the digital interface clock */
    MCLK_REGS->APBAMASK |= MCLK_APBAMASK_GCLK__Msk;

    /* Software reset the module to ensure it is re-initialized correctly */
    GCLK_REGS->CTRLA = GCLK_CTRLA_SWRST_Msk;

    while ((GCLK_REGS->CTRLA & GCLK_CTRLA_SWRST_Msk) == GCLK_CTRLA_SWRST_Msk)
    {
        /* Wait for reset to complete */
    }

<#if GCLK_INST_NUM0 = true>
    /* GCLK Generator 0 Initialization*/

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[0] |= GCLK_GEN_0_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_0_DIV)
                                                            ${GCLK_0_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_0_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_0_SRC});</@compress>

    <#if GCLK_0_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[0] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_0_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[0] |= GCLK_GENCTRL_OOV_Msk ;

    <#else >
    GCLK_REGS->GENCTRL[0] &= ~(GCLK_GENCTRL_OOV_Msk);

    </#if>
    </#if>
    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(0))
    {
        /* wait for the Generator 0 synchronization */
    }

    /* Enabling the GCLK Generator 0 */
    GCLK_REGS->GENCTRL[0] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM1 = true>
    /* GCLK Generator 1 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[1] |= GCLK_GEN_1_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_1_DIV)
                                                            ${GCLK_1_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_1_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_1_SRC});</@compress>

    <#if GCLK_1_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[1] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_1_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[1] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[1] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(1))
    {
        /* wait for the Generator 1 synchronization */
    }

    /* Enabling the GCLK Generator 1 */
    GCLK_REGS->GENCTRL[1] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM2 = true>
    /* GCLK Generator 2 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[2] |= GCLK_GEN_2_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_2_DIV)
                                                            ${GCLK_2_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_2_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_2_SRC});</@compress>

    <#if GCLK_2_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[2] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_2_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[2] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[2] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(2))
    {
        /* wait for the Generator 2 synchronization */
    }

    /* Enabling the GCLK Generator 2 */
    GCLK_REGS->GENCTRL[2] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM3 = true>
    /* GCLK Generator 3 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[3] |= GCLK_GEN_3_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_3_DIV)
                                                            ${GCLK_3_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_3_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_3_SRC});</@compress>
    <#if GCLK_3_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[3] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_3_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[3] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[3] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(3))
    {
        /* wait for the Generator 3 synchronization */
    }

    /* Enabling the GCLK Generator 3 */
    GCLK_REGS->GENCTRL[3] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM4 = true>
    /* GCLK Generator 4 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[4] |= GCLK_GEN_4_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_4_DIV)
                                                            ${GCLK_4_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_4_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_4_SRC});</@compress>

    <#if GCLK_4_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[4] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_4_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[4] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[4] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(4))
    {
        /* wait for the Generator 4 synchronization */
    }

    /* Enabling the GCLK Generator 4 */
    GCLK_REGS->GENCTRL[4] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM5 = true>
    /* GCLK Generator 5 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[5] |= GCLK_GEN_5_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_5_DIV)
                                                            ${GCLK_5_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_5_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_5_SRC});</@compress>

    <#if GCLK_5_OUTPUTENABLE = true>
     /* Output Enable */
    GCLK_REGS->GENCTRL[5] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_5_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[5] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[5] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(5))
    {
        /* wait for the Generator 5 synchronization */
    }

    /* Enabling the GCLK Generator 5 */
    GCLK_REGS->GENCTRL[5] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM6 = true>
    /* GCLK Generator 6 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[6] |= GCLK_GEN_6_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_6_DIV)
                                                            ${GCLK_6_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_6_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_6_SRC});</@compress>

    <#if GCLK_6_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[6] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_6_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[6] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[6] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(6))
    {
        /* wait for the Generator 6 synchronization  */
    }

    /* Enabling the GCLK Generator 6 */
    GCLK_REGS->GENCTRL[6] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM7 = true>
    /* GCLK Generator 7 Initialization */

    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[7] |= GCLK_GEN_7_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_7_DIV)
                                                            ${GCLK_7_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_7_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_7_SRC});</@compress>

    <#if GCLK_7_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[7] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_7_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[7] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[7] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(7))
    {
        /* wait for the Generator 7 synchronization  */
    }

    /* Enabling the GCLK Generator 7 */
    GCLK_REGS->GENCTRL[7] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_INST_NUM8 = true>
    /* GCLK Generator 8 Initialization */
    /*
     * Selection of the DivisonSelction , Division Factor , Run In StandBy ,
     * Source Selection and Duty Cycle
     */
    <@compress single_line=true>GCLK_REGS->GENCTRL[8] |= GCLK_GEN_8_DIV_SEL | GCLK_GENCTRL_DIV(CONF_GCLK_GEN_8_DIV)
                                                            ${GCLK_8_IMPROVE_DUTYCYCLE?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                            ${GCLK_8_RUNSTDBY?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                            | GCLK_GENCTRL_SRC(${GCLK_8_SRC});</@compress>

    <#if GCLK_8_OUTPUTENABLE = true>
    /* Output Enable */
    GCLK_REGS->GENCTRL[8] |=  GCLK_GENCTRL_OE_Msk ;

    /* Selection of Output OFF Value */
    <#if GCLK_8_OUTPUTOFFVALUE = "HIGH">
    GCLK_REGS->GENCTRL[8] |= GCLK_GENCTRL_OOV_Msk ;
    <#else >
    GCLK_REGS->GENCTRL[8] &= ~(GCLK_GENCTRL_OOV_Msk);
    </#if>
    </#if>

    while(GCLK_REGS->SYNCBUSY & GCLK_SYNCBUSY_GENCTRL(8))
    {
        /* wait for the Generator 8 synchronization  */
    }

    /* Enabling the GCLK Generator 8 */
    GCLK_REGS->GENCTRL[8] |= GCLK_GENCTRL_GENEN_Msk;

</#if>
<#if GCLK_ID_AC_CHEN = true >
    /*Analog Comparator(AC) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_AC_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_AC_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_AC_GENSEL})${GCLK_ID_AC_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_ADC0_CHEN = true >
    /*Analog To Digital Converter(ADC) 0 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_ADC0_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_ADC0_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_ADC0_GENSEL})${GCLK_ID_ADC0_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_ADC1_CHEN = true >
    /*Analog To Digital Converter(ADC) 1 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_ADC1_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_ADC1_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_ADC1_GENSEL})${GCLK_ID_ADC1_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_CAN0_CHEN = true >
    /* Control Area Network(CAN) 0 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CAN0_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CAN0_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_CAN0_GENSEL})${GCLK_ID_CAN0_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_CAN1_CHEN = true >
    /* Control Area Network(CAN) 1 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CAN1_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CAN1_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_CAN1_GENSEL})${GCLK_ID_CAN1_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_CCL_CHEN = true >
    /* Configurable Custom Logic(CCL) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CCL_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_CCL_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_CCL_GENSEL})${GCLK_ID_CCL_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_DAC_CHEN = true >
    /* Digital to Analog Converter(DAC) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_DAC_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_DAC_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_DAC_GENSEL})${GCLK_ID_DAC_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EIC_CHEN = true >
    /* External Interrupt Controller(EIC) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EIC_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EIC_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EIC_GENSEL})${GCLK_ID_EIC_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL0_CHEN = true >
    /* Event System(EVSYS) Channel 0 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL0_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL0_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL0_GENSEL})${GCLK_ID_EVSYS_CHANNEL0_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL1_CHEN = true >
    /* Event System(EVSYS) Channel 1 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL1_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL1_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL1_GENSEL})${GCLK_ID_EVSYS_CHANNEL1_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL2_CHEN = true >
    /* Event System(EVSYS) Channel 2 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL2_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL2_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL2_GENSEL})${GCLK_ID_EVSYS_CHANNEL2_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL3_CHEN = true >
    /* Event System(EVSYS) Channel 3 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL3_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL3_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL3_GENSEL})${GCLK_ID_EVSYS_CHANNEL3_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL4_CHEN = true >
    /* Event System(EVSYS) Channel 4 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL4_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL4_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL4_GENSEL})${GCLK_ID_EVSYS_CHANNEL4_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if><#if GCLK_ID_EVSYS_CHANNEL5_CHEN = true >
    /* Event System(EVSYS) Channel 5 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL5_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL5_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL5_GENSEL})${GCLK_ID_EVSYS_CHANNEL5_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL6_CHEN = true >
    /* Event System(EVSYS) Channel 6 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL6_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL6_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL6_GENSEL})${GCLK_ID_EVSYS_CHANNEL6_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL7_CHEN = true >
    /* Event System(EVSYS) Channel 7 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL7_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL7_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL7_GENSEL})${GCLK_ID_EVSYS_CHANNEL7_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if><#if GCLK_ID_EVSYS_CHANNEL8_CHEN = true >
    /* Event System(EVSYS) Channel 8 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL8_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL8_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL8_GENSEL})${GCLK_ID_EVSYS_CHANNEL8_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL9_CHEN = true >
    /* Event System(EVSYS) Channel 9 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL9_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL9_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL9_GENSEL})${GCLK_ID_EVSYS_CHANNEL9_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL10_CHEN = true >
    /* Event System(EVSYS) Channel 10 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL10_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL10_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL10_GENSEL})${GCLK_ID_EVSYS_CHANNEL10_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_EVSYS_CHANNEL11_CHEN = true >
    /* Event System(EVSYS) Channel 11 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL11_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_EVSYS_CHANNEL11_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_EVSYS_CHANNEL11_GENSEL})${GCLK_ID_EVSYS_CHANNEL11_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_FREQM_MSR_CHEN = true >
        /* Frequency Meter(FREQM) Measure peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_FREQM_MSR_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_FREQM_MSR_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_FREQM_MSR_GENSEL})${GCLK_ID_FREQM_MSR_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if><#if GCLK_ID_FREQM_REF_CHEN = true >
    /* Frequency Meter(FREQM) Reference peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_FREQM_REF_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_FREQM_REF_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_FREQM_REF_GENSEL})${GCLK_ID_FREQM_REF_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if><#if GCLK_ID_NVMCTRL_CHEN = true >
    /* Non-Volatile Memory Controller(NVMCTRL) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_NVMCTRL_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_NVMCTRL_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_NVMCTRL_GENSEL})${GCLK_ID_NVMCTRL_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_OSCCTRL_FDPLL_CHEN = true >
    /* Frequency Division Phase Locked Loop(FDPLL) Oscillator peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_OSCCTRL_FDPLL_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_OSCCTRL_FDPLL_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_OSCCTRL_FDPLL_GENSEL})${GCLK_ID_OSCCTRL_FDPLL_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_OSCCTRL_FDPLL32K_CHEN = true >
    /* 32KHz Frequency Division Phase Locked Loop(FDPLL32K) Oscillator peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_OSCCTRL_FDPLL32K_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_OSCCTRL_FDPLL32K_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_OSCCTRL_FDPLL32K_GENSEL})${GCLK_ID_OSCCTRL_FDPLL32K_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_PTC_CHEN = true >
    /* Peripheral Touch Controller(PTC) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_PTC_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_PTC_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_PTC_GENSEL})${GCLK_ID_PTC_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SDADC_CHEN = true >
    /* Sigma-Delta Analog To Digital Converter(SDADC) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SDADC_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SDADC_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SDADC_GENSEL})${GCLK_ID_SDADC_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM0_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 0 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM0_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM0_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM0_CORE_GENSEL})${GCLK_ID_SERCOM0_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM1_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 1 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM1_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM1_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM1_CORE_GENSEL})${GCLK_ID_SERCOM1_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM2_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 2 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM2_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM2_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM2_CORE_GENSEL})${GCLK_ID_SERCOM2_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM3_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 3 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM3_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM3_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM3_CORE_GENSEL})${GCLK_ID_SERCOM3_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM4_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 4 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM4_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM4_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM4_CORE_GENSEL})${GCLK_ID_SERCOM4_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM5_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 5 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM5_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM5_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM5_CORE_GENSEL})${GCLK_ID_SERCOM5_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM6_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 6 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM6_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM6_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM6_CORE_GENSEL})${GCLK_ID_SERCOM6_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM7_CORE_CHEN = true >
    /* Serial Communication(SERCOM) 7 Core peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM7_CORE_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM7_CORE_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM7_CORE_GENSEL})${GCLK_ID_SERCOM7_CORE_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM0_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 0 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM0_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM0_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM0_SLOW_GENSEL})${GCLK_ID_SERCOM0_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM1_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 1 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM1_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM1_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM1_SLOW_GENSEL})${GCLK_ID_SERCOM1_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if><#if GCLK_ID_SERCOM2_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 2 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM2_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM2_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM2_SLOW_GENSEL})${GCLK_ID_SERCOM2_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM3_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 3 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM3_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM3_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM3_SLOW_GENSEL})${GCLK_ID_SERCOM3_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM4_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 4 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM4_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM4_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM4_SLOW_GENSEL})${GCLK_ID_SERCOM4_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM5_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 5 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM5_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM5_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM5_SLOW_GENSEL})${GCLK_ID_SERCOM5_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM6_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 6 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM6_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM6_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM6_SLOW_GENSEL})${GCLK_ID_SERCOM6_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_SERCOM7_SLOW_CHEN = true >
    /* Serial Communication(SERCOM) 7 Slow peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM7_SLOW_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_SERCOM7_SLOW_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_SERCOM7_SLOW_GENSEL})${GCLK_ID_SERCOM7_SLOW_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC0_CHEN = true >
    /* Timer Counter(TC) 0 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC0_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC0_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC0_GENSEL})${GCLK_ID_TC0_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC1_CHEN = true >
    /* Timer Counter(TC) 1 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC1_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC1_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC1_GENSEL})${GCLK_ID_TC1_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC2_CHEN = true >
    /* Timer Counter(TC) 2 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC2_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC2_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC2_GENSEL})${GCLK_ID_TC2_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC3_CHEN = true >
    /* Timer Counter(TC) 3 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC3_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC3_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC3_GENSEL})${GCLK_ID_TC3_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC4_CHEN = true >
    /* Timer Counter(TC) 4 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC4_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC4_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC4_GENSEL})${GCLK_ID_TC4_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC5_CHEN = true >
    /* Timer Counter(TC) 5 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC5_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC5_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC5_GENSEL})${GCLK_ID_TC5_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC6_CHEN = true >
    /* Timer Counter(TC) 6 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC6_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC6_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC6_GENSEL})${GCLK_ID_TC6_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TC7_CHEN = true >
    /* Timer Counter(TC) 7 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC7_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TC7_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TC7_GENSEL})${GCLK_ID_TC7_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TCC0_CHEN = true >
    /* Timer Counter For Control(TCC) 0 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC0_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC0_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TCC0_GENSEL})${GCLK_ID_TCC0_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TCC1_CHEN = true >
    /* Timer Counter For Control(TCC) 1 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC1_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC1_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TCC1_GENSEL})${GCLK_ID_TCC1_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TCC2_CHEN = true >
    /* Timer Counter For Control(TCC) 2 peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC2_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TCC2_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TCC2_GENSEL})${GCLK_ID_TCC2_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
<#if GCLK_ID_TSENS_CHEN = true >
    /*Temperature Sensor(TSENS) peripheral Channel Enable */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TSENS_INDEX}] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Selection of the Generator and write Lock */
    GCLK_REGS->PCHCTRL[${GCLK_ID_TSENS_INDEX}] |= GCLK_PCHCTRL_GEN(${GCLK_ID_TSENS_GENSEL})${GCLK_ID_TSENS_WRITELOCK?then('| GCLK_PCHCTRL_WRTLOCK_Msk', ' ')};

</#if>
    /* Configure the AHB Bridge Clocks */
    MCLK_REGS->AHBMASK = MCLK_AHB_CLOCK_INITIAL_VALUE;

    /* Configure the APBA Bridge Clocks */
    MCLK_REGS->APBAMASK = MCLK_APBA_CLOCK_INITIAL_VALUE;

    /* Configure the APBB Bridge Clocks */
    MCLK_REGS->APBBMASK = MCLK_APBB_CLOCK_INITIAL_VALUE;

    /* Configure the APBC Bridge Clocks */
    MCLK_REGS->APBCMASK = MCLK_APBC_CLOCK_INITIAL_VALUE;

    /* Configure the APBD Bridge Clocks */
    MCLK_REGS->APBDMASK = MCLK_APBD_CLOCK_INITIAL_VALUE;

}

// *****************************************************************************
// *****************************************************************************
// Section: OSCCTRL IMPLEMENTATION
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void OSCCTRL_Initialize (void);

  Summary:
    Initializes all the modules related to the Oscillator Control.

  Description:
    This function initializes the Internal 48MHz Internal Oscillator , External
    Crystal Oscillator and Digital Phase Locked Loop modules

   Remarks:
    This is a local function and should not be called directly from the
    application.
*/

void OSCCTRL_Initialize(void)
{
<#if CONFIG_CLOCK_XOSC_ENABLE = true>
    /****************** XOSC Initialization   ********************************/
    uint32_t xoscFrequency = 0;

    /* Selection of the XOSC Frequency Value */
    xoscFrequency = ${CONFIG_CLOCK_XOSC_FREQUENCY};

    /* Selection of the startup time ,StandBy */
    <@compress single_line=true>OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_STARTUP(${CONFIG_CLOCK_XOSC_STARTUP})
                                                             ${CONFIG_CLOCK_XOSC_RUNSTDBY?then('| OSCCTRL_XOSCCTRL_RUNSTDBY_Msk',' ')};</@compress>

    <#if CONFIG_CLOCK_XOSC_CFDEN = true >
    /* Enabling the Clock failure detection (CFD) */
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_CFDEN_Msk;

    /* Selection of the Clock failure detection (CFD) pre scalar */
    OSCCTRL_REGS->CFDPRESC |= ${CONFIG_CLOCK_XOSC_CFDPRESC};

    </#if>
    <#if XOSC_OSCILLATOR_MODE = "CRYSTAL">
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_XTALEN_Msk;

    <#else>
    OSCCTRL_REGS->XOSCCTRL &= ~(OSCCTRL_XOSCCTRL_XTALEN_Msk);

    </#if>
    /* Gain Value*/
     OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_GAIN(${CONFIG_CLOCK_XOSC_GAIN});

    /* Enabling the External Oscillator(XOSC) */
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_ENABLE_Msk;

    while(!((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) == OSCCTRL_STATUS_XOSCRDY_Msk))
    {
        /* Waiting for the XOSC Ready state */
    }

    /* Selection of the ONDEMAND Control */
    <#if CONFIG_CLOCK_XOSC_ONDEMAND = "Only on Peripheral Request">
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_ONDEMAND_Msk;

    <#else>
    OSCCTRL_REGS->XOSCCTRL &= ~OSCCTRL_XOSCCTRL_ONDEMAND_Msk;

    </#if>
    <#if XOSC_AMPGC = true >
    /* Setting the Automatic Gain Control */
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_AMPGC_Msk;

    </#if>
</#if>
<#if CONFIG_CLOCK_OSC48M_ENABLE = true>
    /****************** OSC48M Initialization  *******************************/

    /* Selection of the ONDEMAND , RUN StandBy ,Startup Time */
    <@compress single_line=true>OSCCTRL_REGS->OSC48MCTRL |= OSCCTRL_OSC48MSTUP_STARTUP(${CONFIG_CLOCK_OSC48M_STARTUP})
                                                               ${CONFIG_CLOCK_OSC48M_RUNSTDY?then('| OSCCTRL_OSC48MCTRL_RUNSTDBY_Msk' ,' ')};</@compress>

    /* Selection of the Division Value */
    OSCCTRL_REGS->OSC48MDIV = OSCCTRL_OSC48MDIV_DIV(${CONFIG_CLOCK_OSC48M_DIV});

    while((OSCCTRL_REGS->OSC48MSYNCBUSY & OSCCTRL_OSC48MSYNCBUSY_OSC48MDIV_Msk) == OSCCTRL_OSC48MSYNCBUSY_OSC48MDIV_Msk)
    {
        /* Waiting for the synchronization */
    }

    /* Enabling the OSC48M */
    OSCCTRL_REGS->OSC48MCTRL |= OSCCTRL_OSC48MCTRL_ENABLE_Msk;

    while(!((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_OSC48MRDY_Msk) == OSCCTRL_STATUS_OSC48MRDY_Msk))
    {
        /* Waiting for the OSC48M Ready state */
    }

    /* Selection of the ONDEMAND Control */
    <#if CONFIG_CLOCK_OSC48M_ONDEMAND = "Only on Peripheral Request">
    OSCCTRL_REGS->OSC48MCTRL |= OSCCTRL_OSC48MCTRL_ONDEMAND_Msk;
    </#if>
</#if>

<#if CONFIG_CLOCK_DPLL_ENABLE = true >
    /****************** DPLL Initialization  *********************************/

    /*
     * Selection of Lock Bypass , Lock Time ,WakeUp Fast , Filter ,Run Standby
     * and Low Power Enable
     */
    <@compress single_line=true>OSCCTRL_REGS->DPLLCTRLB |= OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL_FILTER}) |
                                                              OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL_LOCK_TIME})|
                                                              ${CONFIG_CLOCK_DPLL_RUNSTDY?then('OSCCTRL_DPLLCTRLA_RUNSTDBY_Msk','')}
                                                              OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL_REF_CLOCK})
                                                              ${CONFIG_CLOCK_DPLL_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                              ${CONFIG_CLOCK_DPLL_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                              ${CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE?then('| OSCCTRL_DPLLCTRLB_LPEN_Msk', ' ')};</@compress>

    <#if CONFIG_CLOCK_DPLL_REF_CLOCK = "DPLL_REFERENCE_CLOCK_XOSC">
    /* Selection of the Clock Divider */
    OSCCTRL_REGS->DPLLCTRLB |= OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL_DIVIDER});
    </#if>

    /* Selection of the Integer and Fractional part of the LDR ratio */
    <@compress single_line=true>OSCCTRL_REGS->DPLLRATIO |= OSCCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL_LDR_INTEGER}) |
                                                              OSCCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION});</@compress>

    while((OSCCTRL_REGS->DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk)
    {
        /* Waiting for the synchronization */
    }

    /* Selection of the DPLL Pre-Scalar */
   OSCCTRL_REGS->DPLLPRESC |= OSCCTRL_DPLLPRESC_PRESC(${CONFIG_CLOCK_DPLL_PRESCALAR});

    while((OSCCTRL_REGS->DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLPRESC_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLPRESC_Msk )
    {
        /* Waiting for the synchronization */
    }

    /* Selection of the DPLL Enable */
    OSCCTRL_REGS->DPLLCTRLA |= OSCCTRL_DPLLCTRLA_ENABLE_Msk;

    while((OSCCTRL_REGS->DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk) == OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    while(!((OSCCTRL_REGS->DPLLSTATUS & (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)) ==
                (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)))
    {
        /* Waiting for the Ready state */
    }

    /* Selection of the ONDEMAND Control */
    <#if CONFIG_CLOCK_DPLL_ONDEMAND = "Only on Peripheral Request">
    OSCCTRL_REGS->DPLLCTRLA |= OSCCTRL_DPLLCTRLA_ONDEMAND_Msk;

    <#else>
    OSCCTRL_REGS->DPLLCTRLA &= ~OSCCTRL_DPLLCTRLA_ONDEMAND_Msk;

    </#if>
</#if>
}
<#if CONFIG_CLOCK_XOSC_ENABLE = true>

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSCEnable (bool enable);

  Summary:
    Enables and disables the External Oscillator.

  Description:
    This function enables or disables the external oscillator. The application
    may need to disable the oscillator to reduce power consumption.

    After enabling the external oscillator, the OSCCTRL_XOSCIsReady() function
    must be called to check if the oscillator is ready.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_XOSCEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the XOSC */
        OSCCTRL_REGS->XOSCCTRL |= 1 << OSCCTRL_XOSCCTRL_ENABLE_Pos;
    }
    else
    {
        /* Disabling the XOSC */
        OSCCTRL_REGS->XOSCCTRL &= ~(1 << OSCCTRL_XOSCCTRL_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCIsReady ( void );

  Summary:
    Indicates readiness of the external oscillator.

  Description:
    This function returns true if the external oscillator is ready to be used.
    Once enabled, the oscillator will need a certain amount of time to stabilize
    on the correct frequency.  The oscillator output during this stabilization
    is masked. The function returns true once the external clock or crystal
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCIsReady( void )
{
    bool xoscReadyStatus = false;

    /* Checking for the XOSC Ready state */
    if((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) == OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        xoscReadyStatus = true;
    }

    return xoscReadyStatus;
}
<#if CONFIG_CLOCK_XOSC_CFDEN = true >

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCFailureIsActive( void );

  Summary:
    Indicates the XOSC failure status.

  Description:
    This function returns true if a failure is currently being detected on the
    external oscillator.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCFailureIsActive( void )
{
    bool failureActiveStatus = false;

    /* Checking for the XOSC Failure Detection */
    if((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        failureActiveStatus = true;
    }

    return failureActiveStatus;
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCSafeClockIsActive( void );

  Summary:
    Indicates the XOSC Clock is replaced by the safe clock

  Description:
    This function returns true if the Clock Failure detection system has
    detected a failure and the system has now switched to the safe clock.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCSafeClockIsActive( void )
{
    bool safeClockActiveStatus = false;

    /* Checking for the XOSC Switching to provide a safe Clock */
    if((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCCKSW_Msk) == OSCCTRL_STATUS_XOSCCKSW_Msk)
    {
        safeClockActiveStatus = true;
    }

    return safeClockActiveStatus;
}

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSCMainClockRevert( void );

  Summary:
    Switches the system back to the external oscillator.

  Description:
    This function will switch the system clock from the safe clock to the
    external oscillator. This function should be called when the application is
    able to verify that the external oscillator is functional.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_XOSCMainClockRevert( void )
{
    /* Selection of the Switch Back option */
    OSCCTRL_REGS->XOSCCTRL |= OSCCTRL_XOSCCTRL_SWBEN_Msk ;
}

</#if>

</#if>
<#if CONFIG_CLOCK_OSC48M_ENABLE = true>
// *****************************************************************************
/* Function:
    void OSCCTRL_OSC48MEnable( bool enable );

  Summary:
    Enables and disables the Internal 48MHz Oscillator.

  Description:
    This function enables or disables the Internal 48MHz oscillator.This function
    could be called to disable the oscillator to save power.

    After enabling the oscillator, the OSCCTRL_OSC48MIsReady() function must
    called to call to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/
void OSCCTRL_OSC48MEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the OSC48M */
        OSCCTRL_REGS->OSC48MCTRL |= 1 << OSCCTRL_OSC48MCTRL_ENABLE_Pos;
    }
    else
    {
        /* Disabling the OSC48M */
        OSCCTRL_REGS->OSC48MCTRL &= ~(1 << OSCCTRL_OSC48MCTRL_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_OSC48MIsReady( void );

  Summary:
    Indicates readiness of the internal 48MHz oscillator.

  Description:
    This function returns true if the internal 48MHz oscillator is ready to be
    used.  Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the internal 48MHz
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_OSC48MIsReady( void )
{
    bool osc48mReadyStatus = false;

    /* Checking for the OSC48M Ready state */
    if((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_OSC48MRDY_Msk) == OSCCTRL_STATUS_OSC48MRDY_Msk)
    {
        osc48mReadyStatus = true;
    }

    return osc48mReadyStatus;
}

</#if>
<#if CONFIG_CLOCK_DPLL_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSCCTRL_DPLLEnable( bool enable );

  Summary:
    Enables or disables the Digital Phase Locked Loop (DPLL).

  Description:
    This function enables or disables the DPLL. This function could be called to
    disable the DPLL while entering the available sleep modes and re-enabling it
    exiting from the sleep mode.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_DPLLEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the DPLL  */
        OSCCTRL_REGS->DPLLCTRLA |= 1 << OSCCTRL_DPLLCTRLA_ENABLE_Pos;
    }
    else
    {
        /* Disabling the DPLL  */
        OSCCTRL_REGS->DPLLCTRLA &= ~(1 << OSCCTRL_DPLLCTRLA_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_DPLLIsLocked( void );

  Summary:
    Returns the lock status of the DPLL.

  Description:
    This function returns the lock status of the DPLL. When locked, the DPLL
    output is stable.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_DPLLIsLocked( void )
{
    bool dpllLockedStatus = false;

    /* Checking for the DPLL Lock Status */
    if((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_DPLLLCKR_Msk) == OSCCTRL_STATUS_DPLLLCKR_Msk)
    {
        dpllLockedStatus = true;
    }

    return dpllLockedStatus;
}

</#if>
<#if XOSC_INTERRUPT_MODE = true || DPLL_INTERRUPT_MODE = true >

// *****************************************************************************
/* Function:
    void OSCCTRL_CallbackRegister (OSCCTRL_CALLBACK callback, uintptr_t context);

  Summary:
    Register the function to be called when an External Oscillator or DPLL event
    is generated.

  Description:
    This function registers the callback function to be called when the External
    Oscillator has failed or when the DPLL has lost lock or when the DPLL has
    achieved lock. The event type is passed into the callback function when the
    function is called.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_CallbackRegister(OSCCTRL_CALLBACK callback, uintptr_t context)
{
    oscctrlObj.callback = callback;

    oscctrlObj.context = context;

<#if XOSC_INTERRUPT_MODE = true >
    /* Enabling the Clock Fail Interrupt  */
    OSCCTRL_REGS->INTENSET = OSCCTRL_INTENSET_XOSCFAIL_Msk;

    </#if>
    <#if DPLL_INTERRUPT_MODE = true >
    /* Enabling the DPLL Lock Fall and Rise Edge Interrupts */
    OSCCTRL_REGS->INTENSET = OSCCTRL_INTENSET_DPLLLCKF_Msk | OSCCTRL_INTENSET_DPLLLCKR_Msk ;

</#if>
}

// *****************************************************************************
/* Function:
    void OSCCTRL_Handler(void);

  Summary:
    Handler that handles the XOSC and DPLL Interrupts.

  Description:
    This Function is called from the handler to handle the XOSC Failure and DPLL
    lock based on the Interrupts.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_Handler(void)
{
    <#if XOSC_INTERRUPT_MODE = true >
    /* Checking for the Clock Fail status */
    if ((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_CLOCK_FAIL, oscctrlObj.context);
        }

        /* Clearing the XOSC Fail Interrupt Flag */
        OSCCTRL_REGS->INTFLAG = OSCCTRL_INTFLAG_XOSCFAIL_Msk;
    }

    </#if>
    <#if DPLL_INTERRUPT_MODE = true >
    /* Checking for the DPLL Lock Fail status */
    if ((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_DPLLLCKF_Msk) == OSCCTRL_STATUS_DPLLLCKF_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_DPLL_LOCK_FAIL, oscctrlObj.context);
        }

        /* Clearing the DPLL Lock Fail Interrupt Flag */
        OSCCTRL_REGS->INTFLAG = OSCCTRL_INTFLAG_DPLLLCKF_Msk;
    }

    /* Checking for the DPLL Locked status */
    if ((OSCCTRL_REGS->STATUS & OSCCTRL_STATUS_DPLLLCKR_Msk) == OSCCTRL_STATUS_DPLLLCKR_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_PLL_LOCKED, oscctrlObj.context);
        }

        /* Clearing the DPLL Locked Interrupt Flag */
        OSCCTRL_REGS->INTFLAG = OSCCTRL_INTFLAG_DPLLLCKR_Msk;
    }
    </#if>
}

</#if>

// *****************************************************************************
// *****************************************************************************
// Section: OSC32KCTRL IMPLEMENTATION
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void OSC32KCTRL_Initialize (void);

  Summary:
    Initializes all the modules related to the 32KHz Oscillator Control.

  Description:
    This function initializes the 32KHz Internal Oscillator and 32KHz External
    Crystal Oscillator.

   Remarks:
    This function should only be called once during system
    initialization.
*/

void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE = true>
    /****************** XOSC32K initialization  ******************************/

    /* Selection of the Startup time , standby mode , 1K output ,32k output */
    <@compress single_line=true>OSC32KCTRL_REGS->XOSC32K |= OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP})
                                                               ${XOSC32K_RUNSTDBY?then('| OSC32KCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN1K?then('| OSC32KCTRL_XOSC32K_EN1K_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| OSC32KCTRL_XOSC32K_EN32K_Msk',' ')};</@compress>

    <#if XOSC32K_CFDEN = true >
    /* Selection of the CFD enable and Pre scalar */
    OSC32KCTRL_REGS->CFDCTRL |= OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')};

    </#if>
    <#if XOSC32K_OSCILLATOR_MODE = "CRYSTAL" >
    /* Enable or Disable the XOSC32K Oscillator */
    OSC32KCTRL_REGS->XOSC32K |= OSC32KCTRL_XOSC32K_XTALEN_Msk;
    <#else>
    OSC32KCTRL_REGS->XOSC32K &= ~OSC32KCTRL_XOSC32K_XTALEN_Msk;
    </#if>

    /* Enabling the XOSC32K Oscillator */
    OSC32KCTRL_REGS->XOSC32K |= OSC32KCTRL_XOSC32K_ENABLE_Msk ;

    while(!((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }

    /* Selection of the ONDEMAND Control */
    <#if XOSC32K_ONDEMAND = "Only on Peripheral Request">
    OSC32KCTRL_REGS->XOSC32K |= OSC32KCTRL_XOSC32K_ONDEMAND_Msk;

    <#else>
    OSC32KCTRL_REGS->XOSC32K &= ~OSC32KCTRL_XOSC32K_ONDEMAND_Msk;

    </#if>
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE =true>
    /****************** OSC32K Initialization  ******************************/

    /*
     * Selection of the Startup time , 1K output , 32K output standby
     * and on demand
     */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32K |= OSC32KCTRL_OSC32K_STARTUP(${OSC32K_STARTUP})
                                                              ${OSC32K_RUNSTDBY?then('| OSC32KCTRL_OSC32K_RUNSTDBY_Msk',' ')}
                                                              ${OSC32K_EN1K?then('| OSC32KCTRL_OSC32K_EN1K_Msk',' ')}
                                                              ${OSC32K_EN32K?then('| OSC32KCTRL_OSC32K_EN32K_Msk',' ')};</@compress>

    /* Enabling the OSC32K*/
    OSC32KCTRL_REGS->OSC32K |= OSC32KCTRL_OSC32K_ENABLE_Msk;

    while(!((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_OSC32KRDY_Msk) == OSC32KCTRL_STATUS_OSC32KRDY_Msk))
    {
        /* Waiting for the OSC32K Ready state */
    }

    /* Selection of the ONDEMAND Control */
    <#if OSC32K_ONDEMAND = "Only on Peripheral Request">
    OSC32KCTRL_REGS->OSC32K |= OSC32KCTRL_OSC32K_ONDEMAND_Msk;

    <#else>
    OSC32KCTRL_REGS->OSC32K &= ~OSC32KCTRL_OSC32K_ONDEMAND_Msk;

    </#if>
</#if>
}
<#if CONF_CLOCK_XOSC32K_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_XOSC32KEnable( bool enable );

  Summary:
    Enables and disables the External 32KHz Oscillator.

  Description:
    This function enables or disables the external 32KHz oscillator. This
    function could be called to disable the oscillator to save power.

    After enabling the oscillator, the OSC32KCTRL_XOSC32KIsReady() function must
    be called to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_XOSC32KEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the XOSC32K */
        OSC32KCTRL_REGS->XOSC32K |= 1 << OSC32KCTRL_XOSC32K_ENABLE_Pos;
    }
    else
    {
        /* Disabling the XOSC32K */
        OSC32KCTRL_REGS->XOSC32K &= ~(1 << OSC32KCTRL_XOSC32K_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSC32KCTRL_XOSC32KIsReady( void );

  Summary:
    Indicates readiness of the external 32KHz oscillator.

  Description:
    This function returns true if the external 32KHz oscillator is ready to be
    used.  Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the external clock
    or crystal oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KIsReady( void )
{
    bool xosc32kReadyStatus = false;

    /* Checking for the XOSC32K Ready state */
    if((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk)
    {
        xosc32kReadyStatus = true;
    }

    return xosc32kReadyStatus;
}
<#if XOSC32K_CFDEN = true >

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSC32KFailureIsActive( void );

  Summary:
    Indicates the XOSC32K failure status.

  Description:
    This function returns true if a failure is currently being detected on the
    external 32K oscillator.
   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KFailureIsActive( void )
{
    bool failureActiveStatus = false;

    /* Checking for the XOSC32K Clock Failure Detection */
    if((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_CLKFAIL_Msk) == OSC32KCTRL_STATUS_CLKFAIL_Msk)
    {
        failureActiveStatus = true;
    }

    return failureActiveStatus;
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSC32KSafeClockIsActive( void );

  Summary:
    Indicates the XOSC32K Clock is replaced by the safe clock

  Description:
    This function returns true if the Clock Failure detection system has
    detected a failure and the system has now switched to the safe clock.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KSafeClockIsActive( void )
{
    bool safeClockActiveStatus = false;

    if((OSC32KCTRL_REGS->STATUS & OSCCTRL_STATUS_XOSCCKSW_Msk) == OSCCTRL_STATUS_XOSCCKSW_Msk)
    {
        /* Checking for the XOSC32K Switch and provides a safe Clock */
        safeClockActiveStatus = true;
    }

    return safeClockActiveStatus;
}

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSC32KMainClockRevert( void );

  Summary:
    Switches the system back to the external oscillator.

  Description:
    This function will switch the system clock from the safe clock to the
    external oscillator. This function should be called when the application is
    able to verify that the external oscillator is functional.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_XOSC32KMainClockRevert( void )
{
    /* Selection of the Switch Back option */
    OSC32KCTRL_REGS->CFDCTRL |= OSC32KCTRL_CFDCTRL_SWBACK_Msk ;
}

</#if>
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_OSC32KEnable( bool enable );

  Summary:
    Enables and disables the Internal 32KHz Oscillator.

  Description:
    This function enables or disables the Internal 32KHz oscillator. This function
    could be called to disable the oscillator to reduce power.

    After enabling the oscillator, the OSC32KCTRL_OSC32KIsReady() function must
    called to call to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_OSC32KEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the OSC32K*/
        OSC32KCTRL_REGS->OSC32K |= 1 << OSC32KCTRL_OSC32K_ENABLE_Msk;
    }
    else
    {
        /* Disabling the OSC32K */
        OSC32KCTRL_REGS->OSC32K &= ~(1 << OSC32KCTRL_OSC32K_ENABLE_Msk);
    }
}

// *****************************************************************************
/* Function:
    bool OSC32KCTRL_OSC32KIsReady( void );

  Summary:
    Indicates readiness of the internal 32KHz oscillator.

  Description:
    This function returns true if the internal 32KHz oscillator is ready to be
    used. Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the internal 32KHz
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_OSC32KIsReady( void )
{
    bool osc32kReadyStatus = false;

    /* Waiting for the XOSC32K Ready state */
    if((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_OSC32KRDY_Msk) == OSC32KCTRL_STATUS_OSC32KRDY_Msk)
    {

        osc32kReadyStatus = true;
    }

    return osc32kReadyStatus;
}

</#if>
<#if XOSC32K_INTERRUPT_MODE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback,
                                                    uintptr_t context);

  Summary:
    Register the function to be called when the 32KHz External Oscillator has
    failed.

  Description:
    This function register the function to be called when the 32KHz External
    Oscillator has failed.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    osc32kctrlObj.callback = callback;

    osc32kctrlObj.context = context;

   /* Enabling the Clock Failure Interrupt */
    OSC32KCTRL_REGS->INTENSET = OSC32KCTRL_INTENSET_CLKFAIL_Msk;

}

// *****************************************************************************
/* Function:
    void OSC32KCTRL_Handler(void);

  Summary:
    Handler that handles the XOSC32K Interrupts.

  Description:
    This Function is called from the handler to handle the XOSC32K Failure
    Interrupts.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_Handler(void)
{
    /* Checking for the Clock Failure status */
    if ((OSC32KCTRL_REGS->STATUS & OSC32KCTRL_STATUS_CLKFAIL_Msk) == OSC32KCTRL_STATUS_CLKFAIL_Msk)
    {

        if(osc32kctrlObj.callback != NULL)
        {
            osc32kctrlObj.callback(osc32kctrlObj.context);
        }

       /* Clearing the Clock Fail Interrupt */
        OSC32KCTRL_REGS->INTFLAG = OSC32KCTRL_INTFLAG_CLKFAIL_Msk;
    }
}
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: GCLK Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void GCLK_GeneratorEnable(GCLK_GENERATOR gclk, bool enable);

  Summary:
    Enables or disables the GCLK Generator.

  Description:
    This function will enable or disable the selected generic clock generator.
    The generator to be modified is specified by gclk parameter. A generator may
    be disabled to save power while entering a low power mode and enabled again
    when peripheral operation needs to be resumed.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void GCLK_GeneratorEnable(GCLK_GENERATOR gclk, bool enable)
{
    if(enable)
    {
         GCLK_REGS->GENCTRL[gclk] |= 1 << GCLK_GENCTRL_GENEN_Pos;
    }
    else
    {
         GCLK_REGS->GENCTRL[gclk] &= ~(1 << GCLK_GENCTRL_GENEN_Pos);
    }
}

// *****************************************************************************
/* Function:
    void GCLK_PeripheralChannelEnable (GCLK_PERIPHERAL_CHANNEL peripheralChannel,
                                       bool enable);

  Summary:
    Enables or disables the Peripheral Clock Channel.

  Description:
    This function will enable or disable the specified peripheral channel.
    Enabling the peripheral clock channel will enable the core clock that is
    required for peripheral to function. The peripheral clock channel may be
    disable to stop the clock to a peripheral to save power.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void GCLK_PeripheralChannelEnable (GCLK_PERIPHERAL_CHANNEL peripheralChannel, bool enable)
{
    if(enable)
    {
        /* Enabling the peripheral Channel */
        GCLK_REGS->PCHCTRL[peripheralChannel] |= 1 << GCLK_PCHCTRL_CHEN_Pos;
    }
    else
    {
        GCLK_REGS->PCHCTRL[peripheralChannel] &= ~(1 << GCLK_PCHCTRL_CHEN_Pos);
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: MCLK IMPLEMENTATION
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void MCLK_APBClockEnable ( MCLK_APB_CLOCK peripheral, bool enable );

  Summary:
    Enables or disables APB Clock.

  Description:
    This function will enable or disable the APB clock for the selected
    peripheral given by the peripheral parameter. Enabling the peripheral APB
    clock makes the peripheral register accessible.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void MCLK_APBClockEnable ( MCLK_APB_CLOCK peripheral, bool enable )
{
    uint32_t bridgeMask = peripheral/32;

    uint32_t mclkClockPos = peripheral%32;

    /* Base Address of the APB Bridge */
    uint32_t *apbBridgeAddr = (volatile uint32_t *)0x40000814;

    apbBridgeAddr = apbBridgeAddr + bridgeMask;

    if(enable)
    {
        *apbBridgeAddr |= 1 << mclkClockPos;
    }
    else
    {
        *apbBridgeAddr &= ~(1 << mclkClockPos);
    }

}

// *****************************************************************************
/* Function:
    void MCLK_AHBClockEnable ( MCLK_AHB_CLOCK ahbClock, bool enable );

  Summary:
    Enables or disables AHB Clock.

  Description:
    This function will enable or disable the AHB clock for the selected
    peripheral. Peripherals such CAN and DMAC use the AHB to access other memory
    regions. Enabling the AHB clock enables this access.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void MCLK_AHBClockEnable ( MCLK_AHB_CLOCK ahbClock, bool enable )
{
    if(enable)
    {
        MCLK_REGS->AHBMASK |= ahbClock;
    }
    else
    {
        MCLK_REGS->AHBMASK &= ~(ahbClock);
    }
}

// *****************************************************************************
/* Function:
    bool MCLK_ClockIsReady ( void );

  Summary:
    Returns the status of the Main Clock (MCLK).

  Description:
    This function returns true if the Main clock is ready. If the CPU clock
    divide values are changed, there is some delay involved till the new setting
    become active. This function can be called to check the readiness of the
    MCLK in such a case.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool MCLK_ClockIsReady ( void )
{
    bool clockReadyStatus = false;

    /* Check for the Clock Ready */
    if((MCLK_REGS->INTFLAG & MCLK_INTFLAG_CKRDY_Msk) == MCLK_INTFLAG_CKRDY_Msk)
    {
        clockReadyStatus = true;
    }

    return clockReadyStatus;
}
