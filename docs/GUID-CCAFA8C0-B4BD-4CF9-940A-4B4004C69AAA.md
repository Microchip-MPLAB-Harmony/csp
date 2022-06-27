# NVMCTRL\_RWWEEPROM\_RowErase Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-66187F2C-08F3-4218-B768-FD2C65ECCC20.md)

## C

```c
bool NVMCTRL_RWWEEPROM_RowErase( uint32_t address)
```

## Summary

Erases a Row in the RWWEEPROM.

## Description

This function will erase one row in RWWEEPROM. The address of the row to be erased is specified by the address parameter. This address can be any address in the row. Unlike the NVMCTRL\_RowErase\(\) function, calling this function will not cause the CPU execution to stall. If the interrupt operation was enabled and if a callback was registered, then the callback function will be called. The NVMCTRL\_IsBusy\(\) function can be used to poll for completion of the operation.

The application should ensure that there are no other operations in progress before calling this function. This function is blocking if the library was generated \(in MHC\) with the interrupt option disabled. If blocking, the function will exit only after write operation has completed.

This function is not blocking if the library was generated with the interrupt option enabled. In this mode, the function initiates the operation and then exits. The application can either register a callback function or call the NVMCTRL\_IsBusy\(\) function periodically to check for completion of the operation. Once the operation is complete, the NVMCTRL\_ErrorGet\(\) function can be called to check operation success. Erasing a row will erase all the contents of all the pages in the row.

## Precondition

The NVMCTRL\_Initialize\(\) function should have been called once. Also validate if NVM controller is ready to accept new request by calling NVMCTRL\_IsBusy\(\). The size of the RWWEEPROM memory should have been configured in the NVM User Configuration.

## Parameters

|Param|Description|
|-----|-----------|
|address|Any address in the row to be erased.|

## Returns

Always returns true.

## Example

```c
// This code snippet shows how the NVMCTRL_RWWEEPROM_RowErase function is
// called to erase the row at locatioin SOME_RWWEEPROM_ROW.

NVMCTRL_Initialize();

// Erase the row. This will erase all the pages in the row.
NVMCTRL_RWWEEPROM_RowErase(SOME_RWWEEPROM_ROW);
while(NVMCTRL_IsBusy());

if(NVMCTRL_ErrorGet() == NVMCTRL_ERROR_NONE)
{
    // Operation was successful.
}

```

## Remarks

Erasing the row erases all pages in the row.

