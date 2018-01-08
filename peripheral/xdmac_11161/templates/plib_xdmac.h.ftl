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

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

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


typedef enum
{
    /* Data was transferred successfully. */
    XDMAC_TRANSFER_COMPLETE,

    /* Error while processing the request */
    XDMAC_TRANSFER_ERROR

} XDMAC_TRANSFER_EVENT;
<#if XDMAC_LL_ENABLE == true>


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


// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

/***************************** XDMAC Inline *******************************/
<#if XDMAC_LL_ENABLE == true>

#define XDMAC_UBLEN_BIT_WIDTH 24
</#if>

typedef struct
{
    uint8_t                inUse;
    XDMAC_CHANNEL_CALLBACK callback;
    uintptr_t              context;
    XDMAC_TRANSFER_EVENT   event;

} XDMAC_CH_OBJECT ;

extern XDMAC_CH_OBJECT xdmacChannelObj[XDMAC_CHANNELS_NUMBER];

void inline XDMAC_ISR_Handler( void )
{
    XDMAC_CH_OBJECT *xdmacChObj = (XDMAC_CH_OBJECT *)&xdmacChannelObj[0];
    uint8_t channel = 0;
	volatile uint32_t chanIntStatus = 0;

    /* Iterate all channels */
    for (channel = 0; channel < XDMAC_CHANNELS_NUMBER; channel++)
    {
        /* Process events only on active channels */
        if (1 == xdmacChObj->inUse)
        {
			/* Read the interrupt status for the active DMA channel */
			chanIntStatus = _XDMAC_REGS->XDMAC_CHID[channel].XDMAC_CIS.w;

			if (chanIntStatus & ( XDMAC_CIS_RBEIS_Msk | XDMAC_CIS_WBEIS_Msk | XDMAC_CIS_ROIS_Msk))
			{
				/* It's an error interrupt */
			    xdmacChObj->event = XDMAC_TRANSFER_ERROR;
			}
			else if (chanIntStatus & XDMAC_CIS_BIS_Msk)
			{
				/* It's a block transfer complete interrupt */
				xdmacChObj->event = XDMAC_TRANSFER_COMPLETE;
			}

			if (NULL != xdmacChObj->callback)
			{
				xdmacChObj->callback(xdmacChObj->event, xdmacChObj->context);
			}
        }

        /* Point to next channel object */
        xdmacChObj += 1;
    }
}

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_XDMAC_H
