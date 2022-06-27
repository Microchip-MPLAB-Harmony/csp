# NMIC\_SOURCE Enum

**Parent topic:**[Non-maskable Interrupt Controller \(NMIC\)](GUID-FFDBEA51-E671-4664-A1C3-0E0A899FDF2D.md)

## C

```c
typedef enum
{
    NMIC_SOURCE_NMI		 = 0x01, // External NMI
    NMIC_SOURCE_CPU_FAIL	 = 0x02, // Wrong CPU Frequency Monitor Detection
    NMIC_SOURCE_XTAL_12M_FAIL	= 0x04, // Fast XTAL Clock Failure Detection
    NMIC_SOURCE_XTAL_32K_FAIL	= 0x08,	 // Slow XTAL 32KHZ Clock Failure Detection
    NMIC_SOURCE_VDDCORE_FAIL	= 0x10, // VDDCORE Brownout Detector Failure Detection
    NMIC_SOURCE_NOFIX_TCM = 0x20, // TCM non fixable error Detection
    NMIC_SOURCE_NOFIX_HEMC = 0x40, // HEMC non fixable error detection
    NMIC_SOURCE_NOFIX_HEFC = 0x80, // HEFC non fixable error detection
    NMIC_SOURCE_NOFIX_FlexRAM = 0x100 // FlexRam non fixable error detection
} NMIC_SOURCE;

```

## Summary

Defines the data type for the NMIC\_SOURCE Mask.

## Description

This is used to set up NMIC interrupt.

## Remarks

None.

