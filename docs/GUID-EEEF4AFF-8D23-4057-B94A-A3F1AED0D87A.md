# NVMCTRL\_DisableMainFlashInterruptSource Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-BDDBCD3E-039E-4AB8-86D1-04EEA8A6AE67.md)

## C

```c
void NVMCTRL_DisableMainFlashInterruptSource(NVMCTRL_INTERRUPT0_SOURCE int_source)
```

## Summary

Disables a given interrupt source for the Flash.

## Description

There are multiple interrupt sources supported by the NVMCTRL peripheral. It supports two interrupt vectors, one for interrupts from the SmartEEPROM and another for all other interrupts of the NVMCTRL. This function disables the given interrupt for the first vector which is used by all interrupts except the ones from SmartEEPROM.

## Precondition

Interrupt option in MHC should have been enabled.

## Parameters

|Param|Description|
|-----|-----------|
|int\_source|Refer to enum NVMCTRL\_INTERRUPT0\_SOURCE for possible values.|

## Returns

None.

## Example

```c
NVMCTRL_DisableMainFlashInterruptSource(NVMCTRL_INT_LOCKE);

```

## Remarks

This API is available only if the main interrupt is enabled via the MHC tree.

