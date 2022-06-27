# ADCHS\_DC\_CALLBACK Typedef

**Parent topic:**[Analog to Digital Converter \(ADCHS\)](GUID-8740EC52-3365-4B31-B19A-227EC55268DD.md)

## C

```c
typedef void (*ADCHS_DC_CALLBACK)(ADCHS_CHANNEL_NUM channel, uintptr_t context)
```

## Summary

Defines the function pointer data type and function signature for the adchs digital comparator interrupt callback function.

## Description

This data type defines the function pointer and function signature for the adchs<br />digital comparator interrupt callback function. The adchs peripheral will call back<br />the client's function with this signature when a digital comparator event occurs.

## Parameters

|Param|Description|
|-----|-----------|
|channel|Analog channel number|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

## Remarks

None.

