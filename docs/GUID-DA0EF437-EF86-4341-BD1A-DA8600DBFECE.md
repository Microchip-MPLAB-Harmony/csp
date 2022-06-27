# \(PMP\)

The Parallel Master Port \(PMP\) is a parallel 8-bit/16-bit I/O module<br />specifically designed to communicate with a wide variety of parallel<br />devices such as communications peripherals, LCDs, external memory<br />devices and micro-controllers. Because the interfaces to parallel<br />peripherals vary significantly, the PMP module is highly configurable.

**Using The Library**

The key features of PMP :-

-   8-bit,16-bit interface

-   Up to 16 programmable address lines

-   Up to two Chip Select lines

-   Programmable strobe options

-   Address auto-increment/auto-decrement

-   Programmable address/data multiplexing

-   Programmable polarity on control signals

-   Programmable Wait states


**Library Interface**

peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|PMP\_Initialize|This function initializes the PMP controller of the device|
|PMP\_AddressSet|Sets the current address of the PMP module to the specified address|
|PMP\_AddressGet|Gets the current address of the PMP module|
|PMP\_MasterSend|Sends the specified data in Master mode|
|PMP\_MasterReceive|Receives the data in Master mode|
|PMP\_PortIsBusy|Identifies if the \(Master mode\) PMP port is busy|
|PMP\_AddressPortEnable|Enables the port lines specified as PMP address lines|
|PMP\_AddressPortDisable|Disables the port lines specified as PMP address lines|

-   **[PMP\_Initialize Function](GUID-C44CD989-ED3D-4CBF-B5F4-244E4C1B2A52.md)**  

-   **[PMP\_AddressSet Function](GUID-9D4EE853-9128-4E0C-AA13-1973960CC083.md)**  

-   **[PMP\_AddressGet Function](GUID-12654F3E-A9E5-4D5C-B19B-24BA84E4B2B6.md)**  

-   **[PMP\_MasterSend Function](GUID-17DC1F33-6B41-4DDC-91E8-86BF7AAC79AE.md)**  

-   **[PMP\_MasterReceive Function](GUID-D459134C-7EF8-45C0-8912-CF2C34E9E7BB.md)**  

-   **[PMP\_PortIsBusy Function](GUID-DF5A8CF3-851E-48B0-98D2-83873E6FF35F.md)**  

-   **[PMP\_AddressPortEnable Function](GUID-4EA51BD8-FC9A-42BD-B37A-EB2A3E1A458A.md)**  

-   **[PMP\_AddressPortDisable Function](GUID-F0FA2568-9AEF-444F-BBE9-272D389C7404.md)**  


**Parent topic:**[PIC32MK GPD GPE MCF Peripheral Libraries](GUID-A63F4C14-72E7-44D7-9C70-A48BBD41B583.md)

**Parent topic:**[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)

**Parent topic:**[PIC32MX 1XX 2XX Peripheral Libraries](GUID-DD9F92A3-1B1F-4068-A4CC-C71672A1BF54.md)

**Parent topic:**[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)

**Parent topic:**[PIC32MX 1XX 2XX 5XX Peripheral Libraries](GUID-232A3DC0-B096-45AA-9430-33A2C9BA694A.md)

**Parent topic:**[PIC32MX 330 350 370 430 450 470 Peripheral Libraries](GUID-4F5C226F-136E-4C6B-8A7F-0DF12557C7F8.md)

**Parent topic:**[PIC32MX 3XX 4XX Peripheral Libraries](GUID-2C79235F-A27F-4622-BBDA-943C35FD7940.md)

**Parent topic:**[PIC32MX 5XX 6XX 7XX Peripheral Libraries](GUID-91DC3697-58A9-4E5B-95DE-F4B08BA9C8DD.md)

**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

