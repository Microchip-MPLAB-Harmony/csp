# DAC\_DataWrite Function

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-95143D2D-ED7E-452A-83FC-96902B1A6273.md)

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-E495F067-A363-45EF-A07D-09E16FF6E4DD.md)

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-953A92EF-D699-41B9-8D61-9D393C74DCFF.md)

## C

The prototype of this function varies based on device family. Refer to the generated header file for the actual prototype to be used.

```c
void DAC_DataWrite (DAC_CHANNEL_NUM channel, uint16_t data)
```

```c
void DAC_DataWrite(uint16_t data)
```

## Summary

Converts a Digital data to Analog value

## Description

This function converts a Digital data to Analog value.<br />The behavior of this function call will vary based on the mode selected<br />within MHC.

## Precondition

-   DAC\_Initialize must have been called.

-   The DAC\_IsReady\(\) function should have returned true.


## Parameters

|Param|Description|
|-----|-----------|
|channel|Points to DAC Channel|
|data|Digital data to be converted to Analog value.|

## Returns

None

## Example

Example of this function varies based on device family. Refer to the one which is applicable for the device being used.

```c
char myData[COUNT] = {"0xff","0x3E","0x7A","0x3F"};//COUNT is user dependent
    bool status = false;
    
    //considering count = 4
    for (uint8_t i = 0; i<4; i++)
    {
        DAC_DataWrite (DAC_CHANNEL_0, myData[i]);
    }
```

```c
if(DAC_IsReady() == true)
{
    DAC_DataWrite(data);
}
```

## Remarks

None.

