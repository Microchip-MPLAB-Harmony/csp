# ADCHS\_DMA\_CALLBACK Typedef

**Parent topic:**[Analog to Digital Converter \(ADCHS\)](GUID-8740EC52-3365-4B31-B19A-227EC55268DD.md)

## C

```c
typedef void (*ADCHS_DMA_CALLBACK)(ADCHS_DMA_STATUS dmaStatus, uintptr_t context)
```

## Summary

Defines the function pointer data type and function signature for the adchs DMA interrupt callback function.

## Description

This data type defines the function pointer and function signature for the adchs DMA interrupt<br />callback function. The adchs peripheral will call back the client's<br />function with this signature at the DMA transfer.

## Parameters

|Param|Description|
|-----|-----------|
|dmaStatus|ADCHS DMA status|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

## Remarks

None.

