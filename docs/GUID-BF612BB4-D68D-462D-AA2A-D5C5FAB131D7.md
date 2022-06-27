# PM\_RESET\_CAUSE Enum

**Parent topic:**[Power Manager \(PM\)](GUID-05376A1D-6E89-4AD9-8E74-DC5CD8AA4F8C.md)

## C

```c
typedef enum
{
    /* Power On Reset */
    PM_RESET_CAUSE_POR_RESET,
    
    /* Core Voltage Brown-Out Reset */
    PM_RESET_CAUSE_BOD12_RESET,
    
    /* Input Voltage Brown-Out Reset */
    PM_RESET_CAUSE_BOD33_RESET,
    
    /* External Reset */
    PM_RESET_CAUSE_EXT_RESET,
    
    /* Watchdog Reset */
    PM_RESET_CAUSE_WDT_RESET,
    
    /* System Reset (Software Reset) */
    PM_RESET_CAUSE_SYST_RESET,
} PM_RESET_CAUSE;

```

## Summary

Identifies the type of reset

## Description

This enumeration lists the possible reset sources

## Remarks

None.

