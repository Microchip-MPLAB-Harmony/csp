/*******************************************************************************
  SDADC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdadc_common.h

  Summary:
    SDADC PLIB Header file

  Description:
    This file defines the interface to the SDADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_SDADC_COMMON_H
#define PLIB_SDADC_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Global data
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    SDADC_STATUS_RESRDY = SDADC_INTFLAG_RESRDY_Msk,
    SDADC_STATUS_OVERRUN = SDADC_INTFLAG_OVERRUN_Msk,
    SDADC_STATUS_WINMON = SDADC_INTFLAG_WINMON_Msk,
    /* Force compiler to reserve 32-bit memory for this enum */
    SDADC_STATUS_INVALID = 0xFFFFFFFF
}SDADC_STATUS;

typedef void (*SDADC_CALLBACK)( SDADC_STATUS status, uintptr_t context);

typedef struct
{
    SDADC_CALLBACK callback;
    uintptr_t context;
}SDADC_CALLBACK_OBJECT;


// DOM-IGNORE-BEGIN
    #ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SDADC_COMMON_H */