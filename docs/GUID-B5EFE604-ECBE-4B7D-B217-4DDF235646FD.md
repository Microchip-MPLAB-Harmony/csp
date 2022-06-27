# EVIC\_SourceIsEnabled Function

**Parent topic:**[Enhanced Vectored Interrupt Controller \(EVIC\)](GUID-F600AF2E-CCDD-4C57-B5AC-8D75DD1750C7.md)

**Parent topic:**[Enhanced Vectored Interrupt Controller \(EVIC\)](GUID-F73A6EB5-AB84-4109-9378-DBC108AD5B30.md)

## C

```c
bool EVIC_SourceIsEnabled( INT_SOURCE source )
```

## Summary

Gets the enable state of the interrupt source.

## Description

This function gets the enable state of the interrupt source.

## Precondition

EVIC\_Initialize\(\) function must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|source|One of the possible values from INT\_SOURCE.|

## Returns

-   true: If the interrupt source is enabled

-   false: If the interrupt source is disabled


## Example

```c
if(EVIC_SourceIsEnabled(INT_SOURCE_CORE_TIMER) != true)
{
    EVIC_SourceEnable(INT_SOURCE_CORE_TIMER);
}
```

## Remarks

This function implements an operation of the SourceControl feature. This feature may not be available on all devices. Please refer to the specific device data sheet to determine availability.

