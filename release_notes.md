# Microchip MPLAB Harmony 3 Release Notes
## CSP Release v3.1.0
### NEW FEATURES

- **New part support** -This release introduces initial support for for [SAM C20/C21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-c-mcus), [SAM D20/D21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus), [SAM S70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-s-mcus), [SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus), [SAM V70/V71](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-v-mcus) families of 32-bit microcontrollers.

- **Peripheral support** - The following table provides the list of peripherals supported for different product families.

| Peripheral | Name | SAM S70/E70/V70/V71 | SAM C20/C21 | SAM D20/D21 |
| --- | --- | --- | --- | --- |
| AC | Analog Comparators |   | Yes | Yes |
| ACC | Analog Comparator Controller | Yes |   |   |
| ADC | Analog Digital Converter |   | Yes | Yes  |
| AFEC | Analog Front-End Controller | Yes |   |   |
| CLOCK | Clock | Yes | Yes | Yes |
| DAC | Digital Analog Converter |   | Yes | Yes |
| DACC | Digital-to-Analog Converter Controller | Yes |   |   |
| DIVAS | Divide and Square Root Accelerator |   | Yes |   |
| DMAC | Direct Memory Access Controller |   | Yes | Yes |
| DSU | Device Service Unit |   | Yes | Yes |
| EFC | Embedded Flash Controller | Yes |   |   |
| EIC | External Interrupt Controller |   | Yes | Yes |
| EVSYS | Event System Interface |   | Yes | Yes |
| FREQM | Frequency Meter |   | Yes |   |
| I2SC | Inter-IC Sound Controller | Yes  |   |   |
| MPU | Memory Protection Unit | Yes | Yes | Yes |
| NVIC | Nested Vectored Interrupt Controller | Yes | Yes | Yes |
| NVMCTRL | Non-Volatile Memory Controller |   | Yes | Yes |
| PAC | Peripheral Access Controller |   | Yes | Yes |
| PIO | Parallel Input / Output Controller | Yes |   |   |
| PM | Power Manager |   | Yes | Yes |
| PORT | Port Module |   | Yes | Yes |
| PWM | Pulse Width Modulation Controller | Yes |   |   |
| QSPI | Quad Serial Peripheral Interface | Yes |   |   |
| RSTC | Reset Controller | Yes | Yes |   |
| RSWDT | Reinforced Safety Watchdog Timer | Yes |   |   |
| RTC | Real-Time Counter | Yes | Yes | Yes |
| RTT | Real-time Timer | Yes |   |   |
| SDADC | Sigma-Delta Analog Digital Converter |   | Yes |   |
| SDRAMC | SDRAM Controller | Yes |   |   |
| SERCOM | Serial Communication Interface |   | Yes | Yes |
| SMC | Static Memory Controller | Yes |   |   |
| SPI | Serial Peripheral Interface | Yes |   |   |
| SSC | Synchronous Serial Controller | Yes |   |   |
| SUPC | Supply Controller | Yes | Yes |   |
| SysTick | SysTick | Yes | Yes | Yes |
| TC | Timer Counter | Yes | Yes | Yes |
| TCC | Timer Counter Control |   | Yes |   |
| TRNG | True Random Number Generator | Yes |   |   |
| TWIHS | Two-wire Interface High Speed | Yes |   |   |
| UART | Universal Asynchronous Receiver Transmitter | Yes |   |   |
| USART | Universal Synchronous Asynchronous Receiver Transmitter | Yes |   |   |
| WDT | Watchdog Timer | Yes | Yes | Yes |
| XDMAC | Extensible DMA Controller | Yes |   |   ||

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

| Development Kits | Number of applications |
| --- | --- |
| [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO) | 38 |
| [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO) | 32 |
| [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO) | 26 |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | 39 |
| [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | 36 |

### KNOWN ISSUES

The current known issues are as follows:

* **Programming and debugging through EDBG is not supported**. The ICD4 needs to be used for programming and debugging.

* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The following demo project drives the reset line and requires the ICD4 flex cable to be removed after programming to run the application.

| Project Name | Development Kit |
| --- | --- |
| supc\_wakeup\_rtc | SAM V71 Xplained Ultra Evaluation Kit  |
| supc\_wakeup\_rtt | SAM V71 Xplained Ultra Evaluation Kit  |
| rswdt\_timeout | SAM V71 Xplained Ultra Evaluation Kit  |
| wdt\_timeout | SAM V71 Xplained Ultra Evaluation Kit  |

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).  Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead.  Help is available in both CHM and PDF formats.

### DEVELOPMENT TOOLS

- [MPLAB X IDE v5.10](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
- MPLAB X IDE plug-ins:
 - MPLAB Harmony Configurator (MHC) v3.1.0.
