# PIO\_PinInterruptCallbackRegister Function

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-6E00A15D-D08A-43FF-A05A-C91E7717B5DE.md)

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-CDD19539-F154-487B-A93E-CE1F75932EB8.md)

## C

```c
bool PIO_PinInterruptCallbackRegister(
PIO_PIN pin,
const PIO_PIN_CALLBACK callBack,
uintptr_t context
);
```

## Summary

Allows application to register callback for every pin.

## Description

This function allows application to register an event handling function<br />for the PLIB to call back when I/O interrupt occurs on the selected pin.

At any point if application wants to stop the callback, it can call this<br />function with "eventHandler" value as NULL.

If a pin is not configured for interrupt in Pin Manager and yet its callback<br />registration is attempted using this API, then registration doesn't happen<br />and API returns false indicating the same.

## Precondition

Corresponding pin must be configured in interrupt mode in MHC Pin Manager. The PIO\_Initialize function must have been called.

## Parameters

|Param|Description|
|-----|-----------|
|pin|One of the IO pins from the enum PIO\_PIN|
|eventHandler|Pointer to the event handler function implemented by the user|
|context|The value of parameter will be passed back to the application unchanged, when the eventHandler function is called. It can be used to identify any application specific value.|

## Returns

Callback registration status: - true: Callback was successfully registered - false: Callback was not registered

## Example

```c
if(PIO_PinInterruptCallbackRegister(PIO_PIN_PB3, &APP_PinHandler, NULL))
{
    // callback got registered
}
```

## Remarks

None.

