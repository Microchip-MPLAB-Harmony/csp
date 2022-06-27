# NVMCTRL\_INTERRUPT0\_SOURCE Enum

**Parent topic:**[Non-Volatile Memory Controller \(NVMCTRL\)](GUID-BDDBCD3E-039E-4AB8-86D1-04EEA8A6AE67.md)

## C

```c
typedef enum
{
    NVMCTRL_INT_DONE = NVMCTRL_INTENCLR_DONE_Msk,
    NVMCTRL_INT_ADDRE = NVMCTRL_INTENCLR_ADDRE_Msk,
    NVMCTRL_INT_PROGE = NVMCTRL_INTENCLR_PROGE_Msk,
    NVMCTRL_INT_LOCKE = NVMCTRL_INTENCLR_LOCKE_Msk,
    NVMCTRL_INT_ECCSE = NVMCTRL_INTENCLR_ECCSE_Msk,
    NVMCTRL_INT_ECCDE = NVMCTRL_INTENCLR_ECCDE_Msk,
    NVMCTRL_INT_NVME = NVMCTRL_INTENCLR_NVME_Msk,
    NVMCTRL_INT_SUSP = NVMCTRL_INTENCLR_SUSP_Msk
} NVMCTRL_INTERRUPT0_SOURCE;

```

## Summary

Defines the Interrupt sources for the main flash.

## Description

This enumeration defines the Interrupt sources for the main flash.

## Remarks

None.

