# AC\_SwapInputs Function

**Parent topic:**[Analog Comparators \(AC\)](GUID-5607FF99-7728-4953-B3F7-6E93AC09581A.md)

**Parent topic:**[Analog Comparators \(AC\)](GUID-45B9C329-D2C7-4446-BE93-437006982526.md)

**Parent topic:**[Analog Comparators \(AC\)](GUID-16BFBCA4-9E85-4E87-B1D6-6D79E6DCCEA9.md)

## C

```c
void AC_SwapInputs (AC_CHANNEL channel)
```

## Summary

Swap inputs of a comparator.

## Description

This function swaps inputs of a comparator. This allows the user to measure<br />or compensate for the comparator input offset voltage.

## Precondition

AC\_Initialize must have been called for the associated AC instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel|Points to AC Channel|

## Returns

None.

## Example

```c
AC_SwapInputs (AC_CHANNEL_0);
```

## Remarks

None.

