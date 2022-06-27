# MEM2MEM\_ChannelCallbackRegister Function

**Parent topic:**[Memory to Memory \(MEM2MEM\)](GUID-692A056B-1150-4194-963B-E39865A3B3C3.md)

## C

```c
void MEM2MEM_ChannelCallbackRegister(MEM2MEM_CALLBACK callback, uintptr_t context)
```

## Summary

This function allows a MEM2MEM PLIB client to set a callback.

## Description

This function allows a client to set a callback. The client may want<br />to receive transfer related events in cases when it submits a MEM2MEM PLIB<br />transfer request. The callback should be set before the client<br />intends to perform operations that could generate events.

This function accepts a context parameter. This parameter could be<br />set by the client to contain \(or point to\) any client specific data object<br />that should be associated with this MEM2MEM channel.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|callback|Pointer to the callback function.|
|context|Value identifying the context of the application/driver/middleware that registered the event handling function|

## Returns

None.

## Example

```c
MY_APP_OBJ myAppObj;

void APP_MEM2MEMTransferEventHandler(MEM2MEM_TRANSFER_EVENT event,
uintptr_t contextHandle)
{
    switch(event)
    {
        case MEM2MEM_TRANSFER_COMPLETE:
        // This means the data was transferred.
        break;
        
        case MEM2MEM_TRANSFER_ERROR:
        // Error handling here.
        break;
        
        default:
        break;
    }
}

// User registers an callback with MEM2MEM channel. This is done once.
MEM2MEM_ChannelCallbackRegister(APP_MEM2MEMTransferEventHandler, (uintptr_t)&myAppObj);
```

## Remarks

None.

