# Non-Volatile Memory \(NVM\)

The Non-Volatile Memory \(NVM\) module provides an interface to the device's Non-Volatile Memory controller, so that memory pages can be written, read, erased, and reconfigured in a standardized manner.

**Using The Library**

The main Flash memory can not be read while it is being erased or written, the CPU is stalled during the entire operation. All functions that modify the main Flash can be run from RAM memory to avoid CPU stall while main main Flash is being erased or written.

The Program flash memory is divided into two Virtual regions pointing to the same physical memory location. Client can use any address from these virtual regions to perform erase/write/read operation

-   KSEG0 is cacheable region

-   KSEG1 is non-cacheable region


The program Flash array is built up of a series of rows to form a page. A page of Flash is the smallest unit of memory that can be erased at a single time. The program Flash array can be programmed in one of two ways:

-   Row programming, with 128 instruction words at a time

-   Word programming, with 1 instruction word at a time


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
|NVM\_WordWrite|Writes One word into the Flash|
|NVM\_PageErase|Erases a Page in the NVM|
|NVM\_ErrorGet|Returns the error state of NVM controller|
|NVM\_IsBusy|Returns the current status of NVM controller|
|NVM\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the operation is complete|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|NVM\_ERROR|Enum|Defines the NVM Error Type|
|NVM\_CALLBACK|Typedef|Defines the data type and function signature for the NVM peripheral callback function|

-   **[NVM\_Initialize Function](GUID-D1578E62-CDD7-4417-B37D-E0CCE8D1741E.md)**  

-   **[NVM\_Read Function](GUID-67000342-168A-4F98-BEE2-7861B3B5B236.md)**  

-   **[NVM\_RowWrite Function](GUID-33942AE6-41CC-45A7-B950-0E2A2E0F5929.md)**  

-   **[NVM\_WordWrite Function](GUID-11B81AA8-557B-46F5-BFA3-D4A2B36F5C97.md)**  

-   **[NVM\_PageErase Function](GUID-D3B337A4-DB43-4F6C-95D4-D4950603ACCF.md)**  

-   **[NVM\_ErrorGet Function](GUID-B17E6D26-9C9E-48EF-9274-16AB5B9EE5FA.md)**  

-   **[NVM\_IsBusy Function](GUID-05C82636-CFAE-4469-9486-47026C2E3400.md)**  

-   **[NVM\_CallbackRegister Function](GUID-7029F6B0-181B-4194-AE7D-95ECDFDE7F14.md)**  

-   **[NVM\_ERROR Enum](GUID-7FF0409F-92AB-458A-AF5F-B1C5B6D07D3C.md)**  

-   **[NVM\_CALLBACK Typedef](GUID-717D16DB-4555-4A5F-9487-230CB90044B1.md)**  


**Parent topic:**[PIC32MX 3XX 4XX Peripheral Libraries](GUID-2C79235F-A27F-4622-BBDA-943C35FD7940.md)

**Parent topic:**[PIC32MX 5XX 6XX 7XX Peripheral Libraries](GUID-91DC3697-58A9-4E5B-95DE-F4B08BA9C8DD.md)

