<#assign generateDoxygen = true>
/*******************************************************************************
  MPLAB Harmony TRAPS header File

  File Name:
    ${trapsFileLowerCase}.h

  Summary:
    Traps driver with handler for all types of traps using dsPIC MCUs.   
 
  Description:
    None

 *******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

#ifndef TRAPS_H
#define TRAPS_H

// Section: Included Files
#include <stdint.h>

// Section: Data Type Definitions

#define TRAPS_ILLEGAL_INSTRUCTION   (0U)  /**< Illegal Instruction Trap  */
#define TRAPS_ADDRESS_ERR           (1U)  /**< Address error Trap  */
#define TRAPS_STACK_ERR             (2U)  /**< Stack Error Trap  */
#define TRAPS_BUS_CPU_X_ERR         (3U)  /**< Bus CPU X Data Error Trap  */
#define TRAPS_BUS_CPU_Y_ERR         (4U)  /**< Bus CPU Y Data Error Trap  */
#define TRAPS_BUS_DMA_ERR           (5U)  /**< Bus DMA Error Trap  */
#define TRAPS_BUS_CPU_INSTR_ERR     (6U)  /**< Bus CPU Instruction Error Trap  */
#define TRAPS_DIV0_ERR              (7U)  /**< Divide by zero Error Trap  */
#define TRAPS_DMT_ERR               (8U)  /**< Generic DMT Error Trap  */
#define TRAPS_WDT_ERR               (9U)  /**< Generic WDT Error Trap  */
#define TRAPS_XRAM_ERR              (10U) /**< Generic XRAM PWB DED Error Trap  */
#define TRAPS_YRAM_ERR              (11U) /**< Generic XRAM PWB DED Error Trap  */
#define TRAPS_SOFT_ERR              (12U) /**< Generic Soft Trap  */

<#if generateDoxygen>
/**
 * @brief    TRAPS error codes Type Definition
 *
 * Defines the type used to represent TRAPS error codes in the system. 
 * The value corresponds to various TRAPS error codes available in the device.
 */
</#if>
typedef uint32_t TRAPS_ERROR_CODE;

// Section: Driver Interface Function

<#if generateDoxygen>
/**
 * @ingroup    trapsdriver
 * @brief      Stores the trap error code and waits forever.
 *             This is a weak attribute function. The user can 
 *             override and implement the same function without weak attribute.
 * @param[in]  code - trap error code
 * @return     none  
 */
 </#if>
void ${trapsFileUpperCase}_halt_on_error(uint16_t code);

#endif

