/*******************************************************************************
  Non-Volatile Memory Controller(NVMCTRL${NVMCTRL_INDEX?string}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_nvmctrl${NVMCTRL_INDEX?string}.h

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

#ifndef PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H
#define PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Constants
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} Flash Start Address Constant

  Summary:
    Defines the start address of NVMCTRL${NVMCTRL_INDEX?string} Flash.

  Description:
    This constant defines the start address of Flash. It is recommended for the
    target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_START_ADDRESS         (${.vars["FLASH_START_ADDRESS"]}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} Flash Size Constant

  Summary:
    Defines the size (in bytes) of Flash.

  Description:
    This constant defines the size (in bytes) of flash. It is recommended
    for the target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_SIZE       (${FLASH_SIZE}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} Flash Page Size Constant

  Summary:
    Defines the size (in bytes) of a NVMCTRL${NVMCTRL_INDEX?string} Page.

  Description:
    This constant defines the size (in bytes) of a NVM page. It is recommended
    for the target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_PAGESIZE          (${FLASH_PROGRAM_SIZE}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} Flash Row Size Constant

  Summary:
    Defines the size (in bytes) of a NVMCTRL${NVMCTRL_INDEX?string} Row.

  Description:
    This constant defines the size (in bytes) of a NVM Row. It is recommended
    for the target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_FLASH_ROWSIZE           (${FLASH_ERASE_SIZE}U)

<#if NVMCTRL_RWW_EEPROM == true>
// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM Start Address Constant

  Summary:
    Defines the start address of NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM.

  Description:
    This constant defines the start address of RWWEEPROM. It is recommended for
    the target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_START_ADDRESS     (${.vars["FLASH_RWWEEPROM_START_ADDRESS"]}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM Size Constant

  Summary:
    Defines the size (in bytes) of RWWEEPROM.

  Description:
    This constant defines the size (in bytes) of RWWEEPROM. It is recommended
    for the target application to use this constant in place hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_SIZE   (${FLASH_RWWEEPROM_SIZE}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM Page Size Constant

  Summary:
    Defines the size (in bytes) of a NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM
    Page.

  Description:
    This constant defines the size (in bytes) of a NVM RWWEEPROM page. It is
    recommended for the target application to use this constant in place
    hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PAGESIZE          (${FLASH_RWWEEPROM_PROGRAM_SIZE}U)

// *****************************************************************************
/* NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM Row Size Constant

  Summary:
    Defines the size (in bytes) of a NVMCTRL${NVMCTRL_INDEX?string} RWWEEPROM
    Row.

  Description:
    This constant defines the size (in bytes) of a NVM RWWEEPROM Row.
    It is recommended for the target application to use this constant in place
    hardcoded literals.

  Remarks:
    None.
*/

#define NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_ROWSIZE           (${FLASH_RWWEEPROM_ERASE_SIZE}U)
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* NVMCTRL Error Type

  Summary:
    Defines the NVMCTRL Error Type.

  Description:
    This enumeration defines the NVMCTRL Error type.

  Remarks:
    The NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet function returns a value of this
    type.
*/

typedef enum
{
    /* No error */
    NVMCTRL_ERROR_NONE = 0x0,

    /* NVMCTRL invalid commands and/or bad keywords error */
    NVMCTRL_ERROR_PROG = 0x4,

    /* NVMCTRL lock error */
    NVMCTRL_ERROR_LOCK = 0x8,

    /* NVMCTRL programming or erase error */
    NVMCTRL_ERROR_NVM = 0x10,

} NVMCTRL_ERROR;

<#if NVMCTRL_INTERRUPT_MODE == true>
// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the data type and function signature for the NVMCTRL peripheral
    callback function.

  Description:
    This data type defines the function signature for the NVMCTRL peripheral
    callback function. The NVMCTRL peripheral library will call back the
    client's function with this signature when an on-going erase or write
    operation has completed and the NVMCTRL is ready to accept a new operation
    request.  A function of this should be registered by calling the
    NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister function.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    typedef struct
    {
        bool operationComplete;

    } APP_DATA;

    // Callback is called when an operation completes.
    void APP_NVMTCTRLCallback(uintptr_t context)
    {
        APP_DATA * appdata = (APP_DATA *)context;
        appData->operationComplete = true;
    }

    // Function calls in main thread.
    APP_DATA  myAppData;
    myAppData.operationComplete = false;
    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Register the callback
    NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister(APP_NVMTCTRLCallback, &myAppData);

    // Perform some operation.
    NVMCTRL${NVMCTRL_INDEX?string}_RowErase(SOME_ROW_ALIGNED_ADDRESS);

    // Now wait for the operation to complete.
    while(!myAppData.operationComplete);

    </code>

  Remarks:
    The callback feature is only available when the library was generated with
    interrupt option (in MHC) enabled.
*/

typedef void (*NVMCTRL_CALLBACK)(uintptr_t context);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_Initialize( void )

  Summary:
    Initializes given instance of the NVMCTRL peripheral.

  Description:
    This function initializes the given instance of the NVMCTRL peripheral as
    configured by the user from within the MHC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    </code>

  Remarks:
    This function should be called before calling any other NVMCTRL library
    function.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_Initialize(void);

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
    callback function will be called.The NVMCTRL${NVMCTRL_INDEX?string}_IsBusy()
    function can be used to poll for completion of the operation. The
    application should ensure that there are no other operations in progress
    before calling this function.

    Once the operation is complete,the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet()
    function can be called to check operation success.

  Precondition:
    The NVMCTRL${NVMCTRL_INDEX?string}_Initialize() function should have been
    called once. Also validate if NVM controller is ready to accept a new
    request by calling NVMCTRL${NVMCTRL_INDEX?string}_IsBusy(). A row containing
    the page should be erased before the page can be written.

  Parameters:
    address - start address of page to be written. This should be aligned on a
    page boundary.

    data - pointer to data buffer. The size of this buffer should be the same as
    the page size.

  Returns:
    Always return true.

  Example:
    <code>

    // This code snippet shows how the NVMCTRL${NVMCTRL_INDEX?string}_PageWrite
    // function is called and how the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy
    // function is used to poll for completion.

    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Erase the row. This will erase all the pages in the row.
    NVMCTRL${NVMCTRL_INDEX?string}_RowErase(0x00030000);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    // Now write the page.
    NVMCTRL${NVMCTRL_INDEX?string}_PageWrite(0x00030000, &buffer);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() == NVMCTRL_ERROR_NONE)
    {
        // Operation was successful.
    }

    </code>

  Remarks:
    This function will clear any existing module errors before initiating the
    operation.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_PageWrite( uint32_t address, uint32_t* data );

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

    Once the operation is complete,the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet()
    function can be called to check operation success. Erasing a row will erase
    all the contents of all the pages in the row.

  Precondition:
    The NVMCTRL${NVMCTRL_INDEX?string}_Initialize() function should have been
    called once. Also validate if NVM controller is ready to accept new request
    by calling NVMCTRL${NVMCTRL_INDEX?string}_IsBusy().

  Parameters:
    address - Any address in the row to be erased.

  Returns:
    Always return true.

  Example:
    <code>

    // This code snippet shows how the NVMCTRL${NVMCTRL_INDEX?string}_RowErase
    // function is called to erase the row at locatioin 0x30000.

    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Erase the row. This will erase all the pages in the row.
    NVMCTRL${NVMCTRL_INDEX?string}_RowErase(0x00030000);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() == NVMCTRL_ERROR_NONE)
    {
        // Operation was successful.
    }

    </code>

  Remarks:
    Calling this function will clear any existing module error conditions.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RowErase( uint32_t address );

// *****************************************************************************
/* Function:
    NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void )

  Summary:
    Returns the error state of NVM controller.

  Description:
    This function returns the erorr status of the last NVMCTRL operation. The
    return value can be either NVMCTRL_ERROR_NONE, a single error or a
    combination of multiple error conditions.

  Precondition:
    None.

  Parameters:
    None

  Returns:
    Return NVMCTRL_ERROR type of value. In case of error, this value can be a
    combination of multiple and different error conditions.

  Example:
    <code>

    if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() != NVMCTRL_ERROR_NONE)
    {
        // The error status can indicate multiple error conditions.
        if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() & (NVMCTRL_ERROR_LOCK|NVMCTRL_ERROR_PROG))
        {
            // There are multiple error conditions.
        }
    }

    </code>

  Remarks:
    None.
*/

NVMCTRL_ERROR NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet( void );

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

  Precondition:
    None.

  Parameters:
    None

  Returns:
    true - NVM controller is busy.
    false - NVM controller is ready for a new operation.

  Example:
    <code>

    // Erase the row. This will erase all the pages in the row.
    NVMCTRL${NVMCTRL_INDEX?string}_RowErase(0x00030000);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    // Now write the page.
    NVMCTRL${NVMCTRL_INDEX?string}_PageWrite(0x00030000, &buffer);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    </code>

  Remarks:
    This function is only available when the library is generated (in MHC) with
    interrupt mode enabled.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_IsBusy( void );
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

  Precondition:
    Validate if NVM controller is ready to accept new request by calling
    NVMCTRL${NVMCTRL_INDEX?string}_IsBusy();

  Parameters:
    address - Any address in the region to be locked.

  Returns:
    None.

  Example:
    <code>

    // Wait till the NVM module is available and then lock the region containing
    // address 0x30000.

    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());
    NVMCTRL${NVMCTRL_INDEX?string}_RegionLock(0x00030000);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    </code>

  Remarks:
    This function will clear any existing module errors before initiating the
    operation.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_RegionLock (uint32_t address);

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock (uint32_t address);

  Summary:
    Unlocks a NVM region.

  Description:
    This function unlocks a region that was locked using the
    NVMCTRL${NVMCTRL_INDEX?string}_RegionLock() function. The address parameter
    can be any address within the region. Unlocking a region unlocks all pages
    in the region and makes these pages accessible to write and erase operations.

    This API is generated if the Region Lock/Unlock API option (in MHC) is
    selected.

  Precondition:
    Validate if NVM controller is ready to accept new request by calling
    NVMCTRL${NVMCTRL_INDEX?string}_IsBusy();

  Parameters:
    address - Any address in the region to be unlocked.

  Returns:
    None.

  Example:
    <code>

    // Wait till the NVM module is available and then un-lock the region
    // containing address 0x30000.

    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());
    NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock(0x00030000);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    </code>

  Remarks:
    This function will clear any existing module errors before initiating the
    operation.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_RegionUnlock (uint32_t address);
</#if>

<#if NVMCTRL_RWW_EEPROM == true>
// *****************************************************************************
/* Function:
    bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite( uint32_t address,uint32_t* data )

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
    there are no other operations in progress before calling this function. This
    can be checked by calling the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy()
    function.

    This function is blocking if the library was generated (in MHC) with the
    interrupt option disabled. If blocking, the function will exit only after
    write operation has completed. This function is not blocking if the library
    was generated with the interrupt option enabled. In this mode, the function
    initiates the operation and then exits. The application can either register
    a callback function or call the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy()
    function periodically to check for completion of the operation.

    Once the operation is complete,the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet()
    function can be called to check operation success.

    This API is generated if the RWWEEPROM API option (in MHC) is selected.

  Precondition:
    The NVMCTRL${NVMCTRL_INDEX?string}_Initialize() function should have been
    called once. Also validate if NVM controller is ready to accept new request
    by calling NVMCTRL${NVMCTRL_INDEX?string}_IsBusy(). The row containing the
    page should be erased before any page in that row can be written. The size
    of the RWWEEPROM memory should have been configured in the NVM User
    Configuration.

  Parameters:
    address - RWW EEPROM address to be modified.

    data - pointer to data buffer.

  Returns:
    Always return true.

  Example:
    <code>

    // This code snippet shows how the
    // NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite function is
    // called and how the NVMCTRL${NVMCTRL_INDEX?string}_IsBusy function is used
    // to poll for completion. This assumes the library was generated for
    // interrupt (and hence non-blocking) operation.

    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Erase the row. This will erase all the pages in the row.
    NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase(SOME_RWWEEPROM_ROW);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    // Now write the page.
    NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite(SOME_RWWEEPROM_PAGE, &buffer);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() == NVMCTRL_ERROR_NONE)
    {
        // Operation was successful.
    }

    </code>

  Remarks:
    RWWEEPROM API generation option will appear in the MHC if the device
    supports it.

    This function will clear any existing module errors before initiating the
    operation.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_PageWrite( uint32_t address, uint32_t* data );

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

    Once the operation is complete,the NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet()
    function can be called to check operation success. Erasing a row will erase
    all the contents of all the pages in the row.

    This API is generated if the RWWEEPROM API option (in MHC) is selected.

  Precondition:
    The NVMCTRL${NVMCTRL_INDEX?string}_Initialize() function should have been
    called once. Also validate if NVM controller is ready to accept new request
    by calling NVMCTRL${NVMCTRL_INDEX?string}_IsBusy(). The size of the
    RWWEEPROM memory should have been configured in the NVM User Configuration.

  Parameters:
    address - Any address in the row to be erased.

  Returns:
    Always return true.

  Example:
    <code>

    // This code snippet shows how NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase
    // function is called to erase the row at locatioin SOME_RWWEEPROM_ROW.

    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Erase the row. This will erase all the pages in the row.
    NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase(SOME_RWWEEPROM_ROW);
    while(NVMCTRL${NVMCTRL_INDEX?string}_IsBusy());

    if(NVMCTRL${NVMCTRL_INDEX?string}_ErrorGet() == NVMCTRL_ERROR_NONE)
    {
        // Operation was successful.
    }

    </code>

  Remarks:
    RWWEEPROM API generation option will appear in the MHC if the device
    supports it.

    This function will clear any existing module errors before initiating the
    operation. Erasing the row erases all pages in the row.
*/

bool NVMCTRL${NVMCTRL_INDEX?string}_RWWEEPROM_RowErase ( uint32_t address );
</#if>

<#if NVMCTRL_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister( NVMCTRL_CALLBACK callback,uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    operation is complete.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the NVMCTRL has completed an operation and is ready to receive new command.
    It also passes a context value that is passed into the callback function
    when it is called. This function is available only when the library is
    generated with interrupt option (in MHC) enabled.

  Precondition:
    Interrupt option in MHC should have been enabled

  Parameters:
    callback - A pointer to a function with a calling signature defined by the
    NVMCTRL_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>

    typedef struct
    {
        bool operationComplete;

    } APP_DATA;

    // Callback is called when an operation completes.
    void APP_NVMTCTRLCallback(uintptr_t context)
    {
        APP_DATA * appData = (APP_DATA *)context;
        appData->operationComplete = true;
    }

    // Function calls in main thread.
    APP_DATA  myAppData;
    myAppData.operationComplete = false;
    NVMCTRL${NVMCTRL_INDEX?string}_Initialize();

    // Register the callback
    NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister(APP_NVMTCTRLCallback, &myAppData);

    // Perform some operation.
    NVMCTRL${NVMCTRL_INDEX?string}_RowErase(SOME_ROW_ALIGNED_ADDRESS);

    // Now wait for the operation to complete.
    while(!myAppData.operationComplete);

    </code>

  Remarks:
    The context value may be set to NULL if it is not required. Note that the
    value of NULL will still be passed to the callback function.  To disable the
    callback function, pass a NULL for the callback parameter.  See the
    NVMCTRL_CALLBACK type definition for additional information.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_CallbackRegister ( NVMCTRL_CALLBACK callback, uintptr_t context );

// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void)

  Summary:
    Calls the callback function.

  Description:
    This function calls the callback function when an interrupt occurs due to
    the completion of a write or an erase operation.

  Precondition:
    Should be called from NVMCTRL interrupt handler.

  Parameters:
    None:

  Returns:
    None:

  Remarks:
    None.

  Example:
    <code>

    void NVMCTRL_Handler(void)
    {
        NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler();
    }

    </code>

  Remarks:
    This API is generated if the Interrupt option (in MCC) is selected.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_InterruptHandler(void);
</#if>

<#if NVMCTRL_CACHE_ENABLE == true>
// *****************************************************************************
/* Function:
    void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate ( void );

  Summary:
    Invalidates all cache lines.

  Description:
    This function invalidates all cache lines. This function is available if the
    library was generated with the Cache option (in MHC) enabled.

  Precondition:
    Cache option in MHC should have been enabled.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    // Invalidate all cache lines.
    NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate();

    </code>

  Remarks:
    None.
*/

void NVMCTRL${NVMCTRL_INDEX?string}_CacheInvalidate ( void );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif // PLIB_NVMCTRL${NVMCTRL_INDEX?string}_H
