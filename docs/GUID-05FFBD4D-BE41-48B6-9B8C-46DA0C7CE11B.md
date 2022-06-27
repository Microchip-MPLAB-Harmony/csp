# void GPIO\_GroupToggle\(GPIO\_GROUP group, uint32\_t mask\) Function

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-ED544C7D-3D20-4AEC-99CF-5926C66E9EC7.md)

## C

```c
void GPIO_GroupToggle(GPIO_GROUP group, uint32_t mask)
```

## Summary

Toggles the value in the given Group output register.

## Description

If the control of the GPIO pin is enabled via Group output register, then this API lets application toggle the output data of the corresponding pin.

## Precondition

The pin is enabled to be controlled via the Group output register using the GPIO\_PinGroupOutputEnable\(\) or the GPIO\_PinGroupOutputConfig\(\) APIs.

## Parameters

|Param|Description|
|-----|-----------|
|group|One of the pin groups from the enum GPIO\_GROUP|
|mask|Bit wise OR of pins whose output value needs to be toggled|

## Returns

None

## Example

```c
// Toggle the value of output pins GPIO_007, GPIO_034.
GPIO_GroupToggle(GPIO_GROUP_0, 0x10000010);
```

## Remarks

If the pin is not enabled to be controlled via the Group output register, then writing the corresponding GPIO bit in this register has no impact.

