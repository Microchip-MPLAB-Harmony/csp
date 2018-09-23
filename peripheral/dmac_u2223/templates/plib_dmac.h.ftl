/*******************************************************************************
  DMAC Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dmac${DMAC_INDEX}.h

  Summary:
    DMAC peripheral library interface.

  Description:
    This file defines the interface to the DMAC peripheral library. This
    library provides access to and control of the DMAC controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_DMAC${DMAC_INDEX}_H    // Guards against multiple inclusion
#define PLIB_DMAC${DMAC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include <device.h>
#include <string.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* DMAC Channels

  Summary:
    Lists the set of channels available for data transfer using DMAC.

  Description:
    This enumeration lists the set of channels available for data transfer using
    DMAC. Only channels that are configured in MHC will be available in this
    enumeration. The application should use the enumerators in the enum-list to
    identify the channel to be operated on. The application should not rely on
    the enumerator constant expression as this may change across devices.

  Remarks:
    None.
*/

typedef enum
{
<#list 0..DMAC_HIGHEST_CHANNEL - 1 as i>
    <#assign DMAC_CHCTRLA_ENABLE    = "DMAC_ENABLE_CH_"  + i>
    <#if (.vars[DMAC_CHCTRLA_ENABLE] == true)>
    /* DMAC Channel ${i} */
    DMAC_CHANNEL_${i} = ${i},
    </#if>
</#list>
} DMAC_CHANNEL;

// *****************************************************************************
/* DMAC Transfer Events

  Summary:
    Enumeration of possible DMAC transfer events.

  Description:
    This data type provides an enumeration of all possible DMAC transfer events.
    A data value of this type is returned in the DMAC callback function and
    indicates if the completed transfer was successful.

  Remarks:
    None.
*/

typedef enum
{
    /* Data was transferred successfully. */
    DMAC_TRANSFER_EVENT_COMPLETE,

    /* Error while processing the request */
    DMAC_TRANSFER_EVENT_ERROR

} DMAC_TRANSFER_EVENT;

// *****************************************************************************
/* DMAC Channel Settings

  Summary:
    Defines the channel settings.

  Description:
    This data type defines the channel settings and can be used to update the
    channel settings dynamically .

  Remarks:
    This feature may not be available on all devices. Refer to the specific
    device data sheet to determine availability.
*/

typedef uint32_t DMAC_CHANNEL_CONFIG;

// *****************************************************************************
/* DMAC Transfer Event Handler Function

  Summary:
    Pointer to a DMAC Transfer Event handler function.

  Description:
    This data type defines a DMAC Transfer Event Handler Function.  A DMAC PLIB
    client must register a transfer event handler function of this type to
    receive transfer related events from the PLIB.

    If the event is DMAC_TRANSFER_EVENT_COMPLETE, this means that the data
    was transferred successfully.

    If the event is DMAC_TRANSFER_EVENT_ERROR, this means that the data was
    not transferred successfully.

    The contextHandle parameter contains the context handle that was provided by
    the client at the time of registering the event handler. This context handle
    can be anything that the client considers helpful or necessary to identify
    the client context associated with the DMAC channel that generated the
    event.

    The event handler function executes in an interrupt context of DMAC.  It is
    recommended to the application not to perform process intensive operations
    with in this function.

  Remarks:
    None.
*/

typedef void (*DMAC_CHANNEL_CALLBACK) (DMAC_TRANSFER_EVENT event, uintptr_t contextHandle);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_Initialize( void )

  Summary:
    Initializes the DMAC controller of the device.

  Description:
    This function initializes the DMAC controller of the device as configured
    by the user from within the DMAC manager of MHC.

  Precondition:
    The DMAC module clock requirements should have been configured in the MHC
    Clock Manager utility.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    DMAC${DMAC_INDEX}_Initialize();
    </code>

  Remarks:
    Stops the DMAC controller if it was already running and reinitializes it.
*/

void DMAC${DMAC_INDEX}_Initialize( void );

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelCallbackRegister
    (
        DMAC_CHANNEL channel,
        const DMAC_CHANNEL_CALLBACK eventHandler,
        const uintptr_t contextHandle
    )

  Summary:
    This function allows a DMAC PLIB client to set an event handler.

  Description:
    This function allows a client to set an event handler. The client may want
    to receive transfer related events in cases when it submits a DMAC PLIB
    transfer request. The event handler should be set before the client
    intends to perform operations that could generate events.

    In case of linked transfer descriptors, the callback function will be called
    for every transfer in the transfer descriptor chain. The application must
    implement it's own logic to link the callback to the the transfer descriptor
    being completed.

    This function accepts a contextHandle parameter. This parameter could be
    set by the client to contain (or point to) any client specific data object
    that should be associated with this DMAC channel.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    channel - A specific DMAC channel from which the events are expected.

    eventHandler - Pointer to the event handler function.

    contextHandle - Value identifying the context of the
    application/driver/middleware that registered the event handling function.

  Returns:
    None.

  Example:
    <code>
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
    DMAC${DMAC_INDEX}_ChannelCallbackRegister(channel, APP_DMACTransferEventHandler, (uintptr_t)&myAppObj);
    </code>

  Remarks:
    None.
*/

void DMAC${DMAC_INDEX}_ChannelCallbackRegister (DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle);

//******************************************************************************
/* Function:
    bool DMAC${DMAC_INDEX}_ChannelTransfer
    (
        DMAC_CHANNEL channel,
        const void *srcAddr,
        const void *destAddr,
        size_t blockSize
    )

  Summary:
    Schedules a DMA transfer on the specified DMA channel.

  Description:
    This function schedules a DMA transfer on the specified DMA channel and
    starts the transfer when the configured trigger is received. The transfer is
    processed based on the channel configuration performed in the DMA manager.
    The channel parameter specifies the channel to be used for the transfer.

    The srcAddr parameter specifies the source address from where data will be
    transferred. This address will override the source address which was
    specified at the time of configuring the channel in DMA Manager. When a
    trigger is received, the module will transfer beat size of data from the
    source address. In such a case, the source address is typically a result
    register of the peripheral generating the trigger. For a memory to memory
    transfer, the srcAddress parameter points to the source address location in
    RAM.

    The destAddr parameter specifies the address location where the data will be
    stored. This parameter will override the setting in MHC. If the destination
    address is a peripheral register, the channel trigger may be an interrupt
    generated by the peripheral. In case of a memory to memory transfer, this is
    the address where the data will be stored.

    If the channel is configured for software trigger, calling the channel
    transfer function will set the source and destination address and will also
    start the transfer. If the channel was configured for a peripheral trigger,
    the channel transfer function will set the source and destination address
    and will transfer data when a trigger has occurred.

    If the requesting client registered an event callback function before
    calling the channel transfer function, this function will be called when the
    transfer completes. The callback function will be called with a
    DMAC_TRANSFER_COMPLETE event if the transfer was processed successfully and
    a DMAC_TRANSFER_ERROR event if the transfer was not processed successfully.

    When already a transfer is in progress, this API will return false indicating
    that transfer request is not accepted.

  Precondition:
    DMAC should have been initialized by calling the DMAC${DMAC_INDEX}_Initialize.
    The required channel transfer parameters such as beat size, source and
    destination address increment should have been configured in MHC.

  Parameters:
    channel - The DMAC channel that should be used for the transfer.

    srcAddr - Source address of the DMAC transfer

    destAddr - Destination address of the DMAC transfer

    blockSize - Size of the transfer block in bytes.

  Returns:
    True - If transfer request is accepted.
    False - If previous transfer is in progress and the request is rejected.

  Example:
    <code>
    // Transfer 10 bytes of data to UART TX using DMAC channel 1
    MY_APP_OBJ myAppObj;
    uint8_t buf[10] = {0,1,2,3,4,5,6,7,8,9};
    void *srcAddr = (uint8_t *) buf;
    void *destAddr = (uin8_t*) &U1TXREG;
    size_t size = 10;

    // User registers an event handler with PLIB. This is done once.
    DMAC${DMAC_INDEX}_ChannelCallbackRegister(APP_DMACTransferEventHandler,
        (uintptr_t)&myAppObj);

    if(DMAC${DMAC_INDEX}_ChannelTransfer(DMAC_CHANNEL_1, srcAddr, destAddr, size) == true)
    {
        // do something else
    }
    else
    {
        // try again?
    }
    </code>

  Remarks:
    None.
*/

bool DMAC${DMAC_INDEX}_ChannelTransfer (DMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize);

// *****************************************************************************
/* Function:
    bool DMAC${DMAC_INDEX}_ChannelIsBusy ( DMAC_CHANNEL channel );

  Summary:
    The function returns the busy status of the channel.

  Description:
    The function returns true if the specified channel is busy with a transfer.
    This function can be used to poll for the completion of transfer that was
    started by calling the DMAC${DMAC_INDEX}_ChannelTransfer() function. This
    function can be used as a polling alternative to the setting a callback
    function and receiving an asynchronous notification for transfer
    notification.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    channel - The DMAC channel whose status needs to be checked.

  Returns:
    true - The channel is busy with an on-going transfer.

    false - The channel is not busy and is available for a transfer.

  Example:
    <code>
    // Wait while the channel is busy.
    while(DMAC${DMAC_INDEX}_ChannelIsBusy (DMAC_CHANNEL_0));
    </code>

  Remarks:
    None.
*/

bool DMAC${DMAC_INDEX}_ChannelIsBusy ( DMAC_CHANNEL channel );

// ******************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_ChannelDisable ( DMAC_CHANNEL channel );

  Summary:
    The function disables the specified DMAC channel.

  Description:
    The function disables the specified DMAC channel. Once disabled, the channel
    will ignore triggers and will not transfer data till the next time a
    DMAC${DMAC_INDEX}_ChannelTransfer function is called.  If there is a
    transfer already in progress, this will aborted. If there were multiple
    linked transfers assigned on the channel, the on-going transfer will be
    aborted and the other descriptors will be discarded.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    channel - The DMAC channel whose status needs to be checked.

  Returns:
    None.

  Example:
    <code>
    // Disable the channel.
    DMAC${DMAC_INDEX}_ChannelDisable (DMAC_CHANNEL_0);
    </code>

  Remarks:
    None.
*/

void DMAC${DMAC_INDEX}_ChannelDisable ( DMAC_CHANNEL channel );

<#if DMAC_LL_ENABLE = true>
// ******************************************************************************
/* Function:
    bool DMAC${DMAC_INDEX}_ChannelLinkedListTransfer ( DMAC_CHANNEL channel,
                                     dmacdescriptor_registers_t * channelDesc );

  Summary:
    The function submit a list of DMA transfers.

  Description:
    The function will submit a list of DMA transfers. The DMA channel will
    process all transfers in the list. The transfers will be processed in the
    order in which they added to the list. Each transfer in the list is
    specified by a DmacDescriptor type descriptor. The list is formed by linking
    of the descriptors. While processing each descriptor in the linked list, the
    DMA transfer settings will be updated based on the settings contained in the
    descriptor.

    It is possible to link the last descriptor in the list to the first
    descriptor. This results in an undisrupted transfer sequence. Such type of
    circular linked descriptor list are useful in audio applications. The DMAC
    module will generate a callback for each transfer in the descriptor list.
    The application must keep track of transfer being completed and should only
    modify the descriptors which have been processed.

    The application must submit the entire list while calling the function.
    Adding or inserting of descriptors to a submitted list is not supported. The
    application can change the transfer parameters such as transfer beat size,
    source and address increment step size. This will override the transfer
    setting defined in MHC.

    The BLOCKACT field of the last DMA transfer descriptor in the descriptor
    linked list should be set to the value 0x0 i.e. this should be set to
    disable the channel when the last transfer has been completed. Setting this
    field to any other value will interfere with the operation of the DMAC
    peripheral library.

    When already a transfer is in progress, this API will return false indicating
    that transfer request is not accepted.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.
    The Transfer Linked Option in MHC should have been enabled.

  Parameters:
    channel - The DMAC channel on which the transfer needs to scheduled.

    channelDesc - A pointer to a linked list of DmacDescriptor type descriptor
    chain. Each of the descriptors must be placed at a 128-bit aligned
    SRAM address. If these descriptors belong to an array of descriptors, then
    configuring the starting address of the array at a 128-bit aligned address
    will ensure that all descriptors of the array starts at 128-bit aligned
    address, because the size of each descriptor is 128-bits.

  Returns:
    True - If transfer request is accepted.
    False - If previous transfer is in progress and the request is rejected.

  Example:
    <code>
    // Process a transfer list called transferList. Refer to the DMAC PLIB demo
    // application example for more details on usage.
    if (DMAC${DMAC_INDEX}_ChannelLinkedListTransfer(DMAC_CHANNEL_0, transferList) == true)
    {
        // do something else
    }
    else
    {
        // try again?
    }
    </code>

  Remarks:
    None.
*/

bool DMAC${DMAC_INDEX}_ChannelLinkedListTransfer ( DMAC_CHANNEL channel, dmacdescriptor_registers_t * channelDesc );
</#if>

// ******************************************************************************
/* Function:
    DMAC_CHANNEL_CONFIG  DMAC${DMAC_INDEX}_ChannelSettingsGet ( DMAC_CHANNEL channel );

  Summary:
    Returns the current channel settings for the specified DMAC Channel

  Description:
    This function returns the current channel setting for the specified DMAC
    channel. The application can use this function along with the
    DMAC${DMAC_INDEX}_ChannelSettingsSet function to analyze and if required
    change the transfer parameters of the DMAC channel at run time.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    channel - The DMAC channel whose channel settings need to be obtained.

  Returns:
    Value representing the current DMAC channel setting.

  Example:
    <code>
    // Change the beat size of DMAC Channel 0
    DMAC_CHANNEL_CONFIG settings = 0;
    settings = DMAC${DMAC_INDEX}_ChannelSettingsGet(DMAC_CHANNEL_0);
    settings = (settings & ~DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Msk) | DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_HWORD;
    DMAC${DMAC_INDEX}_ChannelSettingsSet(DMAC_CHANNEL_0, settings);
    </code>

  Remarks:
    None.
*/

DMAC_CHANNEL_CONFIG  DMAC${DMAC_INDEX}_ChannelSettingsGet ( DMAC_CHANNEL channel );

// ******************************************************************************
/* Function:
    bool  DMAC${DMAC_INDEX}_ChannelSettingsSet ( DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG settings );

  Summary:
    Changes the current transfer settings of the specified DMAC channel.

  Description:
    This function changes the current transfer settings of the specified DMAC
    channel.  The application can use this function along with the
    DMAC${DMAC_INDEX}_ChannelSettingsGet function to analyze and if required
    change the transfer parameters of the DMAC channel at run time.

    Calling this function while a transfer is in progress could result in
    unpredictable module operation. The application can use the
    DMAC${DMAC_INDEX}_ChannelTransfer() function to check if the channel is not
    busy and then change the channel settings. The new channel settings will be
    applicable on the next transfer that is schedule using the
    DMAC${DMAC_INDEX}_ChannelTransfer() function.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    channel - The DMAC channel whose channel settings need to be obtained.

    settings - A DMAC_CHANNEL_CONFIG type value containing the channel settings.

  Returns:
    true - The channel settings were updated successfully.

    false - The channel settings were not updated.

  Example:
    <code>
    // Change the beat size of DMAC Channel 0
    DMAC_CHANNEL_CONFIG settings = 0;
    settings = DMAC${DMAC_INDEX}_ChannelSettingsGet(DMAC_CHANNEL_0);
    settings = (settings & ~DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Msk) | DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_HWORD;
    DMAC${DMAC_INDEX}_ChannelSettingsSet(DMAC_CHANNEL_0, settings);
    </code>

  Remarks:
    None.
*/

bool  DMAC${DMAC_INDEX}_ChannelSettingsSet ( DMAC_CHANNEL channel, DMAC_CHANNEL_CONFIG settings );

// *****************************************************************************
/* Function:
    void DMAC${DMAC_INDEX}_InterruptHandler( void );

  Summary:
    Handles the DMA interrupt events.

  Description:
    This function handles the DMA interrupt events.

  Precondition:
    DMAC should have been initialized by calling DMAC${DMAC_INDEX}_Initialize.

  Parameters:
    None.

  Example:
    <code>
    DMAC${DMAC_INDEX}_InterruptHandler();
    </code>

   Remarks:
    None.
*/

void DMAC${DMAC_INDEX}_InterruptHandler( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_DMAC${DMAC_INDEX}_H
