# Low Power Asynchronous Receiver \(RXLP\)

The Low Power Asynchronous Receiver \(RXLP\) is a low-power UART with a slow clock. It works only in Receive mode. It features a Receive Data \(RXD\) pin that can be used to wake up the system. The wakeup occurs only on data matching—expected data can be a single value, two values, or a range of values. The RXLP operates on a slow clock domain to reduce power consumption.

**Using The Library**

The following example demonstrates the waking of the processor using RXLP. UART transmitter is connected to RXD pin of the processor. RXLP is initialized as part of SYS\_Initialize\(\) API call. Application is configured such that the processor asserts SHDWN signal upon a key press. When . It can then be woken up by sending a character using the UART transmitter connected to the RXD pin.

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

Low Power Asynchronous Receiver peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|RXLP\_Initialize|Initialize the RXLP|

-   **[RXLP\_Initialize Function](GUID-F49ECDC1-11A5-431E-8A2E-6ACD5EFBBD97.md)**  


**Parent topic:**[SAM A5D2 Peripheral Libraries](GUID-F6605EDC-FC71-4081-8560-0C1681C1FA8D.md)

