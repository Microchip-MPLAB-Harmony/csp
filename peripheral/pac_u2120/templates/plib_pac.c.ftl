/*******************************************************************************
  Peripheral Access Controller (PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PAC_INSTANCE_NAME?lower_case}.c

  Summary
    Source for PAC peripheral library interface Implementation.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_${PAC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* Peripheral Bridge A - Peripheral count */
#define  PAC_PERIPHERAL_BRIDGE_A_PERI_COUNT     (13)

/* Peripheral Bridge B - Peripheral count */
#define  PAC_PERIPHERAL_BRIDGE_B_PERI_COUNT     (5)

/* Peripheral Bridge C - Peripheral count */
#define  PAC_PERIPHERAL_BRIDGE_C_PERI_COUNT     (24)

/* Peripheral Bridge D - Peripheral count */
#define  PAC_PERIPHERAL_BRIDGE_D_PERI_COUNT     (5)

<#if PAC_INTERRRUPT_MODE = true>

// *****************************************************************************
/* PAC Callback Object

  Summary:
    PAC Peripheral Callback object.

  Description:
    This local data object holds the function signature for the PAC peripheral
    callback function.

  Remarks:
    None.
*/

typedef struct
{
    /* PAC Callback Handler */
    PAC_CALLBACK callback;

    /* client context*/
    uintptr_t context;

} PAC_CALLBACK_OBJ;

/* PAC Callback object */
PAC_CALLBACK_OBJ ${PAC_INSTANCE_NAME?lower_case}CallbackObject;

</#if>

// *****************************************************************************
// *****************************************************************************
// Section: PAC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_Initialize (void);

  Summary:
    Initializes given instance of PAC peripheral.

  Description:
    This function initializes given instance of PAC peripheral of the device
    with the values configured in MCC GUI.

  Remarks:
    Refer plib_pac0.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_Initialize( void )
{
<#list PAC_BRIDGE_COUNT..0 as i>
    <#assign PAC_BRIDGE = "PAC_" + i + "_BRIDGE">
    <#assign PAC_BRIDGE_PERI_COUNT = "PAC_BRIDGE_" + i + "_PERI_COUNT">
        <#if .vars[PAC_BRIDGE_PERI_COUNT]?has_content>
            <#assign PAC_PERI_COUNT = .vars[PAC_BRIDGE_PERI_COUNT]>
            <#list PAC_PERI_COUNT..0 as j>
                <#assign PAC_REG_PROTECT = "PAC_BRIDGE_" + i + "_PERI_" + j + "_REG_PROTECT">
                <#assign PAC_BRIDGE_PERI_NAME = "PAC_BRIDGE_" + i + "_PERI_" + j + "_NAME">
                    <#if .vars[PAC_REG_PROTECT]?has_content>
                        <#if (.vars[PAC_REG_PROTECT] != "OFF")>
    <#lt>    ${PAC_INSTANCE_NAME}_PeripheralProtect (PAC_PERIPHERAL_${.vars[PAC_BRIDGE]}_${.vars[PAC_BRIDGE_PERI_NAME]}, PAC_PROTECTION_${.vars[PAC_REG_PROTECT]});

                        </#if>
                    </#if>
            </#list>
        </#if>
</#list>

    <#if PAC_INTERRRUPT_MODE == true>
    /* Enable PAC interrupt */
    ${PAC_INSTANCE_NAME}_REGS->PAC_INTENSET = PAC_INTENSET_ERR_Msk;
    </#if>

    <#if PAC_ERROR_EVENT == true>
    /* Enable PAC Error Event Output */
    ${PAC_INSTANCE_NAME}_REGS->PAC_EVCTRL |= PAC_EVCTRL_ERREO_Msk;
    </#if>
}

// *****************************************************************************
/* Function:
    bool ${PAC_INSTANCE_NAME}_PeripheralIsProtected (PAC_PERIPHERAL peripheral)

  Summary:
    Gets write protect status for the given interface module

  Description:
    This function returns true if the specified peripheral is write protected.
    It returns false otherwise.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

bool ${PAC_INSTANCE_NAME}_PeripheralIsProtected (PAC_PERIPHERAL peripheral)
{
    uint32_t    u32StatusRegVal = 0x0;
    uint32_t    u32StatusPeriID = 0x0;
    uint32_t    *pu32StatusRegAddr = (uint32_t*) &(${PAC_INSTANCE_NAME}_REGS->PAC_STATUSA);
    bool        bPeriStatus     = false;

    /* Get the Bit index for the peripheral */
    u32StatusPeriID = (peripheral % 32);

    /* Read the Peripheral bridge status register value */
    u32StatusRegVal = *(pu32StatusRegAddr + (peripheral / 32));

    /* Verify if the peripheral is protected or not */
    bPeriStatus = (bool)(u32StatusRegVal & (1 << u32StatusPeriID));

    return (bPeriStatus);
}

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_PeripheralProtect (PAC_PERIPHERAL peripheral,
                                  PAC_PROTECTION operation)

  Summary:
    This function performs a PAC protection operation on the specified
    peripheral.

  Description:
    This function performs a PAC protection operation on the specified
    peripheral. The function can be called to disable the protection
    (PAC_PROTECTION_CLEAR), to set write protection which can be disabled via a
    clear operation (PAC_PROTECTION_SET) and to set write protection that cannot
    be cleared (PAC_PROTECTION_SET_AND_LOCK).

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_PeripheralProtect(PAC_PERIPHERAL peripheral, PAC_PROTECTION operation)
{
    /* Set Peripheral Access Control */
    ${PAC_INSTANCE_NAME}_REGS->PAC_WRCTRL = (PAC_WRCTRL_PERID(peripheral) | (operation << PAC_WRCTRL_KEY_Pos));
}

// *****************************************************************************
/* Function:
    bool ${PAC_INSTANCE_NAME}_PeripheralErrorOccurred (void)

  Summary:
    Returns true if any Peripheral Access Error has occurred.

  Description:
    This function returns true if any peripheral access error has occurred. The
    application can then call the ${PAC_INSTANCE_NAME}_PeripheralErrorGet() function
    to identify the peripheral on which the error has occurred.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

bool ${PAC_INSTANCE_NAME}_PeripheralErrorOccurred (void)
{
    return (bool)((${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGA & PAC_INTFLAGA_Msk) |
                  (${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGB & PAC_INTFLAGB_Msk) |
                  (${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGC & PAC_INTFLAGC_Msk) |
                  (${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGD & PAC_INTFLAGD_Msk));
}

// *****************************************************************************
/* Function:
    PAC_PERIPHERAL ${PAC_INSTANCE_NAME}_PeripheralErrorGet (void)

  Summary:
    Returns the first peripheral that is reporting an access error.

  Description:
    This function returns the first peripheral that is reporting an access
    error. The application can call this function to identify the peripheral
    that is a reporting an access error. In case where multiple peripherals are
    reporting access errors, the application must call this function multiple
    times. The application can use the ${PAC_INSTANCE_NAME}_PeripheralErrorOccurred()
    function to check if a peripheral access error is active. The application
    must use the ${PAC_INSTANCE_NAME}_PeripheralErrorClear() function to clear the
    error before calling the ${PAC_INSTANCE_NAME}_PeripheralErrorGet() function
    again. Not clearing the error will cause the function to continue reporting
    the error on the same peripheral.

    In a case where the peripheral is experiencing repeated access errors, it is
    possible that this function will return the same peripheral ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application implement a convenient break mechanism to prevent a blocking
    loop.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

PAC_PERIPHERAL ${PAC_INSTANCE_NAME}_PeripheralErrorGet (void)
{
    uint32_t    u32PeriBridgeAErrStatus = 0x0;
    uint32_t    u32PeriBridgeBErrStatus = 0x0;
    uint32_t    u32PeriBridgeCErrStatus = 0x0;
    uint32_t    u32PeriBridgeDErrStatus = 0x0;
    uint32_t    u32PACErrBit            = 0x1;
    uint32_t    u32PeriCnt              = 0x0;
    PAC_PERIPHERAL peripheral           = PAC_PERIPHERAL_ANY;

    /* Verify if Peripheral bridge A has an error */
    u32PeriBridgeAErrStatus = ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGA;

    /* Verify if Peripheral bridge B has an error */
    u32PeriBridgeBErrStatus = ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGB;

    /* Verify if Peripheral bridge C has an error */
    u32PeriBridgeCErrStatus = ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGC;

    /* Verify if Peripheral bridge D has an error */
    u32PeriBridgeDErrStatus = ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGD;

    /* Verify if Peripheral in Peripheral Bridge A has reported error */
    if (u32PeriBridgeAErrStatus != 0x0)
    {
        while (u32PeriCnt < PAC_PERIPHERAL_BRIDGE_A_PERI_COUNT)
        {
            if (u32PeriBridgeAErrStatus & u32PACErrBit)
            {
                peripheral = (PAC_PERIPHERAL)u32PeriCnt;
                break;
            }
            else
            {
                u32PACErrBit = u32PACErrBit << 1;
                u32PeriCnt++;
            }
        }
    }
    else if (u32PeriBridgeBErrStatus != 0x0)
    {
        while (u32PeriCnt < PAC_PERIPHERAL_BRIDGE_B_PERI_COUNT)
        {
            if (u32PeriBridgeBErrStatus & u32PACErrBit)
            {
                peripheral = (PAC_PERIPHERAL)(u32PeriCnt + (1 * 32));
                break;
            }
            else
            {
                u32PACErrBit = u32PACErrBit << 1;
                u32PeriCnt++;
            }
        }
    }
    else if (u32PeriBridgeCErrStatus != 0x0)
    {
        while (u32PeriCnt < PAC_PERIPHERAL_BRIDGE_C_PERI_COUNT)
        {
            if (u32PeriBridgeCErrStatus & u32PACErrBit)
            {
                peripheral = (PAC_PERIPHERAL)(u32PeriCnt + (2 * 32));
                break;
            }
            else
            {
                u32PACErrBit = u32PACErrBit << 1;
                u32PeriCnt++;
            }
        }
    }
    else if (u32PeriBridgeDErrStatus != 0x0)
    {
        while (u32PeriCnt < PAC_PERIPHERAL_BRIDGE_D_PERI_COUNT)
        {
            if (u32PeriBridgeDErrStatus & u32PACErrBit)
            {
                peripheral = (PAC_PERIPHERAL)(u32PeriCnt + (3 * 32));
                break;
            }
            else
            {
                u32PACErrBit = u32PACErrBit << 1;
                u32PeriCnt++;
            }
        }
    }

    return (peripheral);
}

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_PeripheralErrorClear (PAC_PERIPHERAL peripheral)

  Summary:
    Clear the peripheral access error flag.

  Description:
    Calling this function will cause the peripheral access error flag to be
    cleared. This will then cause the ${PAC_INSTANCE_NAME}_PeripheralErrorGet()
    function to identify the next peripheral that is reporting an error. If
    after calling this function, there are no peripheral errors active, the
    ${PAC_INSTANCE_NAME}_PeripheralErrorOccurred() function will return false.
    The application must call this function to clear the error on the peripheral
    that was identified by the last call of the
    ${PAC_INSTANCE_NAME}_PeripheralErrorGet() function.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_PeripheralErrorClear (PAC_PERIPHERAL peripheral)
{
    uint32_t    u32PeriIdReg    = 0x0;
    uint32_t    *pu32StatusRegAddr = (uint32_t*) &(${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGA);

    /* Get the Bit index for the peripheral */
    u32PeriIdReg = (peripheral % 32);

    if (peripheral == PAC_PERIPHERAL_ANY)
    {
        ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGA = PAC_INTFLAGA_Msk;
        ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGB = PAC_INTFLAGB_Msk;
        ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGC = PAC_INTFLAGC_Msk;
        ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGD = PAC_INTFLAGD_Msk;
    }
	else
	{
		/* Clear the Peripheral error */
		*(pu32StatusRegAddr + (peripheral / 32)) = (1 << u32PeriIdReg);
	}
}

// *****************************************************************************
/* Function:
    bool ${PAC_INSTANCE_NAME}_AHBSlaveErrorOccurred (void)

  Summary:
    Returns true if an error has occurred on any of the AHB slaves.

  Description:
    This function returns true if any AHB Slave error has occurred. The
    application can then call the ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet() function
    to identify the AHB Slave on which the error has occurred.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

bool ${PAC_INSTANCE_NAME}_AHBSlaveErrorOccurred (void)
{
    return (bool)(${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGAHB & PAC_INTFLAGAHB_Msk);
}

// *****************************************************************************
/* Function:
    PAC_AHB_SLAVE ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet (PAC_AHB_SLAVE ahbSlave)

  Summary:
    Returns the first AHB Slave that is reporting an access error.

  Description:
    This function returns the first AHB Slave that is reporting an access
    error. The application can call this function to identify the AHB Slave
    that is a reporting an access error. In case where multiple AHB Slaves are
    reporting access errors, the application must call this function multiple
    times. The application can use the ${PAC_INSTANCE_NAME}_AHBSlaveErrorOccurred()
    function to check if a AHB Slave access error is active. The application
    must use the ${PAC_INSTANCE_NAME}_AHBSlaveErrorClear() function to clear the
    error before calling the ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet() function again.
    Not clearing the error will cause the function to continue reporting the
    error on the same AHB Slave.

    In a case where the AHB Slave is experiencing repeated access errors, it is
    possible that this function will return the same AHB Slave ID on each call.
    If a while loop is used to process and clear error, it is recommended that
    the application in implement a convenient break mechanism to prevent a
    blocking loop.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

PAC_AHB_SLAVE ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet (void)
{
    uint32_t    u32AHBSlaveErrStatus = 0x0;
    uint32_t    u32AHBSlaveErrorBit  = 0x1;
    PAC_AHB_SLAVE pacAHBSlaveBus = PAC_AHB_SLAVE_ANY;

    /* Read AHB Slave Bus Interrupt Flag Status register */
    u32AHBSlaveErrStatus = ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGAHB;

    if (u32AHBSlaveErrStatus != 0x0)
    {
        while (u32AHBSlaveErrorBit <= PAC_AHB_SLAVE_HPB3)
        {
            if (u32AHBSlaveErrStatus & u32AHBSlaveErrorBit)
            {
                pacAHBSlaveBus = u32AHBSlaveErrorBit;
                break;
            }
            else
            {
                u32AHBSlaveErrorBit = u32AHBSlaveErrorBit << 1;
            }
        }
    }

    return (pacAHBSlaveBus);
}

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_AHBSlaveErrorClear (PAC_AHB_SLAVE ahbSlave)

  Summary:
    Clear the AHB Slave access error flag.

  Description:
    Calling this function will cause the AHB Slave access error flag to be
    cleared. This will then cause the ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet()
    function to identify the next AHB Slave that is reporting an error. If after
    calling this function, there are no AHB Slave errors active, the
    ${PAC_INSTANCE_NAME}_AHBSlaveErrorOccurred() function will return false. The
    application must call this function to clear the error on the AHB Slave that
    was identified by the last call of the ${PAC_INSTANCE_NAME}_AHBSlaveErrorGet()
    function.

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_AHBSlaveErrorClear (PAC_AHB_SLAVE ahbSlave)
{
    ${PAC_INSTANCE_NAME}_REGS->PAC_INTFLAGAHB = ahbSlave & PAC_INTFLAGAHB_Msk;
}

<#if PAC_INTERRRUPT_MODE = true>

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_CallbackRegister (PAC_CALLBACK callback, uintptr_t context)

  Summary:
    Registers the function to be called when a PAC error has occurred.

  Description
    This function registers the callback function to be called when a PAC error
    has occurred. The function is available only when the module interrupt is
    enabled in MHC.

  Remarks:
    plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_CallbackRegister ( PAC_CALLBACK callback, uintptr_t context )
{
    ${PAC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;

    ${PAC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

// *****************************************************************************
/* Function:
    void ${PAC_INSTANCE_NAME}_InterruptHandler ( void )

  Summary:
    PAC Interrupt Handler.

  Description
    This PAC Interrupt handler function handles PAC interrupts

  Remarks:
    Refer plib_${PAC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PAC_INSTANCE_NAME}_InterruptHandler (void)
{
    if (${PAC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL)
    {
        ${PAC_INSTANCE_NAME?lower_case}CallbackObject.callback(${PAC_INSTANCE_NAME?lower_case}CallbackObject.context);
    }
}

</#if>
