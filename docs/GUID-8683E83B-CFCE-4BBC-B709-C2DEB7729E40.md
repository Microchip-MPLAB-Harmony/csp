# FLEXCOMx\_TWI\_NACKDataPhase Function

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* x = FLEXCOM instance number */

/* TWI slave mode */

void FLEXCOMx_TWI_NACKDataPhase(bool isNACKEnable)
```

## Summary

Configures the hardware to send ACK or NAK for the next byte that will be received from the TWI master

## Description

This function lets the application send ACK or NAK for the next data from the I2C master

## Precondition

FLEXCOMx\_TWI\_Initialize must have been called for the associated FLEXCOM TWI instance.

## Parameters

|Param|Description|
|-----|-----------|
|true|Send NAK to the next data from I2C master|
|false|Send ACK to the next data from I2C master|

## Returns

None

## Example

```c
// Send NAK for the next data from I2C master
FLEXCOM0_TWI_NACKDataPhase(true);
```

## Remarks

None

