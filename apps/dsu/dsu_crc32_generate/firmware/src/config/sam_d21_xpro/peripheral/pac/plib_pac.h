/*******************************************************************************
  Peripheral Access Controller(PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pac.h

  Summary
    PAC PLIB Header File.

  Description
    This file defines the interface to the PAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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

#ifndef PLIB_PAC_H  // Guards against multiple inclusion
#define PLIB_PAC_H

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

typedef enum
{
    /* Clear the peripheral write control protection */
    PAC_PROTECTION_CLEAR,

    /* Set the peripheral write control protection */
    PAC_PROTECTION_SET,

} PAC_PROTECTION;

typedef enum
{
    /* Instance Id for Peripheral AC */
    PAC_PERIPHERAL_AC = ID_AC,

    /* Instance Id for Peripheral ADC */
    PAC_PERIPHERAL_ADC = ID_ADC,

    /* Instance Id for Peripheral DAC */
    PAC_PERIPHERAL_DAC = ID_DAC,

    /* Instance Id for Peripheral DMAC */
    PAC_PERIPHERAL_DMAC = ID_DMAC,

    /* Instance Id for Peripheral DSU */
    PAC_PERIPHERAL_DSU = ID_DSU,

    /* Instance Id for Peripheral EIC */
    PAC_PERIPHERAL_EIC = ID_EIC,

    /* Instance Id for Peripheral EVSYS */
    PAC_PERIPHERAL_EVSYS = ID_EVSYS,

    /* Instance Id for Peripheral GCLK */
    PAC_PERIPHERAL_GCLK = ID_GCLK,

    /* Instance Id for Peripheral I2S */
    PAC_PERIPHERAL_I2S = ID_I2S,

    /* Instance Id for Peripheral MTB */
    PAC_PERIPHERAL_MTB = ID_MTB,

    /* Instance Id for Peripheral NVMCTRL */
    PAC_PERIPHERAL_NVMCTRL = ID_NVMCTRL,

    /* Instance Id for Peripheral PM */
    PAC_PERIPHERAL_PM = ID_PM,

    /* Instance Id for Peripheral PORT */
    PAC_PERIPHERAL_PORT = ID_PORT,

    /* Instance Id for Peripheral PTC */
    PAC_PERIPHERAL_PTC = ID_PTC,

    /* Instance Id for Peripheral RTC */
    PAC_PERIPHERAL_RTC = ID_RTC,

    /* Instance Id for Peripheral SERCOM0 */
    PAC_PERIPHERAL_SERCOM0 = ID_SERCOM0,

    /* Instance Id for Peripheral SERCOM1 */
    PAC_PERIPHERAL_SERCOM1 = ID_SERCOM1,

    /* Instance Id for Peripheral SERCOM2 */
    PAC_PERIPHERAL_SERCOM2 = ID_SERCOM2,

    /* Instance Id for Peripheral SERCOM3 */
    PAC_PERIPHERAL_SERCOM3 = ID_SERCOM3,

    /* Instance Id for Peripheral SERCOM4 */
    PAC_PERIPHERAL_SERCOM4 = ID_SERCOM4,

    /* Instance Id for Peripheral SERCOM5 */
    PAC_PERIPHERAL_SERCOM5 = ID_SERCOM5,

    /* Instance Id for Peripheral SYSCTRL */
    PAC_PERIPHERAL_SYSCTRL = ID_SYSCTRL,

    /* Instance Id for Peripheral TC3 */
    PAC_PERIPHERAL_TC3 = ID_TC3,

    /* Instance Id for Peripheral TC4 */
    PAC_PERIPHERAL_TC4 = ID_TC4,

    /* Instance Id for Peripheral TC5 */
    PAC_PERIPHERAL_TC5 = ID_TC5,

    /* Instance Id for Peripheral TC6 */
    PAC_PERIPHERAL_TC6 = ID_TC6,

    /* Instance Id for Peripheral TC7 */
    PAC_PERIPHERAL_TC7 = ID_TC7,

    /* Instance Id for Peripheral TCC0 */
    PAC_PERIPHERAL_TCC0 = ID_TCC0,

    /* Instance Id for Peripheral TCC1 */
    PAC_PERIPHERAL_TCC1 = ID_TCC1,

    /* Instance Id for Peripheral TCC2 */
    PAC_PERIPHERAL_TCC2 = ID_TCC2,

    /* Instance Id for Peripheral USB */
    PAC_PERIPHERAL_USB = ID_USB,

    /* Instance Id for Peripheral WDT */
    PAC_PERIPHERAL_WDT = ID_WDT,

    PAC_PERIPHERAL_NONE = -1

} PAC_PERIPHERAL;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

bool PAC_PeripheralIsProtected( PAC_PERIPHERAL peripheral );

void PAC_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_PAC_H */