# Non-maskable Interrupt Controller \(NMIC\)

Non-Maskable Interrupt controller \(NMIC\) is used to configure and route<br />several critical exceptions to the NMI vector of the ARM CPU.

**Using The Library**

Configure the library using the MHC.

**Library Interface**

Non-maskable Interrupt Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|NMIC\_Initialize|Initializes given instance of the NMIC peripheral|
|NMIC\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the Timeout events occur|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|NMIC\_SOURCE|Enum|Defines the data type for the NMIC\_SOURCE Mask|
|NMIC\_CALLBACK|Typedef|Defines the data type and function signature for the NMIC peripheral callback function|

-   **[NMIC\_Initialize Function](GUID-3F2E3663-E4E8-4018-9EA3-17F3DE02AF46.md)**  

-   **[NMIC\_CallbackRegister Function](GUID-B73F6948-46D6-4BCD-B909-8216343147FC.md)**  

-   **[NMIC\_SOURCE Enum](GUID-F90E6EF0-D986-47DA-BE6C-DFA756B7AB36.md)**  

-   **[NMIC\_CALLBACK Typedef](GUID-3D2230BD-95D7-4356-9C8D-89EA989993E8.md)**  


**Parent topic:**[SAM RH707 Peripheral Libraries](GUID-C2AC236D-363B-4378-A381-B281F67C8647.md)

**Parent topic:**[SAM RH71 Peripheral Libraries](GUID-AC9BE324-E486-46EA-8D16-E04E15288053.md)

