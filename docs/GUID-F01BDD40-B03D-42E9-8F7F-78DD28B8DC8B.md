# Analog Comparator Controller \(ACC\)

The Analog Comparator Controller \(ACC\) configures the analog comparator and generates an interrupt depending on<br />user settings. The analog comparator embeds two 8-to-1 multiplexers that generate two internal inputs. These inputs<br />are compared, resulting in a compare output. The hysteresis level, edge detection and polarity are configurable.<br />The ACC also generates a compare event which can be used by the Pulse Width Modulator \(PWM\).

**Using The Library**

The analog comparison status can be polled by the software or can be configured to generate a callback.

-   With polling, the application will need to continuously poll to check if the comparison edge occurred

-   With Callback, the registered callback function will be called when comparison edge is detected. This means the application do not have to poll continuously.


**Library Interface**

Analog Comparator Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|ACC\_Initialize|Initializes ACC module of the device|
|ACC\_Enable|Enables ACC peripheral|
|ACC\_Disable|Enables ACC peripheral|
|ACC\_StatusGet|Returns comparison status of the ACC|
|ACC\_RegisterCallback|Allows application to register callback with PLIB|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|ACC\_STATUS\_SOURCE|Enum|Identifies ACC Comparison status|
|ACC\_CALLBACK|Typedef|ACC Callback function pointer|

-   **[ACC\_Initialize Function](GUID-9BCE1658-3877-44D6-8EB3-510173F2D43B.md)**  

-   **[ACC\_StatusGet Function](GUID-A1AD8E42-FD92-4B59-B967-9CA9D00A4212.md)**  

-   **[ACC\_Disable Function](GUID-D79C39A4-3012-4A2D-B43E-E352A31F6F51.md)**  

-   **[ACC\_Enable Function](GUID-35F8A1CA-41E6-4AA8-A41D-9468ED7991F4.md)**  

-   **[ACC\_RegisterCallback Function](GUID-AF165091-8951-4D8B-A579-8C7BB983A6FC.md)**  

-   **[ACC\_CALLBACK Typedef](GUID-E3CF6B3F-0480-4FF2-BA83-906BEB087037.md)**  

-   **[ACC\_STATUS\_SOURCE Enum](GUID-FDA3A334-6136-4980-AE57-D3179D36A641.md)**  


**Parent topic:**[PIC32CX MT Peripheral Libraries](GUID-EEA7836F-956F-4526-BF85-CD488C4CE708.md)

**Parent topic:**[SAM A7G5 Peripheral Libraries](GUID-7EEB1AC5-4BFF-4259-97AD-8CF7367D7973.md)

