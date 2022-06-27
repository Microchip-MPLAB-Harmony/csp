# CRCCUx\_Initialize Function

**Parent topic:**[Cyclic Redundancy Check Calculation Unit \(CRCCU\)](GUID-DFABB32F-CEF4-4705-8A6A-C1552576BF69.md)

## C

```c
void CRCCUx_Initialize( void ); // x - Instance of the CRCCU peripheral
```

## Summary

Initializes given instance of CRCCU peripheral.

## Description

This function initializes given instance of CRCCU peripheral of the device<br />with the values configured in MHC GUI. Once the peripheral is initialized,<br />peripheral can be used for CRC Calculation.

## Precondition

MHC GUI should be configured with the right values.

## Parameters

None.

## Returns

None.

## Example

```c
CRCCU_Initialize();
```

## Remarks

This function must be called before any other CRCCU function is called. This function should only be called once during system initialization.

