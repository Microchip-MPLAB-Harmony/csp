/*******************************************************************************
  SHDWC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_shdwc.c

  Summary:
    Shutdown Controller PLIB

  Description:
    Shutdown Controller PLIB Implementation
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


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "device.h"
#include "plib_${SHDWC_INSTANCE_NAME?lower_case}.h"
#include <stdint.h>

void ${SHDWC_INSTANCE_NAME}_Initialize(void)
{
    ${SHDWC_INSTANCE_NAME}_REGS->SHDW_MR = <#list EVENT_LIST?word_list as event> SHDW_MR_${event}_Msk | </#list>
        SHDW_MR_WKUPDBC(${WKUPDBC});

    ${SHDWC_INSTANCE_NAME}_REGS->SHDW_WUIR = 0 <#list PINS_LIST?word_list as pin> | SHDW_WUIR_${pin}_ENABLE <#assign type=.vars[pin?replace("EN", "T")]> | SHDW_WUIR_${pin?replace("EN", "T")}_${type} </#list>;
}

void ${SHDWC_INSTANCE_NAME}_Shutdown(void)
{
    /* Clear previous wake-up event before shutdown */
    ${SHDWC_INSTANCE_NAME}_GetWakeup();
    ${SHDWC_INSTANCE_NAME}_REGS->SHDW_CR = SHDW_CR_KEY_PASSWD | SHDW_CR_SHDW_Msk;
}

uint32_t ${SHDWC_INSTANCE_NAME}_GetWakeup(void)
{
    return ${SHDWC_INSTANCE_NAME}_REGS->SHDW_SR;
}

/*******************************************************************************
 End of File
*/
