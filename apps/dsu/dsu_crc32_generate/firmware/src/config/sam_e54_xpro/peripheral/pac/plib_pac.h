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

/* Guards against multiple inclusion */
#ifndef PLIB_PAC_H
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
    /* No Action */
    PAC_PROTECTION_OFF,

    /* Clear the peripheral write control protection */
    PAC_PROTECTION_CLEAR,

    /* Set the peripheral write control protection */
    PAC_PROTECTION_SET,

    /* Set and lock the peripheral write control until the next hardware reset */
    PAC_PROTECTION_SET_AND_LOCK,

} PAC_PROTECTION;

typedef enum
{
    /* Instance Id for Peripheral AC */
    PAC_PERIPHERAL_AC = ID_AC,

    /* Instance Id for Peripheral ADC0 */
    PAC_PERIPHERAL_ADC0 = ID_ADC0,

    /* Instance Id for Peripheral ADC1 */
    PAC_PERIPHERAL_ADC1 = ID_ADC1,

    /* Instance Id for Peripheral AES */
    PAC_PERIPHERAL_AES = ID_AES,

    /* Instance Id for Peripheral CAN0 */
    PAC_PERIPHERAL_CAN0 = ID_CAN0,

    /* Instance Id for Peripheral CAN1 */
    PAC_PERIPHERAL_CAN1 = ID_CAN1,

    /* Instance Id for Peripheral CCL */
    PAC_PERIPHERAL_CCL = ID_CCL,

    /* Instance Id for Peripheral CMCC */
    PAC_PERIPHERAL_CMCC = ID_CMCC,

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

    /* Instance Id for Peripheral FREQM */
    PAC_PERIPHERAL_FREQM = ID_FREQM,

    /* Instance Id for Peripheral GCLK */
    PAC_PERIPHERAL_GCLK = ID_GCLK,

    /* Instance Id for Peripheral GMAC */
    PAC_PERIPHERAL_GMAC = ID_GMAC,

    /* Instance Id for Peripheral HMATRIX */
    PAC_PERIPHERAL_HMATRIX = ID_HMATRIX,

    /* Instance Id for Peripheral ICM */
    PAC_PERIPHERAL_ICM = ID_ICM,

    /* Instance Id for Peripheral I2S */
    PAC_PERIPHERAL_I2S = ID_I2S,

    /* Instance Id for Peripheral MCLK */
    PAC_PERIPHERAL_MCLK = ID_MCLK,

    /* Instance Id for Peripheral NVMCTRL */
    PAC_PERIPHERAL_NVMCTRL = ID_NVMCTRL,

    /* Instance Id for Peripheral OSCCTRL */
    PAC_PERIPHERAL_OSCCTRL = ID_OSCCTRL,

    /* Instance Id for Peripheral OSC32KCTRL */
    PAC_PERIPHERAL_OSC32KCTRL = ID_OSC32KCTRL,

    /* Instance Id for Peripheral PAC */
    PAC_PERIPHERAL_PAC = ID_PAC,

    /* Instance Id for Peripheral PCC */
    PAC_PERIPHERAL_PCC = ID_PCC,

    /* Instance Id for Peripheral PDEC */
    PAC_PERIPHERAL_PDEC = ID_PDEC,

    /* Instance Id for Peripheral PM */
    PAC_PERIPHERAL_PM = ID_PM,

    /* Instance Id for Peripheral PORT */
    PAC_PERIPHERAL_PORT = ID_PORT,

    /* Instance Id for Peripheral PUKCC */
    PAC_PERIPHERAL_PUKCC = ID_PUKCC,

    /* Instance Id for Peripheral QSPI */
    PAC_PERIPHERAL_QSPI = ID_QSPI,

    /* Instance Id for Peripheral RAMECC */
    PAC_PERIPHERAL_RAMECC = ID_RAMECC,

    /* Instance Id for Peripheral RSTC */
    PAC_PERIPHERAL_RSTC = ID_RSTC,

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

    /* Instance Id for Peripheral SERCOM6 */
    PAC_PERIPHERAL_SERCOM6 = ID_SERCOM6,

    /* Instance Id for Peripheral SERCOM7 */
    PAC_PERIPHERAL_SERCOM7 = ID_SERCOM7,

    /* Instance Id for Peripheral SUPC */
    PAC_PERIPHERAL_SUPC = ID_SUPC,

    /* Instance Id for Peripheral TC0 */
    PAC_PERIPHERAL_TC0 = ID_TC0,

    /* Instance Id for Peripheral TC1 */
    PAC_PERIPHERAL_TC1 = ID_TC1,

    /* Instance Id for Peripheral TC2 */
    PAC_PERIPHERAL_TC2 = ID_TC2,

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

    /* Instance Id for Peripheral TCC3 */
    PAC_PERIPHERAL_TCC3 = ID_TCC3,

    /* Instance Id for Peripheral TCC4 */
    PAC_PERIPHERAL_TCC4 = ID_TCC4,

    /* Instance Id for Peripheral TRNG */
    PAC_PERIPHERAL_TRNG = ID_TRNG,

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

void PAC_Initialize( void );

void PAC_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation );

bool PAC_PeripheralIsProtected( PAC_PERIPHERAL peripheral );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_PAC_H */
