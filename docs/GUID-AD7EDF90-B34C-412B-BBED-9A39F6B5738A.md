# LCDCx\_SetHorizontalFrontPorchWidth Function

**Parent topic:**[LCD Controller \(LCDC\)](GUID-6C399A67-3956-464B-9055-02C390FC3228.md)

## C

```c
// x - Instance of the LCDC peripheral

void LCDCx_SetHorizontalFrontPorchWidth(uint16_t value)
```

## Summary

Sets HSYNC front porch width, give in number of pixel clocks

## Description

Number of pixel clock cycles inserted at the end of the active line

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|value|the 16-bit porch width, must be greater than 1|

## Returns

None

## Remarks

None

