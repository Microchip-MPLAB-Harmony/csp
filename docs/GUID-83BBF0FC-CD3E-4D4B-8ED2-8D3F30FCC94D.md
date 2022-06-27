# EVIC\_ExternalInterruptEnable Function

**Parent topic:**[Enhanced Vectored Interrupt Controller \(EVIC\)](GUID-F600AF2E-CCDD-4C57-B5AC-8D75DD1750C7.md)

**Parent topic:**[Enhanced Vectored Interrupt Controller \(EVIC\)](GUID-F73A6EB5-AB84-4109-9378-DBC108AD5B30.md)

## C

```c
void EVIC_ExternalInterruptEnable( EXTERNAL_INT_PIN extIntPin );
```

## Summary

Enables external interrupt on selected external interrupt pins.

## Description

This function enables external interrupt on selected external interrupt pins.

## Precondition

Iterrupt option for Corresponding pins must be enabled in EVIC manager.

## Parameters

|Param|Description|
|-----|-----------|
|extIntPin|One or multiple external interrupt pins ORed from the enum EXTERNAL\_INT\_PIN|

## Returns

None.

## Example

```c
// Enable external interrupt for INT1 pin
EVIC_ExternalInterruptEnable(EXTERNAL_INT_1);
```

## Remarks

None.

