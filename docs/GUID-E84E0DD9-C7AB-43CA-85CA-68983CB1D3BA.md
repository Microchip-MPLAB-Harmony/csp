# PIO\_PortWrite Function

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-6E00A15D-D08A-43FF-A05A-C91E7717B5DE.md)

**Parent topic:**[Parallel Input/Output \(PIO\) Controller](GUID-CDD19539-F154-487B-A93E-CE1F75932EB8.md)

## C

```c
void PIO_PortWrite(PIO_PORT port, uint32_t mask, uint32_t value);
```

## Summary

Write the value on the masked I/O lines of the selected port.

## Description

This function writes the data values driven on selected output lines of the<br />selected port. Bit values in each position indicate corresponding pin<br />levels.

-   1 - Pin is driven high.

-   0 - Pin is driven low.


## Precondition

The desired pins lines of the selected port must be setup as output\(s\) in MHC Pin Manager. PIO\_Initialize\(\) must have been called.

## Parameters

|Param|Description|
|-----|-----------|
|port|One of the IO ports from the enum PIO\_PORT|
|mask|A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.|

-   1's Will write to corresponding IO pins.

-   0's Will remain unchanged. \|<br />\| value \| Value which has to be written/driven on the I/O lines of the selected port for which mask bits are '1'. Values for the corresponding mask bit '0' will be ignored.


## Returns

None.

## Example

```c
// Write binary value 0011 to the pins PC3, PC2, PC1 and PC0 respectively.
PIO_PortWrite(PIO_PORT_C, 0x0F, 0xF563D453);
```

## Remarks

If the port has less than 32-bits, unimplemented pins will be ignored. Implemented pins are Right aligned in the 32-bit value.

