# TMRx\_CallbackRegister Function

**Parent topic:**[Timer\(TMR\)](GUID-493DD237-5B81-441C-B4FC-53AA6191C224.md)

**Parent topic:**[Timer\(TMR\)](GUID-4FD9BFDE-4887-4C40-B254-C39D2B1DE0F5.md)

## C

```c
/* x = TMR instance number */
void TMRx_CallbackRegister(TMR_CALLBACK callback_fn, uintptr_t context);
```

## Summary

Sets the callback\_fn function for an match.

## Description

This function sets the callback\_fn function that will be called when the TMR<br />match is reached.

## Precondition

TMRx\_Initialize\(\) function must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|callback\_fn|a pointer to the function to be called when match is reached|
|context|Application context|

## Returns

None.

## Example

```c
void TMR_Callback_Fn((uint32_t status, uintptr_t context);

TMR2_Initialize();
TMR2_CallbackRegister(TMR_Callback_Fn, NULL);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter.

