# MCANx\_MessageRAMConfigSet Function

**Parent topic:**[Controller Area Network \(MCAN\)](GUID-C9F1E50C-1EF0-4941-A9CB-89808C7C54AF.md)

## C

```c
void MCANx_MessageRAMConfigSet(uint8_t *msgRAMConfigBaseAddress) // x - Instance of the MCAN peripheral
```

## Summary

Set the Message RAM Configuration.

## Precondition

MCANx\_Initialize must have been called for the associated MCAN instance.

## Parameters

|Param|Description|
|-----|-----------|
|msgRAMConfigBaseAddress|Pointer to application allocated buffer base address.Application must allocate buffer from non-cached contiguous memory and buffer size must be MCANx\_MESSAGE\_RAM\_CONFIG\_SIZE|

## Returns

None

## Example

```c
uint8_t messageRAMConfig[MCAN0_MESSAGE_RAM_CONFIG_SIZE]__attribute__((aligned (32))) __attribute__((__section__(".region_nocache")));
MCAN0_MessageRAMConfigSet(&messageRAMConfig);
```

## Remarks

None.

