# DMAC\_ChainTransferSetup Function

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-FF4E46D0-1926-4335-942C-7767A23A991D.md)

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-2C5A3108-4274-4720-A95E-8017AA500BB4.md)

## C

```c
bool DMAC_ChainTransferSetup( DMAC_CHANNEL channel, const void *srcAddr,
size_t srcSize, const void *destAddr, size_t destSize, size_t cellSize);
```

## Summary

Setup a DMA channel for chain transfer

## Description

This function sets up a DMA channel for chain mode of transfer. The actual<br />transfer doesn't start by using this function.

In chained mode, more than one DMA channels are linked to each other.<br />DMAC\_ChainTransferSetup API should be used to setup all the chained channels<br />except the first channel of the chain. First channel of the chain should be<br />setup and enabled using DMAC\_ChannelTransfer API. Once the first channel<br />transfer is completed, next channel of the chain is automatically enabled<br />and based on its setup, it completes the transfer and chain continues.

If callback is registered for any of the channel which is part of the chain,<br />callback function will be called when the transfer of corresponding channel<br />completes. The callback function will be called with a DMAC\_TRANSFER\_COMPLETE<br />event if the transfer was processed successfully and a DMAC\_TRANSFER\_ERROR<br />event if the transfer was not processed successfully.

When already a transfer is in progress, this API will return false indicating<br />that transfer setup is not accepted.

## Precondition

-   DMAC should have been initialized by calling the DMAC\_Initialize.

-   Channels chaining order should be appropriately configured in MHC


configuration tree

## Parameters

|Param|Description|
|-----|-----------|
|DMAC\_CHANNEL channel|DMA channel to be setup|
|srcAddr|pointer to source data|
|srcSize|Size of the source|
|destAddr|pointer to where data is to be moved to|
|destSize|Size of the destination|
|cellSize|Size of the cell|

## Returns

*- true* - If setup request is accepted.

*- false* - If previous transfer is in progress and the setup request is rejected.

## Example

```c
// Transfer 10 bytes of data to UART TX using DMAC channel 1
uint8_t buf1[10] = {0,1,2,3,4,5,6,7,8,9};
uint8_t buf2[10] = {10,11,12,13,14,15,16,17,18,19};
    void *srcAddr = (uint8_t *) buf1;
    void *destAddr = (uin8_t*) &SPI1BUF;
    size_t size = 10;
    
    // setup channel 2, it should be configured in MHC to be chained after channel 1
    DMAC_ChainTransferSetup(DMAC_CHANNEL_2, (void *)&buf2, size, destAddr, 1, 1)
    // setup and enable channel 1, once its transfer completes, channel 2 will be automatically enabled
    DMAC_ChannelTransfer(DMAC_CHANNEL_1, (void *)&buf1, size, destAddr, 1, 1)
    
```

## Remarks

None.

