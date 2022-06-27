# TCx\_CHy\_TimerCompareSet Function

**Parent topic:**[Timer Counter \(TC\)](GUID-B7C79854-BBCD-49B3-9EA3-C379E6A5FCE0.md)

## C

```c
/* x = TC instance number, y= channel number */

/* 16 bit timer */
void TCx_CHy_TimerCompareSet ( uint16_t compare );

/* 32 bit timer */
void TCx_CHy_TimerCompareSet ( uint32_t compare );
```

## Summary

Sets the compare value of a given timer channel.

## Description

This function writes the compare value. When timer counter matches compare value, interrupt can be generated.

## Precondition

TCx\_CHy\_TimerInitialize function must have been called first for the given channel.

## Parameters

|Param|Description|
|-----|-----------|
|compare|compare value of the timer \(type is based on the bit width of timer\)|

## Returns

None.

## Example

```c
TC0_CH1_TimerInitialize();
TC0_CH1_TimerCompareSet(0x500U);
```

## Remarks

This function is available only when TC timer mode is used by SYS\_TIME module. SYS\_TIME uses compare match interrupt to generate dynamic delay.

