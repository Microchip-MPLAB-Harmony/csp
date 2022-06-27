# CCPx\_Compare16bitRBValueSet Function

**Parent topic:**[Capture/Compare/PWM \(CCP\)](GUID-615BEA57-7216-4351-87D8-94C8B0BF6E7D.md)

## C

```c
/* x = CCP instance number */

void CCPx_Compare16bitRBValueSet( uint16_t compareValue )
```

## Summary

Writes higher 16bits of compare value.

## Description

Set higher 16bits of compare value.

## Precondition

CCPx\_CompareInitialize\(\) function must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|compareValue|higher 16bits value to set for compare|

## Returns

None.

## Example

```c
uint16_t compareValue = 0x100;
CCP1_CompareInitialize();
CCP1_Compare16bitRBValueSet(compareValue);
```

## Remarks

None

