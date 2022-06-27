# EIC\_InterruptEnable Function

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-39448E4A-BB16-4C96-8928-77A4AC964728.md)

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-CD1E7DE5-591C-47DF-AA1B-60D83752B93F.md)

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-0FA8D568-78B0-478D-8936-46B273757F9E.md)

**Parent topic:**[External Interrupt Controller \(EIC\)](GUID-EB8189C1-87AA-4B04-90B3-1853974192C7.md)

## C

```c
void EIC_InterruptEnable (EIC_PIN pin)
```

## Summary

Enable external interrupt on the specified pin.

## Description

This function enables interrupt generation on the specified external interrupt pin.

## Precondition

EIC\_Initialize\(\) function must have been called

## Parameters

|Param|Description|
|-----|-----------|
|pin|EIC Pin number|

## Returns

None

## Example

```c
EIC_InterruptEnable(EIC_PIN_3);
```

## Remarks

None.

