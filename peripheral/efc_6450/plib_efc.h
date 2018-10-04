/*******************************************************************************
 Interface definition of EEFC PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_EEFC.h

 Summary:
    Interface definition of EEFC Plib.

 Description:
    This file defines the interface for the EEFC Plib.
    It allows user to Program, Erase and lock the on-chip FLASH memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef EFC_H    // Guards against multiple inclusion
#define EFC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*  This section lists the other files that are included in this file.
*/
/* This section lists the other files that are included in this file.
*/


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
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************

// *****************************************************************************
/* EEFC ERR
 Summary:
    Defines the data type for the EEFC Error.

 Description:
    This enum is used to define error encountered during last Flash operation.

 Remarks:
    None.
*/
typedef enum
{
    EFC_ERROR_NONE = 0x1,
    /*In-valid command*/
    EFC_CMD_ERROR = 0x2,
    /*Flash region is locked*/
    EFC_LOCK_ERROR = 0x4,
    /*Flash Error*/
    EFC_FLERR_ERROR = 0x8,
    /*Flash Encountered an ECC error*/
    EFC_ECC_ERROR = 0xF0000,
} EFC_ERROR;

// *****************************************************************************
// *****************************************************************************
/* Callback Function Pointer
 Summary:
    Defines the data type and function signature for the EEFC peripheral
    callback function.

 Description:
    This data type defines the function signature for the EEFC peripheral
    callback function. The EEFC peripheral will call back the client's
    function with this signature when the EEFC is ready to accept new operation.

 Precondition:
    EEFC_CallbackRegister must have been called to set the function to be called.

 Parameters:
    context - Allows the caller to provide a context value (usually a pointer
            to the callers context for multi-instance clients).

 Returns:
    None.
*/
typedef void (*EFC_CALLBACK)(uintptr_t context);

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
    bool EFCx_Read( uint32_t *data, uint32_t length, uint32_t address )

 Summary:
    Reads length number of bytes from a given address in FLASH memory.

 Description:
    Reads length number of bytes from a given address in FLASH memory
    into the user buffer.

 Precondition:
    None

 Parameters:
    data    :- pointer to user data buffer
    length  :- Number of bytes to read
    address :- FLASH address to be read from

 Returns:
    None.

 Example:
    <code>
        uint8_t buffer[256];
        EFC0_Read( &buffer, 256, 0x500000);
    </code>
*/
bool EFCx_Read( uint32_t *data, uint32_t length, uint32_t address );

// *****************************************************************************
/* Function:
    bool EFCx_QuadWordWrite( uint32_t address, uint32_t* data )

 Summary:
    Writes a 128-bit data to a given address in FLASH memory.

 Description:
    This function takes a 32-bit address, a pointer to the 128-bit data and writes it to
    the given location in FLASH memory.

 Precondition:
    None

 Parameters:
    address:- FLASH address to be modified
    data   :- pointer to 128-bit data buffer

 Returns:
    None.

 Example:
    <code>
        while(EFC0_IsBusy());
        EFC0_QuadWordWrite( 0x500000, &buffer);
    </code>
*/
bool EFCx_QuadWordWrite( uint32_t* data, uint32_t address );

// *****************************************************************************
/* Function:
    bool EFCx_PageWrite( uint32_t address, uint32_t* data )

 Summary:
    Writes data of size equivalent to page size to a given FLASH address.

 Description:
    This function takes a 32-bit address, a pointer to data of size equivalent to page size
    and writes it to the given location in FLASH memory.

 Precondition:
    None.

 Parameters:
    address:- FLASH address to be modified
    data   :- pointer to data buffer

 Returns:
    None.

 Example:
    <code>
        while(EFC0_IsBusy());
        EFC0_PageWrite( 0x500000, &buffer);
    </code>
*/
bool EFCx_PageWrite( uint32_t* data, uint32_t address );

// *****************************************************************************
/* Function:
    bool EFCx_SectorErase( uint32_t address)

 Summary:
    Erases a Row in the FLASH.

 Description:
    This function is used to erase a row (collection of pages).

 Precondition:
    None.

 Parameters:
    address:- FLASH address to be Erased

 Returns:
    None.

 Example:
    <code>
        while(EFC0_IsBusy());
        EFC0_SectorErase( 0x500000 );
    </code>
*/
bool EFCx_SectorErase( uint32_t address );

// *****************************************************************************
/* Function:
    EFC_ERROR EFCx_ErrorGet( void )

 Summary:
    Returns the error encountered by EFCx controller.

 Description:
    This function is used to check error encountered by EFCx controller.

 Precondition:
    None.

 Parameters:
    None

 Returns:
    uint32_t :- EFCx controller error type

 Example:
    <code>
        uint32_t error = EFCx_ErrorGet();

    </code>
*/

uint32_t EFCx_ErrorGet( void );

// *****************************************************************************
/* Function:
    bool EFCx_IsBusy(void)

 Summary:
    Returns the current status of EFCx controller.

 Description:
    This function is used to check is EFCx is busy or not

 Precondition:
    None.

 Parameters:
    None
 Returns:
    bool :- EFCx status

 Example:
    <code>
        while(EFC0_IsBusy());
        EFC0_SectorErase( 0x500000 );
    </code>
*/

bool EFCx_IsBusy(void);

// *****************************************************************************
/* Function:
    void EFCx_RegionLock(uint32_t address);

 Summary:
    Locks a Flash region.

 Description:
    This function is used to lock a certain region of on-chip flash.
    It takes in address as a parameter and locks the region associated with it.

 Precondition:
    Validate if EFCx controller is ready to accept new request by calling EFCx_IsBusy()

 Parameters:
    address:- Address of the page to be locked

 Returns:
    None.

 Example:
    <code>
        while(EFC0_IsBusy());
        EFCx0_RegionLock(0x00500000);
    </code>
*/

void EFCx_RegionLock(uint32_t address);

// *****************************************************************************
/* Function:
    void EFCx_RegionUnlock(uint32_t address);

 Summary:
    Unlocks a Flash region.

 Description:
    This function is used to Unlock a certain region of on-chip flash.
    It takes in address as a parameter and unlocks the region associated with it.

 Precondition:
    Validate if EFCx controller is ready to accept new request by calling EFCx_IsBusy()

 Parameters:
    address:- Address of the page to be unlocked

 Returns:
    None.

 Example:
    <code>
        while(EFC0_IsBusy());
        EFCx0_RegionUnlock(0x00500000);
    </code>
*/

void EFCx_RegionUnlock(uint32_t address);

// *****************************************************************************
/* Function:
    void EFCx_CallbackRegister( EFCx_CALLBACK callback, uintptr_t context )

 Summary:
    Sets the pointer to the function (and it's context) to be called when the
    operation is complete.

 Description:
    This function sets the pointer to a client function to be called "back"
    when the EFCx is ready to receive new command. It also passes a context value that is passed into the
    function when it is called.
    This function is available only in interrupt mode of operation.

 Precondition:
    None.

 Parameters:
    callback - A pointer to a function with a calling signature defined
                by the EFCx_CALLBACK data type.
    context - A value (usually a pointer) passed (unused) into the function
                identified by the callback parameter.

 Returns:
    None.

 Example:
    <code>
        EFCx_CallbackRegister(MyCallback, &myData);
    </code>

 Remarks:
    The context value may be set to NULL if it is not required. Note that the
    value of NULL will still be passed to the callback function.
    To disable the callback function, pass a NULL for the callback parameter.
    See the EFCx_CALLBACK type definition for additional information.
*/

void EFCx_CallbackRegister( EFCx_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif