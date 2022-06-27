# DMAC\_ChannelLinkedListTransfer Function

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-BC288F92-E404-40EC-B68F-833F6E346C3F.md)

**Parent topic:**[Direct Memory Access Controller \(DMAC\)](GUID-725BAB37-D872-43F1-818D-6350B9533DF3.md)

## C

```c
bool DMAC_ChannelLinkedListTransfer ( DMAC_CHANNEL channel,
dmacdescriptor_registers_t * channelDesc );
```

## Summary

The function submit a list of DMA transfers.

## Description

The function will submit a list of DMA transfers. The DMA channel will<br />process all transfers in the list. The transfers will be processed in the<br />order in which they added to the list. Each transfer in the list is<br />specified by a DmacDescriptor type descriptor. The list is formed by linking<br />of the descriptors. While processing each descriptor in the linked list, the<br />DMA transfer settings will be updated based on the settings contained in the<br />descriptor.

It is possible to link the last descriptor in the list to the first<br />descriptor. This results in an continuous transfer sequence. Such type of<br />circular linked descriptor list are useful in audio applications. The DMAC<br />module will generate a callback for each transfer in the descriptor list.<br />The application must keep track of transfer being completed and should only<br />modify the descriptors which have been processed.

The application must submit the entire list while calling the function.<br />Adding or inserting of descriptors to a submitted list is not supported. The<br />application can change the transfer parameters such as transfer beat size,<br />source and address increment step size. This will override the transfer<br />setting defined in MHC.

The BLOCKACT field of the last DMA transfer descriptor in the descriptor<br />linked list should be set to the value 0x0 i.e. this should be set to<br />disable the channel when the last transfer has been completed. Setting this<br />field to any other value will interfere with the operation of the DMAC<br />peripheral library.

When already a transfer is in progress, this API will return false indicating<br />that transfer request is not accepted.

## Precondition

DMAC should have been initialized by calling DMAC\_Initialize. The Transfer Linked Option in MHC should have been enabled.

## Parameters

|Param|Description|
|-----|-----------|
|channel|The DMAC channel on which the transfer needs to scheduled.|
|channelDesc|A pointer to a linked list of DmacDescriptor type descriptor chain. Each of the descriptors must be placed at a 128-bit aligned SRAM address. If these descriptors belong to an array of descriptors, then configuring the starting address of the array at a 128-bit aligned address will ensure that all descriptors of the array starts at 128-bit aligned address, because the size of each descriptor is 128-bits.|

## Returns

*- True* - If transfer request is accepted.

*- False* - If previous transfer is in progress and the request is rejected.

## Example

```c
// Process a transfer list called transferList. Refer to the DMAC PLIB demo
// application example for more details on usage.
if (DMAC_ChannelLinkedListTransfer(DMAC_CHANNEL_0, transferList) == true)
{
    // do something else
}
else
{
    // try again?
}
```

## Remarks

None.

