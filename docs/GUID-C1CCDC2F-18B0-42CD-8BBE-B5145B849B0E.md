# PIO\_PinSet Function

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-6E00A15D-D08A-43FF-A05A-C91E7717B5DE.md)

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-CDD19539-F154-487B-A93E-CE1F75932EB8.md)

## C

```c
void PIO_PinSet(PIO_PIN pin)
```

## Summary

Sets the selected pin.

## Description

This function drives '1' on the selected I/O line/pin.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|pin|One of the IO pins from the enum PIO\_PIN|

## Returns

None.

## Example

```c
PIO_PinSet(PIO_PIN_PB3);
```

## Remarks

None.

