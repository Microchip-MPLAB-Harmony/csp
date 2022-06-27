# RTC\_BackupRegisterSet Function

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

## C

```c
void RTC_BackupRegisterSet( BACKUP_REGISTER reg, uint32_t value )
```

## Summary

Set the value for the selected Backup Register.

## Description

This function is used to set the 32-bit value for the selected Backup Register. The Backup registers can be used to store critical information when the device<br />enters the Backup Mode.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|reg|Backup register to be used|
|value|The 32-bit value to be stored|

## Returns

None.

## Example

```c
//Set Backup register 0 to 0xAA55AA55
RTC_BackupRegisterSet( BACKUP_REGISTER_0 , 0xAAA55AA55 );
```

## Remarks

This Feature may not be available on all devices. Refer to device Datasheet for more information.

