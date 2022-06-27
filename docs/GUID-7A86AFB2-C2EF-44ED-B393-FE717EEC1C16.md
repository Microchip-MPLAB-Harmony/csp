# Analog-to-Digital Converter \(ADC\)

-   10-bit 1 Msps rate with one Sample and Hold \(S&H\)

-   Up to 48 analog inputs

-   Can operate during Sleep mode

-   Flexible and independent ADC trigger sources


**Using The Library**

**Interrupt mode:**

```c
#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes

#define ADC_VREF                (3.3f)
#define ADC_MAX_COUNT           (1023U)

uint16_t adc_count;
float input_voltage;
volatile bool result_ready = false;

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

void ADC_ResultHandler(uintptr_t context)
{
    /* Read the ADC result */
    adc_count = ADC_ResultGet(ADC_RESULT_BUFFER_0);   
    result_ready = true;
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    ADC_CallbackRegister(ADC_ResultHandler, (uintptr_t)NULL);
    
    printf("\n\r---------------------------------------------------------");
    printf("\n\r                    ADC Demo                 ");
    printf("\n\r---------------------------------------------------------\n\r");
    
    while (1)
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );

        /* Auto sampling mode is used, so no code is needed to start sampling */
		
        /* Start ADC conversion in software */
        ADC_ConversionStart();

        /* Wait till ADC conversion result is available */
        if(result_ready == true)
        {
            result_ready = false;
            input_voltage = (float)adc_count * ADC_VREF / ADC_MAX_COUNT;
            printf("ADC Count = 0x%03x, ADC Input Voltage = %d.%02d V \r", adc_count, (int)input_voltage, (int)((input_voltage - (int)input_voltage)*100.0));
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
#include "definitions.h"                // SYS function prototypes

#define ADC_VREF                (3.3f)
#define ADC_MAX_COUNT           (1023U)

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
    
    while (1)
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );

        /* Auto sampling mode is used, so no code is needed to start sampling */
		
        /* Start ADC conversion in software */
        ADC_ConversionStart();

        /* Wait till ADC conversion result is available */
        while(!ADC_ResultIsReady())
        {

        };

        /* Read the ADC result */
        adc_count = ADC_ResultGet(ADC_RESULT_BUFFER_0);
        input_voltage = (float)adc_count * ADC_VREF / ADC_MAX_COUNT;

        printf("ADC Count = 0x%03x, ADC Input Voltage = %d.%02d V \r", adc_count, (int)input_voltage, (int)((input_voltage - (int)input_voltage)*100.0));
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|ADCx\_Initialize|Initializes ADC peripheral|
|ADCx\_Enable|Enable \(turn ON\) ADC module|
|ADCx\_Disable|Disable ADC module|
|ADC\_SamplingStart|Starts the sampling|
|ADCx\_ConversionStart|Starts the conversion|
|ADC\_InputSelect|Selects input for ADC|
|ADC\_InputScanSelect|Selects input for scanning ADC channels|
|ADC\_ResultIsReady|Returns the status of the channel conversion|
|ADC\_ResultGet|Provides the ADC conversion result based on the buffer index|
|ADCx\_CallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|ADC\_MUX|Enum|Identifies which ADC Mux is to be configured|
|ADC\_RESULT\_BUFFER|Enum|Identifies which ADC buffer has to be read|
|ADC\_INPUT\_POSITIVE|Enum|Identifies possible positive input for ADC|
|ADC\_INPUT\_NEGATIVE|Enum|Identifies possible negative input for ADC|
|ADC\_INPUTS\_SCAN|Enum|Identifies possible ADC inputs which can be scanned|
|ADC\_CALLBACK|Typedef|Defines the data type and function signature for the ADC peripheral callback function|

-   **[ADCx\_Initialize Function](GUID-396C47E4-A7E5-4E83-B9B2-C1C2D6B38DA0.md)**  

-   **[ADCx\_Enable Function](GUID-3A6F7362-5060-4448-A253-5E155F1FB260.md)**  

-   **[ADCx\_Disable Function](GUID-B8220677-A69F-4451-A8CD-70CF1BEE850A.md)**  

-   **[ADC\_SamplingStart Function](GUID-B593C3F4-98AC-4686-92F6-27F0A8BF59FD.md)**  

-   **[ADCx\_ConversionStart Function](GUID-6307B3DB-26C1-412F-A8A1-E25191B387AE.md)**  

-   **[ADC\_InputSelect Function](GUID-40CA1CD8-4300-43F1-A635-A6A9B4F0A643.md)**  

-   **[ADC\_InputScanSelect Function](GUID-C92EAF08-1776-4114-BBB7-F075B6A4FC10.md)**  

-   **[ADC\_ResultIsReady Function](GUID-5D2E6201-5C03-4392-877D-9DA6E1C49AF8.md)**  

-   **[ADC\_ResultGet Function](GUID-18187A2F-87DD-49C8-9F3E-605814181004.md)**  

-   **[ADCx\_CallbackRegister Function](GUID-7E626C3E-2FEB-4000-85F0-795BC62A9F46.md)**  

-   **[ADC\_MUX Enum](GUID-4C1C8E9C-E5F6-40B0-8FEB-0921EDF0E7E2.md)**  

-   **[ADC\_RESULT\_BUFFER Enum](GUID-31AC4D47-0131-46AB-B1AC-646177B2F9BD.md)**  

-   **[ADC\_INPUT\_POSITIVE Enum](GUID-D8FE7F48-1080-4577-9D1A-4A6F255B0387.md)**  

-   **[ADC\_INPUT\_NEGATIVE Enum](GUID-C96446DC-C414-45F0-B5BD-07307DCC3E98.md)**  

-   **[ADC\_INPUTS\_SCAN Enum](GUID-A4F6337C-267A-404A-9631-051BAD0419AD.md)**  

-   **[ADC\_CALLBACK Typedef](GUID-8D89973F-1373-4767-AD21-FCFCF48B5B1F.md)**  


**Parent topic:**[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)

**Parent topic:**[PIC32MX 1XX 2XX 5XX Peripheral Libraries](GUID-232A3DC0-B096-45AA-9430-33A2C9BA694A.md)

