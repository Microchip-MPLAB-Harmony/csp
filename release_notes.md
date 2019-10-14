![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes

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

- **New part support** - This release introduces initial support for following products
[SAM DA1](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus), [SAM D09/D10/D11](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-g-mcus), [PIC32MX5XX/6XX/7XX](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mx-family), PIC32MK GPH/GPG/MCJ, PIC32MK GPK/GPL/MCM, and SAM RH71
families of 32-bit microcontrollers.


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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).
  Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in CHM format.

* ATSAMA5D2C and SAM9X60 example applications build with a warning message: ```Warning[Pe111]: statement is unreachable for return ( EXIT_FAILURE ); statement of main() in IAR```

### Development Tools

* [MPLAB® X IDE v5.25](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.30](https://www.microchip.com/mplab/compilers)
* [IAR Embedded Workbench® for ARM® v8.4](https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm)
* MPLAB® X IDE plug-ins:
  * MPLAB® Harmony Configurator (MHC) v3.3.0.0 and above.
  
  
  


## CSP Release v3.4.0
### New Features

- **New part support** - This release introduces initial support for [SAML10](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-l-mcus)
and [SAMG55](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-g-mcus)
families of 32-bit microcontrollers.
Support for ATSAMD21E17D, ATSAMD21E17DU, ATSAMD21G17D, ATSAMD21J17D, ATSAMD21E17L, ATSAMD21G17L has been added.

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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).

   Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

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

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).

   Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead. Help is available in both CHM and PDF formats.

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
