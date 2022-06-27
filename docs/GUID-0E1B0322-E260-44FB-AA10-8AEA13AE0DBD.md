# Clock Generator \(CLOCK\)

The SAM L21 family contain a sophisticated clocking system, which is<br />designed to give the maximum flexibility to the user application. This<br />system allows a system designer to tune the performance and power<br />consumption of the device in a dynamic manner, to achieve the best<br />trade-off between the two for a particular application.

**Clock Sources**

The SAM devices have a number of master clock source modules, each of<br />which being capable of producing a stabilized output frequency, which<br />can then be fed into the various peripherals and modules within the<br />device. Possible clock source modules include internal R/C oscillators<br />as well as external crystal oscillators and/or clock inputs.

**CPU / Bus Clocks**

The Main Clock \(MCLK\) controls the synchronous clock generation of the<br />device. Using a clock provided by the Generic Clock Module \(GCLK\_MAIN\),<br />the Main Clock Controller provides synchronous system clocks to the CPU<br />and the modules connected to the AHBx and the APBx bus. To save power,<br />the input clock to one or more peripherals on the AHB and APBx buses<br />can be masked away - when masked, no clock is passed into the module.<br />Disabling of clocks of unused modules will prevent all access to the<br />masked module, and will reduce the overall device power consumption.

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

-   **[CLOCK\_Initialize Function](GUID-B20B7C1D-72D7-48F2-BF71-688A22936393.md)**  


**Parent topic:**[SAM L21 Peripheral Libraries](GUID-230EF724-3CDA-4F88-8E42-0EF4C1CA112D.md)

