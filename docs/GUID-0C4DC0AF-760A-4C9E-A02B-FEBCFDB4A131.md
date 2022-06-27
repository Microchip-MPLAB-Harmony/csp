# DBGU\_WriteByte Function

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c

/* Blocking mode */

void DBGU_WriteByte( int data )
```

## Summary

Submits a byte of data to the given DBGU peripheral to transfer

## Description

This function submits a byte of data to the DBGU peripheral to transfer. This Function is available only in non-interrupt mode.

## Precondition

DBGU\_Initialize must have been called for the associated DBGU instance.

## Parameters

|Param|Description|
|-----|-----------|
|data|Data byte to be transferred|

## Returns

None

## Example

```c
char myData = 'A';

DBGU_WriteByte(myData);

```

## Remarks

None

