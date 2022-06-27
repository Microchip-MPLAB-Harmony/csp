# RSWDT\_Clear Function

**Parent topic:**[Reinforced Safety Watchdog Timer \(RSWDT\)](GUID-17C65C1B-EC26-4F1C-9599-EA23E3B7D00B.md)

## C

```c
void RSWDT_Clear( void )
```

## Summary

Restart the RSWDT counter.

## Description

This function is used to restart the RSWDT counter to avoid timeout reset/interrupt.

## Precondition

None

## Parameters

None.

## Returns

None.

## Example

```c
//Application loop
while(1)
{
    RSWDT_Clear();
    //user code
}
```

## Remarks

None.

