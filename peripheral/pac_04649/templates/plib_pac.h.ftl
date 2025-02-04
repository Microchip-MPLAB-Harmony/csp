<#assign generateDoxygen = true>
/*******************************************************************************
  Peripheral Access Controller(PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PAC_INSTANCE_NAME?lower_case}.h

  Summary
    PAC PLIB Header File.

  Description
    PAC(Peripheral Access Controller) is used to prevent accidental enabling or disabling 
    of critical peripherals. The module implements an OR gate between the associated peripheral’s 
    PACCONx lock bit and the inverse of the PACCONx write enable bit.

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

#ifndef PLIB_${PAC_INSTANCE_NAME}_H  // Guards against multiple inclusion
#define PLIB_${PAC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/**
 * @enum     PAC_Operation
 * @brief    List of available Peripheral Access Control Operations.
 *
 * @details  This enum identifies the possible PAC operation. This data type is used along 
 *           with the PAC_PeripheralProtect() function and specifies the type of access operation 
 *           that needs to be performed.
 *
 * @remarks  None.
 */
typedef enum 
{
    PAC_PROTECTION_CLEAR,             /**< Clear the peripheral write control protection */
    PAC_PROTECTION_SET,               /**< Set the peripheral write control protection */
    PAC_PROTECTION_SET_AND_LOCK       /**< Set and lock the peripheral write control until the next hardware reset */
}PAC_PROTECTION;

// Section: Data Types

#define PAC_PERIPHERAL_IVTBASE    0U
#define PAC_PERIPHERAL_IVTCREG    1U
#define PAC_PERIPHERAL_BMXIRAML   2U
#define PAC_PERIPHERAL_BMXIRAMH   3U
#define PAC_PERIPHERAL_PCLKCON    4U
#define PAC_PERIPHERAL_IOIMCON1   5U
#define PAC_PERIPHERAL_IOIMCON2   6U
#define PAC_PERIPHERAL_IOIMCON3   7U
#define PAC_PERIPHERAL_IOIMCON4   8U
#define PAC_PERIPHERAL_NVMCON     9U
#define PAC_PERIPHERAL_OSCCTRL    10U
#define PAC_PERIPHERAL_CM1CON     11U
#define PAC_PERIPHERAL_CM1RANGE   12U
#define PAC_PERIPHERAL_CM2CON     13U
#define PAC_PERIPHERAL_CM2RANGE   14U
#define PAC_PERIPHERAL_CM3CON     15U
#define PAC_PERIPHERAL_CM3RANGE   16U
#define PAC_PERIPHERAL_CM4CON     17U
#define PAC_PERIPHERAL_CM4RANGE   18U
#define PAC_PERIPHERAL_WDTCON     19U
#define PAC_PERIPHERAL_RPCON      20U
#define PAC_PERIPHERAL_MBISTCON   22U

/**
 * @brief    PAC Peripheral Definition
 *
 * Defines the peripheral used to represent PAC Peripheral in the system. 
 * The value corresponds to various PAC peripherals available in the PACCON register.
 */
typedef uint32_t PAC_PERIPHERAL;

<#if generateDoxygen>
/**
 * @brief     Returns PAC protection status of peripheral.
 * @details   This function returns the PAC protection status for the specified peripheral.
 * @pre       On some devices, PAC_Initialize() function needs to be called first.
 * @param[in] peripheral Peripheral to be operated on.
 * @return 
 * - true  : Peripheral is protected.
 * - false : Peripheral is not protected.
 * 
 * @b Example
 * @code
 * bool status = false;
 * status = PAC_PeripheralIsProtected(PAC_PERIPHERAL_WDTCON);
 * @endcode
 * @remarks   None.
 */
</#if>
bool ${PAC_INSTANCE_NAME}_PeripheralIsProtected(PAC_PERIPHERAL peripheral );

<#if generateDoxygen>
/**
 * @brief     This function configures PAC protection for the specified peripheral.
 * @details   This function configures PAC protection for the specified peripheral.
 * @pre       Protection status returned by PAC_PeripheralIsProtected() function needs to be used before calling this function.
 * @param[in] peripheral Peripheral to be operated on.
 * @param[in] operation PAC operation to be performed. Refer to the description of the PAC_PROTECTION enumeration for possible operations.
 * @return    None.
 * @b Example
 * @code
 * bool status = false;
 * 
 * status = PAC_PeripheralIsProtected(PAC_PERIPHERAL_WDTCON);
 * 
 * if (status == true)
 * {
 *     PAC_PeripheralProtectSetup(PAC_PERIPHERAL_WDTCON, PAC_PROTECTION_CLEAR);
 * }
 * else
 * {
 *     PAC_PeripheralProtectSetup(PAC_PERIPHERAL_WDTCON, PAC_PROTECTION_SET);
 * }
 * @endcode
 * @remarks None.
 */
</#if>
void ${PAC_INSTANCE_NAME}_PeripheralProtectSetup(PAC_PERIPHERAL peripheral, PAC_PROTECTION operation);


#endif /* $${PAC_INSTANCE_NAME}_H */