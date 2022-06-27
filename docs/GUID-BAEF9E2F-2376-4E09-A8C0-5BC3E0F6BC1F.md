# Clock Generator \(CLOCK\)

The PIC32MZ EF clock system has the following modules and features:

-   A total of five external and internal oscillator options as clock<br />sources

-   On-Chip PLL with user-selectable input divider, multiplier and output<br />divider to boost operating frequency on select internal and external<br />oscillator sources

-   On-Chip user-selectable divisor postscaler on select oscillator<br />sources

-   Software-controllable switching between various clock sources

-   A Fail-Safe Clock Monitor \(FSCM\) that detects clock failure and<br />permits safe application recovery or shutdown with dedicated Back-up<br />FRC \(BFRC\)

-   Dedicated On-Chip PLL for USB peripheral

-   Flexible reference clock output

-   Multiple clock branches for peripherals for better performance<br />flexibility

-   Clock switch/slew control with output divider


**Using The Library**

The Clock peripheral library initializes the clock system as configured<br />by the user in the MHC easy view.

**Library Interface**

Clock Generator peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CLK\_Initialize|Initializes hardware of the System Clock and Peripheral Clock|

-   **[CLK\_Initialize Function](GUID-7FCC76BB-89CC-4012-9B76-EE5B36D8B26C.md)**  


**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

