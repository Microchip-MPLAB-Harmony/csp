/*******************************************************************************
  ADCHS Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADCHS_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADCHS_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ADCHS peripheral library.

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
#include "device.h"
#include "plib_${ADCHS_INSTANCE_NAME?lower_case}.h"

<#compress>


</#compress>

// *****************************************************************************
// *****************************************************************************
// Section: ${ADCHS_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#-- 
<#if ADCHS_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>ADCHS_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_CallbackObj;
</#if>
 -->
 
void ${ADCHS_INSTANCE_NAME}_Initialize()
{

    ADCCON1bits.ON = 0;

<#list 0..((ADCHS_NUM_CLASS1_SIGNALS + ADCHS_NUM_CLASS2_SIGNALS) - 1) as i>
    <#assign ADCHS_CH_ENABLE = "ADCHS_"+i+"_ENABLE">
    <#assign ADCHS_CH_NAME = "ADCHS_"+i+"_NAME">
    <#assign ADCHS_CH_ADCDIV = "ADC"+i+"TIME__ADCDIV">
    <#assign ADCHS_CH_SAMC = "ADC"+i+"TIME__SAMC">
    <#assign ADCHS_CH_SELRES = "ADC"+i+"TIME__SELRES">
    <#assign ADCHS_CH_ADCEIS = "ADC"+i+"TIME__ADCEIS">
    <#assign ADCHS_CH_SSAMPEN = "ADCTRGMODE__SSAMPEN"+i>
    <#assign ADCHS_CH_STRGEN = "ADCTRGMODE__STRGEN"+i>
    <#assign ADCHS_CH_SHxALT = "ADCTRGMODE__SH"+i+"ALT">
    <#assign ADCHS_CH_TRGSRC = "ADCTRG"+((i/4)+1)+"__TRGSRC"+i>
    <#assign ADCHS_CH_LVL = "ADCTRGSNS__LVL"+i>
    <#assign ADCHS_CH_DIFF = "ADCIMCON"+((i/16)+1)+"__DIFF"+i>
    <#assign ADCHS_CH_SIGN = "ADCIMCON"+((i/16)+1)+"__SIGN"+i>
    <#if .vars[ADCHS_CH_ENABLE] == true>
        // Activation for ADC${i}
        <#if i lt ADCHS_NUM_CLASS1_SIGNALS >
            // Initialize the ADC${i} calibration values
            DEVADC${i} = ADC${i}CFG;
            // keeping all DIGENx = 0
            ADCCON3bits.DIGEN${i} = 0;
            // keeping all analog enables ANENx bit = 0,
            ADCANCONbits.ANEN${i} = 0;

            // ADC${i}TIME
            //   ADCDIV<6:0> ADC${i} Clock 2x Divisor bits
            //     These bits divide the ADC control clock with period
            //     TQ to generate the clock for ADC${i} (TAD${i}).
            //     ${.vars[ADCHS_CH_ADCDIV]*2} * TQ = TAD${i}
            ADC${i}TIMEbits.ADCDIV = ${.vars[ADCHS_CH_ADCDIV]};
            //   SAMC<9:0>: ADC${i} Sample Time bits
            //     Where TAD${i} = period of the ADC conversion clock for the
            //     dedicated ADC controlled by the ADCDIV<6:0> bits.
            //     ${.vars[ADCHS_CH_SAMC]+2} TAD${i}
            ADC${i}TIMEbits.SAMC = ${.vars[ADCHS_CH_SAMC]};
            //   SELRES<1:0>: ADC${i} Resolution Select bits
            //      ${.vars[ADCHS_CH_SELRES]?number} means ${.vars[ADCHS_CH_SELRES]?number*2+6} bits
            ADC${i}TIMEbits.SELRES = ${.vars[ADCHS_CH_SELRES]};
            //   ADCEIS<2:0>: ADC${i} Early Interrupt Select bits
            //      The data ready interrupt is generated 
            //      ${.vars[ADCHS_CH_ADCEIS]?number+1} ADC clocks prior to the end of conversion
            ADC${i}TIMEbits.ADCEIS = ${.vars[ADCHS_CH_ADCEIS]};
            
            ADCTRGMODEbits.SSAMPEN${i} = ${.vars[ADCHS_CH_SSAMPEN]?c};
            ADCTRGMODEbits.STRGEN${i} = ${.vars[ADCHS_CH_STRGEN]?c};
            ADCTRGMODEbits.SH${i}ALT = ${.vars[ADCHS_CH_SHxALT]};
            ADCTRG${(i/4)+1}bits.TRGSRC${i} = ${.vars[ADCHS_CH_TRGSRC]};
            ADCTRGSNSbits.LVL${i} = ${.vars[ADCHS_CH_LVL]?c};
            //   ADCDIFF: ADC${i} Differential Mode bit
            //      ADCADC${i} Differential Mode ${.vars[ADCHS_CH_DIFF]?c}
            ADCIMCON${((i/16)+1)}bits.DIFF${i} = ${.vars[ADCHS_CH_DIFF]?c};
            //   ADCSIGN: ADC${i} Signed Data Mode bit
            //      ADCADC${i} Signed Data Mode ${.vars[ADCHS_CH_SIGN]?c}
            ADCIMCON${((i/16)+1)}bits.SIGN${i} = ${.vars[ADCHS_CH_SIGN]?c};
        <#elseif i == 7 >
            DEVADC${i} = ADC${i}CFG;
            // Shared ADC ADCDIV<6:0>, and SAMC<9:0>, SELRES<1:0>
            ADCCON2bits.ADCDIV = ${ADCCON2__ADCDIV};
            ADCCON2bits.SAMC = ${ADCCON2__SAMC};
            // Shared ADC (ADC7) Resolution
            //    ${ADCCON1__SELRES?number} means ${ADCCON1__SELRES?number*2+6} bits
            ADCCON1bits.SELRES= ${ADCCON1__SELRES};
            // Scan Trigger Source Select
            ADCCON1bits.STRGSRC = ${ADCCON1__STRGSRC};
            // Scan Trigger High Level/Positive Edge Sensitivity
            ADCCON1bits.STRGLVL = ${ADCCON1__STRGLVL};
            //   ADCEIS<2:0>: ADC${i} Early Interrupt Select bits
            //      The data ready interrupt is generated 
            //      ${ADCCON2__ADCEIS?number+1} ADC clocks prior to the end of conversion
            ADCCON2bits.ADCEIS = ${ADCCON2__ADCEIS};
            
        </#if>
    </#if>
</#list>

    // Interrupt Vector Shift
    ADCCON1bits.IRQVS = ${ADCCON1__IRQVS};
    // Fast Synchronous Peripheral Clock to ADC Control Clock
    ADCCON1bits.FSPBCLKEN = ${ADCCON1__FSPBCLKEN};
    // Fast Synchronous System Clock to ADC Control Clock
    ADCCON1bits.FSSCLKEN = ${ADCCON1__FSSCLKEN};
    // Capacitive Voltage Division Enable
    ADCCON1bits.CVDEN = ${ADCCON1__CVDEN};
    // Configure the AICPMPEN bit (ADCCON1<12> and the
    // IOANCPEN bit (CFGCON<7>) = 1 if and only if VDD is
    // less than 2.5V. The default is ‘0’, which assumes VDD
    // is greater than or equal to 2.5V.
    // ADCCON1bits.AICPMPEN = 1;
    // CFGCONbits.IOANCPEN = 1;
    // TBD
    // Stop in Idle Mode
    ADCCON1bits.SIDL = ${ADCCON1__SIDL};
    // Fractional Data Output Format
    ADCCON1bits.FRACT = ${ADCCON1__FRACT};
    // Capacitor Voltage Divider (CVD) Setting
    ADCCON2bits.CVDCPL = ${ADCCON2__CVDCPL};
    // Voltage Reference (VREF) Input Selection
    ADCCON3bits.VREFSEL = ${ADCCON3__VREFSEL};
    // Analog-to-Digital Control Clock (TQ) Divider
    ADCCON3bits.CONCLKDIV = ${ADCCON3__CONCLKDIV};
    // Analog-to-Digital Clock Source (TCLK)
    ADCCON3bits.ADCSEL = ${ADCCON3__ADCSEL};
    // Wake-up Clock Count
    // These bits represent the number of ADC clocks required to warm-up the 
    // ADC module before it can perform conversion. Although the clocks are 
    // specific to each ADC, the WKUPCLKCNT bit is common to all ADC modules
    ADCANCONbits.WKUPCLKCNT = 0x0A;

    // Step 3: Set the ON bit to ‘1’, which enables the ADC control clock.
    ADCCON1bits.ON = 1;
    // Step 4: Poll the status bit BGVRRDY until it is 1, which signals that
    // the device analog environment (band gap and VREF) is ready.
    while ( ADCCON2bits.BGVRRDY ==0 );

<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#if .vars[ADCHS_CH_ENABLE] == true>
        // Analog and Bias Circuitry Enable for ADC${i}
        // Step 5: Set the ANEN bit to ‘1’ for each of the ADC
        // SAR cores to be used.
        ADCANCONbits.ANEN${i} = 1;
        // Step 6: Wait for the interrupt or polls the warm-up
        // ready bits WKRDY = 1, which signals that the
        // respective ADC SAR cores are ready to operate.
        while ( ADCANCONbits.WKRDY${i} == 0 );
        // Step 7: Set the DIGENx bit to ‘1’, which enables the
        // digital circuitry to immediately begin processing
        // incoming triggers to perform data conversions.
        ADCCON3bits.DIGEN${i} = 1;
    </#if>
</#list>
    // Comparators, filters, and so on
    //<TBD>
}


/* Enable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ChannelsEnable (ADCHS_CHANNEL_MASK channelsMask)
{
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#if .vars[ADCHS_CH_ENABLE] == true>
        ADCCON3bits.DIGEN${i} = 1;
    </#if>
</#list>
}

/* Disable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ChannelsDisable (ADCHS_CHANNEL_MASK channelsMask)
{
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#if .vars[ADCHS_CH_ENABLE] == true>
        ADCCON3bits.DIGEN${i} = 0;
    </#if>
</#list>
}

/* Enable Interrupts from ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ChannelsInterruptEnable (ADCHS_INTERRUPT_MASK channelsInterruptMask)
{
}
/* Disable Interrupts from ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ChannelsInterruptDisable (ADCHS_INTERRUPT_MASK channelsInterruptMask)
{
}

void ${ADCHS_INSTANCE_NAME}_ConversionStart(void)
{
    // Start Channel 0 conversion
    ADCCON3bits.ADINSEL = 0;
    ADCCON3bits.RQCNVRT = 1;
}

// ****NEW****
/* Start all conversions with software global trigger */
void ${ADCHS_INSTANCE_NAME}_GlobalConversionStart(void)
{
    ADCCON3bits.GSWTRG = 1;
}

// ****NEW****
/* Start the conversion of a specific channel */
void ${ADCHS_INSTANCE_NAME}_ChannelConversionStart (ADCHS_CHANNEL_NUM channel)
{
    // Start Channel conversion
    ADCCON3bits.ADINSEL = channel;
    ADCCON3bits.RQCNVRT = 1;
}

/*Check if conversion result is available */
bool ${ADCHS_INSTANCE_NAME}_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel)
{
    return((ADCDSTAT1+channel/32)&0x01<<(channel%32));
}

/* Read the conversion result */
uint16_t ${ADCHS_INSTANCE_NAME}_ChannelResultGet(ADCHS_CHANNEL_NUM channel)
{
    return(*((&ADCDATA0)+sizeof(ADCDATA0)*channel));
}

///* Define the conversion sequence */
//void ${ADCHS_INSTANCE_NAME}_ConversionSequenceSet(ADCHS_CHANNEL_NUM *channelList, uint8_t numChannel)
//{
//}
///* Set the gain for a channel */
//void ${ADCHS_INSTANCE_NAME}_ChannelGainSet(ADCHS_CHANNEL_NUM channel, ADCHS_CHANNEL_GAIN gain)
//{
//}
///* Set the offset for a channel */
//void ${ADCHS_INSTANCE_NAME}_ChannelOffsetSet(ADCHS_CHANNEL_NUM channel, uint16_t offset)
//{
//}

