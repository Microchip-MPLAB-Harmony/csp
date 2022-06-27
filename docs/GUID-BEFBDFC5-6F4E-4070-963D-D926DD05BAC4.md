# void GPIO\_PinPwrGateConfig\(GPIO\_PIN pin, GPIO\_PWRGATE pwrGate\) Function

**Parent topic:**[General Purpose I/O \(GPIO\)](GUID-ED544C7D-3D20-4AEC-99CF-5926C66E9EC7.md)

## C

```c
void GPIO_PinPwrGateConfig(GPIO_PIN pin, GPIO_PWRGATE pwrGate)
```

## Summary

Configures the power well to use for the given GPIO pin

## Description

This API lets the application configure the power well for the given GPIO pin

## Precondition

None

## Parameters

|Param|Description|
|-----|-----------|
|pin|One of the values from the enum GPIO\_PIN|
|pwrGate|One of the values from the enum GPIO\_PWRGATE|

## Returns

None

## Example

```c
GPIO_PinPwrGateConfig(GPIO_PIN_GPIO012, GPIO_PWR_VCC);
```

## Remarks

None

