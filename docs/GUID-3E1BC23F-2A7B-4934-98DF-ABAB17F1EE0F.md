# SERCOMx\_I2C\_InterruptFlagsClear Function

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c
/* x = SERCOM instance number */

/* I2C slave in non-interrupt mode */

void SERCOMx_I2C_InterruptFlagsClear(SERCOM_I2C_SLAVE_INTFLAG intFlags)		
```

## Summary

Clears the specified SERCOM I2C slave interrupt flags.

## Description

This function clears the specified SERCOM I2C slave interrupt flags.

## Precondition

SERCOMx\_I2C\_Initialize must have been called for the associated SERCOM I2C instance.

## Parameters

|Param|Description|
|-----|-----------|
|SERCOM\_I2C\_SLAVE\_INTFLAG|Enum with possible interrupt flag values|

## Returns

None.

## Example

```c
SERCOM_I2C_SLAVE_INTFLAG intFlags;

// Read the interrupt flags set
intFlags = SERCOM0_I2C_InterruptFlagsGet();

// Add code to handle the set interrupt flags

// Clear all the interrupt flags that were set
SERCOM0_I2C_InterruptFlagsClear(intFlags);

```

## Remarks

I2C slave application would typically use this API when the SERCOM I2C slave PLIB is used in polled mode \(interrupt is disabled\).

