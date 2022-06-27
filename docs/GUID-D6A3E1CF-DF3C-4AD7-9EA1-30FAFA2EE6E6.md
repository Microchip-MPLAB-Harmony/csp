# DMA\_ChannelPatternIgnoreByteDisable Function

**Parent topic:**[Direct Memory Access Controller \(DMA\)](GUID-FC435976-A639-435D-9C8F-0A08C3D59195.md)

## C

```c
void DMA_ChannelPatternIgnoreByteDisable ( DMA_CHANNEL channel )
```

## Summary

Disable DMA channel pattern ignore byte

## Description

Disables DMA channel pattern ignore byte

## Precondition

DMA should have been initialized by calling DMA\_Initialize.

## Parameters

|Param|Description|
|-----|-----------|
|channel|DMA channel|

## Returns

None

## Example

```c
DMA_ChannelPatternIgnoreByteDisable(DMA_CHANNEL_0);
```

## Remarks

None.

