# MCSPIx\_IsBusy Function

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c

/* x = MCSPI instance number */

/* MCSPI master (non-blocking) and slave mode */

bool MCSPIx_IsBusy (void):
```

## Summary

Returns transfer status of MCSPI

## Description

*MCSPI master mode*

In master mode, this function returns true if the MCSPI module is busy with a transfer. The application can use the function to check if MCSPI module is busy before calling any of the data transfer functions. The library does not allow a data transfer operation if another transfer operation is already in progress. This function can be used as an alternative to the callback function when the library is operating in interrupt mode thereby allowing the application to implement a synchronous interface to the library.

*MCSPI slave mode*

In slave mode, this function returns true if MCSPI slave is busy with a data transfer. The status is returned true when the MCSPI chip select is driven to active state by MCSPI master. The status is returned as false when the MCSPI chip select is driven inactive.

## Precondition

The MCSPIx\_Initialize\(\) should have been called once. The module should have been configured for interrupt mode operation in MCC.

## Parameters

None.

## Returns

|Param|Description|
|-----|-----------|
|*true*|Transfer is currently in progress \(in master mode\) or chip select is in active state when MCSPI is \(in slave mode\)|
|*false*|Transfer is completed \(in master mode\) or chip select is in inactive state \(in slave mode\)|

## Example

*MCSPI master \(non-blocking mode\) mode*

```c
// The following code example demonstrates the use of the
// MCSPIx_IsBusy() function. This example shows a blocking while
// loop. The function can also be called periodically.

uint8_t dataBuffer[20];

MCSPI1_Initialize();
MCSPI1_Write(dataBuffer, 20);

while (MCSPI1_IsBusy() == true)
{
    // Wait here till the transfer is done.
}
```

*MCSPI slave mode*

```c

while (MCSPI1_IsBusy() == true)
{
    // Wait here till the chip select is asserted by the MCSPI master
}
```

## Remarks

None

