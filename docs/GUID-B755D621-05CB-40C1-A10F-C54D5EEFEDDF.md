# uint8\_t ECIA\_GIRQResultGet\(ECIA\_INT\_SOURCE int\_src\) Function

**Parent topic:**[EC Interrupt Aggregator](GUID-1ADFDDF8-20D5-420E-8D3E-6587E5F9A215.md)

## C

```c
uint8_t ECIA_GIRQResultGet(ECIA_INT_SOURCE int_src)
```

## Summary

Returns the status of the given interrupt source

## Description

Returns the status of the given interrupt source. The status is returned as 1 if both the interrupt source is active and the corresponding interrupt is enabled. The status is returned as 0 otherwise.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|int\_src|One of the interrupt source from the enum ECIA\_INT\_SOURCE|

## Returns

1 - Interrupt source is active and interrupt is enabled

0 - Interrupt source is not active or interrupt is disabled

## Example

```c
uint8_t result = ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_GPIO002)
```

## Remarks

None

