# Non-Volatile Memory \(NVM\)

The Non-Volatile Memory \(NVM\) module provides an interface to the device's Non-Volatile Memory controller, so that memory pages can be written, read, erased, and reconfigured in a standardized manner.

**Using The Library**

The main Flash memory can not be read while it is being erased or written, the CPU is stalled during the entire operation. All functions that modify the main Flash can be run from RAM memory to avoid CPU stall while main main Flash is being erased or written.

The Program flash memory is divided into two Virtual regions pointing to the same physical memory location. Client can use any address from these virtual regions to perform erase/write/read operation

-   KSEG0 is cacheable region

-   KSEG1 is non-cacheable region


The program Flash array is built up of a series of rows to form a page. A page of Flash is the smallest unit of memory that can be erased at a single time. The program Flash array can be programmed in one of two ways:

-   Row programming, with 256 instruction words at a time

-   Single Double Word programming, with 2 instruction words at a time

-   Double Quad Word programming, with 8 instruction words at a time


NVM APIs are implemented to be non-blocking, the API will return immediately unless stalled by Flash operation. The user application can either use polling or callback method to indicate the transfer status.

-   With polling, the application will need to continuously check if the flash operation is completed.

-   With callback, the registered callback function will be called once the flash operation is completed. This means the application do not have to poll continuously.


Here is an example code to erase a page and program a row of memory using polling method

```c
#define APP_FLASH_ADDRESS  (NVM_FLASH_START_ADDRESS + (NVM_FLASH_SIZE / 2))

uint8_t CACHE_ALIGN rowBuffer[NVM_FLASH_ROWSIZE] = {0};

void populate_buffer(uint8_t* data)
{
    int i = 0;

    for (i = 0; i < (NVM_FLASH_ROWSIZE); i++)
    {
        *(data + i) = i;
    }
}

int main (void)
{
    /*Populate rowBuffer to programmed*/
    populate_buffer(rowBuffer);

    while(NVM_IsBusy());

    /* Erase the page */
    NVM_PageErase(APP_FLASH_ADDRESS);

    /* Wait for page erase  to complete */
    while(NVM_IsBusy());

    /* Program a row of data */
    NVM_RowWrite((uint32_t *)rowBuffer, APP_FLASH_ADDRESS);

    /* Wait for row program to compete */
    while(NVM_IsBusy());
}

```

**Library Interface**

Peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|NVM\_Initialize|Initializes given instance of the NVM peripheral|
|NVM\_Read|Reads length number of bytes from a given address in FLASH memory|
|NVM\_RowWrite|Writes one row of data to given NVM address|
|NVM\_WordWrite|Writes one Word into the Flash|
|NVM\_QuadWordWrite|Writes Four Words into the Flash|
|NVM\_PageErase|Erases a Page in the NVM|
|NVM\_ErrorGet|Returns the error state of NVM controller|
|NVM\_IsBusy|Returns the current status of NVM controller|
|NVM\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the operation is complete|
|NVM\_ProgramFlashWriteProtect|Protect Program Flash Memory from Writes|
|NVM\_ProgramFlashWriteProtectLock|Disable Writes to Program Flash Write Protect Lock register|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|NVM\_ERROR|Enum|Defines the NVM Error Type|
|NVM\_CALLBACK|Typedef|Defines the data type and function signature for the NVM peripheral callback function|

-   **[NVM\_Initialize Function](GUID-D1578E62-CDD7-4417-B37D-E0CCE8D1741E.md)**  

-   **[NVM\_Read Function](GUID-67000342-168A-4F98-BEE2-7861B3B5B236.md)**  

-   **[NVM\_RowWrite Function](GUID-33942AE6-41CC-45A7-B950-0E2A2E0F5929.md)**  

-   **[NVM\_QuadWordWrite Function](GUID-7BDCAEDC-D98E-446A-8AA7-59493FD59754.md)**  

-   **[NVM\_PageErase Function](GUID-D3B337A4-DB43-4F6C-95D4-D4950603ACCF.md)**  

-   **[NVM\_ErrorGet Function](GUID-B17E6D26-9C9E-48EF-9274-16AB5B9EE5FA.md)**  

-   **[NVM\_IsBusy Function](GUID-05C82636-CFAE-4469-9486-47026C2E3400.md)**  

-   **[NVM\_CallbackRegister Function](GUID-7029F6B0-181B-4194-AE7D-95ECDFDE7F14.md)**  

-   **[NVM\_ProgramFlashWriteProtect Function](GUID-42E4ABAB-6C18-48CF-9AE5-6ECED1E3F459.md)**  

-   **[NVM\_ProgramFlashWriteProtectLock Function](GUID-3B1F1BC5-85B0-4664-A609-86CFEED65D01.md)**  

-   **[NVM\_ERROR Enum](GUID-7FF0409F-92AB-458A-AF5F-B1C5B6D07D3C.md)**  

-   **[NVM\_CALLBACK Typedef](GUID-717D16DB-4555-4A5F-9487-230CB90044B1.md)**  


**Parent topic:**[PIC32CX BZ2 WBZ45 Peripheral Libraries](GUID-3D519D00-FDEE-4A3E-9EF7-20F335E64CEE.md)

**Parent topic:**[PIC32CX BZ3 WBZ3 Peripheral Libraries](GUID-5752DD6D-6E5D-484D-B564-DA87788492F3.md)

