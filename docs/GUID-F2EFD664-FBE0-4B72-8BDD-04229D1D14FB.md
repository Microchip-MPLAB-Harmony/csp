# TCx\_CHy\_CompareStop Function

**Parent topic:**[Timer Counter \(TC\)](GUID-B7C79854-BBCD-49B3-9EA3-C379E6A5FCE0.md)

## C

```c
/* x = TC instance number, y= channel number */
void TCx_CHy_CompareStop ( void )
```

## Summary

Stops the given TC channel counter in compare mode.

## Description

This function stops the clock and thus counter of associated channel, freezing the associated waveform generation.

## Precondition

TCx\_CHy\_CompareInitialize function must have been called first for the given channel.

## Parameters

None.

## Returns

None.

## Example

```c
TC0_CH1_CompareInitialize();
TC0_CH1_CompareStart();
// Generate waveform a long as desired, then...
TC0_CH1_CompareStop();
```

## Remarks

None

