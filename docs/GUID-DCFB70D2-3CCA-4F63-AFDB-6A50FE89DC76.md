# RTC\_TIMER32\_CALLBACK Typedef

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-C95E1695-55CC-4546-9F2C-315F5C908FC1.md)

## C

```c
typedef void (*RTC_TIMER32_CALLBACK)( RTC_TIMER32_INT_MASK interruptCause, uintptr_t context );

```

## Summary

Defines the data type and function signature of the RTC 32-bit Timer Counter callback function.

## Description

This data type defines the function signature of the RTC 32-bit Timer Counter Callback function. The RTC peripheral will call back the client's function with this signature every time when the 32-bit Time Counter related event has occurred. Refer to the description of the RTC\_TIMER32\_INT\_MASK enumeration for possible events. Hardware event flags are cleared when the<br />callback function exits.

The application should register a callback function whose signature \(input arguments and return type\) must match the signature of this function. The callback function should be registered by calling the RTC\_Timer32CallbackRegister\(\) function. The callback function should be registered before starting the timer.

## Precondition

The RTC\_Initialize\(\) function should have been called to initialize the RTC peripheral. The RTC\_Timer32CallbackRegister\(\) function should have been called to register the callback function. The RTC peripheral should have been configured for 32-bit Timer Counter mode in MHC. The RTC peripheral should have been configured for Interrupt mode operation in MHC.

## Parameters

|Param|Description|
|-----|-----------|
|event|The 32-bit Timer Counter event that caused the callback function to be called. Multiple events can be active. The application should check for all events in the callback function|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

## Remarks

This callback if only available when the RTC peripheral is configured for 32-bit Timer Counter operation. The callback function will be execute in an interrupt context. Avoid calling blocking , computationally intensive or interrupt un-safe function from the callback function.

