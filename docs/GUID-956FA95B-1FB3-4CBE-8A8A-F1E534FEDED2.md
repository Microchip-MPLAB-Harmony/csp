# XDMACn\_ChannelIsBusy Function

**Parent topic:**[Extensible DMA Controller \(XDMAC\)](GUID-C2B02311-0F9A-41E7-92B8-C2FEEBDFE755.md)

## C

```c
// n is instance of the peripheral and it is applicable only for devices having multiple instances of the peripheral.
bool XDMACn_ChannelIsBusy (XDMAC_CHANNEL channel)
```

## Summary

Returns the busy status of a specific XDMAC Channel.

## Description

This function returns the busy status of the XDMAC channel.<br />XDMAC channel will be busy if any transfer is in progress.

This function can be used to check the status of the channel prior to<br />submitting a transfer request. And this can also be used to check the status<br />of the submitted request if callback mechanism is not preferred.

## Precondition

XDMAC should have been initialized by calling XDMACn\_Initialize.

## Parameters

|Param|Description|
|-----|-----------|
|channel|A specific XDMAC channel|

## Returns

Busy status of the specific channel.<br />*- True* - Channel is busy

*- False* - Channel is free

## Example

```c
// Transfer 10 bytes of data to UART TX using XDMAC channel 1
MY_APP_OBJ myAppObj;
uint8_t buf[10] = {0,1,2,3,4,5,6,7,8,9};
    void *srcAddr = (uint8_t *) buf;
    void *destAddr = (uin8_t*) &U1TXREG;
    size_t size = 10;
    
    if(false == XDMAC_ChannelIsBusy(XDMAC_CHANNEL_1))
    {
        XDMAC_ChannelTransfer(XDMAC_CHANNEL_1, srcAddr, destAddr, size);
    }
```

## Remarks

None.

