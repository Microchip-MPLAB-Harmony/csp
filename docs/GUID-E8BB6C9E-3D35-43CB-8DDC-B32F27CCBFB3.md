# ADC\_FIFO\_CHNID\_GET Macro

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-FA022CD9-1025-47D5-B8BC-A27AC49112D8.md)

## C

```c
#define ADC_FIFO_CHNID_GET(fifo_data)			((fifo_data & ADC_PFFDATA_PFFCHNID_Msk) >> ADC_PFFDATA_PFFCHNID_Pos)
```

## Summary

Returns the ADC channel id in the ADC FIFO data

## Description

This macro take the FIFO data as input and return the channel ID from the ADC FIFO data

## Remarks

None.

