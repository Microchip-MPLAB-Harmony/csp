# DDR\_Initialize Function

**Parent topic:**[DDR2 SDRAM Controller \(DDR\)](GUID-BB96B771-FA95-407C-9F4B-7812F53E1434.md)

## C

```c
void DDR_Initialize (void)
```

## Summary

Initializes and Enables the DDR External Memory Controller.

## Description

This function Enables the external DDR memory controller module.

## Precondition

Configure DDR module in MHC.

## Parameters

None.

## Returns

None.

## Example

```c
DDR_Initialize();
```

## Remarks

This routine must be called before any attempt to access external DDR memory. Not all features are available on all devices. Refer to the specific device data sheet to determine availability.

