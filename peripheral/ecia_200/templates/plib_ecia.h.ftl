/*******************************************************************************
  ECIA PLIB Header

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ecia.h

  Summary:
    ECIA PLIB Header File

  Description:
    None

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

#ifndef PLIB_ECIA_H
#define PLIB_ECIA_H

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

typedef enum
{
    ${ECIA_INT_SOURCE_ENUM_LIST}
}ECIA_INT_SOURCE;

typedef enum
{
    <#list ECIA_GIRQ_REG_START..ECIA_GIRQ_REG_END as n>
    ECIA_GIRQ_BLOCK_NUM${n} = ${n},
    </#list>
    ECIA_GIRQ_BLOCK_NUM_MAX
}ECIA_GIRQ_BLOCK_NUM;

#define INT_SRC_IS_AGGREGATE                0U
#define INT_SRC_IS_DIRECT                   1U
#define GIRQ_DIR_INT_NUM_GET(int_src)       (((uint32_t)(int_src)) & (uint32_t)0xFF)
#define GIRQ_AGG_INT_NUM_GET(int_src)       ((((uint32_t)(int_src)) & ((uint32_t)0xFF << 8U)) >> 8U)
#define GIRQ_REG_GET(int_src)               ((((uint32_t)(int_src)) & ((uint32_t)0xFF << 16U)) >> 16U)
#define GIRQ_BIT_POS_GET(int_src)           ((((uint32_t)(int_src)) & ((uint32_t)0x1F << 24U)) >> 24U)
#define IS_INT_SRC_AGG_OR_DIR(int_src)      ((((uint32_t)(int_src)) & ((uint32_t)0x01 << 31U)) >> 31U)

void ECIA_Initialize(void);
void ECIA_GIRQBlockEnable(ECIA_GIRQ_BLOCK_NUM block);
void ECIA_GIRQBlockDisable(ECIA_GIRQ_BLOCK_NUM block);
void ECIA_GIRQBlockDisableAll(void);
uint32_t ECIA_GIRQBlockStatusGet(ECIA_GIRQ_BLOCK_NUM block);
void ECIA_GIRQSourceEnable(ECIA_INT_SOURCE int_src);
void ECIA_GIRQSourceDisable(ECIA_INT_SOURCE int_src);
void ECIA_GIRQSourceClear(ECIA_INT_SOURCE int_src);
void ECIA_GIRQSourceClearAll(void);
void ECIA_GIRQSourceDisableAll(void);
void ECIA_InterruptEnable(ECIA_INT_SOURCE int_src);
void ECIA_InterruptDisable(ECIA_INT_SOURCE int_src);
uint8_t ECIA_GIRQResultGet(ECIA_INT_SOURCE int_src);
bool ECIA_GIRQIsInterruptEnabled(ECIA_INT_SOURCE int_src);




// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_NVIC_H
