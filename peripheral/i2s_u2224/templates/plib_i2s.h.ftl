/*******************************************************************************
  I2S PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2S_INSTANCE_NAME?lower_case}.h

  Summary:
    ${I2S_INSTANCE_NAME} PLIB Header File

  Description:
    This file has the prototypes of all the interfaces provided for one
    particular instance of the Inter-IC Sound Controller (I2S) peripheral.

*******************************************************************************/

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

#ifndef PLIB_${I2S_INSTANCE_NAME}_H
#define PLIB_${I2S_INSTANCE_NAME}_H

#include "device.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus  

    extern "C" {

#endif

/****************************** ${I2S_INSTANCE_NAME} Interface *********************************/

void ${I2S_INSTANCE_NAME}_Initialize ( void );

uint32_t ${I2S_INSTANCE_NAME}_LRCLK_Get(void);

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }
    
#endif

#endif // PLIB_${I2S_INSTANCE_NAME}_H
