# Generic Interrupt Controller \(GIC\)

The integrated GIC collates and arbitrates from a large number of<br />interrupt sources. It provides:

-   Masking of interrupts.

-   Prioritization of interrupts.

-   Distribution of the interrupts to the target processors.

-   Tracking the status of interrupts.

-   Generation of interrupts by software.

-   Support for Security Extensions. Support for Virtualization Extensions.


**Using The Library**

Functions provided by CMSIS for accessing GIC registers are used for GIC configuration. GIC plib provides functions for setting up the software vector table for used for interrupt redirection.

**Library Interface**

Generic Interrupt Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|GIC\_Initialize|Initializes GIC hardware and in memory vector table for interrupt redirection|
|GIC\_RegisterSGIInterruptHandler|Registers handler for Software Generated Interrupts|
|GIC\_RegisterPeripheralInterruptHandler|Registers handler for Software Generated Interrupts|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|SGI\_HANDLER|Typedef|SGI interrupt handler function pointer|
|PPI\_SPI\_HANDLER|Typedef|PPI/SPI interrupt handler function pointer|

-   **[GIC\_Initialize Function](GUID-33044EFE-9FA9-4292-BA58-25488B060086.md)**  

-   **[GIC\_RegisterPeripheralInterruptHandler Function](GUID-7274700A-2402-4767-AACF-78F820D45A0A.md)**  

-   **[GIC\_RegisterSGIInterruptHandler Function](GUID-B35426CA-04F8-4779-B4D6-C10F6D17607C.md)**  

-   **[PPI\_SPI\_HANDLER Typedef](GUID-3F06A0FA-A60A-4DF2-8529-7CA438464F7F.md)**  

-   **[SGI\_HANDLER Typedef](GUID-BEE989B1-F7DA-405F-BFF8-922C30189A9B.md)**  


**Parent topic:**[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)

