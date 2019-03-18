![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes
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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB® Harmony Configurator (MHC).

   Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

* ATSAMA5D2C example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```


### Development Tools

* [MPLAB® X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.2.0.0 and above.

## CSP Release v3.2.0
### New Features

- **New part support** - This release introduces initial support for [SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus), [SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus), [SAMA5D2](https://www.microchip.com/design-centers/32-bit-mpus/microprocessors/sama5/sama5d2-series), [PIC32MZ EF](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-ef-family), [PIC32MZ DA](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-da-family) families of 32-bit microcontrollers.

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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).

   Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

* ATSAMA5D2C example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.15](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® (v8.32 or above)](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.2.0.0 and above.

## CSP Release v3.1.0
### New Features

- **New part support** -This release introduces initial support for for [SAM C20/C21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-c-mcus), [SAM D20/D21](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus), [SAM S70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-s-mcus), [SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus), [SAM V70/V71](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-v-mcus) families of 32-bit microcontrollers.

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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).

  Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

### Development Tools

* [MPLAB® X IDE v5.10](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.1.0 and above.
