# Output Compare \(OCMP\)

The Output Compare module is primarily used to generate a single pulse or a series of pulses in response to selected time base events. Each output compare module can select between one of six 16-bit timers for the time base, or two of six 16-bit timers together to form a 32-bit timer. The selected timer can use either an internal or external clock.

Each Output Compare module has the following modes of operation \(OCM bit field\):<br />Single Compare Match Mode:

-   With output drive high - Initial state of the pin is low. OCx pin becomes high on compare match.

-   With output drive low - Initial state of the pin is high. OCx pin becomes low on compare match.

-   With output drive toggles - OCx pin toggles on compare match.


Dual Compare Match Mode:

-   With single output pulse - OCx pin becomes high on compare match and becomes low on secondary compare match

-   With continuous output pulses - OCx pin becomes high on compare match and becomes low on secondary compare match continuously. Compare time base will count up to period value defined in the selected timer source module.


Pulse Width Modulation Mode:

-   PWM without fault protection input - PWM duty cycle is defined by secondary compare register, OCxRS and PWM period is defined by selected timer period register \(PRy\)

-   PWM with fault protection input - PWM duty cycle is defined by secondary compare register, OCxRS and PWM period is defined by selected timer period register \(PRy\). PWM outputs are shut asynchronously when fault condition is detected.


**Using The Library**

This peripheral library is used to generate a single pulse or continuous pulses. The OCMP module needs the TMR module to provide the time base. The period value is defined in the TMR module and the compare value is defined in the OCMP module.

In this application, three OCMP modules are used to generate waveforms.

Active Low Output: By default output is set as high and it is set as low on the compare match

Active High Output: By default output is set as low and it is set as high on the compare match

Toggled Output: Compare match toggles the output.

```c
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    /* Active low output */
    OCMP1_Enable();
    /* Active high output */
    OCMP2_Enable();
    /* toggled output */
    OCMP3_Enable();

    TMR2_Start();    

    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

Peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|OCMPx\_Initialize|Initializes OCMPx module of the device|
|OCMPx\_Enable|Enable function for the OCMPx peripheral|
|OCMPx\_Disable|Disable function for the OCMPx peripheral|
|OCMPx\_FaultStatusGet|Reads the fault status|
|OCMPx\_CompareValueSet|Configures the compare register|
|OCMPx\_CompareValueGet|Reads the compare value|
|OCMPx\_CompareSecondaryValueGet|Reads secondary compare register|
|OCMPx\_CompareSecondaryValueSet|Sets OCMPx Secondary Compare Register|
|OCMPx\_CallbackRegister|Registers the function to be called from interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|OCMP\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the OCMP callback function|

-   **[OCMPx\_Initialize Function](GUID-A1272E6C-EB14-461D-980C-CBDA3A1A3846.md)**  

-   **[OCMPx\_FaultStatusGet Function](GUID-7E898315-4BCA-43C5-854E-BDC3E8BAA702.md)**  

-   **[OCMPx\_Enable Function](GUID-9F679C7E-5368-458F-8B6E-687FA43EE9F0.md)**  

-   **[OCMPx\_Disable Function](GUID-50983357-498D-4EC1-9C50-AF6830EC6D94.md)**  

-   **[OCMPx\_CompareValueSet Function](GUID-7C942567-27EC-488B-AB0D-23539A50E65E.md)**  

-   **[OCMPx\_CompareValueGet Function](GUID-B51CD73A-92D6-4F0A-B4D2-425537F9E9CE.md)**  

-   **[OCMPx\_CompareSecondaryValueSet Function](GUID-D9C390B2-AD51-47AE-98F9-A1AF7A0A937C.md)**  

-   **[OCMPx\_CompareSecondaryValueGet Function](GUID-D37B46F6-424F-48DC-992E-6D0BE3682FE7.md)**  

-   **[OCMPx\_CallbackRegister Function](GUID-52F9F71C-F822-4795-AB7F-EC4C408FE198.md)**  

-   **[OCMP\_CALLBACK Typedef](GUID-8A7A9812-D7DD-408E-B1FE-05EA7A3D2242.md)**  


**Parent topic:**[PIC32MK GPD GPE MCF Peripheral Libraries](GUID-A63F4C14-72E7-44D7-9C70-A48BBD41B583.md)

**Parent topic:**[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)

**Parent topic:**[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)

**Parent topic:**[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)

**Parent topic:**[PIC32MX 1XX 2XX Peripheral Libraries](GUID-DD9F92A3-1B1F-4068-A4CC-C71672A1BF54.md)

**Parent topic:**[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)

**Parent topic:**[PIC32MX 1XX 2XX 5XX Peripheral Libraries](GUID-232A3DC0-B096-45AA-9430-33A2C9BA694A.md)

**Parent topic:**[PIC32MX 330 350 370 430 450 470 Peripheral Libraries](GUID-4F5C226F-136E-4C6B-8A7F-0DF12557C7F8.md)

**Parent topic:**[PIC32MX 3XX 4XX Peripheral Libraries](GUID-2C79235F-A27F-4622-BBDA-943C35FD7940.md)

**Parent topic:**[PIC32MX 5XX 6XX 7XX Peripheral Libraries](GUID-91DC3697-58A9-4E5B-95DE-F4B08BA9C8DD.md)

**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

**Parent topic:**[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)

