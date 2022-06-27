# PDECx\_QDECAngleGet Function

**Parent topic:**[Quadrature Decoder \(PDEC\)](GUID-6A3DDAF4-F27F-43B4-915E-750B2707BF64.md)

## C

```c
uint16_t PDECx_QDECAngleGet( void ) // x is instance of the peripheral and it is applicable only for devices having multiple instances of the peripheral.
```

## Summary

Reads the angle.

## Description

This function reads the angle by reading the angular bits in the counter register

## Precondition

PDECx\_QDECInitialize function must have been called first for the given channel.

## Parameters

None.

## Returns

Returns Position of the encoder. This consists of the angular position and revolution counter.

## Example

```c
uint16_t position;

PDEC_QDECInitialize();
PDEC_QDECStart();
position = PDEC_QDECAngleGet();
```

## Remarks

None

