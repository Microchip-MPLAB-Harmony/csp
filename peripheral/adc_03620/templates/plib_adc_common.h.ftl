/*******************************************************************************
  ADCHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adchs_common.h

  Summary
    Commonly needed stuff for the ADCHS peripheral libraries interfaces.

  Description
    This file defines several items commonly needed by the interfaces to
    the ADCHS peripheral libraries.

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

#ifndef PLIB_ADCHS_COMMON_H    // Guards against multiple inclusion
#define PLIB_ADCHS_COMMON_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************

typedef uint32_t ADC_CMPCTRL;
typedef uint32_t ADC_CORE_INT;
typedef uint32_t ADC_GLOBAL_INT;

<#list 0..((ADC_MAX_CHANNELS) - 1) as n>
	<#lt>#define ADC_CORE_INT_CHRDY_${n} 				(1 << (ADC_INTFLAG_CHRDY_Pos + ${n}))
</#list>
#define ADC_CORE_INT_EOSRDY					(ADC_INTFLAG_EOSRDY_Msk)
#define ADC_CORE_INT_CHNERRC				(ADC_INTFLAG_CHNERRC_Msk)
#define ADC_CORE_INT_FLTRDY					(ADC_INTFLAG_FLTRDY_Msk)
#define ADC_CORE_INT_CHRDYC					(ADC_INTFLAG_CHRDYC_Msk)
#define ADC_CORE_INT_SOVFL					(ADC_INTFLAG_SOVFL_Msk)
#define ADC_CORE_INT_CMPHIT					(ADC_INTFLAG_CMPHIT_Msk)

#define ADC_GLOBAL_INT_PFFHFUL				(ADC_CTLINTENSET_PFFHFUL_Msk)
#define ADC_GLOBAL_INT_PFFRDY				(ADC_CTLINTENSET_PFFRDY_Msk)
#define ADC_GLOBAL_INT_PFFOVF				(ADC_CTLINTENSET_PFFOVF_Msk)
#define ADC_GLOBAL_INT_PFFUNF				(ADC_CTLINTENSET_PFFUNF_Msk)
#define ADC_GLOBAL_INT_VREFRDY				(ADC_CTLINTENSET_VREFRDY_Msk)
#define ADC_GLOBAL_INT_VREFUPD				(ADC_CTLINTENSET_VREFUPD_Msk)
<#list 0..(ADC_NUM_SAR_CORES-1) as n>
	<#assign ADC_CORE_ENABLED    = "ADC_CORE_" + n + "_ENABLE">
	<#if .vars[ADC_CORE_ENABLED] == true>
	<#lt>#define ADC_GLOBAL_INT_CRRDY${n} 				(1 << (ADC_CTLINTENSET_CRRDY_Pos+${n}))
	</#if>
</#list>

#define ADC_CMP_MODE_IEHIHI					(ADC_CMPCTRL_IEHIHI_Msk)
#define ADC_CMP_MODE_IEHILO					(ADC_CMPCTRL_IEHILO_Msk)
#define ADC_CMP_MODE_IELOHI					(ADC_CMPCTRL_IELOHI_Msk)
#define ADC_CMP_MODE_IELOLO					(ADC_CMPCTRL_IELOLO_Msk)
#define ADC_CMP_MODE_IEBTWN					(ADC_CMPCTRL_IEBTWN_Msk)

/* Helper macros to extract channel id and core id from the ADC result read from the FIFO */
#define ADC_FIFO_CHNID_GET(fifo_data)			((fifo_data & ADC_PFFDATA_PFFCHNID_Msk) >> ADC_PFFDATA_PFFCHNID_Pos)
#define ADC_FIFO_CORID_GET(fifo_data)			((fifo_data & ADC_PFFDATA_PFFCORID_Msk) >> ADC_PFFDATA_PFFCORID_Pos)
#define ADC_FIFO_CNT_GET(fifo_data)				((fifo_data & ADC_PFFDATA_PFFCNT_Msk) >> ADC_PFFDATA_PFFCNT_Pos)
#define ADC_FIFO_DATA_GET(fifo_data)			((fifo_data & ADC_PFFDATA_PFFDATA_Msk) >> ADC_PFFDATA_PFFDATA_Pos)

typedef enum
{
<#list 0..(ADC_NUM_SAR_CORES-1) as n>
	<#assign ADC_CORE_ENABLED    = "ADC_CORE_" + n + "_ENABLE">
	<#if .vars[ADC_CORE_ENABLED] == true>
	ADC_CORE_NUM${n} = ${n}U,
	</#if>
</#list>
}ADC_CORE_NUM;


typedef enum
{
<#list 0..((ADC_MAX_CHANNELS) - 1) as k>
	ADC_CH${k} = ${k}U,
</#list>
}ADC_CHANNEL_NUM;



// *****************************************************************************

typedef void (*ADC_GLOBAL_CALLBACK)(ADC_GLOBAL_INT status, uintptr_t context);
typedef void (*ADC_CORE_CALLBACK)(ADC_CORE_INT status, uintptr_t context);

// *****************************************************************************

typedef struct
{
    ADC_GLOBAL_CALLBACK callback;
    uintptr_t context;
}ADC_GLOBAL_CALLBACK_OBJECT;

typedef struct
{
    ADC_CORE_CALLBACK callback;
    uintptr_t context;
}ADC_CORE_CALLBACK_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADC_COMMMON_H

/**
 End of File
*/
