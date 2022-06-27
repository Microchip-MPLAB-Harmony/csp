# FREQM\_CallbackRegister Function

**Parent topic:**[Frequency Meter \(FREQM\)](GUID-53DC3148-AECB-4E2B-B44D-152A975A542B.md)

## C

```c
void FREQM_CallbackRegister(FREQM_CALLBACK freqmcallback, uintptr_t context)
```

## Summary

Allows application to register a callback function.

## Description

This function allows the application to register a callback function that will be called when a frequency measurement operation has completed. The callback feature is only available if the Interrupt operation in the GUI was enabled. If a callback mechanism is desired, then a callback function should be registerd via this function before starting a frequency measurement. The application can read the measured frequency value and the check for errors in the callback function. Calling this function at any time with callback function as NULL will disable the callback feature.

## Precondition

The FREQM\_Initialize function must have been called. Interrupt option in MHC should have been enabled.

## Parameters

|Param|Description|
|-----|-----------|
|callBack|Pointer to an application callback function|
|context|The value of parameter will be passed back to the applicationunchanged, when the callback function is called. It can be used to identify any application specific data object that identifies the instance of the client module \(for example, it may be a pointer to the client modules state structure\)|

## Returns

None.

## Example

```c
FREQM_ERROR errorValue = FREQM_ERROR_NONE;
uint32_t measuredFrequency = 0;

void FREQMCallbackFunction(uintptr_t contextHandle)
{
    if ( FREQM_ERROR_OVERFLOW == FREQM_ErrorGet())
    {
        // indication of the overflow condition
    }
    else
    {
        measuredFrequency = FREQM_FrequencyGet();
    }
}

FREQM_Initialize();
FREQM_CallbackRegister(FREQMCallbackFunction, NULL);
FREQM_MeasurementStart();
```

## Remarks

The callback mechanism allows the application to implement an event based interaction with the library. The application can altenatively use the FREQM\_IsBusy function to implement a polling based logic.

