# Non-Volatile Memory Controller \(NVMCTRL\)

The Non-Volatile Memory \(NVM\) module provides an interface to the device's Non-Volatile Memory controller, so that memory pages can be written, read, erased, and reconfigured in a standardized manner.

**Using The Library**

The main Flash memory can not be read while it is being erased or written, the CPU is stalled during the entire operation.

-   All functions that modify the main Flash can be run from RAM memory to avoid CPU stall while main main Flash is being erased or written.

-   Some devices has the Flash region that support read-while-write feature, it is called Data Flash. The user could execute code from main Flash while the the Data Flash is being erased or written.


The FLASH memory is divided into a number of physical rows, each containing four identically sized flash pages. Pages may be read or written to individually, however pages must be erased before being reprogrammed and the smallest granularity available for erasure is one single row.

NVM APIs are implemented to be non-blocking, the API will return immediately unless stalled by Flash operation. The user application can either use polling or callback method to indicate the transfer status.

-   With polling, the application will need to continuously check if the flash operation is completed.

-   With callback, the registered callback function will be called once the flash operation is completed. This means the application do not have to poll continuously.


Here is an example code to erase a row and program a page of memory using polling method

```c
// Define a constant array in Flash.
// It must be aligned to row boundary and size has to be in multiple of rows
const uint8_t nvm_user_start_address[NVMCTRL_FLASH_ROWSIZE] __attribute__((aligned(NVMCTRL_FLASH_ROWSIZE),keep,externally_visible,space(prog)))= {0};

void populate_buffer(uint8_t* data)
{
    int i = 0;

    for (i = 0; i < (NVMCTRL_FLASH_PAGESIZE); i++)
    {
        *(data + i) = i;
    }
}

int main (void)
{
    uint8_t pageBuffer[NVMCTRL_FLASH_PAGESIZE] = {0};

    /*Populate pageBuffer to programmed*/
    populate_buffer(pageBuffer);

    while(NVMCTRL_IsBusy());

    /* Erase the row */
    NVMCTRL_RowErase((uint32_t)nvm_user_start_address);

    /* Wait for row erase  to complete */
    while(NVMCTRL_IsBusy());

    /* Program a page of data */
    NVMCTRL_PageWrite((uint32_t *)pageBuffer, (uint32_t)nvm_user_start_address);

    /* Wait for page program to compete */
    while(NVMCTRL_IsBusy());
}
```

**Library Interface**

Non-Volatile Memory Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|NVMCTRL\_Initialize|Initializes given instance of the NVMCTRL peripheral|
|NVMCTRL\_Read|Reads length number of bytes from a given address in FLASH memory|
|NVMCTRL\_PageWrite|Writes one page of data to given NVM address|
|NVMCTRL\_RowErase|Erases a Row in the NVM|
|NVMCTRL\_ErrorGet|Returns the error state of NVM controller|
|NVMCTRL\_IsBusy|Returns the current status of NVM controller|
|NVMCTRL\_RegionLock|Locks a NVMCTRL region|
|NVMCTRL\_RegionUnlock|Unlocks a NVM region|
|NVMCTRL\_DATA\_FLASH\_Read|Reads length number of bytes from a given address in Data FLASH memory|
|NVMCTRL\_DATA\_FLASH\_PageWrite|Writes one page of data to given DATA\_FLASH address|
|NVMCTRL\_DATA\_FLASH\_RowErase|Erases a Row in the DATA\_FLASH|
|NVMCTRL\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the operation is complete|
|NVMCTRL\_CacheInvalidate|Invalidates all cache lines|
|NVMCTRL\_PageBufferWrite|Writes data to the internal buffer of NVM known as the page buffer|
|NVMCTRL\_PageBufferCommit|Commits the data present in NVM internal page buffer to flash memory|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|NVMCTRL\_FLASH\_START\_ADDRESS|Macro|Defines the start address of NVMCTRL Flash|
|NVMCTRL\_FLASH\_SIZE|Macro|Defines the size \(in bytes\) of Flash|
|NVMCTRL\_FLASH\_PAGESIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL Page|
|NVMCTRL\_FLASH\_ROWSIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL Row|
|NVMCTRL\_DATA\_FLASH\_START\_ADDRESS|Macro|Defines the start address of NVMCTRL DATA\_FLASH|
|NVMCTRL\_DATA\_FLASH\_SIZE|Macro|Defines the size \(in bytes\) of DATA\_FLASH|
|NVMCTRL\_DATA\_FLASH\_PAGESIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL DATA\_FLASH Page|
|NVMCTRL\_DATA\_FLASH\_ROWSIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL DATA\_FLASH Row|
|NVMCTRL\_ERROR|Enum|Defines the NVMCTRL Error Type|
|NVMCTRL\_CALLBACK|Typedef|Defines the data type and function signature for the NVMCTRL peripheral callback function|

-   **[NVMCTRL\_Initialize Function](GUID-97BB70E9-D9BD-42E8-9C10-D891AC78410A.md)**  

-   **[NVMCTRL\_Read Function](GUID-4E0C86AB-BB30-4AAB-B9EE-D29946742470.md)**  

-   **[NVMCTRL\_PageWrite Function](GUID-33E14272-58A7-44F6-AA3F-CC314B38E515.md)**  

-   **[NVMCTRL\_RowErase Function](GUID-B4D142FE-2252-44FA-9C23-C871374B29A9.md)**  

-   **[NVMCTRL\_ErrorGet Function](GUID-13B4188B-86C2-4395-BAFC-8402E072B0CF.md)**  

-   **[NVMCTRL\_IsBusy Function](GUID-0698B77C-4D56-4951-8150-E6209DDF8D27.md)**  

-   **[NVMCTRL\_RegionLock Function](GUID-4A8274D6-516E-42F3-A508-0EE92C422D60.md)**  

-   **[NVMCTRL\_RegionUnlock Function](GUID-A2F63586-6CFE-4B65-B178-21EE07261A8C.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_Read Function](GUID-E13F7C80-9B06-4995-AFFD-422E11EE6398.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_PageWrite Function](GUID-892F3BDC-B9BD-479E-9BDD-054BE60332AA.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_RowErase Function](GUID-8D3B20DB-40D5-45A5-8049-AE2D7318D182.md)**  

-   **[NVMCTRL\_CallbackRegister Function](GUID-5127A98A-35CE-44D3-BE8A-770A5577EE0B.md)**  

-   **[NVMCTRL\_CacheInvalidate Function](GUID-10C13D36-C66F-4973-AE36-4FDD0344B436.md)**  

-   **[NVMCTRL\_PageBufferWrite Function](GUID-F47D4A31-F6F2-47DD-9803-4E8D3CE52C60.md)**  

-   **[NVMCTRL\_PageBufferCommit Function](GUID-F5552518-2218-41AE-BD7F-7E5AD22353F7.md)**  

-   **[NVMCTRL\_FLASH\_START\_ADDRESS Macro](GUID-C723F312-A1A1-486A-A7D5-5D9A722172C1.md)**  

-   **[NVMCTRL\_FLASH\_SIZE Macro](GUID-85881273-FA8F-441F-94BE-ABA943C5FFED.md)**  

-   **[NVMCTRL\_FLASH\_PAGESIZE Macro](GUID-AB283273-C634-4FB4-B450-F65D15349373.md)**  

-   **[NVMCTRL\_FLASH\_ROWSIZE Macro](GUID-AA16FF87-3E1B-4A03-9484-887C60E839D9.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_START\_ADDRESS Macro](GUID-7DBF182F-0987-4A3A-9760-1B13A2DB461F.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_SIZE Macro](GUID-B52FFC71-6989-480B-A3F4-EA74899C50AA.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_PAGESIZE Macro](GUID-226A8801-F1E4-4534-900A-CCEAAC5C0403.md)**  

-   **[NVMCTRL\_DATA\_FLASH\_ROWSIZE Macro](GUID-F509EEB7-7371-4448-9BB6-7B727C54344B.md)**  

-   **[NVMCTRL\_ERROR Macros](GUID-C25ED0D0-15F7-4BEC-9D8F-7D6B3F033505.md)**  

-   **[NVMCTRL\_CALLBACK Typedef](GUID-1F58B2C0-71DF-44BB-9170-583C52565787.md)**  


**Parent topic:**[PIC32CM JH00 JH01 Peripheral Libraries](GUID-05924E45-D6B3-4F33-A5EA-9B080FC421D8.md)

**Parent topic:**[PIC32CM MC00 Peripheral Libraries](GUID-ADF45DC0-B32C-4D1F-9332-59EC0DF5097E.md)

