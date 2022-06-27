# Embedded Flash Controller \(EFC\)

The Enhanced Embedded Flash Controller \(EEFC\) manages the programming, erasing, locking and unlocking sequences of the Flash using a full set<br />of commands.

**Using The Library**

The main Flash memory can not be read while it is being erased or written, the CPU is stalled during the entire operation. All functions<br />that modify the main Flash can be run from RAM memory to avoid CPU stall while main main Flash is being erased or written.

The FLASH memory is divided into a number of physical rows, each containing four identically sized flash pages. Pages may be read or written to<br />individually, however pages must be erased before being reprogrammed and the smallest granularity available for erasure is one single row.

EFC APIs are implemented to be non-blocking, the API will return immediately if not stalled by Flash operation. The user application can<br />either poll the status or get callback once the flash operation is completed.

-   With polling, the application will need to continuously check if the flash operation is completed

-   With callback, the registered callback function will be called once the flash operation is completed. This means the application do not have to poll continuously. The interrupt must be enabled in MHC for callback method


Here is an example code to erase a row and program a page of memory using polling method

```c
// Define a constant array in Flash.
// It must be aligned to sector boundary and size has to be in multiple of sectors
const uint8_t efc_user_start_address[EFC_SECTORSIZE] __attribute__((aligned(EFC_SECTORSIZE),keep,externally_visible,space(prog)))= {0};

void populate_buffer(uint8_t* data)
{
    int i = 0;

    for (i = 0; i < (EFC_PAGESIZE); i++)
    {
        *(data + i) = i;
    }
}

int main (void)
{
    uint8_t pageBuffer[EFC_PAGESIZE] = {0};

    /*Populate pageBuffer to programmed*/
    populate_buffer(pageBuffer);

    while(EFC_IsBusy());

    /*Erase the sector*/
    EFC_SectorErase(efc_user_start_address);

    /* Wait for erase operation to complete */
    while(EFC_IsBusy());

    /*Program a page*/
    EFC_PageWrite(pageBuffer, efc_user_start_address);

    /* Wait for page program to complete
    while(EFC_IsBusy());
}
```

**Library Interface**

Embedded Flash Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|EFC\_Initialize|Initializes given instance of the EFC peripheral|
|EFC\_Read|Reads length number of bytes from a given address in FLASH memory|
|EFC\_QuadWordWrite|Writes a 128-bit data to a given address in FLASH memory|
|EFC\_PageWrite|Writes data of size equivalent to page size to a given FLASH address|
|EFC\_SectorErase|Erases a Sector in the FLASH|
|EFC\_ErrorGet|Returns the error encountered by EFC controller|
|EFC\_IsBusy|Returns the current status of EFC controller|
|EFC\_RegionLock|Locks a Flash region|
|EFC\_RegionUnlock|Unlocks a Flash region|
|EFC\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the operation is complete|
|EFC\_PageBufferWrite|Writes data to the internal buffer of EFC known as the latch buffer|
|EFC\_PageBufferCommit|Commits the data present in EFC internal latch buffer to flash memory|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|EFC\_ERROR|Enum|Defines the data type for the EFC Error|
|EFC\_CALLBACK|Typedef|Defines the data type and function signature for the EFC peripheral callback function|

-   **[EFC\_Initialize Function](GUID-E7A5E10B-1FF1-4305-8C76-4B249AB8562A.md)**  

-   **[EFC\_Read Function](GUID-165B11C1-09EC-4E75-8EDD-E60DCAA67582.md)**  

-   **[EFC\_QuadWordWrite Function](GUID-C7B4D3EA-687C-4C33-974B-82648CC7FC8F.md)**  

-   **[EFC\_PageWrite Function](GUID-D3E1EB6A-CC83-4B94-B5BD-256A018D1DA5.md)**  

-   **[EFC\_SectorErase Function](GUID-D903C41F-B4D6-45FC-BAF9-615FCADCA286.md)**  

-   **[EFC\_ErrorGet Function](GUID-85D5F7B9-8C68-40A8-B02D-89D9FC374411.md)**  

-   **[EFC\_IsBusy Function](GUID-C215D2DE-109C-40EC-9433-F2825E9EBE05.md)**  

-   **[EFC\_RegionLock Function](GUID-4ADCC0E8-B162-468C-9090-C075EEAECA1B.md)**  

-   **[EFC\_RegionUnlock Function](GUID-9DF05D39-A7B4-4378-B5EC-2A72CDFF26CF.md)**  

-   **[EFC\_CallbackRegister Function](GUID-2158576D-8BD3-47D6-BA12-E36430632443.md)**  

-   **[EFC\_PageBufferWrite Function](GUID-A3CB319A-C41D-412D-A780-B344DD6BCF00.md)**  

-   **[EFC\_PageBufferCommit Function](GUID-54C98610-577D-4D6B-94D6-735B9E4424CB.md)**  

-   **[EFC\_ERROR Enum](GUID-4EE05E8D-4822-4A3C-B57F-C2424E9F37E2.md)**  

-   **[EFC\_CALLBACK Typedef](GUID-EB0BCF07-0611-40E8-8D86-CFBC62FBB7ED.md)**  


**Parent topic:**[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)

**Parent topic:**[SAM G51 G53 G54 Peripheral Libraries](GUID-E97B8116-033B-411A-925B-E8E6252A1E15.md)

**Parent topic:**[SAM G55 Peripheral Libraries](GUID-E3F1DCC4-CB31-4302-A60B-D2833C5CAD18.md)

