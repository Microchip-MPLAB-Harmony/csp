# FLEXCOM\_SPI\_DATA\_BITS Enum

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c

/* SPI master mode */

typedef enum
{
    FLEXCOM_SPI_DATA_BITS_8 = FLEX_SPI_CSR_BITS_8_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_9 = FLEX_SPI_CSR_BITS_9_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_10 = FLEX_SPI_CSR_BITS_10_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_11 = FLEX_SPI_CSR_BITS_11_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_12 = FLEX_SPI_CSR_BITS_12_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_13 = FLEX_SPI_CSR_BITS_13_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_14 = FLEX_SPI_CSR_BITS_14_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_15 = FLEX_SPI_CSR_BITS_15_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_16 = FLEX_SPI_CSR_BITS_16_BIT_Val << FLEX_SPI_CSR_BITS_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_DATA_BITS_INVALID = 0xFFFFFFFF

}FLEXCOM_SPI_DATA_BITS;

```

## Summary

Identifies SPI bits per transfer

## Description

This enumeration identifies number of bits per SPI transfer.

## Remarks

None

