# ADC\_FIFOBufferRead Function

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-FA022CD9-1025-47D5-B8BC-A27AC49112D8.md)

## C

```c
uint32_t ADC_FIFOBufferRead( uint32_t* pBuffer, uint32_t size )
```

## Summary

Returns multiple ADC conversion values from the ADC FIFO

## Description

Returns multiple ADC conversion values from the ADC FIFO.<br />Return value indicates the number of ADC results actually read from the FIFO.

## Precondition

ADCx\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|pBuffer|pointer to the application buffer to save the ADC results read from FIFO|
|size|Number of ADC results to read|

## Returns

*uint32\_t* - Actual number of ADC results read and copied to the application buffer

## Example

```c
uint32_t num_results_read;
uint32_t adc_results_buffer[4];

if (ADC_EOSStatusGet(ADC_CORE_NUM1))
{
    // ADC conversion is complete. Read the conversion result.
    
    num_results_read = ADC_FIFOBufferRead(adc_results_buffer, 4);
}
```

## Remarks

None

