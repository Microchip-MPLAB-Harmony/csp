# FLEXCOM\_SPI\_CLOCK\_POLARITY Enum

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c

/* SPI master mode */

typedef enum
{
    /* The inactive state value of clock is logic level zero */
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_LOW = 0 << FLEX_SPI_CSR_CPOL_Pos,
    
    /* The inactive state value of clock is logic level one */
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_HIGH = 1 << FLEX_SPI_CSR_CPOL_Pos,
    
    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF
    
}FLEXCOM_SPI_CLOCK_POLARITY;

```

## Summary

Identifies FLEXCOM SPI Clock Polarity Options

## Description

This enumeration identifies possible FLEXCOM SPI Clock Polarity Options.

## Remarks

None.

