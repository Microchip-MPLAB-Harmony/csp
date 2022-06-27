# Clock Generator \(CLOCK\)

The Clock system generates and distributes the clock for the processor<br />and peripherals

**Clock Generators:**

-   A low-power 32.768 kHz oscillator supporting crystals, resonators and Bypass mode

-   An embedded always-on, slow RC oscillator generating a typical 32 kHz clock

-   A 20 to 50 MHz oscillator supporting crystals, resonators and Bypass mode

-   A main RC oscillator generating a typical 12 MHz c

-   Five fractional-N PLLs with an input range of 20 to 50 MHz and different internal frequency ranges : System PLL \(PLLA\), USB High-speed PLL \(UPLL\), Audio PLL \(AUDIOPLL\), LVDS PLL \(LVDSPLL\), System PLL divided by 2 \(PLLADIV2\)


**Clock Distribution:**

-   MD\_SLCK-Monitoring Domain Slow clock. This clock, sourced from the<br />always-on Slow RC oscillator only, is the only permanent clock of<br />the system and feeds safety-critical functions of the device \(WDT,<br />RSTC, SCKC, frequency monitors and detectors, PMC startup time<br />counters\).

-   TD\_SLCK-Timing Domain Slow clock. This clock, sourced from the<br />32.768 kHz crystal oscillator or the always-on Slow RC oscillator,<br />is routed to the RTC and RTT peripherals.

-   MAINCK-Output of the Main clock oscillator selection. This clock is<br />either the Main crystal oscillator or Main RC oscillator.

-   PLL Clocks-Outputs of embedded PLLs

-   Main System Bus Clock \(MCK\)-programmable from a few hundred Hz to the<br />maximum operating frequency of the device. It is available to the<br />modules running permanently.

-   Processor Clock \(CPU\_CLK\)-can be tuned through a frequency scaler<br />module and automatically switched off when entering the processor in<br />Sleep mode.

-   Free-running Processor Clock \(FCLK\)-the source clock of<br />CPU\_CLK. Is not affected when Sleep mode is activated.

-   UHDP Clocks \(UHP48M and UHP12M\)-required by USB Host Device Port<br />operations.

-   Peripheral Clocks with independent ON/OFF control, provided to the<br />peripherals. Each peripheral clock is inherited from MCK.

-   Programmable Clock Outputs \(PCKx\), selected from the clock<br />generator outputs to drive the device PCKx pins.

-   Generic Clock \(GCLK\) with controllable division and ON/OFF control,<br />independent of MCK and CPU\_CLK. Provided to selected peripherals.


**Using The Library**

The Clock peripheral library initializes the clock system as configured<br />by the user in the MHC Clock configurator. It can be accessed via the<br />"Tools" drop down of the MPLAB harmony configurator menu bar.

**Library Interface**

Clock Generator peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CLK\_Initialize|Initializes hardware of the System Clock and Peripheral Clock|

-   **[CLK\_Initialize Function](GUID-7FCC76BB-89CC-4012-9B76-EE5B36D8B26C.md)**  


**Parent topic:**[SAM 9X7 Peripheral Libraries](GUID-FB6741AA-355E-483F-9727-37728953D583.md)

