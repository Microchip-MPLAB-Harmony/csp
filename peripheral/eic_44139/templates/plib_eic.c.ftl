/*******************************************************************************
  External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${EIC_INSTANCE_NAME?lower_case}.c

  Summary
    Source for EIC peripheral library interface Implementation.

  Description
    This file defines the interface to the EIC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#include <stddef.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${EIC_INSTANCE_NAME?lower_case}.h"

#define EIC_SCFGR_POL_Pos                    8U
#define EIC_SCFGR_POL_Msk                    (1UL << EIC_SCFGR_POL_Pos)

#define EIC_SCFGR_LVL_Pos                    9U
#define EIC_SCFGR_LVL_Msk                    (1UL << EIC_SCFG0R_LVL_Pos)

#define EIC_SCFGR_EN_Pos                     16U
#define EIC_SCFGR_EN_Msk                     (1UL << EIC_SCFGR_EN_Pos)

#define EIC_SCFGR_FRZ_Pos                    31U
#define EIC_SCFGR_FRZ_Msk                    (1UL << EIC_SCFGR_FRZ_Pos)

/* MISRA C-2012 Rule 7.2 violated ${EIC_NUM_INTERRUPTS} times below. Deviation record ID - H3_MISRAC_2012_R_7_2_DR_1*/
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate:${EIC_NUM_INTERRUPTS} "MISRA C-2012 Rule 7.2" "H3_MISRAC_2012_R_7_2_DR_1"
</#if>

static volatile struct
{
    volatile uint32_t* const pSCFGR;
    bool active;
    EIC_CALLBACK callback;
    uintptr_t context;
}eicData[] =
{
<#list 0..EIC_NUM_INTERRUPTS - 1 as index>
    {(volatile uint32_t* const)(${EIC_INSTANCE_NAME}_BASE_ADDRESS + EIC_SCFG${index}R_REG_OFST), false, NULL, 0U},
</#list>
};

<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 7.2"
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2012 deviation block end for Rule 7.2 */

void ${EIC_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Write protection */
    ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = EIC_WPMR_WPKEY_PASSWD;

<#list 0..EIC_NUM_INTERRUPTS - 1 as index>
<#compress>
<#assign REG_VAL = "">
<#assign COMMENT = "Configure interrupt as ">
<#assign ACTIVATE = .vars["EIC_SRCx_ACTIVATE"?replace("x", index)]>
<#if .vars["EIC_SRCx_DETECT"?replace("x", index)] == "Edge">
<#assign COMMENT = COMMENT + "Edge Interrupt with ">
<#assign POLARITY = .vars["EIC_SRCx_POLARITY_EDGE"?replace("x", index)]>
<#else>
<#assign COMMENT = COMMENT + "Level Interrupt with ">
<#assign POLARITY = .vars["EIC_SRCx_POLARITY_LEVEL"?replace("x", index)]>
<#assign REG_VAL = REG_VAL + "EIC_SCFGxR_LVL_Msk | "?replace("x", index)>
</#if>
<#assign COMMENT = COMMENT + POLARITY + " Polarity">
<#if POLARITY == "Rising Edge" || POLARITY == "Active High">
<#assign REG_VAL = REG_VAL + "EIC_SCFGxR_POL_Msk | "?replace("x", index)>
</#if>
<#if .vars["EIC_SRCx_GLITCH_FILTER_ENABLE"?replace("x", index)]>
<#assign COMMENT = COMMENT + " and glitch filter">
<#assign GLITCH_VAL = .vars["EIC_SRCx_GLITCH_FILTER_VALUE"?replace("x", index)]>
<#assign REG_VAL = REG_VAL + "EIC_SCFGxR_GFEN_Msk | EIC_SCFGxR_GFSEL("?replace("x", index) + GLITCH_VAL + "U)">
</#if>
<#if REG_VAL == "">
<#assign REG_VAL = "0U">
<#else>
<#assign REG_VAL = REG_VAL?remove_ending("| ")>
</#if>
</#compress>
    /************************** Configure Interrupt ${index} *************************/

<#if ACTIVATE>
    /* Mark interrupt as active */
    eicData[${index}].active = true;

    /* Disable Interrupt */
    ${EIC_INSTANCE_NAME}_REGS->EIC_SCFG${index}R &= ~(EIC_SCFG${index}R_EN_Msk);

    /* ${COMMENT} */
    ${EIC_INSTANCE_NAME}_REGS->EIC_SCFG${index}R = (${REG_VAL});
<#if .vars["EIC_SRCx_GLITCH_FILTER_ENABLE"?replace("x", index)]>

    /* Wait for Glitch filter to be ready */
    while((${EIC_INSTANCE_NAME}_REGS->EIC_GFCS & EIC_GFCS_RDY${index}_Msk) == 0U)
	{
		/* Do Nothing */
	}
</#if>

    /* Enable Interrupt */
    ${EIC_INSTANCE_NAME}_REGS->EIC_SCFG${index}R |= EIC_SCFG${index}R_EN_Msk;
<#else>
    /* Mark interrupt as inactive */
    eicData[${index}].active = false;

    /* Keep interrupt disabled */
    ${EIC_INSTANCE_NAME}_REGS->EIC_SCFG${index}R = 0U;
</#if>

</#list>
    /**************************************************************************/

    /* Enable Write protection */
    ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = (EIC_WPMR_WPKEY_PASSWD | EIC_WPMR_WPCFEN_Msk);
}


void ${EIC_INSTANCE_NAME}_CallbackRegister(EIC_PIN pin, EIC_CALLBACK callback, uintptr_t context)
{
    eicData[pin].callback = callback;
    eicData[pin].context = context;
}


bool ${EIC_INSTANCE_NAME}_InterruptEnable(EIC_PIN pin)
{
    bool retVal = false;
    /* check if interrupt is active */
    if(eicData[pin].active)
    {
        /*Check if interrupt configurations are frozen */
        if((*eicData[pin].pSCFGR & EIC_SCFGR_FRZ_Msk) == 0U)
        {
            /* Disable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = EIC_WPMR_WPKEY_PASSWD;

            /* Enable interrupt */
            *eicData[pin].pSCFGR |= EIC_SCFGR_EN_Msk;

            /* Enable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = (EIC_WPMR_WPKEY_PASSWD | EIC_WPMR_WPCFEN_Msk);
            retVal = true;
        }
    }
    return retVal;
}


bool ${EIC_INSTANCE_NAME}_InterruptDisable(EIC_PIN pin)
{
    bool retVal = false;
    /* check if interrupt is active */
    if(eicData[pin].active)
    {
        /*Check if interrupt configurations are frozen */
        if((*eicData[pin].pSCFGR & EIC_SCFGR_FRZ_Msk) == 0U)
        {
            /* Disable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = EIC_WPMR_WPKEY_PASSWD;

            /* Disable interrupt */
            *eicData[pin].pSCFGR &= ~(EIC_SCFGR_EN_Msk);

            /* Enable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = (EIC_WPMR_WPKEY_PASSWD | EIC_WPMR_WPCFEN_Msk);
            retVal = true;
        }
    }
    return retVal;
}


bool ${EIC_INSTANCE_NAME}_SetPolarity(EIC_PIN pin, EIC_POLARITY polarity)
{
    bool retVal = false;
    /* check if interrupt is active */
    if(eicData[pin].active)
    {
        /*Check if interrupt configurations are frozen */
        if((*eicData[pin].pSCFGR & EIC_SCFGR_FRZ_Msk) == 0U)
        {
            /* Disable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = EIC_WPMR_WPKEY_PASSWD;

            /* Set Falling edge/Active Low */
            if (polarity == EIC_POLARITY_FALLING_EDGE)
            {
                *eicData[pin].pSCFGR &= ~(EIC_SCFGR_POL_Msk);
            }
            /* Set Rising Edge/Active High */
            else
            {
                /* Enable interrupt */
                *eicData[pin].pSCFGR |= EIC_SCFGR_POL_Msk;
            }
            /* Enable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = (EIC_WPMR_WPKEY_PASSWD | EIC_WPMR_WPCFEN_Msk);
            retVal = true;
        }
    }
    return retVal;
}


bool ${EIC_INSTANCE_NAME}_FreezeConfiguration(EIC_PIN pin)
{
    bool retVal = false;
    /* check if interrupt is active */
    if(eicData[pin].active)
    {
        /*Check if interrupt configurations are frozen */
        if((*eicData[pin].pSCFGR & EIC_SCFGR_FRZ_Msk) == 0U)
        {
            /* Disable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = EIC_WPMR_WPKEY_PASSWD;

            /* Freeze interrupt configurations, no further modifications are permitted */
            *eicData[pin].pSCFGR |= EIC_SCFGR_FRZ_Msk;

            /* Enable Write protection */
            ${EIC_INSTANCE_NAME}_REGS->EIC_WPMR = (EIC_WPMR_WPKEY_PASSWD | EIC_WPMR_WPCFEN_Msk);
        }
        retVal = true;
    }
    return retVal;
}


<#list 0..EIC_NUM_INTERRUPTS - 1 as index>
<#if  .vars["EIC_SRCx_ACTIVATE"?replace("x", index)]>
void __attribute__((used)) EIC_EXT_IRQ${index}_InterruptHandler(void)
{
    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    uintptr_t context = eicData[${index}].context;

    if (eicData[${index}].callback != NULL)
    {
       eicData[${index}].callback(context);
    }
}


</#if>
</#list>