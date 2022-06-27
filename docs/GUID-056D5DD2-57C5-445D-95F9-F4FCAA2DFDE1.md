# Analog-to-Digital Converter \(ADC\)

-   12-bit Resolution with Enhanced Mode up to 16 bits

-   1 Msps Conversion Rate

-   Digital Averaging Function providing Enhanced Resolution Mode up to 16 bits

-   On-chip Temperature Sensor Management

-   Selectable Single-Ended or Differential Input Voltage

-   Digital Correction of Offset and Gain Errors

-   Individual Enable and Disable of Each Channel

-   Hardware or Software Trigger

-   Drive of PWM Fault Input

-   DMA Support

-   Two Sleep Modes

-   Channel Sequence Customizing

-   Automatic Window Comparison of Converted Values


**Using The Library**

**Interrupt mode:**

```c
#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

#define ADC_VREF               (3.3f)

uint16_t adc_ch5_count, adc_ch6_count, adc_ch7_count;

float adc_ch5_voltage, adc_ch6_voltage, adc_ch7_voltage;

volatile bool result_ready = false;

/* This function is called after conversion of last channel in the user sequence */
void ADC_EventHandler(uint32_t interruptStatus, uint32_t eocInterruptStatus, uintptr_t context)
{
    /* Read the result of 3 channels*/
    adc_ch6_count = ADC_ChannelResultGet(ADC_CH6);
    adc_ch7_count = ADC_ChannelResultGet(ADC_CH7);
    adc_ch5_count = ADC_ChannelResultGet(ADC_CH5);
       
    result_ready = true;

}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    /* Register callback function for ADC end of conversion interrupt*/
    ADC_CallbackRegister(ADC_EventHandler, (uintptr_t)NULL);
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    ADC User Sequence Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    printf("CH5 Count  CH5 Voltage  CH6 Count  CH6 Voltage  CH7 Count  CH7 Voltage \n\r");           

    TC0_CH0_CompareStart();

    while ( true )
    {
        /* Check if result is ready to be transmitted to console */
        if (result_ready == true)
        {
            adc_ch6_voltage = (float)adc_ch6_count * ADC_VREF/4095U;
            adc_ch7_voltage = (float)adc_ch7_count * ADC_VREF/4095U;
            adc_ch5_voltage = (float)adc_ch5_count * ADC_VREF/4095U;
            printf("0x%03x      %0.2f V       0x%03x      %0.2f V       0x%03x      %0.2f V \t\r",
                    adc_ch5_count, adc_ch5_voltage, adc_ch6_count, adc_ch6_voltage, adc_ch7_count, adc_ch7_voltage);
                           
                
            result_ready = false;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Polling mode:**

```c
#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <stdio.h>
#include "definitions.h"                // SYS function prototypes

/*****************************************************
 ADC CH0 - PD19 - Connect to Vcc or GND
 *****************************************************/

#define ADC_VREF               (3.3f)

uint16_t adc_count;
float input_voltage;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    ADC Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    
    PIT64B0_TimerStart();

    while (1)
    {
        /* Start ADC conversion */
        ADC_ConversionStart();

        /* Wait till ADC conversion result is available */
        while(!ADC_ChannelResultIsReady(ADC_CH5))
        {

        };

        /* Read the ADC result */
        adc_count = ADC_ChannelResultGet(ADC_CH5);
        input_voltage = (float)adc_count * ADC_VREF / 4095U;

        printf("ADC Count = 0x%03x, ADC Input Voltage = %0.2f V \r",adc_count, input_voltage);    
        
        PIT64B0_DelayMs(500);
    }
    
    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

Analog-to-Digital Converter peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|ADCx\_Initialize|Initializes given instance of ADC peripheral|
|ADC\_ChannelsEnable|Enables the ADC channels|
|ADC\_ChannelsDisable|Disables the ADC channels|
|ADC\_ChannelsInterruptEnable|Enables the ADC interrupt sources|
|ADC\_ChannelsInterruptDisable|Disables the ADC interrupt sources|
|ADC\_InterruptEnable|This function enables the interrupts|
|ADC\_InterruptDisable|This function disables the interrupts|
|ADC\_InterruptStatusGet|Returns the status of ADC interrupt|
|ADCx\_ConversionStart|Starts the ADC conversion of all the enabled channels with the software trigger|
|ADC\_ChannelResultIsReady|Returns the status of the channel conversion|
|ADC\_ChannelResultGet|Reads the conversion result of the channel|
|ADC\_ConversionSequenceSet|Sets the user sequence of the channel conversion|
|ADCx\_ComparisonWindowSet|Sets Low threshold and High threshold in comparison window|
|ADC\_ComparisonEventResultIsReady|Returns the status of the Comparison event|
|ADC\_ComparisonRestart|Restart the comparison function|
|ADC\_SleepModeEnable|This function enables ADC sleep mode|
|ADC\_SleepModeDisable|This function disables ADC sleep mode|
|ADC\_FastWakeupEnable|This function enables ADC Fast Wakeup|
|ADC\_FastWakeupDisable|This function disables ADC Fast Wakeup|
|ADCx\_CallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|ADC\_CHANNEL\_MASK|Enum|Identifies ADC channel mask|
|ADC\_CHANNEL\_NUM|Enum|Identifies ADC channel number|
|ADC\_INTERRUPT\_EOC\_MASK|Enum|Identifies EOC interrupt sources number|
|ADC\_INTERRUPT\_MASK|Enum|Identifies interrupt sources number|
|ADC\_CALLBACK|Typedef|Defines the data type and function signature for the ADC peripheral callback function|
|ADC\_CALLBACK\_OBJECT|Struct|ADC Callback structure|

-   **[ADCx\_Initialize Function](GUID-396C47E4-A7E5-4E83-B9B2-C1C2D6B38DA0.md)**  

-   **[ADC\_ChannelsEnable Function](GUID-46FC6D36-1CA4-4FA8-B5A6-72FA02059330.md)**  

-   **[ADC\_ChannelsDisable Function](GUID-FE7C41E5-C15A-43F2-BC5A-7F119007EA61.md)**  

-   **[ADC\_ChannelsInterruptEnable Function](GUID-C4703011-1BB9-4835-A7A8-779FBEE2295F.md)**  

-   **[ADC\_ChannelsInterruptDisable Function](GUID-40093DDC-87B6-4D61-B79F-213EB2D6FA41.md)**  

-   **[ADC\_InterruptEnable Function](GUID-29955F6A-A49D-41E5-AF63-34BC50C3A0D9.md)**  

-   **[ADC\_InterruptDisable Function](GUID-6932FDBA-8D80-465C-9B26-35FBC0F69C84.md)**  

-   **[ADC\_InterruptStatusGet Function](GUID-17D37652-B845-4A1C-A8C8-FC5238ECEAB6.md)**  

-   **[ADCx\_ConversionStart Function](GUID-6307B3DB-26C1-412F-A8A1-E25191B387AE.md)**  

-   **[ADC\_ChannelResultIsReady Function](GUID-BB98C900-C5D9-4393-991D-DD40FA2500A1.md)**  

-   **[ADC\_ChannelResultGet Function](GUID-D258B529-BEDB-45C6-82BD-653926FC0F1D.md)**  

-   **[ADC\_ConversionSequenceSet Function](GUID-41E0D61F-0271-4D14-AB03-9329B2C8DC20.md)**  

-   **[ADCx\_ComparisonWindowSet Function](GUID-98A43D93-0158-4DEA-900F-9F0668981AF0.md)**  

-   **[ADC\_ComparisonEventResultIsReady Function](GUID-BFF4E684-1B27-4353-AE5F-C54009D9FB03.md)**  

-   **[ADC\_ComparisonRestart Function](GUID-7EF17FFE-BC33-4182-86D2-45C5ABD271D0.md)**  

-   **[ADC\_SleepModeEnable Function](GUID-81FA0658-D783-4157-92E1-C752F99B7547.md)**  

-   **[ADC\_SleepModeDisable Function](GUID-F52709D1-E89B-4283-9B52-50EB9BC206A0.md)**  

-   **[ADC\_FastWakeupEnable Function](GUID-6B63A7FE-339C-43FC-BEDB-571209DDF3DA.md)**  

-   **[ADC\_FastWakeupDisable Function](GUID-FE744534-4F8C-4461-8ED1-38EF3AF0A70A.md)**  

-   **[ADCx\_CallbackRegister Function](GUID-7E626C3E-2FEB-4000-85F0-795BC62A9F46.md)**  

-   **[ADC\_CHANNEL\_MASK Enum](GUID-3F16CEB2-EE1B-4BBF-BAD6-05654558518B.md)**  

-   **[ADC\_CHANNEL\_NUM Enum](GUID-F95C06AB-841F-4195-B216-E534F0AF9B62.md)**  

-   **[ADC\_INTERRUPT\_EOC\_MASK Enum](GUID-13DD9650-51D7-4817-918B-B3AED2FE0344.md)**  

-   **[ADC\_INTERRUPT\_MASK Enum](GUID-ED022E84-04D8-4C43-962D-E30BBBFDC1D3.md)**  

-   **[ADC\_CALLBACK Typedef](GUID-8D89973F-1373-4767-AD21-FCFCF48B5B1F.md)**  

-   **[ADC\_CALLBACK\_OBJECT Struct](GUID-4EDAD226-0551-425A-9BF7-B824B9BF26F7.md)**  


**Parent topic:**[PIC32CX MT Peripheral Libraries](GUID-EEA7836F-956F-4526-BF85-CD488C4CE708.md)

**Parent topic:**[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)

