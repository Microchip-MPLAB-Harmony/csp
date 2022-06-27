# OSC32KCTRL\_CFD\_CALLBACK Typedef

**Parent topic:**[Clock Generator \(CLOCK\)](GUID-5CA6A655-5BB0-4274-ABCD-AA8378F9B934.md)

**Parent topic:**[Clock Generator \(CLOCK\)](GUID-3658D784-AC4A-4E6F-9CDA-56F83DEAB94A.md)

**Parent topic:**[Clock Generator \(CLOCK\)](GUID-F9783829-A97E-4351-8A32-907D7430CC49.md)

**Parent topic:**[Clock Generator \(CLOCK\)](GUID-75AC227F-AB8C-4E63-B326-D1877E5AC17E.md)

## C

```c
typedef void (*OSC32KCTRL_CFD_CALLBACK)(uintptr_t context);

```

## Summary

Defines the data type and function signature for the External 32KHz Oscillator clock failure detection callback function.

## Description

This data type defines the function signature for the External 32KHz<br />Oscillator clock failure detection callback function. The External 32KHz<br />Oscillator will call back the client's function with this signature when it<br />needs to notify the client of oscillator failure. The context parameter is<br />an application defined data object specified at the time of registering the<br />callback function and is returned in the context parameter of the callback<br />function.

## Precondition

The CLOCK\_Initialize\(\) initialize function should have been called. The callback function should have been registered through OSC32KCTRL\_CallbackRegister\(\) function.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
void MyOscillatorFailureCallback (uintptr_t context )
{
    // This means the 32KHz clock has failed.
}

// Register the callback function. Specify the context as NULL.
OSC32KCTRL_CallbackRegister(MyOscillatorFailureCallback, (uintptr_t)NULL);

```

## Remarks

None.

