/*******************************************************************************
  DWT PLIB Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dwt.c

  Summary:
    Data Watchpoint and Trace (DWT) Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#include "device.h"
#include "plib_dwt.h"

#define CPU_CLOCK_FREQ    ${CPU_CLOCK_FREQUENCY}U

void DWT_Initialize(void)
{
    CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;

<#if CoreArchitecture == "CORTEX-M7">
    DWT->LAR = 0xC5ACCE55U;
</#if>
    DWT->CYCCNT = 0U;
    DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;
}

void DWT_DelayUs(uint32_t delay_us)
{
    uint32_t startCount, endCount;

    /* Calculate the end count for the given delay */
    endCount = (CPU_CLOCK_FREQ / 1000000U) * delay_us;

    startCount = DWT->CYCCNT;
    while((DWT->CYCCNT - startCount) < endCount)
	{
		/* Do Nothing */
	}
}

void DWT_DelayMs(uint32_t delay_ms)
{
    uint32_t startCount, endCount;

    /* Calculate the end count for the given delay */
    endCount = (CPU_CLOCK_FREQ / 1000U) * delay_ms;

    startCount = DWT->CYCCNT;
    while((DWT->CYCCNT - startCount) < endCount)
	{
		/* Do Nothing */
	}
}

void DWT_CounterReset(void)
{
    DWT->CYCCNT = 0U; 
}

void DWT_CounterEnable(void)
{
    DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;
}

void DWT_CounterDisable(void)
{
    DWT->CTRL &= ~DWT_CTRL_CYCCNTENA_Msk;
}

uint32_t DWT_CounterGet(void)
{
    return DWT->CYCCNT;
}
