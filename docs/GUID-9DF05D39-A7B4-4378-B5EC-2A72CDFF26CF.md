# EFC\_RegionUnlock Function

**Parent topic:**[Embedded Flash Controller \(EFC\)](GUID-9D57DC2E-2BF0-4D75-9E5E-FE57C7CDCC4C.md)

## C

```c
void EFC_RegionUnlock(uint32_t address);
```

## Summary

Unlocks a Flash region.

## Description

This function is used to Unlock a certain region of on-chip flash. It takes in address as a parameter and unlocks the region associated with it.

## Precondition

Validate if EFC controller is ready to accept new request by calling EFC\_IsBusy\(\)

## Parameters

|Param|Description|
|-----|-----------|
|address|Address of the page to be unlocked|

## Returns

None.

## Example

```c
EFC_RegionUnlock(0x00500000);

while(EFC_IsBusy());
```

