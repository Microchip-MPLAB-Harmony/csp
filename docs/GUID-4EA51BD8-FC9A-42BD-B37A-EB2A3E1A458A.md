# PMP\_AddressPortEnable Function

**Parent topic:**[\(PMP\)](GUID-DA0EF437-EF86-4341-BD1A-DA8600DBFECE.md)

## C

```c
void PMP_AddressPortEnable( uint32_t portFunctions )
```

## Summary

Enables the port lines specified as PMP address lines.

## Description

This function enables the port lines specified as PMP address lines.

## Precondition

PMP should have been initialized by calling PMP\_Initialize.

## Parameters

|Param|Description|
|-----|-----------|
|portFunctions|One of the possible values|

## Returns

None.

## Example

```c
PMP_Initialize();
PMP_AddressPortEnable(0x1);
```

## Remarks

None.

