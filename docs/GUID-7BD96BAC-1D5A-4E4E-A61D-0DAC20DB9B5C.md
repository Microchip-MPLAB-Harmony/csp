# XDMACn\_ChannelCallbackRegister Function

**Parent topic:**[Extensible DMA Controller \(XDMAC\)](GUID-C2B02311-0F9A-41E7-92B8-C2FEEBDFE755.md)

## C

```c
// n is instance of the peripheral and it is applicable only for devices having multiple instances of the peripheral.
void XDMACn_ChannelCallbackRegister
(
XDMAC_CHANNEL channel,
const XDMAC_CHANNEL_CALLBACK eventHandler,
const uintptr_t contextHandle
)
```

## Summary

This function allows a XDMAC PLIB client to set an event handler.

## Description

This function allows a client to set an event handler. The client may want<br />to receive transfer related events in cases when it submits a XDMAC PLIB<br />transfer request. The event handler should be set before the client<br />intends to perform operations that could generate events.

This function accepts a contextHandle parameter. This parameter could be<br />set by the client to contain \(or point to\) any client specific data object<br />that should be associated with this XDMAC channel.

## Precondition

XDMAC should have been initialized by calling XDMACn\_Initialize.

## Parameters

|Param|Description|
|-----|-----------|
|channel|A specific XDMAC channel from which the events are expected.|
|eventHandler|Pointer to the event handler function.|
|contextHandle|Value identifying the context of the application/driver/middleware that registered the event handling function.|

## Returns

None.

## Example

```c
MY_APP_OBJ myAppObj;

void APP_XDMACTransferEventHandler(XDMAC_TRANSFER_EVENT event,
uintptr_t contextHandle)
{
    switch(event)
    {
        case XDMAC_TRANSFER_COMPLETE:
        // This means the data was transferred.
        break;
        
        case XDMAC_TRANSFER_ERROR:
        // Error handling here.
        break;
        
        default:
        break;
    }
}

// User registers an event handler with XDMAC channel. This is done once.
XDMAC_ChannelCallbackRegister(channel, APP_XDMACTransferEventHandler,
(uintptr_t)&myAppObj);
```

## Remarks

None.

