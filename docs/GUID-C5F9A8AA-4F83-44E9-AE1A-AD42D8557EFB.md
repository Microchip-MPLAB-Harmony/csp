# EIC\_NMICallbackRegister Function

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-39448E4A-BB16-4C96-8928-77A4AC964728.md)

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-CD1E7DE5-591C-47DF-AA1B-60D83752B93F.md)

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-EB8189C1-87AA-4B04-90B3-1853974192C7.md)

## C

```c
void EIC_NMICallbackRegister (EIC_NMI_CALLBACK callback, uintptr_t context);
```

## Summary

Registers the function to be called when an interrupt condition has been sensed on the NMI pin.

## Description

This function registers the callback function to be called when an interrupt<br />condition has been sensed on the NMI pin.

## Precondition

EIC\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|callback|callback function pointer. Setting this to NULL will disable the callback feature|
|context|Allows the caller to provide a context value|

## Returns

None.

## Example

```c
// Refer to the description of the EIC_NMI_CALLBACK data type for details on
// API usage.
```

## Remarks

None.

