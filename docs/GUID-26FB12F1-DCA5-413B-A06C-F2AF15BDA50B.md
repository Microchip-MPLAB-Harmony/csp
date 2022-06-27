# SDMMCx\_IsCmdLineBusy Function

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-670F0003-D51D-457F-BF15-845C30D30C12.md)

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-9384AD3C-4E33-479E-B7BB-005772421CB2.md)

## C

```c

/* x = SDMMC instance number */

bool SDMMCx_IsCmdLineBusy ( void )
```

## Summary

Returns the status of the command line.

## Description

This function returns the state of the command line. If the command line is busy,<br />the function returns true; false otherwise. The status of the command line must<br />be checked before issuing a new command.

## Precondition

SDMMCx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

None.

## Returns

*true* - If the command line is busy.

*false* - If the command line is ready.

## Example

```c
if (SDMMC1_IsCmdLineBusy() == false)
{
    // Command line is free. Transmit a new command.
}
```

## Remarks

None.

