# Clock Generator \(CLOCK\)

The Clock system generates and distributes the clock for the processor<br />and peripherals

**Clock Generators:**

-   A low-power 32.768 kHz oscillator supporting crystals,<br />resonators and Bypass mode

-   An embedded always-on, slow RC oscillator generating a typical<br />32 kHz clock

-   A 8 to 50 MHz oscillator supporting crystals, resonators and Bypass<br />mode

-   A Main RC oscillator generating a typical 12 MHz clock

-   Two fractional-N PLLs with an input range of 8 to 50 MHz and an<br />\\internal frequency range of 600 to 1200 MHz


**Clock Distribution:**

-   MD\_SLCK-Monitoring Domain Slow clock. This clock, sourced from the<br />always-on Slow RC oscillator only, is the only permanent clock of<br />the system and feeds safety-critical functions of the device \(WDT,<br />RSTC, SCKC, frequency monitors and detectors, PMC startup time<br />counters\).

-   TD\_SLCK-Timing Domain Slow clock. This clock, sourced from the<br />32.768 kHz crystal oscillator or the always-on Slow RC oscillator,<br />is routed to the RTC and RTT peripherals.

-   MAINCK-Output of the Main clock oscillator selection. This clock is<br />either the Main crystal oscillator or Main RC oscillator.

-   PLL Clocks-Outputs of embedded PLLs

-   Master Clock \(MCK\)-programmable from a few hundred Hz to the<br />maximum operating frequency of the device. It is available to the<br />modules running permanently.

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
|CLK\_UPLLInitStart|Starts initialization of UPLL Clock|
|CLK\_UPLLInitMiddle|Controls UPLL Voltage Regulator|
|CLK\_UPLLInitEnd|Ends initialization of UPLL Clock|

-   **[CLK\_Initialize Function](GUID-7FCC76BB-89CC-4012-9B76-EE5B36D8B26C.md)**  

-   **[CLK\_UPLLInitStart Function](GUID-8FB7246D-5FD8-4E29-BDCF-8CC880A33B0C.md)**  

-   **[CLK\_UPLLInitMiddle Function](GUID-5972ABD4-CB3B-46D4-B37D-E29EC386D015.md)**  

-   **[CLK\_UPLLInitEnd Function](GUID-8FEB5ECF-0E3A-437A-9730-587A3A0D9FE9.md)**  


**Parent topic:**[SAM 9X60 Peripheral Libraries](GUID-CCAAC7F0-6BA8-4630-91AE-69718D188CBF.md)

