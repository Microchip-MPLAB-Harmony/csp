# HEFC\_SectorErase Function

**Parent topic:**[Harden Embedded Flash Controller \(HEFC\)](GUID-483B2DE9-95CB-4DD4-9F85-592F15C38EFA.md)

## C

```c
bool HEFC_SectorErase( uint32_t address)
```

## Summary

Erases a Sector in the FLASH.

## Description

This function is used to erase a sector \(collection of pages\).

## Precondition

Validate if HEFC controller is ready to accept new request by calling HEFC\_IsBusy\(\)

## Parameters

|Param|Description|
|-----|-----------|
|address|FLASH address to be Erased|

## Returns

Always returns true.

## Example

```c
HEFC_SectorErase( 0x10010000 );

while(HEFC_IsBusy());
```

## Remarks

Application needs to poll for busy bit or wait for callback to be called before sending next request.

