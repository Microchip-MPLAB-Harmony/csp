# NVMCTRL\_StatusGet Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-BDDBCD3E-039E-4AB8-86D1-04EEA8A6AE67.md)

## C

```c
uint16_t NVMCTRL_StatusGet( void )
```

## Summary

Returns status conditions of NVM controller.

## Description

This function returns the content of status register.

## Precondition

None.

## Parameters

None

## Returns

Returns the content of status register.

## Example

```c
uint16_t nvm_status = 0;

nvm_status = NVMCTRL_StatusGet();

```

## Remarks

None.

