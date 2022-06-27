# PWMx\_SyncUpdateEnable Function

**Parent topic:**[Pulse Width Modulation Controller \(PWM\)](GUID-0542D909-604D-44C7-8C7C-B1FE313960D0.md)

## C

```c

/* x = PWM instance number */

void PWMx_SyncUpdateEnable (void);
```

## Summary

This sets the synchronous update unlock bit

## Description

This function sets the synchronous update unlock bit which enables<br />update of period, duty and dead-time values from double buffer register to actual register at the next<br />PWM period border.

## Precondition

PWMx\_Initialize\(\) function must have been called first for the associated instance. And new period or duty or dead-time value must have been written in a double buffer register.

## Parameters

None

## Returns

None

## Example

```c
PWM0_Initialize();
PWM0_SyncUpdateEnable();
```

## Remarks

In sync mode update method 1 \(manual update\), this function has to be called to update period, duty and dead-time values to actual register. In sync mode update method 2 \(automatic update\), this function has to be called to update only period and dead-time. Duty value update happens automatically.

