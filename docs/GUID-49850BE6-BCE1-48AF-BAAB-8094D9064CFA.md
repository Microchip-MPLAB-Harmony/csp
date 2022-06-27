# Clock Generator \(CLOCK\)

The PIC32CZ\_CA clock system has the following modules and features:

Clock sources, i.e. oscillators controlled by OSCCTRL and OSC32KCTRL.

-   A clock source provides a time base that is used by other<br />components, such as Generic Clock Generators. Example clock sources are<br />the external crystal oscillator \(XOSC\) and the Digital Frequency Locked<br />Loop \(DFLL48M\).

-   There are also 2 DPLL's available as clock sources. One is for<br />system functions and one with a Fractional Divider for audio<br />applications.

-   Generic Clock Controller \(GCLK\), which generates, controls and<br />distributes the asynchronous clock consisting of:

    -   Generic Clock Generators

    -   Generic Clocks

-   The MCLK generates and controls the synchronous clocks on the<br />system. This includes the CPU, bus clocks \(APB, AHB\) as well as the<br />synchronous \(to the CPU\) user interfaces of the peripherals. It<br />contains clock masks that can turn on/off the user interface of a<br />peripheral as well as pre-scalers for the CPU and bus clocks

-   Start-up 6Mhz Clock

    -   This clock is used during the power up sequence of the device by<br />the SUL and SUPC macros.


**Using The Library**

The Clock peripheral library initializes the clock system as configured<br />by the user in the MHC easy view.

**Library Interface**

Clock Generator peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CLOCK\_Initialize|Initializes hardware of the System Clock and Peripheral Clock|

-   **[CLOCK\_Initialize Function](GUID-B20B7C1D-72D7-48F2-BF71-688A22936393.md)**  


**Parent topic:**[PIC32CZ-CA Peripheral Libraries](GUID-7EAC3718-3D58-4007-AB2A-A0E3C167A2DF.md)

