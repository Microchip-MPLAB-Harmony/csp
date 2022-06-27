# MCSPIx\_IsTransmitterBusy Function

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c

/* x = MCSPI instance number */

/* MCSPI master (blocking) mode */

bool MCSPIx_IsTransmitterBusy (void):
```

## Summary

Returns transfer status of MCSPI

## Description

*MCSPI master mode*

In master mode, this function returns true if the MCSPI module is busy with a transfer. The application can use the function to check if MCSPI module is busy before calling any of the data transfer functions.

## Precondition

The MCSPIx\_Initialize\(\) should have been called once. The module should have been configured for interrupt mode operation in MCC.

## Parameters

None.

## Returns

|Param|Description|
|-----|-----------|
|*true*|Transfer is currently in progress \(in master mode\)|
|*false*|Transfer is completed \(in master mode\)|

## Example

*MCSPI master \(blocking mode\)*

```c
// The following code example demonstrates the use of the
// MCSPIx_IsTransmitterBusy() function. This example shows a blocking while
// loop.

uint8_t dataBuffer[20];

MCSPI1_Initialize();

while (MCSPI1_IsTransmitterBusy() == true)
{
    // Wait here till the transfer is done.
}

MCSPI1_Write(dataBuffer, 20);
```

## Remarks

None

