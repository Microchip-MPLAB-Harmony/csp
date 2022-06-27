# MCSPIx\_TransferSetup Function

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c
/* x = MCSPI instance number */

/* MCSPI master mode */
bool MCSPIx_TransferSetup(MCSPI_TRANSFER_SETUP *setup, uint32_t mcspiSourceClock);
```

## Summary

Configure MCSPI operational parameters at run time.

## Description

This function allows the application to change the MCSPI operational parameter at run time. The application can thus override the MCC defined configuration for these parameters. The parameter are specified via the MCSPI\_TRANSFER\_SETUP type setup parameter. Each member of this parameter should be initialized to the desired value. The application may need to call this function in situation where multiple MCSPI slaves are connected on the sam MCSPI bus, each with different operation parameters. This function can thus be used to setup the MCSPI Master to meet the communication needs of the slave being talked to. Calling this function will affect any ongoing communication. The application must thus ensure that there is no on-going communication on the MCSPI before calling this function.

## Precondition

MCSPI must first be initialized using MCSPIx\_Initialize\(\).

## Parameters

|Param|Description|
|-----|-----------|
|setup|Pointer to the data structure of type MCSPI\_TRANSFER\_SETUP containing the operation parameters. Each operation parameter must be specified even if the parameter does not need to change.|
|mcspiSourceClock|MCSPI peripheral clock source frequency. If configured to 0, PLIB takes the peripheral clock frequency from MCC.|

## Returns

*true* - setup was successful.

*false* - if mcspiSourceClock and MCSPI clock frequencies are such that resultant baud value is out of the possible range.

## Example

```c
MCSPI_TRANSFER_SETUP setup;
setup.clockFrequency = 1000000;
setup.clockPhase = MCSPI_CLOCK_PHASE_TRAILING_EDGE;
setup.clockPolarity = MCSPI_CLOCK_POLARITY_IDLE_LOW;
setup.dataBits = MCSPI_DATA_BITS_8;

// Assuming 30 MHz as peripheral input clock frequency
if (MCSPI1_TransferSetup (&setup, 30000000) == false)
{
    // this means setup could not be done, debug the reason.
}
```

## Remarks

The application would need to call this function only if the operational parameter need to be different than the ones configured in MCC.

