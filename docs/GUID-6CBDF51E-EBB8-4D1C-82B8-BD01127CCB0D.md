# void GPIO\_GroupPinSet\(GPIO\_PIN pin\) Function

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-ED544C7D-3D20-4AEC-99CF-5926C66E9EC7.md)

## C

```c
void GPIO_GroupPinSet(GPIO_PIN pin)
```

## Summary

Sets the value of the given pin in the Group output register.

## Description

If the output control of the GPIO pin is enabled via Group output register, then this API lets application set the output value of the given pin to 1 using the Group output register.

## Precondition

None

## Parameters

|Param|Description|
|-----|-----------|
|pin|One of the GPIO pins from the enum GPIO\_PIN|

## Returns

None

## Example

```c
GPIO_GroupPinSet(GPIO_PIN_GPIO012);
```

## Remarks

None

