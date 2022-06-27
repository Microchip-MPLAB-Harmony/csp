# DMAC\_ChannelCallbackRegister Function

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-BC288F92-E404-40EC-B68F-833F6E346C3F.md)

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-725BAB37-D872-43F1-818D-6350B9533DF3.md)

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-FF4E46D0-1926-4335-942C-7767A23A991D.md)

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-2C5A3108-4274-4720-A95E-8017AA500BB4.md)

## C

```c
void DMAC_ChannelCallbackRegister
(
DMAC_CHANNEL channel,
const DMAC_CHANNEL_CALLBACK eventHandler,
const uintptr_t contextHandle
)
```

## Summary

This function allows a DMAC PLIB client to set an event handler.

## Description

This function allows a client to set an event handler. The client may want<br />to receive transfer related events in cases when it submits a DMAC PLIB<br />transfer request. The event handler should be set before the client<br />intends to perform operations that could generate events.

In case of linked transfer descriptors, the callback function will be called<br />for every transfer in the transfer descriptor chain. The application must<br />implement it's own logic to link the callback to the the transfer descriptor<br />being completed.

This function accepts a contextHandle parameter. This parameter could be<br />set by the client to contain \(or point to\) any client specific data object<br />that should be associated with this DMAC channel.

## Precondition

DMAC should have been initialized by calling DMAC\_Initialize.

## Parameters

|Param|Description|
|-----|-----------|
|channel|A specific DMAC channel from which the events are expected.|
|eventHandler|Pointer to the event handler function.|
|contextHandle|Value identifying the context of the application/driver/middleware that registered the event handling function.|

## Returns

None.

## Example

```c
MY_APP_OBJ myAppObj;

void APP_DMACTransferEventHandler(DMAC_TRANSFER_EVENT event,
uintptr_t contextHandle)
{
    switch(event)
    {
        case DMAC_TRANSFER_COMPLETE:
        // This means the data was transferred.
        break;
        
        case DMAC_TRANSFER_ERROR:
        // Error handling here.
        break;
        
        default:
        break;
    }
}

// User registers an event handler with DMAC channel. This is done once.
DMAC_ChannelCallbackRegister(DMAC_CHANNEL_0, APP_DMACTransferEventHandler, (uintptr_t)&myAppObj);
```

## Remarks

None.

