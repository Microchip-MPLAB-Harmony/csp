# Power Manager \(PM\)

The Power Manager \(PM\) controls the sleep modes and the power domain<br />gating of the device.

Various sleep modes are provided in order to fit power consumption<br />requirements. This enables the PM to stop unused modules in order to<br />save power. In active mode, the CPU is executing application code. When<br />the device enters a sleep mode, program execution is stopped and some<br />modules and clock domains are automatically switched off by the PM<br />according to the sleep mode. The application code decides which sleep<br />mode to enter and when. Interrupts from enabled peripherals and all<br />enabled reset sources can restore the device from a sleep mode to<br />active mode.

The user manually controls which power domains will be turned on and<br />off in standby, hibernate and backup sleep mode.

In backup and hibernate mode, the PM allows retaining the state of the<br />I/O lines, preventing I/O lines from toggling during wake-up.

**Using The Library**

PM Peripheral library provides non-Blocking API's and they can be used<br />to perform below functionalities. Settings configured via MHC are<br />written into PM registers when initialization function is called. To<br />enter any of the sleep modes, the corresponding API has to be called.

-   Initialize the PM sleep mode configurations

-   Enter specific sleep mode

-   Set/ Clear I/O retention feature \(Usable only with Hibernate or<br />Backup sleep mode\).


**Library Interface**

Power Manager peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|PM\_Initialize|Initializes the PM|
|PM\_IdleModeEnter|Puts the device in Idle mode|
|PM\_StandbyModeEnter|Puts the device in standby mode|
|PM\_HibernateModeEnter|Puts the device in hibernate mode|
|PM\_BackupModeEnter|Puts the device in backup mode|
|PM\_OffModeEnter|Puts the device in off mode|
|PM\_IO\_RetentionSet|Turns on I/O retention when exiting HIBERNATE or BACKUP mode|
|PM\_IO\_RetentionClear|Turns off I/O retention. To be called after exiting HIBERNATE or BACKUP mode|

-   **[PM\_Initialize Function](GUID-BCD65583-3580-44D9-8F17-E70645AC5A36.md)**  

-   **[PM\_IdleModeEnter Function](GUID-893725F2-64BE-49CA-B799-469FFE443CF2.md)**  

-   **[PM\_StandbyModeEnter Function](GUID-2C9E59AB-D8D9-40BD-88AE-C0C434DE25B6.md)**  

-   **[PM\_HibernateModeEnter Function](GUID-FE1B1FB1-2FDD-4520-A9B7-3A975298739A.md)**  

-   **[PM\_BackupModeEnter Function](GUID-5166DF71-CC02-4809-8EDE-0E4E49132471.md)**  

-   **[PM\_OffModeEnter Function](GUID-A901A74E-8D38-4230-B011-2B960C4C30F6.md)**  

-   **[PM\_IO\_RetentionSet Function](GUID-C46E9C1E-432D-45A7-AF6F-7508D627599D.md)**  

-   **[PM\_IO\_RetentionClear Function](GUID-079EF63A-5A54-4BEC-8E38-C5A9499BED95.md)**  


**Parent topic:**[PIC32CZ-CA Peripheral Libraries](GUID-7EAC3718-3D58-4007-AB2A-A0E3C167A2DF.md)

