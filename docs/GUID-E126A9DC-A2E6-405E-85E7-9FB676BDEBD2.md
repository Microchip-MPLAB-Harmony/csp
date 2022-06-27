# Input Capture \(ICAP\)

The Input Capture module is useful in applications requiring frequency \(period\) and pulse measurement.<br />The Input Capture module captures the 16-bit or 32-bit value of the selected Time Base registers when an event occurs at the ICx pin.<br />Capture events are caused by the following:

-   Capture timer value on every edge \(rising and falling\), specified edge first

-   Prescaler capture event modes:

    -   Capture timer value on every 4th rising edge of input at ICx pin

    -   Capture timer value on every 16th rising edge of input at ICx pin<br />Each input capture channel can select between one of six 16-bit timers for the time base, or two of six 16-bit timers together to form a 32-bit timer. The selected timer can use either an internal or external clock.


**Using The Library**

In this application, a pulse signal is generated using the OCMP peripheral and is fed to the ICAP input. ICAP peripheral captures the time at every edge and displays the pulse width on the serial terminal.

```c
uint16_t capturedValue[2];
volatile uint8_t captureIndex = 0;

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    ICAP1_Enable();
    
    OCMP3_Enable();
    
    TMR2_Start();
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
        
        while(!ICAP1_CaptureStatusGet());

        capturedValue[captureIndex++] = ICAP1_CaptureBufferRead();

        if ( captureIndex > 1){
            printf("Pulse Width Count = %d\r\n",(capturedValue[1] - capturedValue[0]));
            captureIndex = 0;
        }
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
|ICAPx\_Initialize|Initializes ICAPx module of the device|
|ICAPx\_Enable|Enable function for the ICAPx peripheral|
|ICAPx\_Disable|Disable function for the ICAPx peripheral|
|ICAPx\_CaptureBufferRead|Read buffer function ICAPx peripheral|
|ICAPx\_CaptureStatusGet|Reads current state buffer not empty status|
|ICAPx\_ErrorStatusGet|Reads current state overflow status ICAPx status|
|ICAPx\_CallbackRegister|Sets the callback function for a ICAPx interrupt|
|ICAPx\_Error\_CallbackRegister|Sets the callback function for a ICAP error interrupt|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|ICAP\_STATUS\_SOURCE|Enum|Identifies ICAP status source mask|
|ICAP\_CALLBACK|Typedef|Defines the function pointer data type and function signature for the ICAPx callback function|

-   **[ICAPx\_Initialize Function](GUID-C08DD1F0-E789-47AC-8082-C11979128BEA.md)**  

-   **[ICAPx\_ErrorStatusGet Function](GUID-BE969122-77F9-4F12-BE98-80B6E2C7ACBD.md)**  

-   **[ICAPx\_Error\_CallbackRegister Function](GUID-7C990FD6-DA76-496F-8C35-3DC097D85D2A.md)**  

-   **[ICAPx\_Enable Function](GUID-491F1623-16F1-4CE7-B8DD-7085E3132541.md)**  

-   **[ICAPx\_Disable Function](GUID-C223C62B-6303-45FA-AE26-550584D7FF15.md)**  

-   **[ICAPx\_CaptureStatusGet Function](GUID-9AFBA430-DC4C-4EEA-93F5-B9F19DCED59F.md)**  

-   **[ICAPx\_CaptureBufferRead Function](GUID-C3E08EC9-5A11-477F-B4C7-005ED2D41EF9.md)**  

-   **[ICAPx\_CallbackRegister Function](GUID-DBFEB230-E999-41F5-9202-6CD60D362223.md)**  

-   **[ICAP\_STATUS\_SOURCE Enum](GUID-65EACBF2-1948-49B4-A6E0-5160E31D8457.md)**  

-   **[ICAP\_CALLBACK Typedef](GUID-08D58C39-B0D7-48D5-9CCA-DAB6D9F26CBF.md)**  


**Parent topic:**[PIC32MK GPD GPE MCF Peripheral Libraries](GUID-A63F4C14-72E7-44D7-9C70-A48BBD41B583.md)

**Parent topic:**[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)

**Parent topic:**[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)

**Parent topic:**[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)

**Parent topic:**[PIC32MX 1XX 2XX Peripheral Libraries](GUID-DD9F92A3-1B1F-4068-A4CC-C71672A1BF54.md)

**Parent topic:**[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)

**Parent topic:**[PIC32MX 330 350 370 430 450 470 Peripheral Libraries](GUID-4F5C226F-136E-4C6B-8A7F-0DF12557C7F8.md)

**Parent topic:**[PIC32MX 3XX 4XX Peripheral Libraries](GUID-2C79235F-A27F-4622-BBDA-943C35FD7940.md)

**Parent topic:**[PIC32MX 5XX 6XX 7XX Peripheral Libraries](GUID-91DC3697-58A9-4E5B-95DE-F4B08BA9C8DD.md)

**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

**Parent topic:**[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)

