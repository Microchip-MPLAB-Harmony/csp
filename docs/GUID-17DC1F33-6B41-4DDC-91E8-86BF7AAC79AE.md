# PMP\_MasterSend Function

**Parent topic:**[\(PMP\)](GUID-DA0EF437-EF86-4341-BD1A-DA8600DBFECE.md)

## C

```c
void PMP_MasterSend( uint32_t data )
```

## Summary

Sends the specified data in Master mode.

## Description

This function sends the specified data. The data flow is from master to<br />slave.

## Precondition

PMP should have been initialized by calling PMP\_Initialize and configured for Master mode.

## Parameters

|Param|Description|
|-----|-----------|
|data|Data to be transmitted|

## Returns

None.

## Example

```c
uint16_t data = 'a';

PMP_Initialize();
PMP_AddressSet(0x1);

if(!PMP_PortIsBusy())
{
    PMP_MasterSend(data);
}
```

## Remarks

None.

