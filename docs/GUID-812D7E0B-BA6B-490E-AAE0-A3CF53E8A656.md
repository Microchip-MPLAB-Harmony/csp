# GPIO\_PIN\_CALLBACK Typedef

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-ED544C7D-3D20-4AEC-99CF-5926C66E9EC7.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-58CDC504-B3EF-44BF-BCCB-7FB20301BF73.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-11B32F22-DEE1-4458-B547-5C80FDD743FA.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-FA913A9D-5DA8-49D8-878C-21D79AE2F4BC.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-24D8C0D2-04AF-4FE8-9AAB-D175C60FD3B8.md)

## C

The prototype varies based on device family. Refer to the generated header file for the actual prototype to be used.

```c
typedef void (*GPIO_PIN_CALLBACK) ( CN_PIN cnPin, uintptr_t context);
```

```c
typedef void (*GPIO_PIN_CALLBACK) ( GPIO_PIN pin, uintptr_t context);
```

## Summary

Pointer to a GPIO Pin-Event handler function.

## Description

This data type defines the required function signature for the<br />GPIO pin-event handling callback function. The client must register<br />a pointer to an event handling function whose function signature \(parameter<br />and return value types\) match the types specified by this function pointer<br />in order to receive calls back from the PLIB when a configured pin event<br />occurs.

The parameters and return values are described here and a partial example<br />implementation is provided.

## Parameters

|Param|Description|
|-----|-----------|
|cnPin|One of the CN pins from the enum CN\_PIN|
|pin|One of the IO pins from the enum GPIO\_PIN|
|context|Value identifying the context of the client that registered the event handling function|

## Returns

None.

## Example

Example of this function varies based on device family. Refer to the one which is applicable for the device being used.

```c
//A function matching this signature:
void APP_PinEventHandler(CN_PIN pin, uintptr_t context)
{
    // Do Something
}

//Is registered as follows:
GPIO_PinInterruptCallbackRegister(CN8_PIN, &APP_PinEventHandler, NULL);
```

```c
//A function matching this signature:
void APP_PinEventHandler(GPIO_PIN pin, uintptr_t context)
{
    // Do Something
}

//Is registered as follows:
GPIO_PinInterruptCallbackRegister(GPIO_PIN_RA5, &APP_PinEventHandler, NULL);
```

## Remarks

The context parameter contains the a handle to the client context, provided at the time the event handling function was registered using the GPIO\_PinInterruptCallbackRegister function. This context handle value is passed back to the client as the "context" parameter. It can be any value \(such as a pointer to the client's data\) necessary to identify the client context. The event handler function executes in the PLIB's interrupt context. It is recommended of the application to not perform process intensive or blocking operations with in this function.

