/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.c

  Summary:
    SERCOM I2C PLIB Implementation file

  Description:
    This file defines the interface to the SERCOM I2C peripheral library.
    This library provides access to and control of the associated peripheral
    instance.

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

#include "plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* ${SERCOM_INSTANCE_NAME} I2C baud value for ${I2C_CLOCK_SPEED} Khz baud rate */
#define ${SERCOM_INSTANCE_NAME}_I2CM_BAUD_VALUE			(${I2CM_BAUD}U)

<#if I2C_ADDR_TENBITEN = true>
#define RIGHT_ALIGNED (8U)

#define TEN_BIT_ADDR_MASK (0x78U)

</#if>
static SERCOM_I2C_OBJ ${SERCOM_INSTANCE_NAME?lower_case}I2CObj;

// *****************************************************************************
// *****************************************************************************
// Section: ${SERCOM_INSTANCE_NAME} I2C Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void)

  Summary:
    Initializes the instance of the SERCOM peripheral operating in I2C mode.

  Description:
    This function initializes the given instance of the SERCOM I2C peripheral as
    configured by the user from the MHC.

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.h for more information.
*/

void ${SERCOM_INSTANCE_NAME}_I2C_Initialize(void)
{
    /* Enable smart mode enable */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB = SERCOM_I2CM_CTRLB_SMEN_Msk;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>

    /* Baud rate - Master Baud Rate*/
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_BAUD = SERCOM_I2CM_BAUD_BAUD(${SERCOM_INSTANCE_NAME}_I2CM_BAUD_VALUE);

    /* Set Operation Mode (Master), SDA Hold time, run in stand by and i2c master enable */
    <@compress single_line=true>${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLA = SERCOM_I2CM_CTRLA_MODE_I2C_MASTER |
                                                                                  SERCOM_I2CM_CTRLA_SDAHOLD_${I2C_SDAHOLD_TIME} |
                                                                                  <#if I2CM_MODE??>SERCOM_I2CM_CTRLA_SPEED_${I2CM_MODE} |</#if>
                                                                                  SERCOM_I2CM_CTRLA_ENABLE_Msk
                                                                                  ${I2C_RUNSTDBY?then(' | SERCOM_I2CM_CTRLA_RUNSTDBY_Msk','')};</@compress>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>

    /* Initial Bus State: IDLE */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS = SERCOM_I2CM_STATUS_BUSSTATE(0x01);

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>

    /* Initialize the ${SERCOM_INSTANCE_NAME} PLib Object */
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;

    /* Enable all Interrupts */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENSET = SERCOM_I2CM_INTENSET_Msk;
}

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_I2C_InitiateRead(uint16_t address)

  Summary:
    Intiates I2C Read

  Description:

  Remarks:
    Refer plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.h for more information.
*/

static void ${SERCOM_INSTANCE_NAME}_I2C_InitiateRead(uint16_t address)
{
    <#if I2C_ADDR_TENBITEN = false>
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_READ;
    <#else>
    if(address > 0x007F)
    {
       ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ADDR_SEND;

       /*
        * Write ADDR.ADDR[10:1] with the 10-bit address.
        * Set direction bit (ADDR.ADDR[0]) equal to 0.
        * Set ADDR.TENBITEN equals to 1.
        */
       ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_WRITE | SERCOM_I2CM_ADDR_TENBITEN_Msk;
    }
    else
    {
       ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

       ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_READ;
    }
    </#if>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>
}

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback,
                                                              uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given SERCOM I2C's transfer events occur.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the SERCOM_I2C_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.
*/

void ${SERCOM_INSTANCE_NAME}_I2C_CallbackRegister(SERCOM_I2C_CALLBACK callback, uintptr_t contextHandle)
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback = callback;

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.context  = contextHandle;
}

/// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_2C_InitiateTransfer(uint16_t address, bool type)

  Summary:
    Send the 7-bit or 10-bit slave address.

  Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
     address - 7-bit / 10-bit slave address.
     type - Read / Write

  Remarks:
    None.
*/

static void ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(uint16_t address, bool type)
{
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount = 0;

    /* Clear all flags */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = SERCOM_I2CM_INTFLAG_Msk;

    /* Smart mode enabled - ACK is set to send while receiving the data */
    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB &= ~SERCOM_I2CM_CTRLB_ACKACT_Msk;

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>

    /* Reset Error Information */
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

    <#if I2C_ADDR_TENBITEN = false>
    if(type)
    {
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

        /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_READ;
    }
    else
    {
        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

        /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 0*/
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_WRITE;
    }
    <#else>
    /* Check for 10-bit address */
    if(address > 0x007F)
    {
        if(type)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ADDR_SEND;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;
        }

        /*
         * Write ADDR.ADDR[10:1] with the 10-bit address.
         * Set direction bit (ADDR.ADDR[0]) equal to 0.
         * Set ADDR.TENBITEN equals to 1.
         */
        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_WRITE | SERCOM_I2CM_ADDR_TENBITEN_Msk;
    }
    else
    {
        if(type)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 1*/
            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_READ;
        }
        else
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_WRITE;

            /* Write 7bit address with direction (ADDR.ADDR[0]) equal to 0*/
            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (address << 1) | I2C_TRANSFER_WRITE;
        }
    }
    </#if>

    /* Wait for synchronization */
    <#if SERCOM_SYNCBUSY = false>
    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
    <#else>
    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
    </#if>
}

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_I2C_Read(uint16_t address, uint8_t *pdata,
                                                                 uint32_t length)

   Summary:
    Reads data from the slave.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to destination data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool ${SERCOM_INSTANCE_NAME}_I2C_Read(uint16_t address, uint8_t *pdata, uint32_t length)
{
    /* Check for ongoing transfer */
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state != SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address = address;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer = pdata;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize = length;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

    ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(address, true);

    return true;
}

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_I2C_Write(uint16_t address, uint8_t *pdata,
                                                                 uint32_t length)

   Summary:
    Writes data onto the slave.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    pdata   - pointer to source data buffer
    length  - length of data buffer in number of bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool ${SERCOM_INSTANCE_NAME}_I2C_Write(uint16_t address, uint8_t *pdata, uint32_t length)
{
    /* Check for ongoing transfer */
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state != SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address = address;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer = NULL;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize = 0;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer = pdata;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize = length;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

    ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(address, false);

    return true;
}

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead(uint16_t address, uint8_t *wdata,
                               uint32_t wlength, uint8_t *rdata, uint32_t rlength)

   Summary:
    Write and Read data from Slave.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    address - 7-bit / 10-bit slave address.
    wdata   - pointer to write data buffer
    wlength - write data length in bytes.
    rdata   - pointer to read data buffer.
    rlength - read data length in bytes.

   Returns:
    Request status.
    True - Request was successful.
    False - Request has failed.
*/

bool ${SERCOM_INSTANCE_NAME}_I2C_WriteRead(uint16_t address, uint8_t *wdata, uint32_t wlength, uint8_t *rdata, uint32_t rlength)
{
    /* Check for ongoing transfer */
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state != SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }

    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address = address;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer = rdata;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize = rlength;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer = wdata;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize = wlength;
    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

    ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(address, false);

    return true;
}

// *****************************************************************************
/* Function:
    bool ${SERCOM_INSTANCE_NAME}_I2C_IsBusy(void)

   Summary:
    Returns the Peripheral busy status.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    None.

   Returns:
    true - Busy.
    false - Not busy.
*/

bool ${SERCOM_INSTANCE_NAME}_I2C_IsBusy(void)
{
    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_IDLE)
    {
        return false;
    }
    else
    {
        return true;
    }
}

// *****************************************************************************
/* Function:
    SERCOM_I2C_ERROR ${SERCOM_INSTANCE_NAME}_I2C_ErrorGet(void)

   Summary:
    Returns the error during transfer.

   Precondition:
    SERCOMx_I2C_Initialize must have been called for the associated SERCOM instance.

   Parameters:
    None.

   Returns:
    Error during transfer.
*/

SERCOM_I2C_ERROR ${SERCOM_INSTANCE_NAME}_I2C_ErrorGet(void)
{
    return ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error;
}

// *****************************************************************************
/* Function:
    void ${SERCOM_INSTANCE_NAME}_I2C_InterruptHandler(void)

  Summary:
    ${SERCOM_INSTANCE_NAME} I2C Peripheral Interrupt Handler.

  Description:
    This function is ${SERCOM_INSTANCE_NAME} I2C Peripheral Interrupt Handler and will
    called on every ${SERCOM_INSTANCE_NAME} I2C interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
    instance interrupt is enabled. If peripheral instance's interrupt is not
    enabled user need to call it from the main while loop of the application.
*/

void ${SERCOM_INSTANCE_NAME}_I2C_InterruptHandler(void)
{
    if(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTENSET != 0)
    {
        /* Checks if the arbitration lost in multi-master scenario */
        if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_ARBLOST_Msk) == SERCOM_I2CM_STATUS_ARBLOST_Msk)
        {
            /*
             * Re-initiate the transfer if arbitration is lost
             * in between of the transfer
             */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_REINITIATE_TRANSFER;

        }
        /* Check for Bus Error during transmission */
        else if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_BUSERR_Msk) == SERCOM_I2CM_STATUS_BUSERR_Msk)
        {
            /* Set Error status */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_BUS;
        }
        /* Checks slave acknowledge for address or data*/
        else if((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_RXNACK_Msk) == SERCOM_I2CM_STATUS_RXNACK_Msk)
        {
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_ERROR;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NAK;
        }
        else
        {
            switch(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state)
            {
                case SERCOM_I2C_REINITIATE_TRANSFER:
                {
                    if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize != 0)
                    {
                        /* Initiate Write transfer */
                        ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address, false);
                    }
                    else
                    {
                        /* Initiate Read transfer */
                        ${SERCOM_INSTANCE_NAME}_I2C_InitiateTransfer(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address, true);
                    }

                    break;
                }

                case SERCOM_I2C_STATE_IDLE:
                {
                    break;
                }
                <#if I2C_ADDR_TENBITEN = true>
                case SERCOM_I2C_STATE_ADDR_SEND:
                {
                    /*
                     * Write ADDR[7:0] register to "11110 address[9:8] 1"
                     * ADDR.TENBITEN must be cleared
                     */
                    ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_ADDR = (((${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address >> RIGHT_ALIGNED) | TEN_BIT_ADDR_MASK) << 1) | I2C_TRANSFER_READ;

                    /* Wait for synchronization */
                    <#if SERCOM_SYNCBUSY = false>
                    while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
                    <#else>
                    while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
                    </#if>

                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_READ;

                    break;
                }
                </#if>
                case SERCOM_I2C_STATE_TRANSFER_WRITE:
                {
                    if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount == (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeSize))
                    {
                        if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize != 0)
                        {
                            ${SERCOM_INSTANCE_NAME}_I2C_InitiateRead(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.address);
                        }
                        else
                        {
                            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_CMD(3);

                            /* Wait for synchronization */
                            <#if SERCOM_SYNCBUSY = false>
                            while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
                            <#else>
                            while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
                            </#if>

                            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_DONE;
                        }
                    }
                    /* Write next byte */
                    else
                    {
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_DATA = ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeBuffer[${SERCOM_INSTANCE_NAME?lower_case}I2CObj.writeCount++];
                    }

                    break;
                }
                case SERCOM_I2C_STATE_TRANSFER_READ:
                {
                    if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount == (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readSize - 1))
                    {
                        /* Set NACK and send stop condition to the slave from master */
                        ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_CTRLB |= SERCOM_I2CM_CTRLB_ACKACT_Msk | SERCOM_I2CM_CTRLB_CMD(3);

                        /* Wait for synchronization */
                        <#if SERCOM_SYNCBUSY = false>
                        while((${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_STATUS & SERCOM_I2CM_STATUS_SYNCBUSY_Msk) & SERCOM_I2CM_STATUS_SYNCBUSY_Msk);
                        <#else>
                        while(${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_SYNCBUSY);
                        </#if>

                        ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_TRANSFER_DONE;
                    }

                    /* Read the received data */
                    ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readBuffer[${SERCOM_INSTANCE_NAME?lower_case}I2CObj.readCount++] = ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_DATA;

                    break;
                }
                default:
                {
                    break;
                }
            }
        }

        /* Error Status */
        if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_ERROR)
        {
            /* Reset the PLib objects and Interrupts */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;

            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = SERCOM_I2CM_INTFLAG_Msk;

            if (${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.context);
            }
        }
        /* Transfer Complete */
        else if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state == SERCOM_I2C_STATE_TRANSFER_DONE)
        {
            /* Reset the PLib objects and interrupts */
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.state = SERCOM_I2C_STATE_IDLE;
            ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.error = SERCOM_I2C_ERROR_NONE;

            ${SERCOM_INSTANCE_NAME}_REGS->I2CM.SERCOM_INTFLAG = SERCOM_I2CM_INTFLAG_Msk;

            if(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback != NULL)
            {
                ${SERCOM_INSTANCE_NAME?lower_case}I2CObj.callback(${SERCOM_INSTANCE_NAME?lower_case}I2CObj.context);
            }

        }
    }

    return;
}