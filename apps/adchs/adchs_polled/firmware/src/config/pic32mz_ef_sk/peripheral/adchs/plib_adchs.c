/*******************************************************************************
  ADCHS Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_adchs.c

  Summary
    ADCHS peripheral library source.

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
#include "plib_adchs.h"


// *****************************************************************************
// *****************************************************************************
// Section: ADCHS Implementation
// *****************************************************************************
// *****************************************************************************

//Xvoid ADCHS_Initialize (void);
//Xvoid ADCHS_ChannelsEnable (ADCHS_CHANNEL_MASK channelsMask);
//Xvoid ADCHS_ChannelsDisable (ADCHS_CHANNEL_MASK channelsMask);
//void ADCHS_ChannelsInterruptEnable (ADCHS_INTERRUPT_MASK channelsInterruptMask);
//void ADCHS_ChannelsInterruptDisable (ADCHS_INTERRUPT_MASK channelsInterruptMask);
//Xvoid ADCHS_ConversionStart(void);
//NEW-void ADCHS_GlobalConversionStart(void);
//NEW-void ADCHS_ChannelConversionStart (ADCHS_CHANNEL_NUM channel)
//Xbool ADCHS_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel);
//Xuint16_t ADCHS_ChannelResultGet(ADCHS_CHANNEL_NUM channel);
//void ADCHS_ConversionSequenceSet(ADCHS_CHANNEL_NUM *channelList, uint8_t numChannel);
//void ADCHS_ChannelGainSet(ADCHS_CHANNEL_NUM channel, ADCHS_CHANNEL_GAIN gain);
//void ADCHS_ChannelOffsetSet(ADCHS_CHANNEL_NUM channel, uint16_t offset);

 
void ADCHS_Initialize()
{

    // ADC0 Activation Sequence
    // Step 1 Initialize the ADC calibration values
    DEVADC0 = ADC0CFG;
    // then configure the AICPMPEN bit (ADCCON1<12> and the
    // IOANCPEN bit (CFGCON<7>) = 1 if and only if VDD is
    // less than 2.5V. The default is ‘0’, which assumes VDD
    // is greater than or equal to 2.5V.
    //<TBD>
    
    // Step 2: Write all the essential ADC configuration
    // SFRs including the ADC control clock and all ADC
    // core clocks setup
    //      ADCCON1, keeping the ON bit = 0
    ADCCON1bits.ON = 0;
    //      ADCCON2, especially paying attention to ADCDIV<6:0> and SAMC<9:0>
    ADCCON2bits.ADCDIV = 0;
    ADCCON2bits.SAMC = 0;
    //      ADCANCON, keeping all analog enables ANENx bit = 0, WKUPCLKCNT bit = 0xA
    ADCANCONbits.WKUPCLKCNT = 0x0A;
    //      ADCCON3, keeping all DIGEN5x = 0, especially paying attention to ADCSEL<1:0>, CONCLKDIV <5:0>, and VREFSEL<2:0>
    ADCCON3bits.ADCSEL = 0;
    ADCCON3bits.CONCLKDIV = 0;
    ADCCON3bits.VREFSEL = 0;
    //      ADCxTIME, ADCDIV<6:0>, and SAMC<9:0>
    ADC0TIMEbits.ADCDIV;
    ADC0TIMEbits.SAMC;
    //      ADCTRGMODE, SH0ALT<1:0>, STRGEN0, SSAMPEN0
    ADCTRGMODEbits.SH0ALT = 0;
    ADCTRGMODEbits.STRGEN0 = 0;
    ADCTRGMODEbits.SSAMPEN0 = 0;
    //      ADCIMCONx DIFF and SIGN bits.
    ADCIMCON1bits.DIFF0 = 0;
    ADCIMCON1bits.SIGN0 = 0;
    //      ADCTRGSNS LVL bits
    ADCTRGSNSbits.LVL0 = 0;
    //      ADCCSSx ADC COMMON SCAN SELECT REGISTER
    //      ADCGIRQENx ADC GLOBAL INTERRUPT ENABLE REGISTER
    //      ADCTRGx ADC TRIGGER SOURCE
    ADCTRG1bits.TRGSRC0 = 0;
    //      ADCBASE ADC BASE REGISTER
    // Comparators, filters, and so on

    // Step 3: Set the ON bit to ‘1’, which enables the ADC control clock.
    ADCCON1bits.ON = 1;
    // Step 4: Wait for the interrupt or polls the status bit
    // BGVRRDY = 1, which signals that the device analog
    // environment (band gap and VREF) is ready.
    while ( ADCCON2bits.BGVRRDY ==0 );
    // Step 5: Set the ANENx bit to ‘1’ for each of the ADC
    // SAR cores to be used.
    ADCANCONbits.ANEN0 = 1;
    // Step 6: Wait for the interrupt or polls the warm-up
    // ready bits WKRDYx = 1, which signals that the
    // respective ADC SAR cores are ready to operate.
    while ( ADCANCONbits.WKRDY0 == 0 );
    // Step 7: Set the DIGENx bit to ‘1’, which enables the
    // digital circuitry to immediately begin processing
    // incoming triggers to perform data conversions.
    ADCCON3bits.DIGEN0 = 1;


}


/* Enable ADCHS channels */
void ADCHS_ChannelsEnable (ADCHS_CHANNEL_MASK channelsMask)
{
    ADCCON3bits.DIGEN0 = 1;
}

/* Disable ADCHS channels */
void ADCHS_ChannelsDisable (ADCHS_CHANNEL_MASK channelsMask)
{
    ADCCON3bits.DIGEN0 = 0;
}

/* Enable Interrupts from ADCHS channels */
void ADCHS_ChannelsInterruptEnable (ADCHS_INTERRUPT_MASK channelsInterruptMask)
{
}
/* Disable Interrupts from ADCHS channels */
void ADCHS_ChannelsInterruptDisable (ADCHS_INTERRUPT_MASK channelsInterruptMask)
{
}

/* Start the conversion with software global trigger */
void ADCHS_ConversionStart(void)
{
    // Start Channel 0 conversion
    ADCCON3bits.ADINSEL = 0;
    ADCCON3bits.RQCNVRT = 1;
}

// ****NEW****
/* Start all conversions with software global trigger */
void ADCHS_GlobalConversionStart(void)
{
    ADCCON3bits.GSWTRG = 1;
}

// ****NEW****
/* Start the conversion of a specific channel */
void ADCHS_ChannelConversionStart (ADCHS_CHANNEL_NUM channel)
{
    // Start Channel conversion
    ADCCON3bits.ADINSEL = channel;
    ADCCON3bits.RQCNVRT = 1;
}

/*Check if conversion result is available */
bool ADCHS_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel)
{
    return(ADCDSTAT1bits.ARDY0);
}

/* Read the conversion result */
uint16_t ADCHS_ChannelResultGet(ADCHS_CHANNEL_NUM channel)
{
    return(ADCDATA0);
}

///* Define the conversion sequence */
//void ADCHS_ConversionSequenceSet(ADCHS_CHANNEL_NUM *channelList, uint8_t numChannel)
//{
//}
///* Set the gain for a channel */
//void ADCHS_ChannelGainSet(ADCHS_CHANNEL_NUM channel, ADCHS_CHANNEL_GAIN gain)
//{
//}
///* Set the offset for a channel */
//void ADCHS_ChannelOffsetSet(ADCHS_CHANNEL_NUM channel, uint16_t offset)
//{
//}

