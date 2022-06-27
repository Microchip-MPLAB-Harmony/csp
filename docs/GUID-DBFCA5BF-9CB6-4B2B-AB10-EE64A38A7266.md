# QSPIx\_RegisterRead Function

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-AA725558-EF5D-4D83-9378-06E61B172173.md)

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-83EB94B5-4BF1-4820-A486-C5B9D1099320.md)

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-56797157-F046-4DD8-9A9F-CFC59C3A989A.md)

## C

```c
// x - Instance of the QSPI peripheral

bool QSPIx_RegisterRead
(
qspi_register_xfer_t *qspi_register_xfer,
uint32_t *rx_data,
uint8_t rx_data_length
);
```

## Summary

Reads particular register of QSPI slave device.

## Description

This function can be used to read a particular register of QSPI slave device which has a command code associated to it.

## Precondition

QSPIx\_Initialize must have been called for the associated QSPI instance.

## Parameters

|Param|Description|
|-----|-----------|
|\*qspi\_register\_xfer|pointer to QSPI register transfer structure holding the instructioncode register and instruction frame register information. \\|
|\*rx\_data|Pointer to receive buffer where the register data will be stored.|
|rx\_data\_length|Register width in bytes.|

## Returns

-   True on transfer request success.

-   False on transfer request failure.


## Example

```c
#define READ_STATUS_REG_CODE 0x05

static qspi_register_xfer_t qspi_register_xfer;
static uint8_t reg_data;

// Use QAUD SPI Lane
qspi_register_xfer.width = QUAD_CMD;
qspi_register_xfer.dummy_cycles = 2;

// Read status register of 1 Byte width
qspi_register_xfer.instruction = READ_STATUS_REG_CODE;

if (QSPI0_RegisterRead(&qspi_register_xfer, (uint32_t *)&reg_data, 1) == false)
{
    // Handle Error
}

```

