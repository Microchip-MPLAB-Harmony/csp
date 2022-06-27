# EFC\_PageWrite Function

**Parent topic:**[Embedded Flash Controller \(EFC\)](GUID-9D57DC2E-2BF0-4D75-9E5E-FE57C7CDCC4C.md)

## C

```c
bool EFC_PageWrite( uint32_t* data, uint32_t address )
```

## Summary

Writes data of size equivalent to page size to a given FLASH address.

## Description

This function takes a 32-bit address, a pointer to data of size equivalent to page size and writes it to the given location in FLASH memory.

## Precondition

Validate if EFC controller is ready to accept new request by calling EFC\_IsBusy\(\) The Page to be written should be in Erased State.

## Parameters

|Param|Description|
|-----|-----------|
|address|FLASH address to be modified|
|data|pointer to data buffer|

## Returns

Always returns true.

## Example

```c
EFC_PageWrite( (uint32_t *) buffer, 0x500000);

while(EFC_IsBusy());
```

## Remarks

Application needs to poll for busy bit or wait for callback to be called before sending next request.

