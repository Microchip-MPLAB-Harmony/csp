# AFECx\_ChannelsInterruptEnable Function

**Parent topic:**[Analog Front-End Controller \(AFEC\)](GUID-89A24A8B-C8CE-48B6-9F65-764983A80D78.md)

## C

```c
void AFECx_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask) // x - Instance of the AFEC peripheral
```

## Summary

Enables the ADC interrupt sources

## Description

This function enables interrupt sources specified in channelsInterruptMask.

## Precondition

AFECx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|channelsInterruptMask|interrupt sources|

## Returns

None.

## Example

```c
AFEC0_Initialize();
AFEC0_ChannelsInterruptEnable(AFEC_INTERRUPT_EOC_0_MASK);
```

## Remarks

This function does not disable interrupts which are not included in the mask.

