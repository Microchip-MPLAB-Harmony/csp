# DACC\_DataWrite Function

**Parent topic:**[Digital-to-Analog Converter Controller \(DACC\)](GUID-140A9CAD-70CC-40D6-896A-A9E9697CEDFD.md)

**Parent topic:**[Digital-to-Analog Converter Controller \(DACC\)](GUID-1355B5F9-6D7B-4092-91E4-2E2F3B5675D1.md)

## C

The prototype of this function varies based on device family. Refer to the generated header file for the actual prototype to be used.

```c
void DACC_DataWrite (DACC_CHANNEL_NUM channel, uint32_t data)
```

```c
void DACC_DataWrite(uint16_t data)
```

## Summary

Converts a Digital data to Analog value

## Description

This function converts a Digital data to Analog value.<br />The behavior of this function call will vary based on the mode selected<br />within MHC.

## Precondition

DACC\_Initialize must have been called.

## Parameters

|Param|Description|
|-----|-----------|
|channel|Points to DACC Channel|
|data|Digital data to be converted to Analog value.|

## Returns

None

## Example

Example of this function varies based on device family. Refer to the one which is applicable for the device being used.

```c
char myData[COUNT] = {"0xff","0x3E","0x7A","0x3F"};//COUNT is user
    //dependent
    bool status = false;
    
    //considering count = 4
    for (uint8_t i = 0; i<4; i++)
    {
        DACC_DataWrite (DACC_CHANNEL_0, myData[i]);
    }
```

```c
bool status = false;
DACC_ChannelSelect(DACC_CHANNEL_0);
if (true == DACC_IsReady())
{
    DACC_DataWrite (0xff);
}
else
{
    //DACC is not ready to accept new conversion request
    //User Application code
}
```

## Remarks

None.

