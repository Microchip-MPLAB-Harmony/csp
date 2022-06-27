# void PCR\_PeripheralResetUnLock \(void\) Function

**Parent topic:**[Power, Clock and Reset \(PCR\) module](GUID-5F4E8EE0-D3FB-41D1-A116-D73324623BD8.md)

## C

```c
void PCR_PeripheralResetUnLock (void)
```

## Summary

Unlocks the peripheral reset enable register.

## Description

Unlocks the Peripheral Reset Enable register, thereby application can reset any peripheral by writing to the Peripheral Reset Enable register.

## Precondition

None

## Parameters

None

## Returns

None

## Example

```c
PCR_PeripheralResetUnLock();
```

## Remarks

None

