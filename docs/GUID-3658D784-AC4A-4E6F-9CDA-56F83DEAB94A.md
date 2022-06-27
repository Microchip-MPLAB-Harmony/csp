# Clock Generator \(CLOCK\)

The PIC32CM LE/LS family contain a sophisticated clocking system, which<br />is designed to give the maximum flexibility to the user application.<br />This system allows a system designer to tune the performance and power<br />consumption of the device in a dynamic manner, to achieve the best<br />trade-off between the two for a particular application.

**Clock sources**

The SAM devices have a number of master clock source modules, each of<br />which being capable of producing a stabilized output frequency, which<br />can then be fed into the various peripherals and modules within the<br />device. Possible clock source modules include internal R/C oscillators<br />as well as external crystal oscillators and/or clock inputs.

**CPU/Bus Clocks**

The Main Clock \(MCLK\) controls the synchronous clock generation of the<br />device. Using a clock provided by the Generic Clock Module \(GCLK\_MAIN\),<br />the Main Clock Controller provides

synchronous system clocks to the CPU and the modules connected to the<br />AHBx and the APBx bus. To save power, the input clock to one or more<br />peripherals on the AHB and APBx buses can be masked away - when masked,<br />no clock is passed into the module. Disabling of clocks of unused<br />modules will prevent all access to the masked module, and will reduce<br />the overall device power consumption.

**Generic Clock Generators**

The Generic Clock controller \(GCLK\) are used to provide clocks to the<br />various peripheral clock domains in the device in a standardized<br />manner. One or more master source clocks can be selected as the input<br />clock to a Generic Clock Generator, which can prescale down the input<br />frequency to a slower rate for use in a peripheral.

**Generic Clock Channels**

To connect a Generic Clock Generator to a peripheral within the device,<br />a Generic Clock Channel is used. Each peripheral or peripheral group<br />has an associated Generic Clock Channel, which serves as the clock<br />\\input for the peripheral\(s\). To supply a clock to the peripheral<br />module\(s\), the associated channel must be connected to a running<br />Generic Clock Generator and the channel enabled.

**Using The Library**

The Clock peripheral library initializes the clock system as configured<br />by the user in the MHC Clock configurator. It can be accessed via the<br />"Tools" drop down of the MPLAB harmony configurator menu bar.

**Library Interface**

Clock Generator peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CLOCK\_Initialize|Initializes the clock for system and peripherals|
|OSCCTRL\_CallbackRegister|Register the function to be called when an External Oscillator or DPLL event is generated|
|OSC32KCTRL\_CallbackRegister|Register the function to be called when the 32KHz External Oscillator has failed|
|MCLK\_CallbackRegister|Register the function to be called when the MCLK is ready|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|OSCCTRL\_CFD\_CALLBACK|Typedef|Defines the data type and function signature for the External Oscillator callback function|
|OSC32KCTRL\_CFD\_CALLBACK|Typedef|Defines the data type and function signature for the External 32KHz Oscillator clock failure detection callback function|
|MCLK\_CKRDY\_CALLBACK|Typedef|Defines the data type and function signature for the Main Clock Ready callback function|

-   **[CLOCK\_Initialize Function](GUID-B20B7C1D-72D7-48F2-BF71-688A22936393.md)**  

-   **[OSCCTRL\_CallbackRegister Function](GUID-94ED7AF5-F0BC-4251-AADF-F40890006A20.md)**  

-   **[OSC32KCTRL\_CallbackRegister Function](GUID-ED651B12-7E2E-49E1-85AA-14364996037A.md)**  

-   **[MCLK\_CallbackRegister Function](GUID-DA2E3E7A-05A5-4001-9906-F623781809FB.md)**  

-   **[OSCCTRL\_CFD\_CALLBACK Typedef](GUID-CE769701-F66D-46F9-9749-9F2643BDE0E5.md)**  

-   **[OSC32KCTRL\_CFD\_CALLBACK Typedef](GUID-DB1F8A86-E00B-448D-A9AB-EAFCD741BC7D.md)**  

-   **[MCLK\_CKRDY\_CALLBACK Typedef](GUID-73BC9100-2632-4CB8-B3D1-5D5ED3927A93.md)**  


**Parent topic:**[PIC32CM LE00 LS00 LS60 Peripheral Libraries](GUID-F80F1B47-C3E4-4803-ACB6-D30AC5EB7B45.md)

