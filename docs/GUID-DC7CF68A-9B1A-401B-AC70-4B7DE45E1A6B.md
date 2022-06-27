# NVMCTRL\_SmartEEPROM\_IsBusy Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-BDDBCD3E-039E-4AB8-86D1-04EEA8A6AE67.md)

## C

```c
bool NVMCTRL_SmartEEPROM_IsBusy( void )
```

## Summary

Checks whether SmartEEPROM is ready to perform next command.

## Description

This function should be called to check for module readiness before initiating any SmartEEPROM command. This function can be used as an alternative to the callback function. In that, the application can call this function periodically to check for operation completion instead of using a callback.

## Precondition

None.

## Parameters

None

## Returns

*true* - SmartEEPROM is busy.

*false* - SmartEEPROM is ready for a new operation.

## Example

```c
uint32_t * SMART_EEPROM32 = (uint32_t *)SEEPROM_ADDR;

while(NVMCTRL_SmartEEPROM_IsBusy());

SMART_EEPROM32[0] = 0x11223344;

```

## Remarks

None.

