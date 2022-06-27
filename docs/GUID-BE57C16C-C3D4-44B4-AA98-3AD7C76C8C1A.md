# SPI\_CLOCK\_PHASE Enum

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c

/* SPI master mode */

typedef enum
{
    /* Input data is sampled on clock trailing edge and changed on leading edge */
    SPI_CLOCK_PHASE_TRAILING_EDGE = SERCOM_SPIM_CTRLA_CPHA_TRAILING_EDGE,

    /* Input data is sampled on clock leading edge and changed on trailing edge */
    SPI_CLOCK_PHASE_LEADING_EDGE = SERCOM_SPIM_CTRLA_CPHA_LEADING_EDGE,

    /* Force the compiler to reserve 32-bit space for each enum value */
    SPI_CLOCK_PHASE_INVALID = 0xFFFFFFFFU

} SPI_CLOCK_PHASE;

```

## Summary

Identifies SPI Clock Phase Options

## Description

This enumeration identifies possible SPI Clock Phase Options

## Remarks

None

