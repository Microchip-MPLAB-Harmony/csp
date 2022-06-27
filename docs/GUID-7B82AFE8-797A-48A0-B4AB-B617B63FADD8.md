# void ECIA\_GIRQBlockDisable\(ECIA\_GIRQ\_BLOCK\_NUM block\) Function

**Parent topic:**[EC Interrupt Aggregator](GUID-1ADFDDF8-20D5-420E-8D3E-6587E5F9A215.md)

## C

```c
void ECIA_GIRQBlockDisable(ECIA_GIRQ_BLOCK_NUM block)
```

## Summary

Disables the given GIRQ block

## Description

Disables the interruput generation from the given GIRQ block to NVIC

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
ECIA_GIRQBlockDisable(ECIA_GIRQ_BLOCK_NUM8);
```

## Remarks

None

