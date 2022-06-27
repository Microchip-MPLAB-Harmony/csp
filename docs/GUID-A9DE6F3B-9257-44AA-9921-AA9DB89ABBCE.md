# SPIx\_TransferSetup Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI master mode */
bool SPIx_TransferSetup(SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);
```

## Summary

Configure SPI operational parameters at run time.

## Description

This function allows the application to change the SPI operational parameter at run time. The application can thus override the MHC defined configuration for these parameters. The parameter are specified via the SPI\_TRANSFER\_SETUP type setup parameter. Each member of this parameter should be initialized to the desired value. The application may need to call this function in situation where multiple SPI slaves are connected on the sam SPI bus, each with different operation parameters. This function can thus be used to setup the SPI Master to meet the communication needs of the slave being talked to. Calling this function will affect any ongoing communication. The application must thus ensure that there is no on-going communication on the SPI before calling this function.

## Precondition

SPI must first be initialized using SPIx\_Initialize\(\).

## Parameters

|Param|Description|
|-----|-----------|
|setup|Pointer to the data structure of type SPI\_TRANSFER\_SETUP containing the operation parameters. Each operation parameter must be specified even if the parameter does not need to change.|
|spiSourceClock|SPI peripheral clock source frequency. If configured to 0, PLIB takes the peripheral clock frequency from MHC.|

## Returns

*true* - setup was successful.

*false* - if spiSourceClock and SPI clock frequencies are such that resultant baud value is out of the possible range.

## Example

```c
SPI_TRANSFER_SETUP setup;
setup.clockFrequency = 1000000;
setup.clockPhase = SPI_CLOCK_PHASE_TRAILING_EDGE;
setup.clockPolarity = SPI_CLOCK_POLARITY_IDLE_LOW;
setup.dataBits = SPI_DATA_BITS_8;

// Assuming 30 MHz as peripheral input clock frequency
if (SPI1_TransferSetup (&setup, 30000000) == false)
{
    // this means setup could not be done, debug the reason.
}
```

## Remarks

The application would need to call this function only if the operational parameter need to be different than the ones configured in MHC.

