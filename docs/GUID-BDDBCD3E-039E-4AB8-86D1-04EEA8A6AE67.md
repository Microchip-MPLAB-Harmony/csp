# Non-Volatile Memory Controller \(NVMCTRL\)

The Non-Volatile Memory \(NVM\) module provides an interface to the device's Non-Volatile Memory controller, so that memory pages can be written, read, erased, and reconfigured in a standardized manner.

**Using The Library**

NVMCTRL Peripheral library provides non-Blocking API's and they can be used to perform below functionalities on the NVMCTRL peripheral.

-   Initialize the NVMCTRL

-   Register a callback

-   Perform NVM write and erase operations

-   Manage region locks

-   Manage SmartEEPROM

-   Check error and status of NVM


The Flash memory main address space on this device is arranged as two memory banks. It is possible to execute code from one memory bank while a write or erase operation is progressing on the other memory bank. The entire flash memory is divided into 32 regions.

Each region has a corresponding lock bit which can be programmed \(with Lock Region command\) to temporarily prevent write and erase operations. Temporarily here means until the region is unlocked with an unlock command. These lock bits can be erased \(with an Unlock Region command\)\) to temporarily unlock a region. When the device is reset, region lock values are loaded with the default value stored in the NVM User Page.

The main address space is divided into blocks . Each of the block contains several flash pages. Commands used for the main address space and NVM User Page are different.

There are multiple commands to perform erase and write operations.

|Memory|WP|WQW|EP|EB|
|------|--|---|--|--|
|Main Address Space|X|X||X|
|User Page Address Space||X|X||

-   **EB:** Erase Block

-   **EP:** Erase Page

-   **WP:** Write Page

-   **WQW:** Write Quad Word


SmartEEPROM is the feature which perform EEPROM emulation on the device flash. There are fuse bits in the NVM User Page to configure SmartEEPROM total size and page size. Refer the datasheet and code examples for more details on the SmartEEPROM.

Here is an example code to erase a block and program a page of memory using polling method

```c
// Define a constant array in Flash.
// It must be aligned to block boundary and size has to be in multiple of rows
const uint8_t nvm_user_start_address[NVMCTRL_FLASH_BLOCKSIZE] __attribute__((aligned(NVMCTRL_FLASH_BLOCKSIZE),keep,externally_visible,space(prog)))= {0};

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

    /* Erase the block */
    NVMCTRL_BlockErase((uint32_t)nvm_user_start_address);

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
|NVMCTRL\_SetWriteMode|Sets the write mode for Flash|
|NVMCTRL\_PageWrite|Writes one page of data to given NVM address|
|NVMCTRL\_BlockErase|Erases a Block in the NVM|
|NVMCTRL\_ErrorGet|Returns error conditions of NVM controller|
|NVMCTRL\_StatusGet|Returns status conditions of NVM controller|
|NVMCTRL\_IsBusy|Returns the current status of NVM controller|
|NVMCTRL\_RegionLock|Locks a NVMCTRL region|
|NVMCTRL\_RegionUnlock|Unlocks a NVM region|
|NVMCTRL\_RegionLockStatusGet|Returns the value of RUNLOCK register|
|NVMCTRL\_BankSwap|Swaps NVM Banks|
|NVMCTRL\_MainCallbackRegister|Sets the pointer to the function \(and it's context\) to be called when an operation on the Flash is complete, provided the corresponding interrupt is enabled|
|NVMCTRL\_SmartEEPROM\_IsBusy|Checks whether SmartEEPROM is ready to perform next command|
|NVMCTRL\_SmartEepromStatusGet|Returns status conditions of SmartEEPROM|
|NVMCTRL\_SmartEEPROM\_IsActiveSectorFull|Check whether active sector used by the SmartEEPROM is full|
|NVMCTRL\_SmartEepromSectorReallocate|Performs sector reallocation for the SmartEEPROM|
|NVMCTRL\_SmartEepromFlushPageBuffer|Flush SmartEEPROM data when in buffered mode|
|NVMCTRL\_SmartEEPROMCallbackRegister|Sets the pointer to the function \(and it's context\) to be called when an operation on the SmartEEPROM is complete, provided the corresponding interrupt is enabled|
|NVMCTRL\_EnableMainFlashInterruptSource|Enables a given interrupt source for the Flash|
|NVMCTRL\_DisableMainFlashInterruptSource|Disables a given interrupt source for the Flash|
|NVMCTRL\_EnableSmartEepromInterruptSource|Enables a given interrupt source for the SmartEEPROM|
|NVMCTRL\_DisableSmartEepromInterruptSource|Disables a given interrupt source for the SmartEEPROM|
|NVMCTRL\_PageBufferWrite|Writes data to the internal buffer of NVM known as the page buffer|
|NVMCTRL\_PageBufferCommit|Commits the data present in NVM internal page buffer to flash memory|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|NVMCTRL\_FLASH\_START\_ADDRESS|Macro|Defines the start address of NVMCTRL Flash|
|NVMCTRL\_FLASH\_SIZE|Macro|Defines the size \(in bytes\) of Flash|
|NVMCTRL\_FLASH\_PAGESIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL Page|
|NVMCTRL\_FLASH\_BLOCKSIZE|Macro|Defines the size \(in bytes\) of a NVMCTRL Block|
|NVMCTRL\_WRITEMODE|Enum|Defines the NVMCTRL Write Modes|
|NVMCTRL\_INTERRUPT0\_SOURCE|Enum|Defines the Interrupt sources for the main flash|
|NVMCTRL\_INTERRUPT1\_SOURCE|Enum|Defines the Interrupt sources for the SmartEEPROM|
|NVMCTRL\_CALLBACK|Typedef|Defines the data type and function signature for the NVMCTRL peripheral callback function|

-   **[NVMCTRL\_Initialize Function](GUID-97BB70E9-D9BD-42E8-9C10-D891AC78410A.md)**  

-   **[NVMCTRL\_Read Function](GUID-4E0C86AB-BB30-4AAB-B9EE-D29946742470.md)**  

-   **[NVMCTRL\_SetWriteMode Function](GUID-8B25E692-5F57-4DBB-9386-7C34339666AF.md)**  

-   **[NVMCTRL\_PageWrite Function](GUID-33E14272-58A7-44F6-AA3F-CC314B38E515.md)**  

-   **[NVMCTRL\_BlockErase Function](GUID-32767A6E-93C5-4E80-AE76-250B7BB905C6.md)**  

-   **[NVMCTRL\_ErrorGet Function](GUID-13B4188B-86C2-4395-BAFC-8402E072B0CF.md)**  

-   **[NVMCTRL\_StatusGet Function](GUID-210DCA62-8662-4F71-B5CB-47DB7CE1DBBF.md)**  

-   **[NVMCTRL\_IsBusy Function](GUID-0698B77C-4D56-4951-8150-E6209DDF8D27.md)**  

-   **[NVMCTRL\_RegionLock Function](GUID-4A8274D6-516E-42F3-A508-0EE92C422D60.md)**  

-   **[NVMCTRL\_RegionUnlock Function](GUID-A2F63586-6CFE-4B65-B178-21EE07261A8C.md)**  

-   **[NVMCTRL\_RegionLockStatusGet Function](GUID-99DD0AFF-EBAF-4141-8582-59C981BA3A96.md)**  

-   **[NVMCTRL\_BankSwap Function](GUID-DAC15FDD-BBF1-4620-AF8D-3A417023440C.md)**  

-   **[NVMCTRL\_MainCallbackRegister Function](GUID-9F37D7C8-DFB3-45A0-BD27-C06389C37965.md)**  

-   **[NVMCTRL\_SmartEEPROM\_IsBusy Function](GUID-DC7CF68A-9B1A-401B-AC70-4B7DE45E1A6B.md)**  

-   **[NVMCTRL\_SmartEepromStatusGet Function](GUID-1793B3A5-1B71-4A51-8104-6A44ADB2060A.md)**  

-   **[NVMCTRL\_SmartEEPROM\_IsActiveSectorFull Function](GUID-6D437592-BBC4-4AE2-91AF-A65F010BCED7.md)**  

-   **[NVMCTRL\_SmartEepromSectorReallocate Function](GUID-9C4135F1-9B0F-4251-B97F-29D07ACAAA2D.md)**  

-   **[NVMCTRL\_SmartEepromFlushPageBuffer Function](GUID-9E700087-B39B-4F25-A030-23E1D031AB64.md)**  

-   **[NVMCTRL\_SmartEEPROMCallbackRegister Function](GUID-9CF21C82-B611-4A05-BAEB-1AE43F314BF8.md)**  

-   **[NVMCTRL\_EnableMainFlashInterruptSource Function](GUID-EEE8D049-A673-4716-A4A0-3DE65D76FC9F.md)**  

-   **[NVMCTRL\_DisableMainFlashInterruptSource Function](GUID-EEEF4AFF-8D23-4057-B94A-A3F1AED0D87A.md)**  

-   **[NVMCTRL\_EnableSmartEepromInterruptSource Function](GUID-BE4E5F06-25A4-4AF7-B740-56B590FA9ED5.md)**  

-   **[NVMCTRL\_DisableSmartEepromInterruptSource Function](GUID-269E2C49-C297-4DAF-AE83-9E8D8A727CC9.md)**  

-   **[NVMCTRL\_PageBufferWrite Function](GUID-F47D4A31-F6F2-47DD-9803-4E8D3CE52C60.md)**  

-   **[NVMCTRL\_PageBufferCommit Function](GUID-F5552518-2218-41AE-BD7F-7E5AD22353F7.md)**  

-   **[NVMCTRL\_FLASH\_START\_ADDRESS Macro](GUID-C723F312-A1A1-486A-A7D5-5D9A722172C1.md)**  

-   **[NVMCTRL\_FLASH\_SIZE Macro](GUID-85881273-FA8F-441F-94BE-ABA943C5FFED.md)**  

-   **[NVMCTRL\_FLASH\_PAGESIZE Macro](GUID-AB283273-C634-4FB4-B450-F65D15349373.md)**  

-   **[NVMCTRL\_FLASH\_BLOCKSIZE Macro](GUID-9BDA3DF9-2A0E-4579-A437-51B908F1B405.md)**  

-   **[NVMCTRL\_WRITEMODE Enum](GUID-1E6D5DD6-30EA-4C51-BA8B-D143A4A0E019.md)**  

-   **[NVMCTRL\_INTERRUPT0\_SOURCE Enum](GUID-F4B38454-41AE-40BC-BF9F-9A7DB7C95BA5.md)**  

-   **[NVMCTRL\_INTERRUPT1\_SOURCE Enum](GUID-4B2E35D2-4A10-4A67-A59B-F35B362B6584.md)**  

-   **[NVMCTRL\_CALLBACK Typedef](GUID-1F58B2C0-71DF-44BB-9170-583C52565787.md)**  


**Parent topic:**[SAM D51 E51 E53 E54 Peripheral Libraries](GUID-E33B93DD-6680-477E-AA96-966208DC9A50.md)

