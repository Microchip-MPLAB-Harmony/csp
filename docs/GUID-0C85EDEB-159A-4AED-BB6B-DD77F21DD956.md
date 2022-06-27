# FLEXCOMx\_TWI\_LastByteAckStatusGet Function

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* x = FLEXCOM instance number */

/* TWI slave mode */
FLEXCOM_TWI_SLAVE_ACK_STATUS FLEXCOMx_TWI_LastByteAckStatusGet(void)
```

## Summary

Returns the ACK status of the last byte written to the TWI master.

## Description

This function returns the ACK status of the last byte written to the TWI master.

## Precondition

FLEXCOMx\_TWI\_Initialize must have been called for the associated FLEXCOM TWI instance.

## Parameters

None.

## Returns

*FLEXCOM\_TWI\_SLAVE\_ACK\_STATUS\_RECEIVED\_ACK* - TWI master acknowledged the last byte

*FLEXCOM\_TWI\_SLAVE\_ACK\_STATUS\_RECEIVED\_NAK* - TWI master sent NAK

## Example

```c
FLEXCOM_TWI_SLAVE_ACK_STATUS ackStatus;
ackStatus = FLEXCOM1_TWI_LastByteAckStatusGet();

```

## Remarks

Since this API indicates the status of the last byte sent to the TWI master; for sending the first byte to the TWI master, the application must not call this API. Instead, the application should always send the first byte to TWI master's read request. The application would use this API when the FLEXCOM TWI slave PLIB is used in polled mode \(interrupt is disabled\).

