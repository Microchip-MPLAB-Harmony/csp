# AC\_ChannelSelect Function

**Parent topic:**[Analog Comparators \(AC\)](GUID-5607FF99-7728-4953-B3F7-6E93AC09581A.md)

**Parent topic:**[Analog Comparators \(AC\)](GUID-45B9C329-D2C7-4446-BE93-437006982526.md)

**Parent topic:**[Analog Comparators \(AC\)](GUID-16BFBCA4-9E85-4E87-B1D6-6D79E6DCCEA9.md)

## C

```c
void AC_ChannelSelect( AC_CHANNEL channel_id , AC_POSINPUT positiveInput, AC_NEGINPUT negativeInput);
```

## Summary

Selects the positive and negative inputs of a channel

## Description

This function configures positive and negative input of a comparator channel.

## Precondition

AC\_Initialize must have been called for the associated AC instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel\_id|Points to AC Channel|
|positiveInput|positive input of AC channel|
|negativeInput|negative input of AC channel|

## Returns

None.

## Example

```c
AC_ChannelSelect (AC_CHANNEL_0, AC_POSINPUT_AIN0, AC_NEGINPUT_GND);
```

## Remarks

Comparator channel is disabled before changing the inputs and enabled again.

