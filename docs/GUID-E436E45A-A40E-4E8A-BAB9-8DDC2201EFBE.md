# uint32\_t ECIA\_GIRQBlockStatusGet\(ECIA\_GIRQ\_BLOCK\_NUM block\) Function

**Parent topic:**[EC Interrupt Aggregator](GUID-1ADFDDF8-20D5-420E-8D3E-6587E5F9A215.md)

## C

```c
uint32_t ECIA_GIRQBlockStatusGet(ECIA_GIRQ_BLOCK_NUM block)
```

## Summary

Reports the status of the group GIRQ interrupt assertion to the NVIC.

## Description

Reports the status of the group GIRQ interrupt assertion to the NVIC.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|block|One of the GIRQ block number from the enum ECIA\_GIRQ\_BLOCK\_NUM|

## Returns

None

## Example

```c
uint32_t status = ECIA_GIRQBlockStatusGet(ECIA_GIRQ_BLOCK_NUM8);
```

## Remarks

None

