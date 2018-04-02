/*******************************************************************************
  XDMAC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_xdmac.h

  Summary:
    XDMAC PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_XDMAC_H
#define PLIB_XDMAC_H

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/****************************** XDMAC Data Types ******************************/
/* Peripheral address macros for DMA */
<#list 0..XDMAC_CHANNEL_COUNT as i>
<#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
<#assign XDMAC_CH_PERID = "XDMAC_CC" + i + "_PERID">
<#assign XDMAC_CH_PER_REGISTER = "XDMAC_CH" + i + "_PER_REGISTER">
    <#if .vars[XDMAC_CH_ENABLE]?has_content>
        <#if (.vars[XDMAC_CH_ENABLE] != false)>
            <#if (.vars[XDMAC_CH_PER_REGISTER]?has_content) && (.vars[XDMAC_CH_PER_REGISTER] != "None")>
#define ${.vars[XDMAC_CH_PERID]?upper_case}_ADDRESS  (&${.vars[XDMAC_CH_PER_REGISTER]})
            </#if>
        </#if>
    </#if>
</#list>

/* XDMAC Channels */
typedef enum {
    <#list 0..XDMAC_CHANNEL_COUNT as i>
    <#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
        <#if .vars[XDMAC_CH_ENABLE]?has_content>
            <#if (.vars[XDMAC_CH_ENABLE] != false)>
    XDMAC_CHANNEL_${i},
            </#if>
        </#if>
    </#list>
    XDMAC_CHANNELS_NUMBER

} XDMAC_CHANNEL;


/* XDMAC Transfer Events */
typedef enum
{
    /* Data was transferred successfully. */
    XDMAC_TRANSFER_COMPLETE,

    /* Error while processing the request */
    XDMAC_TRANSFER_ERROR

} XDMAC_TRANSFER_EVENT;

/* XDMAC Channel Config Type */
typedef uint32_t XDMAC_CHANNEL_CONFIG;
<#if XDMAC_LL_ENABLE == true>

/* XDMAC Lilnked List Datatypes */
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
</#if>


typedef void (*XDMAC_CHANNEL_CALLBACK)( XDMAC_TRANSFER_EVENT event, uintptr_t contextHandle );


/****************************** XDMAC API *********************************/

void XDMAC_Initialize( void );

void XDMAC_ChannelCallbackRegister( XDMAC_CHANNEL channel, const XDMAC_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle );

void XDMAC_ChannelTransfer( XDMAC_CHANNEL channel, const void *srcAddr, const void *destAddr, size_t blockSize );
<#if XDMAC_LL_ENABLE == true>

void XDMAC_ChannelLinkedListTransfer( XDMAC_CHANNEL channel, uint32_t descriptor, XDMAC_DESCRIPTOR_CONTROL* descriptorControl );
</#if>

bool XDMAC_ChannelIsBusy (XDMAC_CHANNEL channel);

XDMAC_CHANNEL_CONFIG XDMAC_ChannelSettingsGet (XDMAC_CHANNEL channel);

bool XDMAC_ChannelSettingsSet (XDMAC_CHANNEL channel, XDMAC_CHANNEL_CONFIG setting);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

void XDMAC_InterruptHandler(void);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_XDMAC_H
