/*******************************************************************************
  DMAC Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMA_INSTANCE_NAME?lower_case}.h

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
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_${DMA_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${DMA_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <device.h>
#include <string.h>
#include <stdbool.h>
#include <sys/kmem.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: type definitions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* DMA error type

  Summary:
    Identifies the available DMA operating modes.

  Description:
    This data type Identifies if a transfer had an address error or not.


  Remarks:
    The identification of an error transaction takes place in the DMA ISR.
*/
typedef enum
{
    /* Data was transferred successfully. */
    DMAC_ERROR_NONE /*DOM-IGNORE-BEGIN*/ = 1, /* DOM-IGNORE-END*/

    /* DMA address error. */
    DMAC_ERROR_ADDRESS_ERROR /*DOM-IGNORE-BEGIN*/ = 2 /* DOM-IGNORE-END*/

} DMAC_ERROR;

// *****************************************************************************
/* DMA transfer event

  Summary:
    Identifies the status of the transfer event.

  Description:
    Used to report back, via registered callback, the status of a transaction.

  Remarks:
    None
*/
typedef enum
{
    /* Data was transferred successfully. */
    DMAC_TRANSFER_EVENT_COMPLETE,

    /* Error while processing the request */
    DMAC_TRANSFER_EVENT_ERROR,

    /* No events yet. */
    DMAC_TRANSFER_EVENT_NONE

} DMAC_TRANSFER_EVENT;

typedef void (*DMAC_CHANNEL_CALLBACK) (DMAC_TRANSFER_EVENT status, uintptr_t contextHandle);

// *****************************************************************************
/* DMA channel object

  Summary:
    Fundamental data object for a DMA channel.

  Description:
    Used by DMA logic to register/use a DMA callback, report back error information
    from the ISR handling a transfer event.

  Remarks:
    None
*/
typedef struct
{
    bool inUse;

    /* Inidcates the error information for
       the last DMA operation on this channel */
    DMAC_ERROR errorInfo;

    /* Call back function for this DMA channel */
    DMAC_CHANNEL_CALLBACK  pEventCallBack;

    /* Client data(Event Context) that will be returned at callback */
    uintptr_t hClientArg;

} DMAC_CHANNEL_OBJECT;

// *****************************************************************************
/* DMA channel

  Summary:
    Fundamental data object that represents DMA channel number.

  Description:
    None

  Remarks:
    None
*/
typedef enum
{
<#list 0..NUM_DMA_CHANS - 1 as i>
<#assign CHAN = "DMA_" + i + "_CHANNEL_NUMBER">
    DMAC_CHANNEL_${i} = 0x${.vars[CHAN]},

</#list>
    DMAC_NUMBER_OF_CHANNELS = 0x${NUM_DMA_CHANS}

} DMAC_CHANNEL;

// *****************************************************************************
// *****************************************************************************
// Section: DMAC API
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister

  Summary:
    Callback function registration function

  Description:
    Registers the callback function (and context pointer, if used) for a given DMA interrupt.

  Parameters:
    DMAC_CHANNEL channel - DMA channel this callback pertains to
    const DMAC_CHANNEL_CALLBACK eventHandler - pointer to callback function
    const uintptr_t contextHandle - pointer of context information callback is to use (set to NULL if not used)

  Returns:
    void

  Example:
    <code>
    ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMAC_CHANNEL_0, DMAC_Callback, 0);
    </code>
*/
void ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMAC_CHANNEL channel, const DMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle );

// *****************************************************************************
/* Function:
   bool ${DMA_INSTANCE_NAME}_ChannelTransfer

  Summary:
    DMA channel transfer function

  Description:
    Sets up a DMA transfer, and starts the transfer if user specified a
    software-initiated transfer in Harmony.

  Parameters:
    DMAC_CHANNEL channel - DMA channel to use for this transfer
    const void *srcAddr - pointer to source data
    size_t srcSize - Size of the source
    const void *destAddr - pointer to where data is to be moved to
    size_t destSize - Size of the destination
    size_t cellSize - Size of the cell

  Returns:
    false, if DMA already is busy / true, if DMA is not busy before calling function

  Example:
    <code>
    ${DMA_INSTANCE_NAME}_ChannelCallbackRegister(DMAC_CHANNEL_0, DMAC_Callback, 0);
    ${DMA_INSTANCE_NAME}_ChannelTransfer(DMAC_CHANNEL_0,srcAddr,srcSize,destAddr,destSize,cellSize);
    </code>
*/
bool ${DMA_INSTANCE_NAME}_ChannelTransfer( DMAC_CHANNEL channel, const void *srcAddr, size_t srcSize, const void *destAddr, size_t destSize, size_t cellSize);

// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_ChannelDisable (DMAC_CHANNEL channel)

  Summary:
    This function disables the DMA channel.

  Description:
    Disables the DMA channel specified.

  Parameters:
    DMAC_CHANNEL channel - the particular channel to be disabled

  Returns:
    void

  Example:
    <code>
    ${DMA_INSTANCE_NAME}_ChannelDisable (DMAC_CHANNEL_0);
    </code>
*/
void ${DMA_INSTANCE_NAME}_ChannelDisable (DMAC_CHANNEL channel);

// *****************************************************************************
/* Function:
   bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (DMAC_CHANNEL channel)

  Summary:
    Reads the busy status of a channel.

  Description:
    Reads the busy status of a channel and returns status to caller.

  Parameters:
    DMAC_CHANNEL channel - the particular channel to be interrogated

  Returns:
    true - channel is busy
    false - channel is not busy

  Example:
    <code>
    bool returnVal;
    returnVal = ${DMA_INSTANCE_NAME}_ChannelIsBusy(DMAC_CHANNEL_0);
    while( returnVal )
        ;
    </code>
*/
bool ${DMA_INSTANCE_NAME}_ChannelIsBusy (DMAC_CHANNEL channel);

// *****************************************************************************
/* Function:
   void ${DMA_INSTANCE_NAME}_Initialize( void )

  Summary:
    This function initializes the DMAC controller of the device.

  Description:
    Sets up a DMA controller for subsequent transfer activity.

  Parameters:
    none

  Returns:
    void

  Example:
    <code>
    ${DMA_INSTANCE_NAME}_Initialize();
    </code>
*/
void ${DMA_INSTANCE_NAME}_Initialize( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${DMA_INSTANCE_NAME}_H
