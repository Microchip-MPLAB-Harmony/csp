# void PCR\_ResetEnablex \(PCR\_RESET\_ENx blockId\) Function

**Parent topic:**[Power, Clock and Reset \(PCR\) module](GUID-5F4E8EE0-D3FB-41D1-A116-D73324623BD8.md)

## C

```c

/* x = Peripheral Reset Enable Register number */

void PCR_ResetEnablex (PCR_RESET_ENx blockId)
```

## Summary

Resets the given peripheral

## Description

Resets the given peripheral

## Precondition

None

## Parameters

|Param|Description|
|-----|-----------|
|blockId|One of the peripheral block ID from the PCR\_RESET\_ENx Enum|

## Returns

None

## Example

```c
PCR_ResetEnable0(PCR_RESET_EN0_GPIO_RST_EN);
```

## Remarks

None

