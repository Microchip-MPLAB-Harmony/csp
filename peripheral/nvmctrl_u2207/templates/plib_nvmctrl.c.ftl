/*******************************************************************************
  Non-Volatile Memory Controller(NVMCTRL${NVMCTRL_INDEX?string}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvmctrl${NVMCTRL_INDEX?string}.c

  Summary:
    Interface definition of NVMCTRL${NVMCTRL_INDEX?string} Plib.

  Description:
    This file defines the interface for the NVMCTRL${NVMCTRL_INDEX?string} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_nvmctrl${NVMCTRL_INDEX?string}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Constants
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} Error Status Constant

  Summary:
    Stores the NVMCTRL Error.

  Description:
    This constant Stores the NVMCTRL Error.

  Remarks:
    None.
*/

static uint32_t status = 0;

// *****************************************************************************
// *****************************************************************************
// Section: NVMCTRL${NVMCTRL_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************

<#if NVMCTRL_INTERRUPT_MODE == true>
// *****************************************************************************
/* nvmctrl${NVMCTRL_INDEX?string}CallbackFunc callback function pointer

  Summary:
    A pointer to a function.

  Description:
    A pointer to a function with a calling signature defined by the
    NVMCTRL_CALLBACK data type.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

NVMCTRL_CALLBACK nvmctrl${NVMCTRL_INDEX?string}CallbackFunc;

// *****************************************************************************
/* nvmctrl${NVMCTRL_INDEX?string}context pointer variable

  Summary:
    A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Description:
    Provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

uintptr_t nvmctrl${NVMCTRL_INDEX?string}context;

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    operation is complete.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the NVMCTRL has completed an operation and is ready to receive new command.
    It also passes a context value that is passed into the callback function
    when it is called. This function is available only when the library is
    generated with interrupt option (in MHC) enabled.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister( NVMCTRL_CALLBACK callback, uintptr_t context )
{
    /* Register callback function */
    nvmctrl${NVMCTRL_INDEX?string}CallbackFunc = callback;
    nvmctrl${NVMCTRL_INDEX?string}context = context;
}

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void)

  Summary:
    Calls the callback function.

  Description:
    This function calls the callback function when an interrupt occurs due to
    the completion of a write or an erase operation.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void)
{
    if(( NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk ) && (NVMCTRL_REGS->NVMCTRL_INTENSET & NVMCTRL_INTENSET_READY_Msk))
    {
        if(*nvmctrl0CallbackFunc != NULL)
        {
            /* Calling callback func */
            (*nvmctrl0CallbackFunc)(nvmctrl0context);
        }

        /* Clear interrupt */
        NVMCTRL_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
    }
}
</#if>

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_Initialize( void )

  Summary:
    Initializes given instance of the NVMCTRL peripheral.

  Description:
    This function initializes the given instance of the NVMCTRL peripheral as
    configured by the user from within the MHC.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_Initialize(void)
{
    /* Disable Manual Write */
    <@compress single_line=true>NVMCTRL_REGS->NVMCTRL_CTRLB = NVMCTRL_CTRLB_READMODE_${NVMCTRL_CTRLB_READMODE_SELECTION}
                                                         | NVMCTRL_CTRLB_SLEEPPRM_${NVMCTRL_CTRLB_POWER_REDUCTION_MODE}
                                                         ${NVMCTRL_CACHE_ENABLE?then('', '| NVMCTRL_CTRLB_CACHEDIS_Msk')};</@compress>

    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = (0x00U);

<#if NVMCTRL_INTERRUPT_MODE == true>
    /* Clear interrupt flag */
    NVMCTRL_REGS->NVMCTRL_INTENCLR = NVMCTRL_INTENCLR_READY_Msk;
</#if>
}

<#if NVMCTRL_CACHE_ENABLE == true>
// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate ( void );

  Summary:
    Invalidates all cache lines.

  Description:
    This function invalidates all cache lines. This function is available if the
    library was generated with the Cache option (in MHC) enabled.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate(void)
{
    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_INVALL | NVMCTRL_CTRLA_CMDEX_KEY;
}
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite( uint32_t address, uint32_t* data )

  Summary:
    Writes one page of data to given RWWEEPROM address.

  Description:
    This function will write one page of data to the RWWEEPROM address specified
    by the address parameter. The size of the input buffer should be one NVM
    page.  The address should be aligned on a page boundary. Unlike the
    NVMCTRL${NVMCTRL_INDEX?string}_PageWrite function, calling this function
    will not cause the CPU execution to stall. If the interrupt operation was
    enabled and if a callback was registered, then the callback function will be
    called. The NVMCTRL${NVMCTRL_INDEX?string}_IsBusy() function can be used to
    poll for completion of the operation. The application should ensure that
    there are no other operations in progress before calling this function.
    This can be checked by calling the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy()
    function.

    This function is blocking if the library was generated (in MHC) with the
    interrupt option disabled. If blocking, the function will exit only after
    write operation has completed. This function is not blocking if the library
    was generated with the interrupt option enabled. In this mode, the function
    initiates the operation and then exits. The application can either register
    a callback function or call the NVMCTRL0_IsBusy() function periodically to
    check for completion of the operation.

    Once the operation is complete,
    the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() function can be called to
    check operation success.

    This API is generated if the RWWEEPROM API option (in MHC) is selected.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite (const uint32_t address,  uint32_t *data)
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Erase the page buffer before buffering new data */
    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    /* Writing 32-bit words in the given address */
    for ( i = 0; i < (NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

     return true;

}

// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase( uint32_t address)

  Summary:
    Erases a Row in the RWWEEPROM.

  Description:
    This function will erase one row in RWWEEPROM. The address of the row to be
    erased is specified by the address parameter. This address can be any
    address in the row.  Unlike the NVMCTRL${NVMCTRL_INDEX?string}_RowErase()
    function, calling this function will not cause the CPU execution to stall.
    If the interrupt operation was enabled and if a callback was registered,
    then the callback function will be called.
    The NVMCTRL${NVMCTRL_INDEX?string}_IsBusy() function can be used to poll for
    completion of the operation. The application should ensure that there are no
    other operations in progress before calling this function.

    This function is blocking if the library was generated (in MHC) with the
    interrupt option disabled. If blocking, the function will exit only after
    write operation has completed. This function is not blocking if the library
    was generated with the interrupt option enabled. In this mode, the function
    initiates the operation and then exits. The application can either register
    a callback function or call the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy()
    function periodically to check for completion of the operation.

    Once the operation is complete,
    the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() function can be called to
    check operation success. Erasing a row will erase all the contents of all
    the pages in the row.

    This API is generated if the RWWEEPROM API option (in MHC) is selected.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase( uint32_t address )
{
    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

     /* Set address and command */
    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_RWWEEER | NVMCTRL_CTRLA_CMDEX_KEY;

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

     return true;

}
</#if>

// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_PageWrite( uint32_t address, uint32_t* data )

  Summary:
    Writes one page of data to given NVM address.

  Description:
    This function will write one page of data to the NVM address specified by
    the address parameter. The size of the input buffer should be one NVM page.
    The address should be aligned on a page boundary. Calling this function will
    cause the CPU execution to stall, hence blocking execution of any other
    thread. Execution resumes when the Write operation has completed. If the
    interrupt operation was enabled and if a callback was registered, then the
    callback function will be called.
    The NVMCTRL${NVMCTRL_INDEX?string}_IsBusy() function can be used to poll for
    completion of the operation. The application should ensure that there are no
    other operations in progress before calling this function.

    Once the operation is complete,
    the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() function can be called to
    check operation success.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_PageWrite(const uint32_t address, uint32_t *data)
{
    uint32_t i = 0;
    uint32_t * paddress = (uint32_t *)address;

    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Erase the page buffer before buffering new data */
    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_PBC_Val | NVMCTRL_CTRLA_CMDEX_KEY;

    /* writing 32-bit data into the given address */
    for (i = 0; i < (NVMCTRL${NVMCTRL_INDEX?string}_FLASH_PAGESIZE/4); i++)
    {
        *paddress++ = data[i];
    }

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_RowErase( uint32_t address)

  Summary:
    Erases a Row in the NVM

  Description:
    This function will erase one row in NVM. The address of the row to be erased
    is specified by the address parameter. This address can be any address in
    the row.  Calling this function will cause the CPU execution to stall, hence
    blocking execution of any other thread. Execution resumes when the Erase
    operation has completed. If the interrupt operation was enabled and if a
    callback was registered, then the callback function will be called.  The
    NVMCTRL${NVMCTRL_INDEX?string}_IsBusy() function can be used to poll for
    completion of the operation. The application should ensure that there are no
    other operations in progress before calling this function.

    Once the operation is complete, the
    NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() function can be called to check
    operation success. Erasing a row will erase all the contents of all the
    pages in the row.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RowErase( uint32_t address )
{
    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_ER_Val | NVMCTRL_CTRLA_CMDEX_KEY;

<#if NVMCTRL_INTERRUPT_MODE == true>
    NVMCTRL_REGS->NVMCTRL_INTENSET = NVMCTRL_INTENSET_READY_Msk;
<#else>
    /* Check if the module is busy */
    while((NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk) != NVMCTRL_INTFLAG_READY_Msk)
    {
        /* Force-wait for the buffer clear to complete */
    }
</#if>

    return true;
}

// *****************************************************************************
/* Function:
    NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void )

  Summary:
    Returns the error state of NVM controller.

  Description:
    This function returns the erorr status of the last NVMCTRL operation. The
    return value can be either NVMCTRL_ERROR_NONE, a single error or a
    combination of multiple error conditions.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void )
{
    return (status |= NVMCTRL_REGS->NVMCTRL_STATUS);
}

<#if NVMCTRL_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_IsBusy( void )

  Summary:
    Returns the current status of NVM controller.

  Description:
    This function returns the busy status of the NVM Controller. This function
    should be called to check for module readiness before initiating a Erase or
    a Write operation. The controller becomes busy on a NVM Write, Erase or an
    EEPROM Write, Erase operation. Once initiated, this function
    can be called to poll the completion of the Erase or Write operation.

    This function can be used as an alternative to the callback function. In
    that, the application can call this function periodically to check for
    operation completion instead of waiting for callback to be called.

    This API is generated if the interrupt option (in MHC) is enabled.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_IsBusy(void)
{
    return (!(NVMCTRL_REGS->NVMCTRL_INTFLAG & NVMCTRL_INTFLAG_READY_Msk));
}
</#if>

<#if NVMCTRL_REGION_LOCK_UNLOCK == true>
// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_RegionLock (uint32_t address);

  Summary:
    Locks a NVMCTRL region.

  Description:
    This function locks the region that contains the address specified in
    address parameter. Locking a region prevents write and erase operations on
    all pages in the region. A region is unlocked by either calling the
    NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock() function or by device reset.
    The NVM is divided into 16 equal sized regions. The size of each region is
    device dependant. Refer to the device specific datasheet for more details.

    This API is generated if the Region Lock/Unlock API option (in MHC) is
    selected.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_RegionLock(uint32_t address)
{
    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_LR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
}

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock (uint32_t address);

  Summary:
    Unlocks a NVM region.

  Description:
    This function unlocks a region that was locked using the
    NVMCTRL${NVMCTRL_INDEX?string}_RegionLock() function. The address
    parameter can be any address within the region. Unlocking a region unlocks
    all pages in the region and makes these pages accessible to write and erase
    operations.

    This API is generated if the Region Lock/Unlock API option (in MHC) is
    selected.

  Remarks:
    Refer plib_nvmctrl${NVMCTRL_INDEX?string}.h file for more information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock(uint32_t address)
{
    /* Clear error flags */
    NVMCTRL_REGS->NVMCTRL_STATUS = 0x1C;

    /* Clear global error flag */
    status = 0;

    /* Set address and command */
    NVMCTRL_REGS->NVMCTRL_ADDR = address >> 1;

    NVMCTRL_REGS->NVMCTRL_CTRLA = NVMCTRL_CTRLA_CMD_UR_Val | NVMCTRL_CTRLA_CMDEX_KEY;
}
</#if>
