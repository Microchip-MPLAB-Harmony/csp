# Non-Volatile Memory Controller \(NVMCTRL\)

The Non-Volatile Memory \(NVM\) module provides an interface to the device's Non-Volatile Memory controller, so that memory pages can be written, read, erased, and reconfigured in a standardized manner.

**Using The Library**

The main Flash memory can not be read while it is being erased or written, the CPU is stalled during the entire operation.

-   All functions that modify the main Flash can be run from RAM memory to avoid CPU stall while main main Flash is being erased or written.


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
|NVMCTRL\_RegionUnlock|Unlocks a NVMCTRL region|
|NVMCTRL\_SecureRegionLock|Locks a NVMCTRL secure region|
|NVMCTRL\_SecureRegionUnlock|Unlocks a NVMCTRL secure region|
|NVMCTRL\_DataScrambleEnable|Enable or Disable data scrambling of the Secure Data Flash|
|NVMCTRL\_DataScrambleKeySet|Sets the key for data scrambling of the Secure Data Flash|
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
|NVMCTRL\_ERROR|Enum|Defines the NVMCTRL Error Type|
|NVMCTRL\_MEMORY\_REGION|Enum|Defines the NVMCTRL Memory Region|
|NVMCTRL\_SECURE\_MEMORY\_REGION|Enum|Defines the NVMCTRL Secure Memory Region|
|NVMCTRL\_CALLBACK|Typedef|Defines the data type and function signature for the NVMCTRL peripheral callback function|

-   **[NVMCTRL\_Initialize Function](GUID-97BB70E9-D9BD-42E8-9C10-D891AC78410A.md)**  

-   **[NVMCTRL\_Read Function](GUID-4E0C86AB-BB30-4AAB-B9EE-D29946742470.md)**  

-   **[NVMCTRL\_PageWrite Function](GUID-33E14272-58A7-44F6-AA3F-CC314B38E515.md)**  

-   **[NVMCTRL\_RowErase Function](GUID-B4D142FE-2252-44FA-9C23-C871374B29A9.md)**  

-   **[NVMCTRL\_ErrorGet Function](GUID-13B4188B-86C2-4395-BAFC-8402E072B0CF.md)**  

-   **[NVMCTRL\_IsBusy Function](GUID-0698B77C-4D56-4951-8150-E6209DDF8D27.md)**  

-   **[NVMCTRL\_RegionLock Function](GUID-4A8274D6-516E-42F3-A508-0EE92C422D60.md)**  

-   **[NVMCTRL\_RegionUnlock Function](GUID-A2F63586-6CFE-4B65-B178-21EE07261A8C.md)**  

-   **[NVMCTRL\_SecureRegionLock Function](GUID-E3205D47-0438-4F5C-A095-499147C22A8B.md)**  

-   **[NVMCTRL\_SecureRegionUnlock Function](GUID-F8CDCFC7-7192-45AD-AF76-4EDD14713B94.md)**  

-   **[NVMCTRL\_DataScrambleEnable Function](GUID-2D90B9EA-4153-4947-8B3B-97E20CCFFF17.md)**  

-   **[NVMCTRL\_DataScrambleKeySet Function](GUID-DE992F75-89B9-439C-BA55-981C75227987.md)**  

-   **[NVMCTRL\_CallbackRegister Function](GUID-5127A98A-35CE-44D3-BE8A-770A5577EE0B.md)**  

-   **[NVMCTRL\_CacheInvalidate Function](GUID-10C13D36-C66F-4973-AE36-4FDD0344B436.md)**  

-   **[NVMCTRL\_PageBufferWrite Function](GUID-F47D4A31-F6F2-47DD-9803-4E8D3CE52C60.md)**  

-   **[NVMCTRL\_PageBufferCommit Function](GUID-F5552518-2218-41AE-BD7F-7E5AD22353F7.md)**  

-   **[NVMCTRL\_FLASH\_START\_ADDRESS Macro](GUID-C723F312-A1A1-486A-A7D5-5D9A722172C1.md)**  

-   **[NVMCTRL\_FLASH\_SIZE Macro](GUID-85881273-FA8F-441F-94BE-ABA943C5FFED.md)**  

-   **[NVMCTRL\_FLASH\_PAGESIZE Macro](GUID-AB283273-C634-4FB4-B450-F65D15349373.md)**  

-   **[NVMCTRL\_FLASH\_ROWSIZE Macro](GUID-AA16FF87-3E1B-4A03-9484-887C60E839D9.md)**  

-   **[NVMCTRL\_ERROR Macros](GUID-C25ED0D0-15F7-4BEC-9D8F-7D6B3F033505.md)**  

-   **[NVMCTRL\_MEMORY\_REGION Enum](GUID-D92B9E41-2F9B-4ACB-A0D2-8628F3A63AA7.md)**  

-   **[NVMCTRL\_SECURE\_MEMORY\_REGION Enum](GUID-7362BF95-83F6-4B12-9329-0A1B074A87C7.md)**  

-   **[NVMCTRL\_CALLBACK Typedef](GUID-1F58B2C0-71DF-44BB-9170-583C52565787.md)**  


**Parent topic:**[PIC32CM LE00 LS00 LS60 Peripheral Libraries](GUID-F80F1B47-C3E4-4803-ACB6-D30AC5EB7B45.md)

**Parent topic:**[SAM L1X Peripheral Libraries](GUID-D259BBBC-6BC2-4F69-849B-C06DF4DDD5F8.md)

