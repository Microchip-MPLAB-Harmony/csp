# NVMCTRL\_RWWEEPROM\_Read Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-66187F2C-08F3-4218-B768-FD2C65ECCC20.md)

## C

```c
bool NVMCTRL_RWWEEPROM_Read( uint32_t *data, uint32_t length, const uint32_t address)
```

## Summary

Reads length number of bytes from a given address in Data FLASH memory.

## Description

Reads length number of bytes from a given address in Data FLASH memory into the user buffer.

## Precondition

None

## Parameters

|Param|Description|
|-----|-----------|
|data|pointer to user data buffer|
|length|Number of bytes to read|
|address|Data FLASH address to be read from|

## Returns

Always returns true.

## Example

```c
uint8_t buffer[256];
NVMCTRL_RWWEEPROM_Read( (uint32_t *) buffer, 256, 0x20000);
```

