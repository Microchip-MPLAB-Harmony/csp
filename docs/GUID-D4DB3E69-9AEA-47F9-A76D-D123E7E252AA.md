# Shutdown Controller \(SHDWC\)

The Shutdown Controller asserts the SHUTDOWN output pin and performs wakeup detection on debounced input lines.

It has the following Embedded Characteristics:

-   Shutdown Logic

    -   Software Assertion of the Shutdown Output Pin \(SHDN\)

    -   Programmable deassertion from the PIOBU, WKUP Input Pins

-   Wakeup Logic

    -   Programmable Assertion from the PIOBU, WKUP Input Pins, and Internal Wakeup Event from RTC, RXLP, ACC, Security Module


**Using The Library**

Shutdown peripheral library can be used to:

-   Configure the wakeup events for the MPU

-   Software assert the SHDN signal to indicate that the MPU needs to be shutdown. A typical application connects the pin SHDN to the shutdown input of the DC/DC Converter providing the main power supplies of the system, and especially VDDCORE and/or VDDIO.

-   Get the event that caused the MPU to wake up


The following program demonstrates assertion of the SHDN signal on pressing of a switch connected to the PIO.The program normally toggles an LED, and upon pressing the switch the SHDN signal is asserted. This signal,if connected to the external PMIC, would then be used to manage the power to the MPU.

```c
void switchHandler( PIO_PIN pin, uintptr_t context)
{
    SHDWC_Shutdown();
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    PIO_PinInterruptCallbackRegister(SWITCH_PIN, switchHandler, 0);
    PIO_PinInterruptEnable(SWITCH_PIN);

    while ( true )
    {
        PIT_DelayMs(500);
        LED_Toggle();
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}
```

**Library Interface**

Shutdown Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|SHDWC\_Initialize|Initialize shutdown controller|
|SHDWC\_Shutdown|Assert the shutdown signal|
|SHDWC\_GetWakeup|Read and clear the status register|

-   **[SHDWC\_Initialize Function](GUID-418F36B2-4893-4492-8C51-9D3BB02B41C0.md)**  

-   **[SHDWC\_Shutdown Function](GUID-29C2735C-4D6B-409C-BF54-5C84BD515EE9.md)**  

-   **[SHDWC\_GetWakeup Function](GUID-0CDB2D57-03AC-41BC-8F06-D3B5E1D18F34.md)**  


**Parent topic:**[SAM 9X60 Peripheral Libraries](GUID-CCAAC7F0-6BA8-4630-91AE-69718D188CBF.md)

**Parent topic:**[SAM 9X7 Peripheral Libraries](GUID-FB6741AA-355E-483F-9727-37728953D583.md)

**Parent topic:**[SAM A5D2 Peripheral Libraries](GUID-F6605EDC-FC71-4081-8560-0C1681C1FA8D.md)

**Parent topic:**[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)

