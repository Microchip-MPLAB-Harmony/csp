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

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk) != 0U)
    {
        ;   // spin lock
    }

    /* DLYCS  = 0x0 */
    /* DLYBCT = 0x0 */
    <#if (QSPI_NBBITS?has_content)>
    /* NBBITS = ${QSPI_NBBITS} */
    <#else>
    /* NBBITS = 0x0 */
    </#if>
    /* CSMODE = 0x0 */
    /* WDRBT  = 0 */
    /* LLB    = 0 */
    /* SMM    = ${QSPI_SMM} */
    <#if (QSPI_NBBITS?has_content)>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} | QSPI_MR_NBBITS(${QSPI_NBBITS}U));
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_MR = ( QSPI_MR_SMM_${QSPI_SMM} );
    </#if>

    /* CPOL = <#if QSPI_CPOL=="HIGH">1 <#else>0 </#if>*/
    /* CPHA = <#if QSPI_CPHA=="TRAILING">1 <#else>0 </#if>*/
    /* SCBR = ${QSPI_SCBR} */
    /* DLYBS = 0 */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_SCR = (QSPI_SCR_SCBR(${QSPI_SCBR}U)) <#if QSPI_CPOL=="HIGH"> | QSPI_SCR_CPOL_Msk </#if> <#if QSPI_CPHA=="TRAILING"> | QSPI_SCR_CPHA_Msk </#if>;

    // Enable the qspi Module
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_QSPIEN_Msk;

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_QSPIENS_Msk) == 0U)
    {
        ;   // spin lock
    }
}

static void ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit(uint32_t* dst, uint32_t* src, uint32_t count)
{
    while (count-- != 0U)
    {
        *dst = *src;
         dst++;
         src++;
    }
}

static void ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit(uint8_t* dst, uint8_t* src, uint32_t count)
{
    while (count-- != 0U)
    {
        *dst = *src;
         dst++;
         src++;

    }
}

static bool ${QSPI_INSTANCE_NAME?lower_case}_setup_transfer( qspi_memory_xfer_t *qspi_memory_xfer, QSPI_TRANSFER_TYPE tfr_type, uint32_t address )
{
    uint32_t mask = 0;
    volatile uint32_t dummy = 0;

    /* Set instruction address register */
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

    /* Set Instruction code register */
    <#if HAS_SPLIT_ICR>
    if (tfr_type == QSPI_REG_READ || tfr_type == QSPI_MEM_READ)
    {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_RICR = (QSPI_RICR_RDINST(qspi_memory_xfer->instruction)) | (QSPI_RICR_RDOPT(qspi_memory_xfer->option));
    }
    else
    {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_WICR = (QSPI_WICR_WRINST(qspi_memory_xfer->instruction)) | (QSPI_WICR_WROPT(qspi_memory_xfer->option));
    }
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST((uint32_t)qspi_memory_xfer->instruction)) | (QSPI_ICR_OPT((uint32_t)qspi_memory_xfer->option));
    </#if>

    /* Set Instruction Frame register*/

    mask |= (uint32_t)qspi_memory_xfer->width;
    mask |= (uint32_t)qspi_memory_xfer->addr_len;

    if (qspi_memory_xfer->option_en)
    {
        mask |= (uint32_t)qspi_memory_xfer->option_len;
        mask |= QSPI_IFR_OPTEN_Msk;
    }

    if (qspi_memory_xfer->continuous_read_en)
    {
        mask |= QSPI_IFR_CRM_Msk;
    }

    mask |= QSPI_IFR_NBDUM((uint32_t)qspi_memory_xfer->dummy_cycles);

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
        default:
            /*default*/
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
        default:
            /*default*/
            break;
    };
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    /* To synchronize APB and AHB accesses */
    dummy = ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR;
    (void)dummy;

    return true;
}

void ${QSPI_INSTANCE_NAME}_EndTransfer( void )
{
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_CR = QSPI_CR_LASTXFER_Msk;
}

bool ${QSPI_INSTANCE_NAME}_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address )
{
    uint32_t mask = 0;

    /* Configure address */
    if(qspi_command_xfer->addr_en)
    {
        ${QSPI_INSTANCE_NAME}_REGS->QSPI_IAR = QSPI_IAR_ADDR(address);

        mask |= QSPI_IFR_ADDREN_Msk;
        mask |= (uint32_t)qspi_command_xfer->addr_len;
    }

    /* Configure instruction */
    <#if HAS_SPLIT_ICR>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_WICR = (QSPI_WICR_WRINST(qspi_command_xfer->instruction));
    <#else>
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST((uint32_t)qspi_command_xfer->instruction));
    </#if>

    /* Configure instruction frame */
    mask |= (uint32_t)qspi_command_xfer->width;
    mask |= QSPI_IFR_INSTEN_Msk;
    <#if HAS_SPLIT_ICR>
    mask |= QSPI_IFR_TFRTYP(0);
    mask |= QSPI_IFR_APBTFRTYP(0);
    <#else>
    mask |= QSPI_IFR_TFRTYP(QSPI_IFR_TFRTYP_TRSFR_READ_Val);
    </#if>

    ${QSPI_INSTANCE_NAME}_REGS->QSPI_IFR = mask;

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk) == 0U)
    {
        /* Poll Status register to know status if instruction has end */
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
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST((uint32_t)qspi_register_xfer->instruction));
    </#if>

    /* Configure Instruction Frame */
    mask |= (uint32_t)qspi_register_xfer->width;

    mask |= QSPI_IFR_NBDUM((uint32_t)qspi_register_xfer->dummy_cycles);

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
    (void)dummy;

    /* Read the register content */
    ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit((uint8_t *)rx_data , (uint8_t *)qspi_buffer,  rx_data_length);

    __DSB();
    __ISB();

    ${QSPI_INSTANCE_NAME}_EndTransfer();

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk) == 0U)
    {
        /* Poll Status register to know status if instruction has end */
    }

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
    ${QSPI_INSTANCE_NAME}_REGS->QSPI_ICR = (QSPI_ICR_INST((uint32_t)qspi_register_xfer->instruction));
    </#if>

    /* Configure Instruction Frame */
    mask |= (uint32_t)qspi_register_xfer->width;

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

    ${QSPI_INSTANCE_NAME}_EndTransfer();

    while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk) == 0U)
    {
        /* Poll Status register to know status if instruction has end */
    }

    (void)dummy;
    return true;
}

/* MISRA C-2012 Rule 11.3 violated 2 times below. Deviation record ID - H3_MISRAC_2012_R_11_3_DR_1*/
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate:2 "MISRA C-2012 Rule 11.3" "H3_MISRAC_2012_R_11_3_DR_1"
</#if>

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
    bool readStatus = false;

    ///// device preliminaries
    if( ${QSPI_INSTANCE_NAME?lower_case}_setup_transfer( qspi_memory_xfer,
                            QSPI_MEM_READ,
                            address
                        ) )
    {
        //// dst and src buffer characterization
        numDstPreWordBytes =  0x03U & (uint32_t) pRxBuffer;
        if( numDstPreWordBytes != 0U )
        {
            numDstPreWordBytes =  sizeof(uint32_t) - numDstPreWordBytes;
        }

        if( rx_data_length >= numDstPreWordBytes )
        {
            numDstPostWordBytes = 0x03U & (uint32_t) (pRxBuffer + rx_data_length);
        }

        numSrcPreWordBytes =  0x03U & (uint32_t) qspi_mem;
        if( numSrcPreWordBytes != 0U)
        {
            numSrcPreWordBytes =  sizeof(uint32_t) - numSrcPreWordBytes;
        }
        if( rx_data_length >= numSrcPreWordBytes )
        {
            numSrcPostWordBytes = 0x03U & (uint32_t) (qspi_mem + rx_data_length);
        }
        else
        {
            numSrcPreWordBytes = rx_data_length;
        }

        if( rx_data_length > (numSrcPreWordBytes + numSrcPostWordBytes) )
        {
            // number of word size transfers is equal to length of buffer
            // minus single byte transfers
            numWordTransferBytes = rx_data_length - (numSrcPreWordBytes + numSrcPostWordBytes);
        }

        // test if src has same number of word alignments as the dst buffer
        if( (numDstPreWordBytes + numDstPostWordBytes) != (numSrcPreWordBytes + numSrcPostWordBytes))
        {
            // a word size space will be needed for shifting purposes; the
            // common case optimization for equal word alignments cannot be used
            if( numWordTransferBytes >= sizeof(uint32_t))
            {
                numWordTransferBytes -= sizeof(uint32_t);
                numSrcPostWordBytes += sizeof(uint32_t);
            }
            else
            {
                numWordTransferBytes = 0;
            }
        }

        shiftBytes = ((int32_t)numSrcPreWordBytes - (int32_t)numDstPreWordBytes);

        ///// Transfer of data from src device to dst buffer
        // Perform single byte transfers necessary before word alignment begins
        if( numSrcPreWordBytes != 0U)
        {
            // get these now so we don't have to backup the device access later
            ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( tmpBuffer, qspi_mem, numSrcPreWordBytes );
            // word alignment point for the src
            qspi_mem += numSrcPreWordBytes;
        }
        // word alignment point for the dst
        pRxBuffer += numDstPreWordBytes;

        // Perform word aligned transfers
        if( (numWordTransferBytes / 4U) != 0U )
        {
            ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit( (uint32_t *) pRxBuffer,
                    (uint32_t *) qspi_mem,
                    numWordTransferBytes / 4U
                );

            qspi_mem += numWordTransferBytes;
            pRxBuffer += numWordTransferBytes;
        }

        // left, or no, shift
        if( 0 >= shiftBytes )
        {
            if( shiftBytes != 0 )
            {
                if(numWordTransferBytes > 0U)
                {
                    // Shift the data left to its final destination buffer location
                    (void)memmove( ((uint8_t *) rx_data) + numDstPreWordBytes + shiftBytes,
                            ((uint8_t *) rx_data) + numDstPreWordBytes,
                            numWordTransferBytes
                        );
                }
                // adjust end point
                pRxBuffer += shiftBytes;
            }
            // Now we have room at the end, perform the single byte transfers
            // necessary after word alignment ends
            if( numSrcPostWordBytes != 0U )
            {
                ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( pRxBuffer, qspi_mem, numSrcPostWordBytes );
            }
        }
        // right shift
        else
        {
            // Perform the single byte transfers necessary after word alignment ends
            if( numSrcPostWordBytes != 0U )
            {
                ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit( pRxBuffer, qspi_mem, numSrcPostWordBytes );
            }
            if((numWordTransferBytes + numSrcPostWordBytes) > 0U)
            {
                // Shift the data to right to its final destination buffer location
                (void)memmove( ((uint8_t *) rx_data) + numDstPreWordBytes + shiftBytes,
                        ((uint8_t *) rx_data) + numDstPreWordBytes,
                        numWordTransferBytes + numSrcPostWordBytes
                    );
            }
        }

        if( numSrcPreWordBytes != 0U)
        {
            // Now we have room at the beginning;
            // place the previously saved pre-word aligned bytes
            (void)memmove((uint8_t *) rx_data, tmpBuffer, numSrcPreWordBytes );
        }
        ///// Clean up
        /* Dummy Read to clear QSPI_SR.INSTRE and QSPI_SR.CSR */
        (void) ${QSPI_INSTANCE_NAME}_REGS->QSPI_SR;
        __DSB();
        __ISB();

        ${QSPI_INSTANCE_NAME}_EndTransfer();

        while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR & QSPI_SR_INSTRE_Msk) == 0U )
        {
            // Poll Status register to know status if instruction has ended
        }
        readStatus = true;
    }
    return readStatus;
}

<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 11.3"
<#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2012 deviation block end */

bool ${QSPI_INSTANCE_NAME}_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address )
{
    uint32_t *qspi_mem = (uint32_t *)(${QSPI_INSTANCE_NAME}MEM_ADDR | address);
    uint32_t length_32bit, length_8bit;
    bool writeStatus = false;

    if (${QSPI_INSTANCE_NAME?lower_case}_setup_transfer(qspi_memory_xfer, QSPI_MEM_WRITE, address))
    {
        /* Write to serial flash memory */
        if ((0x03U & (uint32_t) tx_data) == 0U)
        {
            length_32bit = tx_data_length / 4U;
            length_8bit= tx_data_length & 0x03U;

            if(length_32bit != 0U)
            {
                ${QSPI_INSTANCE_NAME?lower_case}_memcpy_32bit(qspi_mem, tx_data, length_32bit);
            }
            tx_data = tx_data + length_32bit;
            qspi_mem = qspi_mem + length_32bit;
        }
        else
        {
            length_8bit = tx_data_length;
        }

        if(length_8bit != 0U)
        {
            ${QSPI_INSTANCE_NAME?lower_case}_memcpy_8bit((uint8_t *)qspi_mem, (uint8_t *)tx_data, length_8bit);
        }
        __DSB();
        __ISB();

        ${QSPI_INSTANCE_NAME}_EndTransfer();

        while((${QSPI_INSTANCE_NAME}_REGS->QSPI_SR& QSPI_SR_INSTRE_Msk) == 0U)
        {
            /* Poll Status register to know status if instruction has end */
        }
        writeStatus = true;
    }
    return writeStatus;
}

/*******************************************************************************
 End of File
*/
