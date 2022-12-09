![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes

## CSP Release v3.15.0-E1

### New Features

- This engineering release adds support for the following features in PIC32CZ-CA family of devices:
   -  CRC support in FCR Peripheral library
   -  Support for programming fuse bits

- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

### Bug fixes
  - None

### Known Issues

  - Same as v3.14.0

### Development Tools

  - Same as v3.14.0

### Notes

-  None

## CSP Release v3.14.0

### New Features

- This release adds support for QMSPI, SMBUS and DMA peripheral libraries for CEC173x family of devices

- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

### Bug fixes
- Updated the clock initialization routine in PIC32MZ-W1 devices
- Fixed SPI slave write issue on E70/S70/V70/V71 devices

### Known Issues

  - Same as v3.13.0

### Development Tools

  - Same as v3.13.0

### Notes

-  None

## CSP Release v3.13.1

### New Features
- N/A

### Bug fixes
- Fixed issue in serial setup API of UART Peripheral library for PIC32M devices whereby transmit and receive gets disabled after the API is called
- Fixed issue in PIO peripheral library when interrupt generation is enabled on multiple pins of the same port
- Fixed issue related to context save and restore in Azure RTOS ThreadX for PIC32M devices
- Fixed MISRA-C violations in a few peripheral libraries

### Known Issues
- Same as v3.13.0

### Development Tools
- Same as v3.13.0

## CSP Release v3.13.0

### New Features

- **New part support** - This release introduces support for
PIC32CM-JH,
PIC32MK-MCA,
PIC32CX-BZ2 family of wireless microcontrollers (MCUs) and WBZ451 modules,
[ATSAMA5D29](https://www.microchip.com/en-us/product/ATSAMA5D29),
[SAMA7G54](https://www.microchip.com/en-us/product/sama7g54)

- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

- **New Features and Enhancements**
  - MISRA-C 2012 required rules compliance for all M0+, M4F, M23 based MCUs
  - Added ADC comparision mode in SAM E70/S70/V70/V71 and SAM G51/G53/G54/G55 Family of devices
  - Added support for non-blocking delay in Systick Plib
  - Added pin export feature to export pin configurations to a CSV file for all devices except PIC32M devices

### Known Issues

The current known issues are as follows:
- The default/max clock for ATSAMG55 devices is changed from 120MHz to 100MHz. Some of the clock dependent peripheral configuration may need to be verified/updated.
- The following product families specifically requires the below mentioned DFP versions to be [installed](https://microchipdeveloper.com/mplabx:projects-packs)  with MPLABX v6.00. It is always recommended to use the latest version of DFPs for all products provided by Microchip.
     -  **CEC173x Family**: CEC DFP v1.5.142 or higher
     -  **PIC32CX-BZ2 family of wireless microcontrollers (MCUs) and WBZ451 modules**: PIC32CX-BZ DFP 1.0.107 or higher

### Development Tools

- [MPLAB® X IDE v6.00](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v4.10](https://www.microchip.com/mplab/compilers)
- MPLAB® X IDE plug-ins:
    - MPLAB® Code Configurator 5.1.9 or higher

### Notes

-  None

## CSP Release v3.12.0

### New Features

- **New part support** - This release adds basic support (clock, pin, interrupts and UART Peripheral library) for CEC173x family of devices

- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

- **New Features and Enhancements**
  - None

### Known Issues

  - Same as v3.11.0

### Development Tools

For CEC173x family of devices:
  - [MPLAB® X IDE v6.00](https://www.microchip.com/mplab/mplab-x-ide)
  - [MPLAB® XC32 C/C++ Compiler v4.00](https://www.microchip.com/mplab/compilers)
  - MPLAB® X IDE plug-ins:
    - MPLAB® Code Configurator 5.1.2

For LAN9255:
  - Same as v3.11.0

For all other parts:
  - Same as v3.10.0


### Notes

-  None

## CSP Release v3.11.0

### New Features

- **New part support** - This release introduces support for [LAN9255](https://www.microchip.com/en-us/product/LAN9255)

- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).
  - All MPLAB X applications are updated to work with both MHC and MCC tools.

- **New Features and Enhancements**
  - None

### Known Issues

The current known issues are as follows:
  - Same as v3.10.0
  - With XC32 v4.00, any stdio library functions that reference "stdin" generates a warning message "warning: read is not implemented and will always fail". As a result, any function that reads from standard input does not work. XC32 v3.01 may be used to read from standard input.

### Development Tools

For LAN9255:
  - [MPLAB® X IDE v6.00](https://www.microchip.com/mplab/mplab-x-ide)
  - [MPLAB® XC32 C/C++ Compiler v4.00](https://www.microchip.com/mplab/compilers)
  - MPLAB® X IDE plug-ins:
    - MPLAB® Code Configurator 5.1.1

For all other parts:
  - Same as v3.10.0


### Notes

-  None

## CSP Release v3.10.0

### New Features

- **New part support** - This release introduces support for
[PIC32MM](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/32-bit-mcus/pic32-32-bit-mcus/pic32mm),
[WFI32E01](https://www.microchip.com/en-us/product/WFI32E01PE) and
[SAMRH707](https://www.microchip.com/en-us/product/SAMRH707)


- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).
  - All MPLAB X applications are updated to work with both MHC and MCC tools.

- **New Features and Enhancements**
  - Added CMSIS v5.8.0 Support
  - Added blocking millisecond and microsecond delay APIs for MCU and MPU products
  - Added DMA mode support, Digital Comparator and Digital Filter support in ADCHS peripheral library used in PIC32MZ and PIC32MK products
  - Added polled mode support in DMA peripheral library
  - Added edge interrupt support for PIC32M/PIC32C products

### Known Issues

The current known issues are as follows:
- Simplified the API for CAN and MCAN peripheral library used in MCU and MPU products based on ARM Cortex-M and Cortex-A series processor. Configuration option is provided to generate older version of API and the old APIs will be deprecated in the future release.
- The following product families specifically requires the below mentioned DFP versions to be [installed](https://microchipdeveloper.com/mplabx:projects-packs)  with MPLABX v5.50. It is always recommended to use the latest version of DFPs for all products provided by Microchip.
     -  **SAM L11 Family**: SAML11 DFP v4.3.139 or higher
     -  **SAM RH707 Family**: SAMRH707 DFP 1.0.28 or higher

### Development Tools

- [MPLAB® X IDE v5.50](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v3.01](https://www.microchip.com/mplab/compilers)
- [IAR EWARM v8.50](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
- [KEIL MDK v5.31](https://www2.keil.com/mdk5)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.8.0


### Notes

-  None

## CSP Release v3.9.1

### New Features
- N/A

### Bug fixes
- Fixed issues reported by MPLAB XC32 Compiler v3.00 in HSMCI and PIO

### Known Issues
- Same as v3.9.0

### Development Tools
- Same as v3.9.0

## CSP Release v3.9.0

### New Features

- **New part support** - This release introduces support for
[PIC32MX3/4](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/32-bit-mcus/pic32-32-bit-mcus/pic32mx),
[SAM R21](https://www.microchip.com/wwwproducts/en/ATSAMR21G18A),
[SAM R30](https://www.microchip.com/en-us/products/wireless-connectivity/sub-ghz/sam-r30), and
[SAM R34/R35](https://www.microchip.com/en-us/products/wireless-connectivity/lora-technology/sam-r34-r35) families of 32-bit microcontrollers.


- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embedded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

- **New Features and Enhancements**
  - Added Compatibility with C++
  - Added SPI Slave support for FLEXCOM and SPI peripheral
  - Added I2C Slave support for FLEXCOM and TWIHS peripheral
  - Added 9-bit UART mode support
  - Added UART FIFO support for FLEXCOM peripheral
  - Added SPI FIFO and multiple chip-select support for FLEXCOM and SPI peripheral
  - Added CRC support for DMA peripheral
  - Added Timer, Compare and Capture mode support for TCC peripheral
  - Added DWT peripheral library for Cortex-M4 and Cortex-M7
  - Added support to configure security bit to lock FLASH memory for SAM MCUs
  - Added Power peripheral library to support low power mode for PIC32M MCUs
  - Added support for DMA chaining, Auto-enable, Half-done and pattern match features in PIC32M DMA peripheral

### Known Issues

The current known issues are as follows:
- PIC32M SPI peripheral library is updated to allow only IO pins with SSEN function as the chip select lines in slave mode. If the SPI slave mode is used in PIC32M, then SPI component must be re-configured by removing from the project graph and then re-adding it.
-  Clock PLIB on SAM D20 is updated to use DFLL in closed loop mode by default. This requires enabling the internal 8 MHZ Oscillator clock source for GLCK1 in MHC Clock configurator, which is used as a reference clock for DFLL.
- The following product families specifically requires the below mentioned DFP versions to be [installed](https://microchipdeveloper.com/mplabx:projects-packs)  with MPLABX v5.45. It is always recommended to use the latest version of DFPs for all products provided by Microchip.
     -  **SAM 9X6 Family**: SAM9X6 DFP v1.5.50 or higher
     -  **SAM A5D2 Family**: SAMA5D2 DFP 1.5.53 or higher
     -  **SAM D51 Family**: SAMD51 DFP v3.4.91 or higher
     -  **SAM E51 Family**: SAME51 DFP v3.4.98 or higher
     -  **SAM E53 Family**: SAME53 DFP v3.4.79 or higher
     -  **SAM E54 Family**: SAME54 DFP v3.5.87 or higher
     -  **PIC32MZ-W Family**: PIC32MZ-W DFP v1.4.193 or higher
- CANFD peripheral library data types are updated to support co-existence of CAN and CANFD peripheral in the same MCU. Applications that use CANFD peripheral in PIC32M devices should be updated to use the new data types.

### Development Tools

- [MPLAB® X IDE v5.45](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v2.50](https://www.microchip.com/mplab/compilers)
- [IAR EWARM v8.50](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
- [KEIL MDK v5.31](https://www2.keil.com/mdk5)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.7.0


### Notes

-  Removed weak declaration for interrupts that are enabled in NVIC to enforce definition of interrupt handlers for MISRA C Required rules compliance. Any interrupts that are enabled without a corresponding interrupt handler will result in build error and hence the unused interrupts must be disabled.

## CSP Release v3.8.3

### New Features
- Same as v3.8.2

### Bug fixes
- Fixed compiler warnings in QEI PLib

### Known Issues
- Same as v3.8.2

### Development Tools
- Same as v3.8.2

## CSP Release v3.8.2

### New Features
- Same as v3.8.1

### Bug fixes
- Fixed issues related to clock and NVM wait states

### Known Issues
- Same as v3.8.1

### Development Tools
- Same as v3.8.1

## CSP Release v3.8.1

### New Features
- Updated supported product families

### Bug fixes
- N/A

### Known Issues
- Same as v3.8.0

### Development Tools
- Same as v3.8.0

## CSP Release v3.8.0

### New Features

- **New part support** - This release introduces support for SAM A5D2 SiP/SOM and SAM R34/R35 products.


- **Applications**
  - MPLAB Harmony provides large number of application examples to accelerate learning and reduce the development cycles for your embeeded systems with reusable software components. The applications examples are moved to the [product family specific repository](apps/readme.md).

- **New Features and Enhancements**
  - I2C HS mode (3.4 Mbps) support for SERCOM peripheral
  - SPI Slave support for SERCOM peripheral
  - LIN Master and LIN Slave support for SERCOM peripheral
  - I2C Slave support for PIC32M devices
  - SPI Slave support for PIC32M devices
  - CLC Peripheral library for PIC32MK product
  - Shadow Register support for PIC32M devices
  - External interrupt support for PIC32M devices
  - Reset Peripheral library for PIC32M devices
  - Single-lane transfer mode for SQI peripheral


### Known Issues

The current known issues are as follows:
  -  Default linker file is added to the MPLAB X projects. The applications that uses custom linker script must disable the linker file generation.
  -  The following product family requires newer DFP version to be downloaded from packs server and to be used in the MPLAB project to build with MPLAB X IDE v5.4.
     -  **SAM L21 Family**: SAML21_DFP v3.4.80
     -  **SAM L22 Family**: SAML22_DFP v3.4.59
     -  **SAM L10/L11 Family**: SAML10_DFP v3.3.82, SAML11_DFP v4.0.114
     -  **PIC32MK MCM/GPK Family**: PIC32MK-GP_DFP v1.4.117, PIC32MK-MC_DFP v1.5.115


### Development Tools

- [MPLAB® X IDE v5.40](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
- [IAR EWARM v8.50](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
- [KEIL MDK v5.29](https://www2.keil.com/mdk5)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.6.0


## CSP Release v3.7.1

### New Features
- N/A

### Bug fixes
- Fixed UART ring buffer transmit interrupt related issue.

### Known Issues
- Same as v3.7.0

### Development Tools
- Same as v3.7.0

## CSP Release v3.7.0

### New Features

- **New part support** - This release introduces support for the following devices
  - [SAM L11](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus/sam-l10-and-l11-microcontroller-family),
  - [SAM RH71 Revision C](https://www.microchip.com/wwwproducts/en/SAMRH71),
  - [SAM D20 Revision B](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus)

- **New Features and Enhancements**
  - Ring buffer support for UART peripheral
  - IAR EWARM Projects for Cortex-M MCU, SAM A5D2 MPU and SAM 9X60 MPU devices
  - KEIL MDK Projects for Cortex-M MCU devices
  - Updated demos to use newlib-nano with XC32
  - Created group project with at91bootloader for SAM A5D2 MPU to debug with MPLAB X IDE

- **Development kit and demo application support** - The following table provides number of peripheral library examples available for different development kits and toolchain.

    | Development Kits                                                                                                                               | MPLAB X   | IAR EWARM |  KEIL MDK |
    |------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------|-----------|
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   |    44     |    3      |     1     |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   |    40     |           |           |
    | [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                     |    1      |           |           |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/ATSAMC21N-XPRO)                               |    44     |           |     1     |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     |    28     |           |           |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     |    34     |           |           |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 |    45     |    3      |     1     |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  |    28     |           |           |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320010-C) |    24     |           |           |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320010)     |    19     |           |           |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320008)     |    4      |           |           |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               |    24     |           |           |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             |    38     |    36     |           |
    | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAML21-XPRO-B)                        |    37     |           |           |
    | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml22-xpro-b)                               |    34     |           |           |
    | [PIC32MX470 Curisoity Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320103)                                   |    24     |           |           |
    | [PIC32 USB Starter Kit III](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320003-3)                                              |    1      |           |           |
    | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/developmenttools/productdetails/dm320100)                                                 |    3      |           |           |
    | [PIC32MX1XX/2XX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320013)                                               |    1      |           |           |
    | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320105)                                        |    20     |           |           |
    | [ATSAM9X60-EK](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9)                                                      |    32     |    28     |           |
    | [SAM L10 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320204)                                      |    37     |           |     1     |
    | [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro)                                 |    27     |           |           |
    | PIC32MK MCJ Curiosity Pro                                                                                                                      |    24     |           |           |
    | [SAM DA1 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMDA1-XPRO)                          |    34     |           |           |
    | [SAM D11 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd11-xpro)                                 |    32     |           |           |
    | [SAM D10 Xplained Mini](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMD10-XMINI)                                       |    5      |           |           |
    | [PIC32 Ethernet Starter Kit II](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320004-2)                                          |    9      |           |           |
    | [SAMRH71 Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/SAMRH71F20-EK)                                       |    25     |           |           |
    | PIC32MK MCM Curiosity Pro                                                                                                                      |    24     |           |           |
    | PIC32MZ W1 Curiosity Board                                                                                                                     |    22     |           |           |
    | [SAM HA1G16A Xplained Pro](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMHA1G16A-XPRO)                                 |    26     |           |           |
    | [SAM L11 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320205)                                      |    4      |           |           |

### Known Issues

The current known issues are as follows:

- IAR application examples build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

- When using MPLABx to program/debug SAMA5D27C projects

  - "Run project" feature is not supported. Clicking on the "Run Project" button will not run the application on the target board.
  - "Step out" feature is not supported. Clicking on the "Step Out" button (or pressing Ctrl + F7) while debugging an application will not move the program counter.

### Development Tools

- [MPLAB® X IDE v5.4](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
- [IAR EWARM v8.50](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
- [KEIL MDK v5.29](https://www2.keil.com/mdk5)
- MPLAB® X IDE plug-ins:
  - MPLAB® Harmony Configurator (MHC) v3.5.0

## CSP Release v3.6.1

### New Features
- Regenerated PIC32MK MCJ Family Applications to work with updated Board

### Bug fixes
- None

### Known Issues
- Same as v3.6.0

### Development Tools
- Same as v3.6.0

## CSP Release v3.6.0
### New Features

- **New part support** - This release introduces support for
[SAM HA1](https://www.microchip.com/wwwproducts/en/ATSAMHA1G16A-B),
[SAM9x60 SiPs](https://www.microchip.com/design-centers/32-bit-mpus/sip-som/system-in-package),
[SAM G51](https://www.microchip.com/wwwproducts/en/ATSAMG51),
[SAM G53](https://www.microchip.com/wwwproducts/en/ATSAMG53),
[SAM G54](https://www.microchip.com/wwwproducts/en/ATSAMG54), and
PIC32MZ W1 families of 32-bit microcontrollers.

- **New Features and Enhancements**
   * Added I2C slave support for SERCOM peripheral library
   * Added SPI mode support for QSPI peripheral library
   * Added Normal Frequency and Normal PWM mode support for TC peripheral library
   * Added timestamp support for CAN and MCAN peripheral library
   * Added hall mode support for PDEC peripheral library
   * Added XC32 support for SAM9x60 device


- **Development kit and demo application support** - The following table provides number of peripheral library examples available for different development kits

    | Development Kits                                                                                                                               | # Examples |
    | ---                                                                                                                                            | ---|
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 42 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 39 |
    | [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                     | 1  |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/ATSAMC21N-XPRO)                               | 43 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 27 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 33 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 43 |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 26 |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto) ](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320010-C) | 22 |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit ](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320010)     | 17 |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320008)     | 3  |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               | 21 |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 36 |
    | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAML21-XPRO-B)                        | 36 |
    | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml22-xpro-b)                               | 33 |
    | [PIC32MX470 Curisoity Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320103)                                   | 22 |
    | [PIC32 USB Starter Kit III](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320003-3)                                              | 1  |
    | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/developmenttools/productdetails/dm320100)                                                 | 3  |
    | [PIC32MX1XX/2XX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320013)                                               | 1  |
    | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320105)                                        | 18 |
    | [ATSAM9X60-EK](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9)                                                      | 30 |
    | [SAM L10 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320204)                                      | 36 |
    | [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro)                                 | 27 |
    | PIC32MK MCJ Curiosity Pro                                                                                                                      | 23 |
    | [SAM DA1 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMDA1-XPRO)                          | 33 |
    | [SAM D11 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd11-xpro)                                 | 31 |
    | [SAM D10 Xplained Mini](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMD10-XMINI)                                       | 5  |
    | [PIC32 Ethernet Starter Kit II](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320004-2)                                          | 9  |
    | [SAMRH71 Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/SAMRH71F20-EK)                                       | 25 |
    | PIC32MK MCM Curiosity Pro                                                                                                                      | 22 |
    | PIC32MZ W1 Curiosity Board                                                                                                                     | 20 |
    | [SAM HA1G16A Xplained Pro](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMHA1G16A-XPRO)                                 | 25 |

### Known Issues

The current known issues are as follows:
* Use MPLAB X IDE V5.25 with SAM D10 Xplained Mini, SAM RH71 and SAM DA1 Xplained Pro.
* SAM HA1 and PIC32MZ W1 will be supported in the next version of MPLAB X IDE release.
* ATSAMA5D2C and SAM9X60 example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.3](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.30](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® v8.4](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.4.1


## CSP Release v3.5.2
### New Features
- N/A

### Bug fixes
- Fixed issue with Pin Manager hanging in some cases.

### Known Issues
- Same as v3.5.1

### Development Tools
- Same as v3.5.1

## CSP Release v3.5.1
### New Features
- N/A

### Bug fixes
- Fixed documentation and PLIB of gpio_01166 (PIC32MX7)
- Fixed API documentation for missing XXX_I2C_TransferSetup
- Fixed wrong clock generation for SAM G55 and SAM D11
- Fixed NVMCTRL PLIB for SAM E54
- Fixed SAM RH71 startup code, HEMC PLIB template and TC clock configuration
- Fixed SDI1 pin-setting for SPI in PIC32MX270F256B
- Fixed multiple issues in CAN_03247 and CAN_01152 (PIC32Mxx)

### Known Issues
- Same as v3.5.0

### Development Tools
- Same as v3.5.0

## CSP Release v3.5.0
### New Features

- **New part support** - This release introduces support for
[SAM DA1](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus),
[SAM D09/D10/D11](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-g-mcus),
[PIC32MX5XX/6XX/7XX](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mx-family),
PIC32MK GPH/GPG/MCJ, PIC32MK GPK/GPL/MCM, and SAM RH71 families of 32-bit microcontrollers.


- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                                               | Number of applications |
    | ---                                                                                                                                            | --- |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/ATSAMC21N-XPRO)                               | 41 |
    | [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                     | 1  |
    | [SAM D10 Xplained Mini](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMD10-XMINI)                                       | 5  |
    | [SAM D11 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd11-xpro)                                 | 29 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 26 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 32 |
    | [SAM DA1 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMDA1-XPRO)                          | 32 |
    | [SAM L10 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320204)                                      | 35 |
    | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAML21-XPRO-B)                        | 35 |
    | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml22-xpro-b)                               | 33 |
    | [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro)                                 | 27 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 41 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 40 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 38 |
    | SAMRH71 Evaluation Kit                                                                                                                         | 24 |
    | [PIC32 Ethernet Starter Kit II](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320004-2)                                          | 8  |
    | [Curiosity PIC32MX470 Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320103)                                   | 22 |
    | [PIC32 USB Starter Kit III](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320003-3)                                              | 1  |
    | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/developmenttools/productdetails/dm320100)                                                 | 2  |
    | [PIC32MX1XX/2XX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320013)                                               | 1  |
    | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320105)                                        | 18 |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               | 20 |
    | PIC32MK MCJ Curiosity Pro                                                                                                                      | 22 |
    | PIC32MK GPL Curiosity Pro                                                                                                                      | 21 |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit ](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320010)     | 17 |
    | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto) ](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320010-C) | 22 |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320008)     | 3  |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 25 |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 36 |
    | [ATSAM9X60-EK](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9)                                                      | 28 |

### Known Issues

The current known issues are as follows:
* Configuration fuse macros are not generated for SAM D09/D10/D11 devices.
* PIC32MK GPK/GPL/MCM and SAM RH71 will be supported in the next version of MPLAB X IDE release.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in CHM format.
* ATSAMA5D2C and SAM9X60 example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.25](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.30](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® v8.4](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.3.0.0 and above.





## CSP Release v3.4.0
### New Features

- **New part support** - This release introduces initial support for
[SAML10](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus) and
[SAMG55](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-g-mcus)
families of 32-bit microcontrollers and Support for ATSAMD21E17D, ATSAMD21E17DU, ATSAMD21G17D, ATSAMD21J17D, ATSAMD21E17L, ATSAMD21G17L has been added.

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                                               | Number of applications |
    | ---                                                                                                                                            | --- |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/ATSAMC21N-XPRO)                               | 40 |
    | [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                     | 1 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 26 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 32 |
    | [SAM L10 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320204)                                      | 35 |
    | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAML21-XPRO-B)                        | 35 |
    | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml22-xpro-b)                               | 32 |
    | [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro)                                 | 27 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 40 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 40 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 37 |
    | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/developmenttools/productdetails/dm320100)                                                 | 1  |
    | [PIC32MX1XX/2XX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320013)                                               | 1  |
    | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320105)                                        | 18 |
    | [Curiosity PIC32MX470 Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320103)                                   | 23 |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               | 19 |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320008-C) | 22 |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 24 |
    | [PIC32 USB Starter Kit III](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320003-3)                                              | 1  |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 35 |
    | [ATSAM9X60-EK](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9)                                                      | 28 |

### Known Issues

The current known issues are as follows:
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.
* ATSAMA5D2C and SAM9X60 example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```
* Preliminary support added for ATSAMA5D2C using MPLAB X and XC32. This complete tooling support will be added in future release of MPLAB X.

### Development Tools

* [MPLAB® X IDE v5.20](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.20](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.3.0.0 and above.


## CSP Release v3.3.0
### New Features

- **New part support** - This release introduces initial support for [SAML21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus),
[SAML22](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus),
[PIC32MX 1/2/5](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mx-family),
[PIC32MX 1/2 XLP](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mx-family),
[PIC32MX 3/4](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mx-family) families of 32-bit microcontrollers
and [SAM9X60](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9) family of 32-bit microprocessors.

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                                               | Number of applications |
    | ---                                                                                                                                            | --- |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                    | 39 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 26 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 32 |
    | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAML21-XPRO-B)                        | 34 |
    | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml22-xpro-b)                               | 32 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 39 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 40 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 37 |
    | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/developmenttools/productdetails/dm320100)                                                 | 1  |
    | [PIC32MX1XX/2XX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320013)                                               | 1  |
    | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320105)                                        | 18 |
    | [Curiosity PIC32MX470 Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320103)                                   | 22 |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               | 19 |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320008-C) | 22 |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 24 |
    | [PIC32 USB Starter Kit III](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320003-3)                                              | 1  |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 35 |
    | [ATSAM9X60-EK](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sam9)                                                      | 28 |

### Known Issues

The current known issues are as follows:
* Flash wait states are now calculated as part of respective flash Plib(EFC/NVMCTRL) instead of clock manager for SAM microcontrollers. Older projects must be reconfigured to add the respective Flash Plib to the project graph.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.
* ATSAMA5D2C and SAM9X60 example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.20](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.20](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.3.0.0 and above.


## CSP Release v3.2.1
### New Features

- **New part support** - This release introduces initial support for [PIC32MK](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mk-family) family of 32-bit microcontrollers.

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                                               | Number of applications |
    | ---                                                                                                                                            | --- |
    | [PIC32MK GP Development Kit](https://www.microchip.com/developmenttools/ProductDetails/dm320106)                                               | 18 |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320008-C) | 22 |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 24 |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 35 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 39 |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                    | 22 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 32 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 26 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 40 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 37 |

### Known Issues

The current known issues are as follows:
* Programming and debugging through PKOB is not yet supported for PIC32MZ DA, need to use external debugger (ICD4).
* PIC32MZ DA device family will be supported by next version of XC32 compiler.
* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The ICD4 flex cable must be removed after programming the device to run the application.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB® Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.
* ATSAMA5D2C example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```


### Development Tools

* [MPLAB® X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.2.0.0 and above.

## CSP Release v3.2.0
### New Features

- **New part support** - This release introduces initial support for
[SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus),
[SAMA5D2](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sama5/sama5d2-series),
[PIC32MZ EF](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-ef-family),
[PIC32MZ DA](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-da-family) families of 32-bit microcontrollers.

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                                               | Number of applications |
    | ---                                                                                                                                            | --- |
    | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320008-C) | 22 |
    | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/Dm320007)                  | 24 |
    | [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult)                             | 35 |
    | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)                                 | 39 |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)                    | 22 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)                     | 32 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)                     | 26 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)                   | 40 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)                   | 37 |

### Known Issues

The current known issues are as follows:
* Programming and debugging through PKOB is not yet supported for PIC32MZ DA, need to use external debugger (ICD4)
* PIC32MZ DA device family will be supported by next version of XC32 compiler.
* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The ICD4 flex cable must be removed after programming the device to run the application.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.
* ATSAMA5D2C example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.2.0.0 and above.

## CSP Release v3.1.0
### New Features

- **New part support** -This release introduces initial support for
[SAM C20/C21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-c-mcus),
[SAM D20/D21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus),
[SAM S70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-s-mcus),
[SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAM V70/V71](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-v-mcus) families of 32-bit microcontrollers.

- **Development kit and demo application support** - The following table provides number of peripheral library application available for different development kits

    | Development Kits                                                                                                             | Number of applications |
    | ---                                                                                                                          | --- |
    | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO)  | 38 |
    | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)   | 32 |
    | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)   | 26 |
    | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | 39 |
    | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | 36 |

### Known Issues

The current known issues are as follows:
* **Programming and debugging through EDBG is not supported**. The ICD4 needs to be used for programming and debugging.
* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The ICD4 flex cable must be removed after programming the device to run the application.
* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC). Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

### Development Tools

* [MPLAB® X IDE v5.10](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.1.0 and above.
