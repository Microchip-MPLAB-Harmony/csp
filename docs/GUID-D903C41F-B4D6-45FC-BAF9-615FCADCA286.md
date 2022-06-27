# EFC\_SectorErase Function

**Parent topic:**[Embedded Flash Controller \(EFC\)](GUID-9D57DC2E-2BF0-4D75-9E5E-FE57C7CDCC4C.md)

## C

```c
bool EFC_SectorErase( uint32_t address)
```

## Summary

Erases a Sector in the FLASH.

## Description

This function is used to erase a sector \(collection of pages\).

## Precondition

Validate if EFC controller is ready to accept new request by calling EFC\_IsBusy\(\)

## Parameters

|Param|Description|
|-----|-----------|
|address|FLASH address to be Erased|

## Returns

Always returns true.

## Example

```c
EFC_SectorErase(0x500000);

while(EFC_IsBusy());
```

## Remarks

Application needs to poll for busy bit or wait for callback to be called before sending next request.

