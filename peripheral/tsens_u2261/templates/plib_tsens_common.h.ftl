/*******************************************************************************
  Temperature Sensor (TSENS) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_tsens_common.h

  Summary
    TSENS Peripheral Library Interface Header File.

  Description
    This file defines the common types for the TSENS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_TSENS_COMMON_H    // Guards against multiple inclusion
#define PLIB_TSENS_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Preprocessor macros
// *****************************************************************************
// *****************************************************************************
#define TSENS_STATUS_NONE 0U
#define TSENS_STATUS_RESRDY TSENS_INTFLAG_RESRDY_Msk
#define TSENS_STATUS_WINMON TSENS_INTFLAG_WINMON_Msk
#define TSENS_STATUS_MASK (TSENS_STATUS_RESRDY | TSENS_STATUS_WINMON)    
#define TSENS_STATUS_INVALID 0xFFFFFFFFU

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

typedef uint32_t TSENS_STATUS;

typedef enum
{
    TSENS_WINMODE_DISABLED = TSENS_CTRLC_WINMODE_DISABLE_Val,
    TSENS_WINMODE_GREATER_THAN_WINLT = TSENS_CTRLC_WINMODE_ABOVE_Val,
    TSENS_WINMODE_LESS_THAN_WINUT = TSENS_CTRLC_WINMODE_BELOW_Val,
    TSENS_WINMODE_BETWEEN_WINLT_AND_WINUT = TSENS_CTRLC_WINMODE_INSIDE_Val,
    TSENS_WINMODE_OUTSIDE_WINLT_AND_WINUT = TSENS_CTRLC_WINMODE_OUTSIDE_Val,
    TSENS_WINMODE_HYST_GREATER_WINUT = TSENS_CTRLC_WINMODE_HYST_ABOVE_Val,
    TSENS_WINMODE_HYST_LESS_THAN_WINLT = TSENS_CTRLC_WINMODE_HYST_BELOW_Val
}TSENS_WINMODE;


// *****************************************************************************


typedef void (*TSENS_CALLBACK)(TSENS_STATUS status, uintptr_t context);


typedef struct
{
    TSENS_CALLBACK callback;

    uintptr_t context;

} TSENS_CALLBACK_OBJ;



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_TSENS_COMMON_H*/
