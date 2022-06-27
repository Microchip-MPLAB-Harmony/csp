# EFC\_RegionLock Function

**Parent topic:**[Embedded Flash Controller \(EFC\)](GUID-9D57DC2E-2BF0-4D75-9E5E-FE57C7CDCC4C.md)

## C

```c
void EFC_RegionLock(uint32_t address);
```

## Summary

Locks a Flash region.

## Description

This function is used to lock a certain region of on-chip flash. It takes in address as a parameter and locks the region associated with it.

## Precondition

Validate if EFC controller is ready to accept new request by calling EFC\_IsBusy\(\)

## Parameters

|Param|Description|
|-----|-----------|
|address|Address of the page to be locked|

## Returns

None.

## Example

```c
EFC_RegionLock(0x00500000);

while(EFC_IsBusy());
```

