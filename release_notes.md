# Microchip MPLAB Harmony 3 Release Notes
## CSP Release v3.2.0
### New Features
- **New part support** - This release introduces initial support for [SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus), [SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus), [SAMA5D2](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sama5/sama5d2-series), [PIC32MZ EF](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-ef-family), [PIC32MZ DA](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-da-family), [PIC32MK](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mk-family) families of 32-bit microcontrollers.

- **Peripheral support** - The following table provides the list of peripherals added for different product families in this release.

| PLIB | Name | SAM E70/S70/V70/V71 | SAM C20/C21 | SAM D5x/E5x | PIC32MZ EF | PIC32MZ DA | SAM A5D2 | PIC32MK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC | Analog Comparators |   |   | Yes |   |   |   |   |
| ACC | Analog Comparator Controller |   |   |   |   |   | Yes |   |
| ADC | Analog to Digital Converter |   |   | Yes |   |   | Yes |   |
| ADCHS | Analog-to-Digital Converter |   |   |   | Yes | Yes |   |   |
| AIC | Advanced Interrupt Controller |   |   |   |   |   | Yes |   |
| CACHE | PIC32MZ EF Cache |   |   |   | Yes | Yes |   |   |
| CAN | Controller Area Network |   | Yes | Yes |   |   |   |   |
| CLOCK | Clocks |   |   | Yes | Yes | Yes | Yes | Yes |
| CMP | Comparator |   |   |   | Yes | Yes |   |   |
| CORETIMER | Core Timer |   |   |   | Yes | Yes |   | Yes |
| CVR | CMP Voltage Reference |   |   |   | Yes | Yes |   |   |
| DAC | Digital Analog Converter |   |   | Yes |   |   |   |   |
| DDR | DDR2 SDRAM Controller |   |   |   |   | Yes |   |   |
| DMAC | Direct Memory Access Controller |   |   | Yes | Yes | Yes |   | Yes |
| DMT | Dead Man Timer |   |   |   | Yes | Yes |   | Yes |
| DSU | Device Service Unit |   |   | Yes |   |   |   |   |
| EBI | External Bus Interface |   |   |   | Yes | Yes |   |   |
| EIC | External Interrupt Controller |   |   | Yes |   |   |   |   |
| EVIC | Interrupt Controller |   |   |   | Yes | Yes |   | Yes |
| EVSYS | Event System Interface |   |   | Yes |   |   |   |   |
| FLEXCOM | Flexible Serial Communication Controller (SPI, USART, TWI) |   |   |   |   |   | Yes |   |
| FREQM | Frequency Meter |   |   | Yes |   |   |   |   |
| GPIO | General Purpose IO |   |   |   | Yes | Yes |   | Yes |
| HSMCI | High-Speed Multimedia Card Interface | Yes |   |   |   |   |   |   |
| I2C | Inter-Integrated Circuit |   |   |   | Yes | Yes |   |   |
| I2SC | Inter-IC Sound Controller |   |   |   |   |   | Yes |   |
| ICAP | Input Capture |   |   |   | Yes | Yes |   | Yes |
| L2CC | L2 Cache Controller |   |   |   |   |   | Yes |   |
| LCDC | LCD Controller |   |   |   |   |   | Yes |   |
| MATRIX | Bus Matrix |   |   |   |   |   | Yes |   |
| MCAN | Controller Area Network | Yes |   |   |   |   | Yes |   |
| MMU | Memory Management Unit |   |   |   |   |   | Yes |   |
| MPU | Memory Protection Unit |   |   | Yes |   |   |   |   |
| NVIC | Nested Vectored Interrupt Controller |   |   | Yes |   |   |   |   |
| NVM | Non-Volatile Memory Controller |   |   |   | Yes | Yes |   | Yes |
| NVMCTRL | Non-Volatile Memory Controller |   |   | Yes |   |   |   |   |
| OCMP | Output Compare |   |   |   | Yes | Yes |   | Yes |
| PAC | Peripheral Access Controller |   |   | Yes |   |   |   |   |
| PDEC | Quadrature Decoder |   |   | Yes |   |   |   |   |
| PIO | Parallel Input/Output Controller |   |   |   |   |   | Yes |   |
| PIT | Periodic Interval Timer |   |   |   |   |   | Yes |   |
| PM | Power Manager |   |   | Yes |   |   |   |   |
| PORT | Port Module |   |   | Yes |   |   |   |   |
| PWM | Pulse Width Modulation Controller |   |   |   |   |   | Yes |   |
| QSPI | Quad Serial Peripheral Interface |   |   | Yes |   |   | Yes |   |
| RNG | Random Number Generator |   |   |   | Yes | Yes |   |   |
| RSTC | Reset Controller |   |   | Yes |   |   | Yes |   |
| RSWDT | Reinforced Safety Watchdog Timer |   |   |   |   |   |   |   |
| RTC | Real-time Clock |   |   | Yes |   |   | Yes |   |
| RTCC | Real-time Clock Counter |   |   |   | Yes | Yes |   | Yes |
| RXLP | Low Power Asynchronous Receiver |   |   |   |   |   | Yes |   |
| SDADC | Sigma-Delta Analog Digital Converter |   |   |   |   |   |   |   |
| SDHC | SD/MMC Host Controller |   |   | Yes |   |   |   |   |
| SDMMC | Secure Digital MultiMedia Card Controller |   |   |   |   |   | Yes |   |
| SDRAMC | SDRAM Controller |   |   |   |   |   |   |   |
| SERCOM | Serial Communication Interface |   |   | Yes |   |   |   |   |
| SHDWC | Shutdown Controller |   |   |   |   |   | Yes |   |
| SMC | Static Memory Controller |   |   |   |   |   | Yes |   |
| SPI | Serial Peripheral Interface |   |   |   | Yes | Yes | Yes | Yes |
| SQI | Serial Quad Interface |   |   |   | Yes | Yes |   |   |
| SSC | Synchronous Serial Controller |   |   |   |   |   | Yes |   |
| SUPC | Supply Controller |   |   | Yes |   |   |   |   |
| SYSTICK | SysTick |   |   | Yes |   |   |   |   |
| TC | Timer Counter |   |   | Yes |   |   | Yes |   |
| TCC | Timer Counter Control |   |   | Yes |   |   |   |   |
| TMR | Timer |   |   |   | Yes | Yes |   | Yes |
| TMR1 | Timer |   |   |   | Yes | Yes |   | Yes |
| TRNG | True Random Number Generator |   |   | Yes |   |   | Yes |   |
| TWIHS | Two-wire Interface High Speed |   |   |   |   |   | Yes |   |
| UART | Universal Asynchronous Receiver Transmitter |   |   |   | Yes | Yes | Yes | Yes |
| WDT | Watchdog Timer |   |   | Yes | Yes | Yes | Yes | Yes |
| XDMAC | DMA Controller |   |   |   |   |   | Yes |   |


- **Development kit and demo application support** - The following table provides number of peripheral library applications added for different development kits.

| Development Kits | Number of applications |
| --- | --- |
| [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106) | 1 |
| [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320008-C) | 22 |
| [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007) |  24 |
| [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult) | 35  |
| [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO) | 39 |
| [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO) | +1 (can_normal_operation_blocking) |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | +1 (mcan_normal_operation_blocking) |
| [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | +1 (mcan_normal_operation_blocking) |


### Known Issues

The current known issues are as follows:

* Programming and debugging through PKOB is not yet supported for PIC32MZ DA, need to use external debugger (ICD4)
* PIC32MZ DA device family will be supported by next version of XC32 compiler.
* ATSAMA5D2C demo applications build with a warning message - Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR
* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The following demo project drives the reset line and requires the ICD4 flex cable to be removed after programming to run the application.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).
   Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead.  Help is available in both CHM and PDF formats.
* ATSAMA5D2C example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

- [MPLAB X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
- [IAR Embedded workbench for ARM (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
- MPLAB X IDE plug-ins:
  - MPLAB Harmony Configurator (MHC) v3.2.0.0

## CSP Release v3.1.0
### New Features

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
| XDMAC | DMA Controller | Yes |   |   ||

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

| Development Kits | Number of applications |
| --- | --- |
| [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO) | 38 |
| [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO) | 32 |
| [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO) | 26 |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | 39 |
| [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | 36 |

### Known Issues

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

### Development Tools

- [MPLAB X IDE v5.10](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
- MPLAB X IDE plug-ins:
  - MPLAB Harmony Configurator (MHC) v3.1.0.
