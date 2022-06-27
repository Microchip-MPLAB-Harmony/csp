# LCDCx\_SetBlenderDMALayerEnable Function

**Parent topic:**[LCD Controller \(LCDC\)](GUID-6C399A67-3956-464B-9055-02C390FC3228.md)

## C

```c
// x - Instance of the LCDC peripheral

void LCDCx_SetBlenderDMALayerEnable(LCDCx_LAYER_ID layer, bool enable)
```

## Summary

Enables/disables the blender DMA channel

## Description

None

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|layer|the target layer|
|enable|if true, default color is used on the layer if false, DMA channel retrieves pixels from memory|

## Returns

None

## Remarks

Only OVR1, OVR2 and HEO layers are supported

