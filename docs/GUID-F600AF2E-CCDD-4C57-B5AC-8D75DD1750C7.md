# Enhanced Vectored Interrupt Controller \(EVIC\)

PIC32MZ EF devices generate interrupt requests in response to interrupt<br />events from peripheral modules. The Interrupt Controller module exists<br />outside of the CPU and prioritizes the interrupt events before<br />presenting them to the CPU.

The Interrupt Controller module includes the following features:

-   Up to 213 interrupt sources and vectors with dedicated programmable<br />offsets, eliminating the need for redirection

-   Single and multi-vector mode operations

-   Five external interrupts with edge polarity control

-   Interrupt proximity timer

-   Seven user-selectable priority levels for each vector

-   Four user-selectable sub-priority levels within each priority

-   Seven shadow register sets that can be used for any priority level,<br />eliminating software context switch and reducing interrupt latency

-   Software can generate any interrupt


**Using The Library**

**Library Interface**

Enhanced Vectored Interrupt Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|EVIC\_Initialize|Configures and initializes the interrupt subsystem|
|EVIC\_SourceEnable|Enables the interrupt source|
|EVIC\_SourceDisable|Disables the interrupt source|
|EVIC\_SourceIsEnabled|Gets the enable state of the interrupt source|
|EVIC\_SourceStatusGet|Returns the status of the interrupt flag for the selected source|
|EVIC\_SourceStatusSet|Sets the status of the interrupt flag for the selected source|
|EVIC\_SourceStatusClear|Clears the status of the interrupt flag for the selected source|
|EVIC\_ExternalInterruptCallbackRegister|Allows application to register callback for every external interrupt pin|
|EVIC\_ExternalInterruptEnable|Enables external interrupt on selected external interrupt pins|
|EVIC\_ExternalInterruptDisable|Disables external interrupt on selected external interrupt pins|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|INT\_SOURCE|Enum|Identifies interrupt sources|
|EXTERNAL\_INT\_PIN|Enum|Identifies the active external interrupt pins|
|EXTERNAL\_INT\_PIN\_CALLBACK|Typedef|Pointer to a external Pin-Event handler function|

-   **[EVIC\_Initialize Function](GUID-1C08A4DA-D0F3-4836-8F2B-5B489560C25B.md)**  

-   **[EVIC\_SourceEnable Function](GUID-5009201F-17A3-4F81-9391-31BA2F75727E.md)**  

-   **[EVIC\_SourceDisable Function](GUID-B23EE5A2-1999-41E2-B0FA-FF3BA47533E0.md)**  

-   **[EVIC\_SourceIsEnabled Function](GUID-B5EFE604-ECBE-4B7D-B217-4DDF235646FD.md)**  

-   **[EVIC\_SourceStatusGet Function](GUID-198755D4-3500-429A-989B-8D3A4BD93BA8.md)**  

-   **[EVIC\_SourceStatusSet Function](GUID-CF1B659C-7A6A-497D-BC8A-319FB3D2186A.md)**  

-   **[EVIC\_SourceStatusClear Function](GUID-39BEFB78-AD5E-4C8F-B5E5-085FAE7227F8.md)**  

-   **[EVIC\_ExternalInterruptCallbackRegister Function](GUID-5E1AC210-9DF5-4888-897C-D405263DC5FC.md)**  

-   **[EVIC\_ExternalInterruptEnable Function](GUID-83BBF0FC-CD3E-4D4B-8ED2-8D3F30FCC94D.md)**  

-   **[EVIC\_ExternalInterruptDisable Function](GUID-78152059-5F55-4483-B32F-0BB0C91827F7.md)**  

-   **[INT\_SOURCE Enum](GUID-D16EF788-99DB-46B0-B044-A65C34A1E0D2.md)**  

-   **[EXTERNAL\_INT\_PIN Enum](GUID-37681BD0-A0EC-487C-AE00-5B5CD3A57E65.md)**  

-   **[EXTERNAL\_INT\_PIN\_CALLBACK Typedef](GUID-36535E36-8880-4D28-BA21-39DCED7FC98C.md)**  


**Parent topic:**[PIC32MK GPD GPE MCF Peripheral Libraries](GUID-A63F4C14-72E7-44D7-9C70-A48BBD41B583.md)

**Parent topic:**[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)

**Parent topic:**[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)

**Parent topic:**[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)

**Parent topic:**[PIC32MM GPL Peripheral Libraries](GUID-1AE2B428-AA57-43A7-A52E-C35ABF67EDC4.md)

**Parent topic:**[PIC32MM GPM Peripheral Libraries](GUID-CB22E113-2DFF-40FB-BA9B-BFA1C8003FEC.md)

**Parent topic:**[PIC32MX 1XX 2XX Peripheral Libraries](GUID-DD9F92A3-1B1F-4068-A4CC-C71672A1BF54.md)

**Parent topic:**[PIC32MX 1XX 2XX XLP Peripheral Libraries](GUID-8819552A-CB58-4DAC-BE25-EC305892232E.md)

**Parent topic:**[PIC32MX 1XX 2XX 5XX Peripheral Libraries](GUID-232A3DC0-B096-45AA-9430-33A2C9BA694A.md)

**Parent topic:**[PIC32MX 330 350 370 430 450 470 Peripheral Libraries](GUID-4F5C226F-136E-4C6B-8A7F-0DF12557C7F8.md)

**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

**Parent topic:**[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)

