# QSPIx\_Write Function

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-AA725558-EF5D-4D83-9378-06E61B172173.md)

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-83EB94B5-4BF1-4820-A486-C5B9D1099320.md)

**Parent topic:**[Quad Serial Peripheral Interface \(QSPI\)](GUID-56797157-F046-4DD8-9A9F-CFC59C3A989A.md)

## C

```c
// x - Instance of the QSPI peripheral

bool QSPIx_Write(void* pTransmitData, size_t txSize);
```

## Summary

Write data on QSPI peripheral. This is used in SPI mode only.

## Description

This function should be used to write "txSize" number of bytes on QSPI module. Data pointed by pTransmitData is transmitted.

## Precondition

The QSPIx\_Initialize function must have been called. Callback has to be registered using QSPIx\_CallbackRegister API if the peripheral instance has been configured in Interrupt mode and transfer completion status needs to be communicated back to application via callback.

## Parameters

|Param|Description|
|-----|-----------|
|\*pTransmitData|Pointer to the data which has to be transmitted. if it isNULL, that means only data receiving is expected. For 9 to 15bit mode, data should be right aligned in the 16 bit memory location.|
|txSize|Number of bytes to be transmitted. Always, size should begiven in terms of bytes. For example, if 5 16-bit data are to be transmitted, the transmit size should be 10 bytes.|

## Returns

-   In Blocking mode:

    -   API returns True once the transfer is complete. It returns False if txSize parameter is 0 and transmit data pointer is NULL.

-   In interrupt mode:

    -   If previous buffer request is not completed and a new transfer request comes, then this API will reject the new request and will return "False".

    -   Also, Same as blocking mode, It returns False if txSize parameter is 0 and transmit data pointer is NULL.


## Example

```c
uint8_t txBuffer[4];
size_t txSize = 4;
bool reqAccepted;

reqAccepted = QSPI0_Write(&txBuffer, txSize);
```

## Remarks

Non-blocking interrupt mode configuration implementation of this function will be used by Harmony driver implementation APIs.

