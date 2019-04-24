/*******************************************************************************
  ADC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc.c

  Summary
    ADC peripheral library source.

  Description
    This file implements the ADC peripheral library.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END
#include "device.h"
#include "plib_adc.h"

// *****************************************************************************
// *****************************************************************************
// Section: ADC Implementation
// *****************************************************************************
// *****************************************************************************


void ADC_Initialize()
{
    AD1CON1CLR = _AD1CON1_ON_MASK;

    AD1CON1 = 0x4;
    AD1CHS = 0x90000;


    /* Turn ON ADC */
    AD1CON1SET = _AD1CON1_ON_MASK;
}

void ADC_Enable()
{
    AD1CON1SET = _AD1CON1_ON_MASK;
}

void ADC_Disable()
{
    AD1CON1CLR = _AD1CON1_ON_MASK;
}

void ADC_SamplingStart(void)
{
    AD1CON1CLR = _AD1CON1_DONE_MASK;
    AD1CON1SET = _AD1CON1_SAMP_MASK;
}

void ADC_ConversionStart()
{
    AD1CON1CLR = _AD1CON1_SAMP_MASK;
}

void ADC_InputSelect(ADC_MUX muxType, ADC_INPUT_POSITIVE positiveInput, ADC_INPUT_NEGATIVE negativeInput)
{
	if (muxType == ADC_MUX_B)
	{
    	AD1CHSbits.CH0SB = positiveInput;
        AD1CHSbits.CH0NB = negativeInput;
	}
	else
	{
    	AD1CHSbits.CH0SA = positiveInput;
        AD1CHSbits.CH0NA = negativeInput;
	}
}

void ADC_InputScanSelect(ADC_INPUTS_SCAN scanInputs)
{
    AD1CSSL = scanInputs;
}

/*Check if conversion result is available */
bool ADC_ResultIsReady()
{
    return AD1CON1bits.DONE;
}

/* Read the conversion result */
uint32_t ADC_ResultGet(ADC_RESULT_BUFFER bufferNumber)
{
    return (*((&ADC1BUF0) + bufferNumber));
}

