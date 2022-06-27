# NVM\_ProgramFlashWriteProtect Function

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-A1DC59E3-704B-445E-BE7D-D91D9DADD4A1.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-04191B57-EC62-4B95-AF5B-93EDB447F6D9.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-C41BA1D1-EFF7-435E-901E-9A87AC140FE6.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-B0854C03-A30D-4E50-A3A5-948BE02E7EE8.md)

## C

The prototype of NVM\_ProgramFlashWriteProtect\(\) varies based on device family. Refer to the generated header file for the actual prototype to be used.

```c
void NVM_ProgramFlashWriteProtect( uint32_t address );

void NVM_ProgramFlashWriteProtect( uint32_t lt_address, uint32_t gte_address );
```

## Summary

Protect Program Flash Memory from Writes

## Description

**For NVM\_ProgramFlashWriteProtect\( uint32\_t address \)**

-   Protects the Program Flash Page in which the address falls and all the lower pages below it from writes. Passing address value as 0 will unlock the entire program flash memory for writes.


**For NVM\_ProgramFlashWriteProtect\( uint32\_t lt\_address, uint32\_t gte\_address \)**

-   Protects the Program pages at Flash addresses less than the "lt\_address" and the pages at Flash addresses greater than or equal to "gte\_address". Passing address value as 0 will unlock the entire program flash memory for writes.


## Precondition

None

## Parameters

|Param|Description|
|-----|-----------|
|address|24-Bit address till where the memory has to be protected from start of flash memory.|
|lt\_address|Pages at Flash addresses less than this value are write protected|
|gte\_address|Pages at Flash addresses greater than or equal to this value are write protected.|

## Returns

None.

## Example

```c
// Protects Memory locations 0x9D000000 - 0x9D001000
NVM_ProgramFlashWriteProtect(0x9D001000);

```

```c
// Protects Memory locations below 0x9D001000 and Memory locations above 0x9D003000
NVM_ProgramFlashWriteProtect(0x9D001000, 0x9D003000);

```

