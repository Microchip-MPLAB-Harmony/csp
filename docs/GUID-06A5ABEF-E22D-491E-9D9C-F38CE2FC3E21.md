# GPIO\_PortSet Function

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-58CDC504-B3EF-44BF-BCCB-7FB20301BF73.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-11B32F22-DEE1-4458-B547-5C80FDD743FA.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-FA913A9D-5DA8-49D8-878C-21D79AE2F4BC.md)

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-24D8C0D2-04AF-4FE8-9AAB-D175C60FD3B8.md)

## C

```c
void GPIO_PortSet(GPIO_PORT port, uint32_t mask)
```

## Summary

Set the selected IO pins of a port.

## Description

This function sets \(to '1'\) the selected IO pins of a port.

## Precondition

Pins of the port must be made output before setting.

## Parameters

|Param|Description|
|-----|-----------|
|port|One of the IO ports from the enum GPIO\_PORT|
|mask|A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be set.|

-   1's Will set corresponding IO pins to high \(to 1\).

-   0's Will remain unchanged.


## Returns

None.

## Example

```c
// Set RC5 and RC7 pins to 1
GPIO_PortSet(GPIO_PORT_C, 0x00A0);
```

## Remarks

If the port has less than 32-bits, unimplemented pins will be ignored. Implemented pins are Right aligned in the 32-bit value.

