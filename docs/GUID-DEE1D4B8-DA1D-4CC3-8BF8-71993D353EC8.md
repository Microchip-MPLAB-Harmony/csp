# PDECx\_HALLPatternSet Function

**Parent topic:**[Quadrature Decoder \(PDEC\)](GUID-6A3DDAF4-F27F-43B4-915E-750B2707BF64.md)

## C

```c
bool PDECx_HALLPatternSet ( uint8_t pattern ) // x is instance of the peripheral and it is applicable only for devices having multiple instances of the peripheral.
```

## Summary

Writes the hall pattern.

## Description

This function writes the hall pattern in CC0 LSB.

## Precondition

PDECx\_HALLInitialize function must have been called first for the given channel.

## Parameters

|Param|Description|
|-----|-----------|
|pattern|hall pattern|

## Returns

*true* - If hall pattern set<br />*false* - If hall pattern is not set

## Example

```c
uint8_t position;

PDEC_HALLInitialize();
PDEC_HALLStart();
PDEC_HALLPatternSet(0x3);
```

## Remarks

None

