<#assign functionHeaderExample = false>
<#assign generateDoxygen = true>
/*******************************************************************************
  ${dmaModuleName} Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${dmaModuleName?lower_case}.h

  Summary:
    ${dmaModuleName} peripheral library interface.

  Description:
    This file defines the interface to the ${dmaModuleName} peripheral library. This
    library provides access to and control of the ${dmaModuleName} controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${dmaModuleName}_H    // Guards against multiple inclusion
#define PLIB_${dmaModuleName}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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
// Section: type definitions
// *****************************************************************************
// *****************************************************************************

/*
 @enum         ${dmaModuleName}_TRANSFER_EVENT
 @brief        Identifies the status of the transfer event.
 @details      Used to report back, via registered callback, the status of a transaction.
 @remarks      None
*/
typedef enum
{
    /* No events yet. */
    ${dmaModuleName}_TRANSFER_EVENT_NONE = 0,

    /* Data was transferred successfully. */
    ${dmaModuleName}_TRANSFER_EVENT_COMPLETE = 1,

    /* Half Data is transferred */
    ${dmaModuleName}_TRANSFER_EVENT_HALF_COMPLETE = 2,

    /* Overrun error: The ${dmaModuleName} channel cannot keep up with data rate requirements. */
    ${dmaModuleName}_OVERRUN_ERROR = 3,

    /* Pattern match detected */
    ${dmaModuleName}_PATTERN_MATCH = 4

} ${dmaModuleName}_TRANSFER_EVENT;


typedef void (*${dmaModuleName}_CHANNEL_CALLBACK) (${dmaModuleName}_TRANSFER_EVENT status, uintptr_t contextHandle);


/*
 @struct       DMA_CHANNEL_OBJECT
 @brief        Fundamental data object for a ${dmaModuleName} channel.
 @details      Used by ${dmaModuleName} logic to register/use a ${dmaModuleName} callback, report back error information
               from the ISR handling a transfer event.
 @remarks      None
*/
typedef struct
{
    bool inUse;

    /* Call back function for this ${dmaModuleName} channel */
    ${dmaModuleName}_CHANNEL_CALLBACK  callback;

    /* data or Event Context that will be returned at callback */
    uintptr_t context;

} ${dmaModuleName}_CHANNEL_OBJECT;


/*
 @brief        Fundamental data object that represents ${dmaModuleName} channel number.
 @details      None
 @remarks      None
*/
<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
            <#lt>#define    ${dmaModuleName}_CHANNEL_${i}             (0x${i}U)
    </#if>
</#list>

#define    ${dmaModuleName}_NUMBER_OF_CHANNELS    (0x${MAX_CHANNEL_COUNT}U)

typedef uint32_t ${dmaModuleName}_CHANNEL;

typedef uint32_t DMA_CHANNEL_CONFIG;

// *****************************************************************************
// *****************************************************************************
// Section: ${dmaModuleName} API's
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

<#if generateDoxygen>
/**
 * @brief    Initializes the DMA controller of the device.
 *
 * @details  This function initializes the DMA controller of the device as configured by the user
 *           from within the DMA manager of MHC.
 *
 * @pre      The DMA module clock requirements should have been configured in the MHC Clock Manager utility.
 *
 * @param    none
 *
 * @return   none
 *
 * @b Example:
 * @code
 *     DMA_Initialize();
 * @endcode
 *
 * @remarks  none.
 */
</#if>
void ${dmaModuleName}_Initialize( void );

<#if generateDoxygen>
/**
 * @brief    De-initializes the DMA controller of the device to POR Values.
 *
 * @details  This function de-initializes the DMA controller control and status registers to it's POR state.
 *
 * @pre      The DMA module clock requirements should have been configured in the MHC Clock Manager utility.
 *
 * @param    none
 *
 * @return   none
 *
 * @b Example:
 * @code
 *     DMA_Deinitialize();
 * @endcode
 *
 * @remarks  none.
 */
</#if>
void ${dmaModuleName}_Deinitialize( void );

<#if anyChannelEnabled == true>
<#if generateDoxygen>
/**
 * @brief   Schedules a DMA transfer on the specified DMA channel.
 * @details This function schedules a DMA transfer on the specified DMA channel and starts the transfer
 *          when the configured trigger is received. The transfer is processed based on the channel
 *          configuration performed in the DMA manager. The channel parameter specifies the channel to
 *          be used for the transfer.
 *
 *          The srcAddr parameter specifies the source address from where data will be transferred.
 *
 *          The destAddr parameter specifies the address location where the data will be stored.
 *
 *          If the channel is configured for a software trigger, calling the channel transfer function
 *          will set the source and destination address and will also start the transfer. If the channel
 *          was configured for a peripheral trigger, the channel transfer function will set the source and
 *          destination address and will transfer data when a trigger has occurred.
 *
 *          If the requesting client registered an event callback function before calling the channel transfer
 *          function, this function will be called when the transfer completes. The callback function will be
 *          called with a DMA_TRANSFER_EVENT_BLOCK_TRANSFER_COMPLETE event if the transfer was processed
 *          successfully and a DMA_TRANSFER_EVENT_ERROR event if the transfer was not processed successfully.
 *
 *          When a transfer is already in progress, this API will return false indicating that the transfer
 *          request is not accepted.
 *
 * @pre     DMA should have been initialized by calling the DMA_Initialize. The required channel transfer
 *          parameters such as beat size, source and destination address increment should have been configured
 *          in MHC.
 *
 * @param[in] channel   The DMA channel that should be used for the transfer.
 * @param[in] srcAddr   Source address of the DMA transfer.
 * @param[in] destAddr  Destination address of the DMA transfer.
 * @param[in] blockSize Size of the transfer block in bytes.
 *
 * @return  True - if the transfer request is accepted.
 *          False - if a previous transfer is in progress and the request is rejected.
 *
 * @note None.
 *
 * @example
 * @code
 * MY_APP_OBJ myAppObj;
 * uint8_t buf[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
 * void *srcAddr = (uint8_t *) buf;
 * void *destAddr = (uint8_t*) &SERCOM1_REGS->USART_INT.SERCOM_DATA;
 * size_t size = 10;
 *
 * DMA_ChannelCallbackRegister(DMA_CHANNEL_1, APP_DMATransferEventHandler, (uintptr_t)&myAppObj);
 *
 * if (DMA_ChannelTransfer(DMA_CHANNEL_1, srcAddr, destAddr, size) == true)
 * {
 *
 * }
 * else
 * {
 *
 * }
 * @endcode
 */
</#if>
bool ${dmaModuleName}_ChannelTransfer(${dmaModuleName}_CHANNEL channel, const void *srcAddr, const void *destAddr, uint32_t blockSize);

<#if generateDoxygen>
/**
 * @brief    This API is used to setup DMA pattern matching.
 * @details  When the content of the incoming data is required in making decisions in real time,
 *           the 32-bit DMA Controller can recognize a data pattern in its internal buffer being
 *           transferred from the source to the destination locations. The pattern match capability,
 *           when enabled, allows a user-programmable data pattern to be compared against a (partial)
 *           content of DMABUF[31:0]. Upon match detection, the DMA Controller invokes its interrupt
 *           to inform the CPU to take further action.
 *
 * @pre      DMA should have been initialized by calling DMA_Initialize.
 * @param    channel            DMA channel
 * @param    patternMatchMask   The value used to mask certain bits in the incoming data
 * @param    patternMatchData   Pattern match data.
 *
 * @return None
 *
 * @example
 * @code
 * DMA_ChannelPatternMatchSetup(DMA_CHANNEL_0, 0x00FF, 0x0055);
 * @endcode
 *
 * @remarks None.
 */
</#if>
void ${dmaModuleName}_ChannelPatternMatchSetup(${dmaModuleName}_CHANNEL channel, uint32_t patternMatchMask, uint32_t patternMatchData);

<#if generateDoxygen>
/**
 * @brief     Enables the specified DMA channel.
 * @details   The function enables the specified DMA channel. Once enabled, DMA will initiate a block transfer
 *            when the selected trigger is received.
 * @pre       DMA should have been initialized by calling DMA_Initialize.
 * @param[in] channel The DMA channel that needs to be enabled.
 * @return    None.
 * @code
 *
 * DMA_ChannelEnable(DMA_CHANNEL_0);
 * @endcode
 *
 * @remarks   None.
 */
</#if>
void ${dmaModuleName}_ChannelEnable (${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief     Disables the specified DMA channel.
 * @details   The function disables the specified DMA channel. Once disabled, the channel will ignore triggers
 *            and will not transfer data until the next time a DMA_ChannelTransfer function is called. If there
 *            is a transfer already in progress, this will be suspended.
 * @pre       DMA should have been initialized by calling DMA_Initialize.
 * @param[in] channel The DMA channel that needs to be disabled.
 *
 * @return    None.
 *
 * @code
 *
 * DMA_ChannelDisable(DMA_CHANNEL_0);
 * @endcode
 *
 * @remarks   None.
 */
</#if>
void ${dmaModuleName}_ChannelDisable (${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief    Enable DMA channel pattern matching
 * @details  This API is used to enable DMA pattern matching.
 * @pre      DMA should have been initialized by calling DMA_Initialize.
 * @param    channel DMA channel
 * @return   none
 * @b Example:
 * @code
 *     DMA_ChannelPatternMatchEnable(DMA_CHANNEL_0);
 * @endcode
 * @remarks  none.
 */
</#if>
void ${dmaModuleName}_ChannelPatternMatchEnable(${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief    Disable DMA channel pattern matching
 * @details  This API is used to disable DMA pattern matching.
 * @pre      DMA should have been initialized by calling DMA_Initialize.
 * @param    channel DMA channel
 * @return   none
 * @b Example:
 * @code
 *     DMA_ChannelPatternMatchDisable(DMA_CHANNEL_0);
 * @endcode
 * @remarks  none.
 */
</#if>
void ${dmaModuleName}_ChannelPatternMatchDisable(${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @ingroup    dmadriver
 * @brief      This function returns the status of the software request of the DMA channel.
 * @details    This function checks if there is a pending software request for the specified DMA channel.
 * @pre        DMA_Initialize must be called.
 * @param[in]  channel  - DMA channel number.
 * @b Example:
 * @code
 *     ${dmaModuleName}_IsSoftwareRequestPending(DMA_CHANNEL_0);
 * @endcode
 * @return     true     - DMA request is pending.
 * @return     false    - DMA request is not pending.
 */
 </#if>
bool ${dmaModuleName}_IsSoftwareRequestPending(${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @ingroup    dmadriver
 * @brief      This function sets the software trigger of the DMA channel.
 * @details    This function enables the software trigger for the specified DMA channel, initiating a DMA transfer.
 * @pre        DMA_Initialize must be called.
 * @param[in]  channel - DMA channel number.
 * @b Example:
 * @code
 *     ${dmaModuleName}_ChannelSoftwareTriggerEnable(DMA_CHANNEL_0);
 * @endcode
 * @return     None.
 */
 </#if>
void ${dmaModuleName}_ChannelSoftwareTriggerEnable(${dmaModuleName}_CHANNEL channel) ;

<#if generateDoxygen>
/**
 * @brief       Returns the busy status of the channel.
 * @details     The function returns true if the specified channel is busy with a transfer.
 *              This function can be used to poll for the completion of transfer that was started by
 *              calling the DMA_ChannelTransfer() function. This function can be used as a polling
 *              alternative to setting a callback function and receiving an asynchronous notification
 *              for transfer notification.
 * @pre         DMA should have been initialized by calling DMA_Initialize.
 * @param[in]   channel The DMA channel whose status needs to be checked.
 * @return      True - The channel is busy with an on-going transfer.
 * @return      False - The channel is not busy and is available for a transfer.
 * @code
 *
 * while(DMA_ChannelIsBusy(DMA_CHANNEL_0));
 * @endcode
 * @remarks     None.
 */
</#if>
bool ${dmaModuleName}_ChannelIsBusy (${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief           Returns transfer count of the ongoing DMA transfer.
 * @details         Returns transfer count of the ongoing DMA transfer.
 * @pre             DMA should have been initialized by calling DMA_Initialize.
 * @param[in]       channel DMA channel.
 * @return          None.
 * @code
 * uint32_t transfer_cnt;
 * transfer_cnt = DMA_ChannelGetTransferredCount(DMA_CHANNEL_0);
 * @endcode
 * @remarks         None.
 */
</#if>
uint32_t ${dmaModuleName}_ChannelGetTransferredCount(${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief           Returns the current channel settings for the specified DMA Channel.
 * @details         Returns the current channel settings for the specified DMA Channel.
 * @pre             DMA should have been initialized by calling DMA_Initialize.
 * @param           channel DMA channel.
 * @return          Current channel settings for the specified DMA Channel.
 * @code
 * uint32_t setting;
 * setting = DMA_ChannelSettingsGet(DMA_CHANNEL_0);
 * @endcode
 * @remarks         None.
 */
</#if>
DMA_CHANNEL_CONFIG ${dmaModuleName}_ChannelSettingsGet(${dmaModuleName}_CHANNEL channel);

<#if generateDoxygen>
/**
 * @brief           This function changes the current settings of the specified DMA channel.
 * @details         This function changes the current settings of the specified DMA channel.
 * @pre             DMA should have been initialized by calling DMA_Initialize.
 * @param           channel DMA channel.
 * @param           setting Value to be set in the specified DMA Channel.
 * @return          True - Settings updated successfully for the specified DMA channel.
 * @return          False - Failed to update the settings for the specified DMA channel.
 * @code
 * uint32_t setting;
 * bool status;
 * setting = DMA_ChannelSettingsGet(DMA_CHANNEL_0);
 * setting |= _DMA0CH_CHEN_MASK;
 * status = DMA_ChannelSettingsSet(DMA_CHANNEL_0, setting);
 * @endcode
 * @remarks         None.
 */
</#if>
bool ${dmaModuleName}_ChannelSettingsSet(${dmaModuleName}_CHANNEL channel, DMA_CHANNEL_CONFIG setting);

<#if dmaIntEnabled == true>
<#if generateDoxygen>
/**
 * @brief           Allows a DMA PLIB client to set an event handler.
 * @details         This function allows a client to set an event handler. The client may want to receive
 *                  transfer related events in cases when it submits a DMA PLIB transfer request.
 *                  The event handler should be set before the client intends to perform operations that could generate events.
 *                  In case of linked transfer descriptors, the callback function will be called for every transfer
 *                  in the transfer descriptor chain. The application must implement its own logic to link the callback
 *                  to the transfer descriptor being completed.
 *                  This function accepts a context parameter. This parameter could be set by the client to contain
 *                  (or point to) any client specific data object that should be associated with this DMA channel.
 * @pre             DMA should have been initialized by calling DMA_Initialize.
 * @param[in]       channel A specific DMA channel from which the events are expected.
 * @param[in]       callback Pointer to the event handler function.
 * @param[in]       context Value identifying the context of the application/driver/middleware that registered the event handling function.
 * @return          None.
 * @code
 * MY_APP_OBJ myAppObj;
 * void APP_DMATransferEventHandler(DMA_TRANSFER_EVENT event, uintptr_t contextHandle)
 * {
 *     switch(event)
 *     {
 *         case ${dmaModuleName}_TRANSFER_EVENT_COMPLETE:
 *         break;
 *
 *         case ${dmaModuleName}_OVERRUN_ERROR:
 *         break;
 *
 *         default:
 *         break;
 *     }
 * }
 * DMA_ChannelCallbackRegister(DMA_CHANNEL_1, APP_DMATransferEventHandler, (uintptr_t)&myAppObj);
 * @endcode
 * @remarks         None.
 */
</#if>
void ${dmaModuleName}_ChannelCallbackRegister(${dmaModuleName}_CHANNEL channel, const ${dmaModuleName}_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle );
<#else>
<#if generateDoxygen>
/**
 * @brief           Returns the DMA channel's transfer status.
 * @details         Returns the DMA channel's transfer status.
 * @pre             DMA should have been initialized by calling the DMA_Initialize.
 * @param[in]       channel The particular channel to be interrogated.
 * @return          DMA_TRANSFER_EVENT - enum of type DMA_TRANSFER_EVENT indicating the status of the DMA transfer.
 * @code
 * bool isBusy;
 *
 * isBusy = ${dmaModuleName}_ChannelIsBusy(${dmaModuleName}_CHANNEL_0);
 *
 * if (isBusy == false)
 * {
 *     if (${dmaModuleName}_ChannelTransferStatusGet() == ${dmaModuleName}_TRANSFER_EVENT_ERROR)
 *     {
 *
 *     }
 *     else
 *     {
 *
 *     }
 * }
 * @endcode
 * @remarks         None.
 */
</#if>
${dmaModuleName}_TRANSFER_EVENT ${dmaModuleName}_ChannelTransferStatusGet(${dmaModuleName}_CHANNEL channel);
</#if>

</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_${dmaModuleName}_H