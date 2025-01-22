/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}_common.h
 
  Summary:
    CMP Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    CMP peripherals.
 
*******************************************************************************/
 
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

#ifndef PLIB_CMP_TYPES_H
#define PLIB_CMP_TYPES_H

/**
 @enum     CMP_DAC_SLOPE_UPDATE_MODE
 @brief    CMP slope data registers update mode
 @note     Applicable in slope mode
*/
typedef enum 
{
    CMP_DAC_SLOPE_UPDATE_IMMIDIATE = 0U, /**< Updates slope related data registers immidiately */
    CMP_DAC_SLOPE_UPDATE_TRIGGERED = 1U, /**< Updates slope related data registers during the external trigger */
    
} CMP_DAC_SLOPE_UPDATE_MODE;

/** 
 * @ summary      CMP Callback Function Pointer.
 * @ breif        This data type defines the CMP Callback Function Pointer.
 * @ remarks      None
 **/
typedef void (*CMP_CALLBACK) (uintptr_t contextHandle);

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****
typedef struct
{
    CMP_CALLBACK            callback;
    uintptr_t               context;

} CMP_OBJECT;

#endif // PLIB_CMP_TYPES_H


