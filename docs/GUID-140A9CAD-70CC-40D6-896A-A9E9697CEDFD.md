# Digital-to-Analog Converter Controller \(DACC\)

The Digital-to-Analog Converter Controller \(DACC\) peripheral provides<br />the following features:

-   Up to two single-ended analog outputs or one differential<br />analog output

-   12-bit resolution

-   Free-running mode, Max speed mode, Trigger mode or<br />Interpolation mode

-   Provides a Bypass mode which minimizes power consumption in case of<br />a limited sampling rate conversion


**Using The Library**

The DACC peripheral library provides an interface for the conversion of<br />digital values to analog voltage.

The DAC can operate in free-running mode, where a write to the<br />conversion-data register initiates an update on the analog output, or<br />in triggered mode, where updates are initiated by a rising edge on an<br />\\internal or external synchronization signal.

The user must ensure that new data is not written to the DAC before the<br />last conversion is complete as illustrated below.

```c
/* Write new data if DAC is ready */
 if (DACCx_IsReady(DACC_CHANNEL_0))
 {
    DACCx_DataWrite (DACC_CHANNEL_1, 0xff)
 }
```

**Library Interface**

Digital-to-Analog Converter Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|DACC\_Initialize|Initializes DACC module of the device|
|DACC\_IsReady|Returns the status of readiness of Channel x of DACC module for new conversion request|
|DACC\_DataWrite|Converts a Digital data to Analog value|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|DACC\_CHANNEL\_NUM|Enum|Identifies the Channel index of DACC module|

-   **[DACC\_Initialize Function](GUID-1A686210-D6AD-4760-823F-BD4E1117733C.md)**  

-   **[DACC\_IsReady Function](GUID-04E09208-62E8-4591-B88F-ABB2E0082432.md)**  

-   **[DACC\_DataWrite Function](GUID-C8B67DA5-DCAD-4FBA-A2D7-30EF5B79A9A1.md)**  

-   **[DACC\_CHANNEL\_NUM Enum](GUID-30B508BB-DD64-49D8-8404-1FC649905896.md)**  


**Parent topic:**[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)

