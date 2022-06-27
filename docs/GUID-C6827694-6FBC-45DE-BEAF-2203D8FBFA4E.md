# XDMACn\_Initialize Function

**Parent topic:**[Extensible DMA Controller \(XDMAC\)](GUID-C2B02311-0F9A-41E7-92B8-C2FEEBDFE755.md)

## C

```c
// n is instance of the peripheral and it is applicable only for devices having multiple instances of the peripheral.
void XDMACn_Initialize( void )
```

## Summary

Initializes the XDMAC controller of the device.

## Description

This function initializes the XDMAC controller of the device as configured<br />by the user from within the XDMAC manager of MCC.

## Precondition

None.

## Parameters

None.

## Returns

None.

## Example

```c
XDMAC_Initialize();
```

## Remarks

Stops the XDMAC controller if it was already running and re-initializes it.

