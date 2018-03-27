/*******************************************************************************
  QSPI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_qspi.c

  Summary
    QSPi peripheral library interface.

  Description

  Remarks:
    
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#include "plib_qspi${INDEX?string}.h"


void QSPI${INDEX?string}_Initialize(void)
{
    // Reset and Disable the qspi Module
    QSPI_REGS->QSPI_CR = QSPI_CR_SWRST_Msk | QSPI_CR_QSPIDIS_Msk;

    while(QSPI_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk);

    // Set Mode Register values
    QSPI_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} );

    // Set serial clock register
    QSPI_REGS->QSPI_SCR = (QSPI_SCR_SCBR(${QSPI_SCBR})) <#if QSPI_CPOL=="HIGH"> | QSPI_SCR_CPOL_Msk </#if> <#if QSPI_CPHA=="FALLING"> | QSPI_SCR_CPHA_Msk </#if>;

    // Enable the qspi Module
    QSPI_REGS->QSPI_CR = QSPI_CR_QSPIEN_Msk;

    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk));
}

static void qspi${INDEX?string}_memcpy_32bit(uint32_t* dst, uint32_t* src, uint32_t count)
{
    while (count--) {
        *dst++ = *src++;
    }
}

static void qspi${INDEX?string}_memcpy_8bit(uint8_t* dst, uint8_t* src, uint32_t count)
{
    while (count--) {
        *dst++ = *src++;
    }
}

static inline void qspi${INDEX?string}_end_transfer( void )
{
    QSPI_REGS->QSPI_CR = QSPI_CR_LASTXFER_Msk;
}

static bool qspi${INDEX?string}_setup_transfer( qspi_memory_xfer_t *qspi_memory_xfer, uint8_t tfr_type, uint32_t address )
{
    uint32_t mask = 0;

    /* Set instruction address register */
    QSPI_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

    /* Set Instruction code register */
    QSPI_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_memory_xfer->instruction)) | (QSPI_ICR_OPT(qspi_memory_xfer->option));

    /* Set Instruction Frame register*/

    mask |= qspi_memory_xfer->width;
    mask |= qspi_memory_xfer->addr_len;

    if (qspi_memory_xfer->option_en) {
        mask |= qspi_memory_xfer->option_len;
        mask |= QSPI_IFR_OPTEN_Msk;
    }

    mask |= QSPI_IFR_NBDUM(qspi_memory_xfer->dummy_cycles);

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_ADDREN_Msk | QSPI_IFR_DATAEN_Msk;

    mask |= QSPI_IFR_TFRTYP(tfr_type);

    QSPI_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    (volatile uint32_t)QSPI_REGS->QSPI_IFR;

    return true;
}

bool QSPI${INDEX?string}_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address )
{
    uint32_t mask = 0;

    /* Configure address */
    if(qspi_command_xfer->addr_en) {
        QSPI_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

        mask |= QSPI_IFR_ADDREN_Msk;
        mask |= qspi_command_xfer->addr_len;
    }

    /* Configure instruction */
    QSPI_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_command_xfer->instruction));

    /* Configure instruction frame */
    mask |= qspi_command_xfer->width;
    mask |= QSPI_IFR_INSTEN_Msk;
    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);

    QSPI_REGS->QSPI_IFR = mask;

    /* Poll Status register to know status if instruction has end */
    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk));

    return true;
}

bool QSPI${INDEX?string}_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length )
{
    uint32_t *qspi_buffer = (uint32_t *)QSPIMEM_ADDR;
    uint32_t mask = 0;

    /* Configure Instruction */
    QSPI_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_register_xfer->instruction));

    /* Configure Instruction Frame */
    mask |= qspi_register_xfer->width;

    mask |= QSPI_IFR_NBDUM(qspi_register_xfer->dummy_cycles);

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_DATAEN_Msk;

    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);

    QSPI_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    (volatile uint32_t)QSPI_REGS->QSPI_IFR;

    /* Read the register content */
    qspi${INDEX?string}_memcpy_8bit((uint8_t *)rx_data , (uint8_t *)qspi_buffer,  rx_data_length);

    __DSB();
    __ISB();

    qspi${INDEX?string}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk));

    return true;
}

bool QSPI${INDEX?string}_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length )
{
    uint32_t *qspi_buffer = (uint32_t *)QSPIMEM_ADDR;
    uint32_t mask = 0;

    /* Configure Instruction */
    QSPI_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_register_xfer->instruction));

    /* Configure Instruction Frame */
    mask |= qspi_register_xfer->width;

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_DATAEN_Msk;

    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_WRITE_Val);

    QSPI_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    (volatile uint32_t)QSPI_REGS->QSPI_IFR;

    /* Write the content to register */
    qspi${INDEX?string}_memcpy_8bit((uint8_t *)qspi_buffer, (uint8_t *)tx_data, tx_data_length);

    __DSB();
    __ISB();

    qspi${INDEX?string}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk));

    return true;
}

bool QSPI${INDEX?string}_MemoryRead( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *rx_data, uint32_t rx_data_length, uint32_t address )
{
    uint32_t *qspi_mem = (uint32_t *)(QSPIMEM_ADDR | address);
    uint32_t length_32bit, length_8bit;

    if (false == qspi${INDEX?string}_setup_transfer(qspi_memory_xfer, QSPI_IFR_TFRTYP_TRSFR_READ_MEMORY_Val, address))
        return false;

    /* Read serial flash memory */
    length_32bit = rx_data_length / 4;
    length_8bit = rx_data_length & 0x03;

    if(length_32bit)
        qspi${INDEX?string}_memcpy_32bit(rx_data , qspi_mem,  length_32bit);

    rx_data = rx_data + length_32bit;
    qspi_mem = qspi_mem + length_32bit;

    if(length_8bit)
        qspi${INDEX?string}_memcpy_8bit((uint8_t *)rx_data , (uint8_t *)qspi_mem,  length_8bit);

    /* Dummy Read to clear QSPI_SR.INSTRE and QSPI_SR.CSR */
    (volatile uint32_t)QSPI_REGS->QSPI_SR;

    __DSB();
    __ISB();

    qspi${INDEX?string}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk));

    return true;
}

bool QSPI${INDEX?string}_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address )
{
    uint32_t *qspi_mem = (uint32_t *)(QSPIMEM_ADDR | address);
    uint32_t length_32bit, length_8bit;

    if (false == qspi${INDEX?string}_setup_transfer(qspi_memory_xfer, QSPI_IFR_TFRTYP_TRSFR_WRITE_MEMORY_Val, address))
        return false;

    /* Write to serial flash memory */
    length_32bit = tx_data_length / 4;
    length_8bit= tx_data_length & 0x03;

    if(length_32bit)
        qspi${INDEX?string}_memcpy_32bit(qspi_mem, tx_data, length_32bit);
    
    tx_data = tx_data + length_32bit;
    qspi_mem = qspi_mem + length_32bit;

    if(length_8bit)
        qspi${INDEX?string}_memcpy_8bit((uint8_t *)qspi_mem, (uint8_t *)tx_data, length_8bit);

    __DSB();
    __ISB();

    qspi${INDEX?string}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(QSPI_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk));

    return true;
}

/*******************************************************************************
 End of File
*/