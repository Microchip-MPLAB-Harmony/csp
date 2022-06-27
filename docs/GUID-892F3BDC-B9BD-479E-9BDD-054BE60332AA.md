# NVMCTRL\_DATA\_FLASH\_PageWrite Function

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-A30BB89B-1FD8-4F1A-B3AC-83992F5EFDFF.md)

## C

```c
bool NVMCTRL_DATA_FLASH_PageWrite( uint32_t* data, uint32_t address )
```

## Summary

Writes one page of data to given DATA\_FLASH address.

## Description

This function will write one page of data to the DATA\_FLASH address specified by the address parameter. The size of the input buffer should be one NVM page. The address should be aligned on a page boundary. Unlike the NVMCTRL\_PageWrite function, calling this function will not cause the CPU execution to stall. If the interrupt operation was enabled and if a callback was registered, then the callback function will be called. The NVMCTRL\_IsBusy\(\) function can be used to poll for completion of the operation.

The application should ensure that there are no other operations in progress before calling this function. This can be checked by calling the NVMCTRL\_IsBusy\(\) function. This function is blocking if the library was generated \(in MHC\) with the interrupt option disabled. If blocking, the function will exit only after write operation has completed.

This function is not blocking if the library was generated with the interrupt option enabled. In this mode, the function initiates the operation and then exits. The application can either register a callback function or call the NVMCTRL\_IsBusy\(\) function periodically to check for completion of the operation. Once the operation is complete, the NVMCTRL\_ErrorGet\(\) function can be called to check operation success.

## Precondition

The NVMCTRL\_Initialize\(\) function should have been called once. Also validate if NVM controller is ready to accept new request by calling NVMCTRL\_IsBusy\(\).

The row containing the page should be erased before any page in that row can be written. The size of the DATA\_FLASH memory should have been configured in the NVM User Configuration.

## Parameters

|Param|Description|
|-----|-----------|
|address|Data Flash address to be modified.|
|data|pointer to data buffer.|

## Returns

Always returns true.

## Example

```c
// This code snippet shows how the NVMCTRL_DATA_FLASH_PageWrite function is
// called and how the NVMCTRL_IsBusy function is used to poll for
// completion. This assumes the library was generated for interrupt (and
// hence non-blocking) operation.

NVMCTRL_Initialize();

// Erase the row. This will erase all the pages in the row.
NVMCTRL_DATA_FLASH_RowErase(DATA_FLASH_ROW_ADDRESS);
while(NVMCTRL_IsBusy());

// Now write the page.
NVMCTRL_DATA_FLASH_PageWrite((uint32_t *)buffer, DATA_FLASH_PAGE_ADDRESS);
while(NVMCTRL_IsBusy());

if(NVMCTRL_ErrorGet() == NVMCTRL_ERROR_NONE)
{
    // Operation was successful.
}
```

## Remarks

None.

