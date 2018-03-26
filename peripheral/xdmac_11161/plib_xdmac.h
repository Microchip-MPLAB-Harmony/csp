/*******************************************************************************
  XDMAC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_xdmac.h

  Summary
    XDMAC peripheral library interface.

  Description
    This file defines the interface to the XDMAC peripheral library.  This
    library provides access to and control of the XDMAC controller.

  Remarks:
    This header is for documentation only.  The actual plib_xdmac header
    will be generated as required by the MCC.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_XDMAC_H    // Guards against multiple inclusion
#define PLIB_XDMAC_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <stddef.h>

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
/* XDMAC Channels

  Summary:
    This lists the set of channels available for data transfer using XDMAC.

  Description:
    This lists the set of channels available for data transfer using XDMAC.

  Remarks:
    None.
*/

typedef enum {

    XDMAC_CHANNEL_0,
    XDMAC_CHANNEL_1,
    XDMAC_CHANNEL_2,
    XDMAC_CHANNEL_3,
    XDMAC_CHANNEL_4,
    XDMAC_CHANNEL_5,
    XDMAC_CHANNEL_6,
    XDMAC_CHANNEL_7,
    XDMAC_CHANNEL_8,
    XDMAC_CHANNEL_9,
    XDMAC_CHANNEL_10,
    XDMAC_CHANNEL_11,
    XDMAC_CHANNEL_12,
    XDMAC_CHANNEL_13,
    XDMAC_CHANNEL_14,
    XDMAC_CHANNEL_15,
    XDMAC_CHANNEL_16,
    XDMAC_CHANNEL_17,
    XDMAC_CHANNEL_18,
    XDMAC_CHANNEL_19,
    XDMAC_CHANNEL_20,
    XDMAC_CHANNEL_21,
    XDMAC_CHANNEL_22,
    XDMAC_CHANNEL_23,
    XDMAC_CHANNELS_NUMBER

} XDMAC_CHANNEL;


// *****************************************************************************
/* XDMAC Transfer Events

   Summary:
    Enumeration of possible XDMAC transfer events.

   Description:
    This data type provides an enumeration of all possible XDMAC transfer
    events.

   Remarks:
    None.

*/
typedef enum
{
    /* Data was transferred successfully. */
    XDMAC_TRANSFER_COMPLETE,

    /* Error while processing the request */
    XDMAC_TRANSFER_ERROR

} XDMAC_TRANSFER_EVENT;


// *****************************************************************************
/* DMA Channel Settings

  Summary:
    Defines the channel settings.

  Description:
    This data type defines the channel settings and can be used to update the
    channel settings dynamically .

  Remarks:
    This feature may not be available on all devices. Refer to the specific
    device data sheet to determine availability.
*/

typedef uint32_t XDMAC_CHANNEL_CONFIG;


// *****************************************************************************
/* DMA descriptor control

  Summary:
    Defines the descriptor control for linked list operation.

  Description:
    This data type defines the descriptor control for linked list operation.

  Remarks:
    This feature may not be available on all devices. Refer to the specific
    device data sheet to determine availability.
*/

typedef union {

    struct
    {
        /* Size of block for the current descriptor.
           This variable is not needed for the descriptor control
           parameter of XDMAC_ChannelLinkedListTransfer because block length
           for first descriptor is configured by the first descriptor itself. */
        uint32_t blockDataLength:24;

        /* Next descriptor fetch enable.
           Zero in this field indicates the end of linked list. */
        uint32_t nextDescriptorFetchEnable:1;

        /* Enable/Disable source parameters update when the descriptor
           is retrieved*/
        uint32_t nextDescriptorSrcUpdate:1;

        /* Enable/Disable destination parameters update when the descriptor
           is retrieved*/
        uint32_t nextDescriptorDestUpdate:1;

        /* Next descriptor view type.
           Views can be changed when switching descriptors. */
        uint32_t nextDescriptorView:2;

        /* Reserved */
        uint32_t :3;
    } mbr_ubc_type;

    uint32_t mbr_ubc;

} XDMAC_DESCRIPTOR_CONTROL;


// *****************************************************************************
/* DMA descriptor views

  Summary:
    Defines the different descriptor views available for master transfer.

  Description:
    This data type defines the different descriptor views available.

  Remarks:
    This feature may not be available on all devices. Refer to the specific
    device data sheet to determine availability.
*/

/* View 0 */
typedef struct {

    /* Next Descriptor Address number. */
    uint32_t mbr_nda;

    /* Micro-block Control Member. */
    XDMAC_DESCRIPTOR_CONTROL mbr_ubc;

    /* Destination Address Member. */
    uint32_t mbr_da;

} XDMAC_DESCRIPTOR_VIEW_0;

/* View 1 */
typedef struct {

    /* Next Descriptor Address number. */
    uint32_t mbr_nda;

    /* Micro-block Control Member. */
    XDMAC_DESCRIPTOR_CONTROL mbr_ubc;

    /* Source Address Member. */
    uint32_t mbr_sa;

    /* Destination Address Member. */
    uint32_t mbr_da;

} XDMAC_DESCRIPTOR_VIEW_1;

/* View 2 */
typedef struct {

    /* Next Descriptor Address number. */
    uint32_t mbr_nda;

    /* Micro-block Control Member. */
    XDMAC_DESCRIPTOR_CONTROL mbr_ubc;

    /* Source Address Member. */
    uint32_t mbr_sa;

    /* Destination Address Member. */
    uint32_t mbr_da;

    /* Configuration Register. */
    /* TODO: Redefine type to XDMAC_CC white updating to N type */
    uint32_t mbr_cfg;

} XDMAC_DESCRIPTOR_VIEW_2;

/* View 3 */
typedef struct {

    /* Next Descriptor Address number. */
    uint32_t mbr_nda;

    /* Micro-block Control Member. */
    XDMAC_DESCRIPTOR_CONTROL mbr_ubc;

    /* Source Address Member. */
    uint32_t mbr_sa;

    /* Destination Address Member. */
    uint32_t mbr_da;

    /* Configuration Register. */
    uint32_t mbr_cfg;

    /* Block Control Member. */
    uint32_t mbr_bc;

    /* Data Stride Member. */
    uint32_t mbr_ds;

    /* Source Micro-block Stride Member. */
    uint32_t mbr_sus;

    /* Destination Micro-block Stride Member. */
    uint32_t mbr_dus;

} XDMAC_DESCRIPTOR_VIEW_3;


// *****************************************************************************
/* XDMAC Transfer Event Handler Function

   Summary:
    Pointer to a XDMAC Transfer Event handler function.

   Description:
    This data type defines a XDMAC Transfer Event Handler Function.

    A XDMAC PLIB client must register a transfer event handler function of this
    type to receive transfer related events from the PLIB.

    If the event is XDMAC_TRANSFER_EVENT_COMPLETE, this means that the data
    was transferred successfully.

    If the event is XDMAC_TRANSFER_EVENT_ERROR, this means that the data was
    not transferred successfully.

    The contextHandle parameter contains the context handle that was provided by
    the client at the time of registering the event handler. This context handle
    can be anything that the client consider helpful or necessary to identify
    the client context object associated with the channel of the XDMAC PLIB that
    generated the event.

    The event handler function executes in an interrupt context of XDMAC.
    It is recommended to the application not to perform process intensive
    operations with in this function.

   Remarks:
    None.

*/
typedef void (*XDMAC_CHANNEL_CALLBACK) (XDMAC_TRANSFER_EVENT event, uintptr_t contextHandle);


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
    void XDMAC_Initialize( void )

   Summary:
    Initializes the XDMAC controller of the device.

   Description:
    This function initializes the XDMAC controller of the device as configured
    by the user from within the XDMAC manager of MCC.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
    XDMAC_Initialize();
    </code>

   Remarks:
    Stops the XDMAC controller if it was already running and reinitializes it.
*/

void XDMAC_Initialize( void );


//******************************************************************************
/*
  Function:
    void XDMAC_ChannelCallbackRegister
    (
        XDMAC_CHANNEL channel,
        const XDMAC_CHANNEL_CALLBACK eventHandler,
        const uintptr_t contextHandle
    )

  Summary:
    This function allows a XDMAC PLIB client to set an event handler.

  Description:
    This function allows a client to set an event handler. The client may want
    to receive transfer related events in cases when it submits a XDMAC PLIB
    transfer request. The event handler should be set before the client
    intends to perform operations that could generate events.

    This function accepts a contextHandle parameter. This parameter could be
    set by the client to contain (or point to) any client specific data object
    that should be associated with this XDMAC channel.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.

  Parameters:
    channel - A specific XDMAC channel from which the events are expected.

    eventHandler - Pointer to the event handler function.

    contextHandle - Value identifying the context of the
    application/driver/middleware that registered the event handling function.

  Returns:
    None.

  Example:
    <code>
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
    </code>

  Remarks:
    None.
 */

void XDMAC_ChannelCallbackRegister (XDMAC_CHANNEL channel, const XDMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle);


//******************************************************************************
/* Function:
    void XDMAC_ChannelTransfer
    (
        XDMAC_CHANNEL channel,
        const void *srcAddr,
        const void *destAddr,
        size_t blockSize
    )

  Summary:
    Adds a data transfer to a XDMAC channel and enables the channel to start
    data transfer.

  Description:
    This function adds a single block data transfer characteristics for a
    specific XDMAC channel. It also enables the channel to start data transfer.

    If the requesting client registered an event callback with the PLIB,
    the PLIB will issue a XDMAC_TRANSFER_COMPLETE event if the transfer was
    processed successfully and XDMAC_TRANSFER_ERROR event if the transfer was
    not processed successfully.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.

  Parameters:
    channel - A specific XDMAC channel

    srcAddr - Source of the XDMAC transfer

    destAddr - Destination of the XDMAC transfer

    blockSize - Size of the transfer block

  Returns:
    None.

  Example:
    <code>
    // Transfer 10 bytes of data to UART TX using XDMAC channel 1
    MY_APP_OBJ myAppObj;
    uint8_t buf[10] = {0,1,2,3,4,5,6,7,8,9};
    void *srcAddr = (uint8_t *) buf;
    void *destAddr = (uin8_t*) &U1TXREG;
    size_t size = 10;

    // User registers an event handler with PLIB. This is done once.
    XDMAC_ChannelCallbackRegister(APP_XDMACTransferEventHandler,
        (uintptr_t)&myAppObj);

    XDMAC_ChannelTransfer(XDMAC_CHANNEL_1, srcAddr, destAddr, size);
    </code>

  Remarks:
    The source/destination buffers should be made coherent and aligned to the
    device cache line size to avoid the cache coherency issues.
    For example:
    <code>
    uint8_t buffer[1024];
    uint8_t __attribute__((coherent)) __attribute__((aligned(32))) buffer[1024];
    </code>
*/

void XDMAC_ChannelTransfer (XDMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize);


//******************************************************************************
/* Function:
    void XDMAC_ChannelLinkedListTransfer
    (
        XDMAC_CHANNEL channel,
        uint32_t descriptor,
        XDMAC_DESCRIPTOR_CONTROL* descriptorControl
    )

  Summary:
    Sets up a multi-block data transfer on a specified XDMAC channel using
    linked list feature.

  Description:
    This function sets up multi-block data transfer for a XDMAC channel by
    linked list operation mode. That is each block of data to be transferred
    is configured as descriptors of a linked list.
    Each descriptor can be defined in any available descriptor view formats and
    the views are available as XDMAC_DESCRIPTOR_VIEW_x.

    Specified XDMAC channel will be enabled by default upon linked list
    addition. Upon each block transfer completion XDMAC PLIB will call event
    handler if the event handler is registered through
    XDMAC_ChannelCallbackRegister.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.
    Linked list with descriptors in any available descriptor view formats must
    be defined.

  Parameters:
    channel - A specific XDMAC channel

    descriptor - Address of the first descriptor of the linked list.
    All descriptors must be defined in the device specific view formats
    available as XDMAC_DESCRIPTOR_VIEW_x and must be cache line aligned.

    descriptorControl - Control settings for the first descriptor.
    This must be defined in device specific view format,
    XDMAC_DESCRIPTOR_CONTROL and must be cache line aligned.

  Returns:
    None.

  Example:
    <code>
    // Transfer 2 blocks of data to UART TX, each 10 bytes.

    //Two blocks of data
    char src1[11] = {"1234567890"};
    char src2[11] = {"ABCDEFGHIJ"};

    //Cache line aligned first descriptor control, "descptr_crtl"
    //Cache line aligned linked list with descriptors in any supported view,
    //"linkedList1[2]" with 2 descriptors of different source addresses.

    // User registers an event handler with PLIB.
    XDMAC_ChannelCallbackRegister(handle, APP_XDMAC_TransferEventHandler,
        NULL);

    // Add linked list to the XDMAC PLIB, channel will be enabled by default.
    XDMAC_ChannelLinkedListTransfer(XDMAC_CHANNEL_1, (uint32_t)&linkedList1[0],
        &descptr_crtl);
    </code>

  Remarks:
    This is supported by only the devices with multi-block transfer feature.
    The "descriptorControl" parameter is a XDMAC hardware version specific
    requirement and may not be needed in some of the devices.
*/

void XDMAC_ChannelLinkedListTransfer (XDMAC_CHANNEL channel, uint32_t descriptor, XDMAC_DESCRIPTOR_CONTROL* descriptorControl);


//******************************************************************************
/* Function:
    bool XDMAC_ChannelIsBusy (XDMAC_CHANNEL channel)

  Summary:
    Returns the busy status of a specific XDMAC Channel.

  Description:
    This function returns the busy status of the XDMAC channel.
    XDMAC channel will be busy if any transfer is in progress.

    This function can be used to check the status of the channel prior to
    submitting a transfer request. And this can also be used to check the status
    of the submitted request if callback mechanism is not preferred.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.

  Parameters:
    channel - A specific XDMAC channel

  Returns:
    Busy status of the specific channel.
    True - Channel is busy
    False - Channel is free

  Example:
    <code>
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
    </code>

  Remarks:
    None.
*/

bool XDMAC_ChannelIsBusy (XDMAC_CHANNEL channel);


//******************************************************************************
/* Function:
    XDMAC_CHANNEL_SETTINGS XDMAC_ChannelSettingsGet (XDMAC_CHANNEL channel)

  Summary:
    Returns the channel settings of a specific XDMAC Channel.

  Description:
    This function returns the channel settings of the XDMAC channel.

    This function can be used along with the XDMAC_ChannelSettingsSet to update
    any specific setting of the XDMAC channel.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.

  Parameters:
    channel - A specific XDMAC channel

  Returns:
    Settings of a specific channel.

  Example:
    <code>
    //Update the transfer direction dynamically which was set to
    //PER2MEM from within DMA manager to MEM2PER.
    XDMAC_CHANNEL_CONFIG settings = 0;
    settings = XDMAC_ChannelSettingsGet(XDMAC_CHANNEL_0);
    settings = (settings & ~XDMAC_CC_DSYNC_Msk) | XDMAC_CC_DSYNC_MEM2PER;
    XDMAC_ChannelSettingsSet(XDMAC_CHANNEL_0, settings);
    </code>

  Remarks:
    Use macro definitions from the packs header to compare with the settings.
*/

XDMAC_CHANNEL_CONFIG XDMAC_ChannelSettingsGet (XDMAC_CHANNEL channel);


//******************************************************************************
/* Function:
    bool XDMAC_ChannelSettingsSet (XDMAC_CHANNEL channel,
        XDMAC_CHANNEL_SETTINGS setting)

  Summary:
    Sets the channel settings of a specific XDMAC Channel.

  Description:
    This function sets the channel settings of the XDMAC channel.

    This function can be used along with the XDMAC_ChannelSettingsGet to update
    any specific setting of the XDMAC channel.
    Any ongoing transaction of the specified XDMAC channel will be aborted when
    this function is called.

  Precondition:
    XDMAC should have been initialized by calling XDMAC_Initialize.

  Parameters:
    channel - A specific XDMAC channel
    setting - Settings for a channel

  Returns:
    Settings update status.
    True - Channel settings are updated successfully.
    False - Channel settings update failed.

  Example:
    <code>
    //Update the transfer direction dynamically which was set to
    //PER2MEM from within DMA manager to MEM2PER.
    XDMAC_CHANNEL_CONFIG settings = 0;
    settings = XDMAC_ChannelSettingsGet(XDMAC_CHANNEL_0);
    settings = (settings & ~XDMAC_CC_DSYNC_Msk) | XDMAC_CC_DSYNC_MEM2PER;
    XDMAC_ChannelSettingsSet(XDMAC_CHANNEL_0, settings);
    </code>

  Remarks:
    Use macro definitions from the packs header to construct a new setting.
*/

bool XDMAC_ChannelSettingsSet (XDMAC_CHANNEL channel, XDMAC_CHANNEL_CONFIG setting);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_XDMAC_H
