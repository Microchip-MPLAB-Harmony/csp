# HSMCI\_IsDatLineBusy Function

**Parent topic:**[High Speed MultiMedia Card Interface \(HSMCI\)](GUID-E5CEFDBB-10FA-4C89-AAAF-A8ED4107A071.md)

## C

```c
bool HSMCI_IsDatLineBusy (void)
```

## Summary

Returns the status of the data line.

## Description

The status of the data line must be checked before initiating a data transfer.

## Precondition

HSMCI\_Initialize\(\) must have been called first.

## Parameters

None.

## Returns

*true* - If the data line is busy.

*false* - If the data line is ready.

## Example

```c
if (HSMCI_IsDatLineBusy() == false)
{
    // Transmit next data
}
```

## Remarks

None.

