/*******************************************************************************
  ${QSPI_INSTANCE_NAME} Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${QSPI_INSTANCE_NAME?lower_case}.c

  Summary
    ${QSPI_INSTANCE_NAME} peripheral library interface.

  Description

  Remarks:
    
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

#include "plib_${QSPI_INSTANCE_NAME?lower_case}.h"
#include "string.h" // memmove

void ${QSPI_INSTANCE_NAME}_Initialize(void)
{
    // Reset and Disable the qspi Module
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_SWRST_Msk | QSPI_CR_QSPIDIS_Msk;

    while(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk){
        ;   // spin lock
    }

    // Set Mode Register values
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} );

    // Set serial clock register
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_SCR = (QSPI_SCR_SCBR(${QSPI_SCBR})) <#if QSPI_CPOL=="HIGH"> | QSPI_SCR_CPOL_Msk </#if> <#if QSPI_CPHA=="TRAILING"> | QSPI_SCR_CPHA_Msk </#if>;

    // Enable the qspi Module
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_QSPIEN_Msk;

    while(!(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk)){
        ;   // spin lock
    }
}

static void ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit(uint32_t* dst, uint32_t* src, uint32_t count)
{
    while (count--) {
        *dst++ = *src++;
    }
}

static void ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit(uint8_t* dst, uint8_t* src, uint32_t count)
{
    while (count--) {
        *dst++ = *src++;
    }
}

static inline void ${QSPI_INSTANCE_NAME?lower_case}_end_transfer( void )
{
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_LASTXFER_Msk;
}

static bool ${QSPI_INSTANCE_NAME?lower_case}_setup_transfer( qspi_memory_xfer_t *qspi_memory_xfer, QSPI_TRANSFER_TYPE tfr_type, uint32_t address )
{
    uint32_t mask = 0;
    volatile uint32_t dummy = 0;

    /* Set instruction address register */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

    /* Set Instruction code register */
    <#if HAS_SPLIT_ICR>
    if (tfr_type == QSPI_REG_READ || tfr_type == QSPI_MEM_READ) {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_RICR = (QSPI_RICR_RDINST(qspi_memory_xfer->instruction)) | (QSPI_RICR_RDOPT(qspi_memory_xfer->option));
    } else {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_WICR = (QSPI_WICR_WRINST(qspi_memory_xfer->instruction)) | (QSPI_WICR_WROPT(qspi_memory_xfer->option));
    }
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_memory_xfer->instruction)) | (QSPI_ICR_OPT(qspi_memory_xfer->option));
    </#if>

    /* Set Instruction Frame register*/

    mask |= qspi_memory_xfer->width;
    mask |= qspi_memory_xfer->addr_len;

    if (qspi_memory_xfer->option_en) {
        mask |= qspi_memory_xfer->option_len;
        mask |= QSPI_IFR_OPTEN_Msk;
    }

    if (qspi_memory_xfer->continuous_read_en) {
        mask |= QSPI_IFR_CRM_Msk;
    }

    mask |= QSPI_IFR_NBDUM(qspi_memory_xfer->dummy_cycles);

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_ADDREN_Msk | QSPI_IFR_DATAEN_Msk;

    <#if HAS_SPLIT_ICR>
    switch (tfr_type){
        case QSPI_REG_READ:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_REGISTER_Val);
            mask |= QSPI_IFR_APBTFRTYP(1);
            break;
        case QSPI_REG_WRITE:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_REGISTER_Val);
            mask |= QSPI_IFR_APBTFRTYP(0);
            break;
        case QSPI_MEM_READ:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_MEMORY_Val);
            mask |= QSPI_IFR_APBTFRTYP(1);
            break;
        case QSPI_MEM_WRITE:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_MEMORY_Val);
            mask |= QSPI_IFR_APBTFRTYP(0);
            break;
    };
    <#else>
    switch (tfr_type){
        case QSPI_REG_READ:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);
            break;
        case QSPI_REG_WRITE:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_WRITE_Val);
            break;
        case QSPI_MEM_READ:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_MEMORY_Val);
            break;
        case QSPI_MEM_WRITE:
            mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_WRITE_MEMORY_Val);
            break;
    };
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    dummy = ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR;
    (void)dummy;

    return true;
}

bool ${QSPI_INSTANCE_NAME}_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address )
{
    uint32_t mask = 0;

    /* Configure address */
    if(qspi_command_xfer->addr_en) {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

        mask |= QSPI_IFR_ADDREN_Msk;
        mask |= qspi_command_xfer->addr_len;
    }

    /* Configure instruction */
    <#if HAS_SPLIT_ICR>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_WICR = (QSPI_WICR_WRINST(qspi_command_xfer->instruction));
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_command_xfer->instruction));
    </#if>

    /* Configure instruction frame */
    mask |= qspi_command_xfer->width;
    mask |= QSPI_IFR_INSTEN_Msk;
    <#if HAS_SPLIT_ICR>
    mask |= QSPI_IFR_TFRTYP(0);
    mask |= QSPI_IFR_APBTFRTYP(0);
    <#else>
    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    /* Poll Status register to know status if instruction has end */
    while(!(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk)) {
        ;   // spin lock
    }

    return true;
}

bool ${QSPI_INSTANCE_NAME}_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length )
{
    uint32_t *qspi_buffer = (uint32_t *)${QSPI_INSTANCE_NAME}MEM_ADDR;
    uint32_t mask = 0;
    volatile uint32_t dummy = 0;

    /* Configure Instruction */
    <#if HAS_SPLIT_ICR>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_RICR = (QSPI_RICR_RDINST(qspi_register_xfer->instruction));
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_register_xfer->instruction));
    </#if>

    /* Configure Instruction Frame */
    mask |= qspi_register_xfer->width;

    mask |= QSPI_IFR_NBDUM(qspi_register_xfer->dummy_cycles);

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_DATAEN_Msk;

    <#if HAS_SPLIT_ICR>
    mask |= QSPI_IFR_TFRTYP(0);
    mask |= QSPI_IFR_APBTFRTYP(1);
    <#else>
    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    dummy = ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR;

    /* Read the register content */
    ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit((uint8_t *)rx_data , (uint8_t *)qspi_buffer,  rx_data_length);

    __DSB();
    __ISB();

    ${QSPI_INSTANCE_NAME?lower_case}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk)) {
        ;   // spin lock
    }

    (void)dummy;
    return true;
}

bool ${QSPI_INSTANCE_NAME}_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length )
{
    uint32_t *qspi_buffer = (uint32_t *)${QSPI_INSTANCE_NAME}MEM_ADDR;
    uint32_t mask = 0;
    volatile uint32_t dummy = 0;

    /* Configure Instruction */
    <#if HAS_SPLIT_ICR>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_WICR = (QSPI_WICR_WRINST(qspi_register_xfer->instruction));
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST(qspi_register_xfer->instruction));
    </#if>

    /* Configure Instruction Frame */
    mask |= qspi_register_xfer->width;

    mask |= QSPI_IFR_INSTEN_Msk | QSPI_IFR_DATAEN_Msk;

    <#if HAS_SPLIT_ICR>
    mask |= QSPI_IFR_TFRTYP(0);
    mask |= QSPI_IFR_TFRTYP(0);
    <#else>
    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_WRITE_Val);
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    dummy = ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR;

    /* Write the content to register */
    ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit((uint8_t *)qspi_buffer, (uint8_t *)tx_data, tx_data_length);

    __DSB();
    __ISB();

    ${QSPI_INSTANCE_NAME?lower_case}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk)) {
        ;   // spin lock
    }

    (void)dummy;
    return true;
}

bool
${QSPI_INSTANCE_NAME}_MemoryRead(
    qspi_memory_xfer_t *    qspi_memory_xfer,
    uint32_t *              rx_data,
    uint32_t                rx_data_length,
    uint32_t                address
    )
{
    /*  This implements a transfer from device source to a destination memory buffer 
        without an intermediate local buffer.  The algorithm is used for efficiency 
        sake, allowing a maximum number of word transfers from the device; but, 
        not requiring word alignment at either end of source, or destination,
        locations.
        The non-boundary aligned header and trailer element sizes are used to 
        characterizes the number of word transfers for the body.  The body is 
        transfered in a word wide fashion followed by an appropriate shift of the
        bytes in the destination buffer.
        Single byte accesses at the head, or tail, are done as necessary.  The 
        coding attempts to minimize unnecessary byte manipulations.
    */
    uint8_t *   qspi_mem  = (uint8_t *) (${QSPI_INSTANCE_NAME}MEM_ADDR | address);
    uint8_t *   pRxBuffer = (uint8_t *) rx_data;
    uint32_t    numDstPreWordBytes;
    uint32_t    numSrcPreWordBytes;
    uint32_t    numDstPostWordBytes = 0;
    uint32_t    numSrcPostWordBytes = 0;
    uint32_t    numWordTransferBytes = 0;
    int32_t     shiftBytes = 0;             // gt(0)=>right, lt(0)=>left shift
    uint8_t     tmpBuffer[ sizeof( uint32_t) ];

    ///// device preliminaries
    if( false == ${QSPI_INSTANCE_NAME?lower_case}_setup_transfer( qspi_memory_xfer, 
                            QSPI_MEM_READ, 
                            address 
                        ) ) {
        return false;
    }

    ///// dst and src buffer characterization
    numDstPreWordBytes =  0x03 & (uint32_t) pRxBuffer;
    if( numDstPreWordBytes ) {
        numDstPreWordBytes =  sizeof( uint32_t ) - numDstPreWordBytes;
    }
    if( rx_data_length >= numDstPreWordBytes ) {
        numDstPostWordBytes = 0x03 & (uint32_t) (pRxBuffer + rx_data_length);
    }
    //
    numSrcPreWordBytes =  0x03 & (uint32_t) qspi_mem;
    if( numSrcPreWordBytes ) {
        numSrcPreWordBytes =  sizeof( uint32_t ) - numSrcPreWordBytes;
    }
    if( rx_data_length >= numSrcPreWordBytes ) {
        numSrcPostWordBytes = 0x03 & (uint32_t) (qspi_mem + rx_data_length);
    }
    else {
        numSrcPreWordBytes = rx_data_length;
    }

    if( rx_data_length > (numSrcPreWordBytes + numSrcPostWordBytes) ) {
        // number of word size transfers is equal to length of buffer
        // minus single byte transfers
        numWordTransferBytes = rx_data_length - (numSrcPreWordBytes + numSrcPostWordBytes);
    }

    // test if src has same number of word alignments as the dst buffer
    if( (numDstPreWordBytes + numDstPostWordBytes) != (numSrcPreWordBytes + numSrcPostWordBytes)) {
        // a word size space will be needed for shifting purposes; the
        // common case optimization for equal word alignments cannot be used
        if( numWordTransferBytes >= sizeof( uint32_t ) ) {
            numWordTransferBytes -= sizeof( uint32_t );
            numSrcPostWordBytes += sizeof( uint32_t );
        }
        else {
            numWordTransferBytes = 0;
        }
    }

    shiftBytes = numSrcPreWordBytes - numDstPreWordBytes;

    ///// Transfer of data from src device to dst buffer
    // Perform single byte transfers necessary before word alignment begins
    if( numSrcPreWordBytes ) {
        // get these now so we don't have to backup the device access later
        ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( tmpBuffer, qspi_mem, numSrcPreWordBytes );
        qspi_mem += numSrcPreWordBytes;     // word alignment point for the src
    }
    pRxBuffer += numDstPreWordBytes;        // word alignment point for the dst

    // Perform word aligned transfers
    if( numWordTransferBytes / 4 ) {
        ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit( (uint32_t *) pRxBuffer, 
                (uint32_t *) qspi_mem, 
                numWordTransferBytes / 4 
            );
        qspi_mem += numWordTransferBytes;
        pRxBuffer += numWordTransferBytes;
    }

    if( 0 >= shiftBytes ) {                 // left, or no, shift
        if( shiftBytes ) {
            // Shift the data left to its final destination buffer location
            memmove( ((uint8_t *) rx_data) + numDstPreWordBytes + shiftBytes,
                    ((uint8_t *) rx_data) + numDstPreWordBytes,
                    numWordTransferBytes 
                );
            pRxBuffer += shiftBytes;        // adjust end point
        }
        // Now we have room at the end, perform the single byte transfers 
        // necessary after word alignment ends
        if( numSrcPostWordBytes ) {
            ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( pRxBuffer, qspi_mem, numSrcPostWordBytes );
        }
    }
    else {                                  // right shift
        // Perform the single byte transfers necessary after word alignment ends
        if( numSrcPostWordBytes ) {
            ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( pRxBuffer, qspi_mem, numSrcPostWordBytes );
        }
        // Shift the data to right to its final destination buffer location
        memmove( ((uint8_t *) rx_data) + numDstPreWordBytes + shiftBytes, 
                ((uint8_t *) rx_data) + numDstPreWordBytes, 
                numWordTransferBytes + numSrcPostWordBytes 
            );
    }

    if( numSrcPreWordBytes ) {
        // Now we have room at the beginning; 
        // place the previously saved pre-word aligned bytes
        memmove( rx_data, tmpBuffer, numSrcPreWordBytes );
    }
    ///// Clean up
    /* Dummy Read to clear QSPI_SR.INSTRE and QSPI_SR.CSR */
    (uint32_t) ${QSPI_INSTANCE_NAME}_REGS->QSPI_SR;
    __DSB();
    __ISB();

    ${QSPI_INSTANCE_NAME?lower_case}_end_transfer();
    // Poll Status register to know status if instruction has ended
    while( !(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_INSTRE_Msk) ) {
        ;   // spin lock
    }
  
    return true;
}

bool ${QSPI_INSTANCE_NAME}_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address )
{
    uint32_t *qspi_mem = (uint32_t *)(${QSPI_INSTANCE_NAME}MEM_ADDR | address);
    uint32_t length_32bit, length_8bit;

    if (false == ${QSPI_INSTANCE_NAME?lower_case}_setup_transfer(qspi_memory_xfer, QSPI_MEM_WRITE, address))
        return false;

    /* Write to serial flash memory */
    length_32bit = tx_data_length / 4;
    length_8bit= tx_data_length & 0x03;

    if(length_32bit)
        ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit(qspi_mem, tx_data, length_32bit);
    
    tx_data = tx_data + length_32bit;
    qspi_mem = qspi_mem + length_32bit;

    if(length_8bit)
        ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit((uint8_t *)qspi_mem, (uint8_t *)tx_data, length_8bit);

    __DSB();
    __ISB();

    ${QSPI_INSTANCE_NAME?lower_case}_end_transfer();

    /* Poll Status register to know status if instruction has end */
    while(!(${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk)) {
        ;   // spin lock
    }

    return true;
}

/*******************************************************************************
 End of File
*/
