/*******************************************************************************
  OTP Memory controller (OTPC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${OTPC_INSTANCE_NAME?lower_case}.c

  Summary
    Source for OTPC peripheral library interface Implementation.

  Description
    This file implements the interface to the OTPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

<#assign USE_FIXUP = __PROCESSOR?contains("SAM9X6") && !ENABLE_OTPC_EMULATION>

#include "plib_${OTPC_INSTANCE_NAME?lower_case}.h"

#define OTPC_UID_DISABLED 0XCAFECAFEU

#define OTPC_KEY_FOR_WRITING      (0x7167U)
#define OTPC_KEY_FOR_UPDATING     (0x7167U)
#define OTPC_KEY_FOR_LOCKING      OTPC_KEY_FOR_UPDATING
#define OTPC_KEY_FOR_INVALIDATING OTPC_KEY_FOR_UPDATING
#define OTPC_KEY_FOR_EMUL         OTPC_KEY_FOR_UPDATING

#define OTPC_MAX_PAYLOAD_ALLOWED  1024U

#define OTPC_4B_AND_REGULAR       (OTPC_HR_PACKET_REGULAR | OTPC_HR_ONE_Msk)

#define OTPC_MR_ALWAYS_RESET_Msk (OTPC_MR_KBDST_Msk | OTPC_MR_NPCKT_Msk)

#define TIMEOUT 500000

#define OTPC_AES_MODULE    1
#define OTPC_TZAESB_MODULE 2
#define OTPC_TDES_MODULE   3

<#if ENABLE_OTPC_EMULATION>
#define EMULATION_START     ${OTPC_EMULATION_ADDRESS}U
#define EMULATION_SIZE      ${OTPC_EMULATION_SIZE}
</#if>

<#if USE_FIXUP>
#define ARRAY_SIZE(array) \
    (sizeof(array) / sizeof(array[0]))

#define DBGU_CIDR_REVISION_Pos  0
#define DBGU_CIDR_REVISION_Msk  (0x7u << DBGU_CIDR_REVISION_Pos)
#define DBGU_CIDR_REVISION_A    (0x1u << DBGU_CIDR_REVISION_Pos)

static void otpc_fixup()
{
    static const uint32_t fixup_reg1[4] = {0x04194801, 0x01000000, 0x00000008, 0x00000000};
    static const uint32_t fixup_reg2[4] = {0xfb164801, 0x4c017d12, 0x02120e01, 0x00004000};
    __IO uint32_t *reg0 = (__IO uint32_t *)(0xeff00090);
    __IO uint32_t *reg1 = (__IO uint32_t *)(0xeff000a0);
    __IO uint32_t *reg2 = (__IO uint32_t *)(0xeff000b0);
    uint32_t timeout;
    int i;

    if ((DBGU_REGS->DBGU_CIDR & DBGU_CIDR_REVISION_Msk) != DBGU_CIDR_REVISION_A)
      return;

    timeout = TIMEOUT;
    *reg0 = 0x43910001;
    while (((${OTPC_INSTANCE_NAME}_REGS->OTPC_SR & OTPC_SR_UNLOCK_Msk) == 0U) && (--timeout > 0U))
    {
            /* Nothing to do */
    }

    for (i = 0; i < ARRAY_SIZE(fixup_reg1); i++)
    {
      reg1[i] = fixup_reg1[i];
    }

    for (i = 0; i < ARRAY_SIZE(fixup_reg2); i++)
    {
      reg2[i] = fixup_reg2[i];
    }

    timeout = TIMEOUT;
    *reg0 = 0x43910000;
    while (((${OTPC_INSTANCE_NAME}_REGS->OTPC_SR & OTPC_SR_UNLOCK_Msk) != 0U) && (--timeout > 0U))
    {
            /* Nothing to do */
    }
}

</#if>
<#if ENABLE_OTPC_EMULATION>

static void clear_otp_emulation_memory(void)
{
    volatile uint8_t *memory_addr = (volatile uint8_t *)EMULATION_START;
    uint32_t memory_size = EMULATION_SIZE;
    while(memory_size-- != 0U)
    {
        *memory_addr = 0;
         memory_addr++;
    }
}
</#if>

static uint32_t otp_wait_isr(uint32_t mask)
{
    uint32_t timeout = TIMEOUT;
    uint32_t reg = 0;
    do {
        reg |= ${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;
        if ((reg & mask) != 0U)
        {
            break;
        }
        timeout--;
    } while (timeout != 0U);
    return reg;
}


static otpc_error_code_t otp_trigger_packet_read(uint16_t hdr_addr, uint32_t *pckt_hdr)
{
    uint32_t isr_reg, mr_reg;

    /* Write address of the header in OTPC_MR register (AADDR field)*/
    mr_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR;
    mr_reg &= ~OTPC_MR_ALWAYS_RESET_Msk;
    mr_reg = (mr_reg & ~OTPC_MR_ADDR_Msk) | OTPC_MR_ADDR((uint32_t)hdr_addr);
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = mr_reg;

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    /* Set READ bit in OTPC_CR register*/
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_READ_Msk;

    /* Wait for EOR bit in OTPC_ISR to be 1 (packet was transfered )*/
    isr_reg = otp_wait_isr(OTPC_ISR_EOR_Msk);
    if ((isr_reg & OTPC_ISR_EOR_Msk) == 0U)
    {
        return OTPC_READING_DID_NOT_STOP;
    }

    /* Read the header value from OTPC_HR */
    if (pckt_hdr != NULL)
    {
        *pckt_hdr = ${OTPC_INSTANCE_NAME}_REGS->OTPC_HR;
    }

    return OTPC_NO_ERROR;
}


static otpc_error_code_t otp_set_type(OTPC_PACKET_TYPE type, uint32_t *pckt_hdr)
{
    *pckt_hdr &= ~OTPC_HR_PACKET_Msk;

    switch (type) {
    case OTP_PCKT_REGULAR:
        *pckt_hdr |= OTPC_HR_PACKET_REGULAR;
        break;

    case OTP_PCKT_KEY:
        *pckt_hdr |= OTPC_HR_PACKET_KEY;
        break;

    case OTP_PCKT_BOOT_CONFIGURATION:
        *pckt_hdr |= OTPC_HR_PACKET_BOOT_CONFIGURATION;
        break;

    case OTP_PCKT_SECURE_BOOT_CONFIGURATION:
        *pckt_hdr |= OTPC_HR_PACKET_SECURE_BOOT_CONFIGURATION;
        break;

    case OTP_PCKT_HARDWARE_CONFIGURATION:
        *pckt_hdr |= OTPC_HR_PACKET_HARDWARE_CONFIGURATION;
        break;

    case OTP_PCKT_CUSTOM:
        *pckt_hdr |= OTPC_HR_PACKET_CUSTOM;
        break;

    default:
        return OTPC_ERROR_BAD_HEADER; 
        break;        
    }

    return OTPC_NO_ERROR;
}

static otpc_error_code_t otp_set_payload_size(uint32_t size, uint32_t *pckt_hdr)
{
    if ((size == 0U) || ((size & 3U)!= 0U))
    {
        return OTPC_ERROR_BAD_HEADER;
    }

    *pckt_hdr &= ~OTPC_HR_SIZE_Msk;
    *pckt_hdr |= OTPC_HR_SIZE((size >> 2U) - 1U);

    return OTPC_NO_ERROR;
}

static uint16_t otp_get_payload_size(uint32_t pckt_hdr)
{
    uint16_t pckt_size;

    pckt_size = (uint16_t)((pckt_hdr & OTPC_HR_SIZE_Msk) >> OTPC_HR_SIZE_Pos);
    
    uint32_t temp_pck_size = (uint32_t)pckt_size + 1U;
    return (uint16_t)(temp_pck_size * sizeof(uint32_t));
}

static otpc_error_code_t otp_set_new_packet_header(const OTPC_NEW_PACKET *pckt,
                     uint32_t *pckt_hdr)
{
    otpc_error_code_t error;

    *pckt_hdr = OTPC_HR_ONE_Msk;
    error = otp_set_type(pckt->type, pckt_hdr);
    error = (error != 0U)  ? error : otp_set_payload_size(pckt->size, pckt_hdr);
    return error;
}


static otpc_error_code_t otp_trans_key(uint32_t key_bus_dest)
{
    static const uint32_t isr_err = OTPC_ISR_KBERR_Msk;
    uint32_t isr_reg;
    uint32_t value;

    switch (key_bus_dest)
    {
        case OTPC_AES_MODULE:
            value = OTPC_MR_KBDST_AES;
            break;

        case OTPC_TDES_MODULE:
            value = OTPC_MR_KBDST_TDES;
            break;

        default:
            return OTPC_CANNOT_TRANSFER_KEY;   
            break;            
    }
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = (${OTPC_INSTANCE_NAME}_REGS->OTPC_MR & ~OTPC_MR_KBDST_Msk) | value;

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_WRITING) | OTPC_CR_KBSTART_Msk;
    isr_reg = otp_wait_isr(OTPC_ISR_EOKT_Msk | isr_err);
    if (((isr_reg & OTPC_ISR_EOKT_Msk) == 0U) || ((isr_reg & isr_err) != 0U))
    {
        return OTPC_CANNOT_TRANSFER_KEY;
    }
    return OTPC_NO_ERROR;
}


static otpc_error_code_t otp_emulation_mode(bool on_off)
{
    static const uint32_t isr_err = OTPC_ISR_COERR_Msk | OTPC_ISR_CKERR_Msk;
    uint32_t reg;
    uint32_t mr_emul_value;

    mr_emul_value = (((uint32_t)!!on_off) * (OTPC_MR_EMUL_Msk & ((~OTPC_MR_EMUL_Msk) << 1)));
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = (${OTPC_INSTANCE_NAME}_REGS->OTPC_MR & (~OTPC_MR_EMUL_Msk)) | mr_emul_value;

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_REFRESH_Msk | OTPC_CR_KEY(OTPC_KEY_FOR_EMUL);

    /* Wait for refreshing data */
    reg = otp_wait_isr(OTPC_ISR_EORF_Msk | isr_err);
    if (((reg & OTPC_ISR_EORF_Msk) == 0U) || ((reg & isr_err)!= 0U))
    {
        return OTPC_CANNOT_REFRESH;
    }

    /* Check if the Emulation mode state */
    if (((!!(${OTPC_INSTANCE_NAME}_REGS->OTPC_SR & OTPC_SR_EMUL_Msk)) ^ (!!on_off)) != 0)
    {
        return OTPC_ERROR_CANNOT_ACTIVATE_EMULATION;
    }

    return OTPC_NO_ERROR;
}


void ${OTPC_INSTANCE_NAME}_Initialize( void )
{
<#if USE_FIXUP>
    otpc_fixup();

</#if>
<#if ENABLE_OTPC_EMULATION>
    clear_otp_emulation_memory();

</#if>
    (void)otp_emulation_mode(${ENABLE_OTPC_EMULATION?string('true', 'false')});
}


otpc_error_code_t OTPC_LockPacket(uint16_t headerAddress)
{
    static const uint32_t isr_err = OTPC_ISR_LKERR_Msk;
    uint32_t hdr_value;
    uint32_t reg;
    otpc_error_code_t error;

    error = otp_trigger_packet_read(headerAddress, &hdr_value);
    if (error != OTPC_NO_ERROR)
    {
        return error;
    }

    if ((hdr_value & OTPC_HR_INVLD_Msk) == OTPC_HR_INVLD_Msk)
    {
        return OTPC_ERROR_PACKET_IS_INVALID;
    }

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    /* Set the KEY field */
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_LOCKING) | OTPC_CR_CKSGEN_Msk;

    /* Wait for locking the packet */
    reg = otp_wait_isr(OTPC_ISR_EOL_Msk | isr_err);
    if (((reg & OTPC_ISR_EOL_Msk) == 0U) || ((reg & isr_err)!= 0U))
    {
        return OTPC_CANNOT_LOCK;
    }

    return OTPC_NO_ERROR;
}


otpc_error_code_t OTPC_InvalidatePacket(uint16_t headerAddress)
{
    static const uint32_t isr_err = OTPC_ISR_IVERR_Msk;
    uint32_t reg;

    /* Set the header address and using reg as temp value */
    reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR;
    reg &= ~OTPC_MR_ALWAYS_RESET_Msk;
    reg = (reg & ~OTPC_MR_ADDR_Msk) | OTPC_MR_ADDR((uint32_t)headerAddress);
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = reg;

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_INVALIDATING) | OTPC_CR_INVLD_Msk;

    /* Wait for invalidating the packet */
    reg = otp_wait_isr(OTPC_ISR_EOI_Msk | isr_err);
    if ((0U == (reg & OTPC_ISR_EOI_Msk)) || (0U != (reg & isr_err)))
    {
        return OTPC_CANNOT_INVALIDATE;
    }

    return OTPC_NO_ERROR;
}


otpc_error_code_t OTPC_HidePacket(uint16_t headerAddress)
{
    static const uint32_t isr_err = OTPC_ISR_HDERR_Msk;
    uint32_t reg;

    reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR;
    reg &= ~OTPC_MR_ALWAYS_RESET_Msk;
    reg = (reg & ~OTPC_MR_ADDR_Msk) | OTPC_MR_ADDR((uint32_t)headerAddress);
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = reg;

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_WRITING) | OTPC_CR_HIDE_Msk;

    reg = otp_wait_isr(OTPC_ISR_EOH_Msk | isr_err);
    if (((reg & OTPC_ISR_EOH_Msk)== 0U) || ((reg & isr_err)!= 0U))
    {
        return OTPC_CANNOT_PERFORM_HIDING;
    }

    return OTPC_NO_ERROR;
}


otpc_error_code_t OTPC_ReadPacket(  uint16_t headerAddress,
                                    uint32_t *readBuffer,
                                    uint16_t bufferSize,
                                    uint16_t *sizeRead)
{
    uint32_t hdr_value = 0;
    uint16_t payload_size = 0;
    otpc_error_code_t error = OTPC_NO_ERROR;
    uint32_t ar_reg;

    if ((${OTPC_INSTANCE_NAME}_REGS->OTPC_MR & OTPC_MR_RDDIS_Msk) != 0U)
    {
        return  OTPC_CANNOT_START_READING;
    }

    error = otp_trigger_packet_read(headerAddress, &hdr_value);
    if (error != OTPC_NO_ERROR)
    {
        return error;
    }

    if ((hdr_value & OTPC_HR_INVLD_Msk) == OTPC_HR_INVLD_Msk)
    {
        return OTPC_ERROR_PACKET_IS_INVALID;
    }

    if ((hdr_value & OTPC_HR_PACKET_Msk) == OTPC_HR_PACKET_KEY)
    {
        return otp_trans_key(*readBuffer);
    }

    /*
     * Read packet payload from offset 0:
     * clear DADDR field and set INCRT to AFTER_READ
     */
    ar_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR;
    ar_reg &= ~(OTPC_AR_DADDR_Msk | OTPC_AR_INCRT_Msk);
    ar_reg |= OTPC_AR_INCRT_AFTER_READ;
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR = ar_reg;

    /* The value read from header shall be interpreted as follows: */
    /* 0   ==> 4 bytes */
    /* 255 ==> 1024 bytes */
    payload_size = otp_get_payload_size(hdr_value);

    if (payload_size > bufferSize)
    {
        return OTPC_ERROR_BUFFER_OVERFLOW;
    }

    *sizeRead = payload_size;

    while (payload_size != 0U) {
        /* Start reading the payload (one word at a time) */
        /* otpc_struct->OTPC_DR will be incremented automatically (default value) */
        *readBuffer =  ${OTPC_INSTANCE_NAME}_REGS->OTPC_DR;
         readBuffer++;

        /* Update the size of the payload to be read */
        payload_size -= (uint16_t)sizeof(uint32_t);
    }

    return OTPC_NO_ERROR;
}


otpc_error_code_t OTPC_WritePacket(const OTPC_NEW_PACKET *packet,
                         const uint32_t *payload,
                         uint16_t *headerAddress,
                         uint16_t *sizeWritten)
{
    static const uint32_t isr_err = OTPC_ISR_WERR_Msk | OTPC_ISR_PGERR_Msk;
    uint32_t hdr_value;
    uint32_t backup_header_reg;
    uint32_t backup_data_reg;
    uint32_t backup_header_value;
    const uint32_t *backup_src = payload;
    uint32_t isr_reg, mr_reg, ar_reg;
    uint16_t payload_size;
    uint16_t backup_size;
    uint16_t size_field=0;
    bool must_invalidate = false;
    bool is_key = false;
    bool ready_to_program   =   false;
    bool backup_full_payload = true;

    otpc_error_code_t error = otp_set_new_packet_header(packet, &hdr_value);
    if (error != OTPC_NO_ERROR)
    {
        return error;
    }

    backup_header_value = hdr_value;
    payload_size = otp_get_payload_size(hdr_value);
    backup_size = payload_size;

    if (payload_size > OTPC_MAX_PAYLOAD_ALLOWED)
    {
        return OTPC_PACKET_TOO_BIG;
    }

    /* Check against the hardware write disable */
    if ((${OTPC_INSTANCE_NAME}_REGS->OTPC_MR & OTPC_MR_WRDIS_Msk) != 0U)
    {
        return OTPC_ERROR_HW_WRITE_DISABLED;
    }

    if ((hdr_value & OTPC_HR_PACKET_Msk) == OTPC_HR_PACKET_KEY) {
        is_key = true;
        backup_header_value &= ~OTPC_HR_PACKET_Msk;
        backup_header_value |= OTPC_HR_PACKET_REGULAR;
    }

    /* Set MR_ADDR to its maximum value then read packet */
    error = otp_trigger_packet_read(~((uint16_t)0), NULL);
    if (error != OTPC_NO_ERROR)
    {
        return error;
    }

    /* There is "1" */
    if ((${OTPC_INSTANCE_NAME}_REGS->OTPC_SR & OTPC_SR_ONEF_Msk) != 0U)
    {
        backup_header_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_HR;
        size_field = otp_get_payload_size(backup_header_reg);
        backup_header_reg |= hdr_value;

        if (backup_header_reg != hdr_value)
        {
            /* Try to minimize the waste of memory, allocate 4 bytes and invalidate the packet */
            backup_size = size_field;
            backup_header_value &= OTPC_4B_AND_REGULAR;
            must_invalidate = true;
            ready_to_program = true;
        }

        /* Header is safe to be written, but what about payload ? */
        else if (!must_invalidate)
        {
            while (backup_size != 0U)
            {
                backup_data_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_DR;
                backup_data_reg |= *backup_src;

                /* Can payload be safely written ? */
                if (backup_data_reg != (*backup_src))
                {
                    must_invalidate = true;
                    backup_size = size_field;
                    backup_header_value &= OTPC_4B_AND_REGULAR;
                    backup_src = payload;
                    backup_full_payload = false;
                    break;
                }

                backup_size -= (uint16_t)sizeof(uint32_t);
                backup_src++;
            }
        }
        else
        {
            ; /* No action required - ; is optional */
        }
        if(backup_full_payload)
        {
            backup_size = payload_size;
        }
    }

    if(!ready_to_program)
    {
        /* Write OTPC_MR.ADDR to '0' and set NPCKT */
        mr_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR;
        mr_reg &= ~(OTPC_MR_ALWAYS_RESET_Msk | OTPC_MR_ADDR_Msk);
        mr_reg |= OTPC_MR_NPCKT_Msk;
        ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR = mr_reg;

        /* Check for flushing process */
        if ((${OTPC_INSTANCE_NAME}_REGS->OTPC_SR & OTPC_SR_FLUSH_Msk) != 0U)
        {
            /* Wait until flush operation is done or timeout occured */
            isr_reg = otp_wait_isr(OTPC_ISR_EOF_Msk);
            if ((isr_reg & OTPC_ISR_EOF_Msk) == 0U) {
                error = OTPC_FLUSHING_DID_NOT_END;
                ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR &= ~OTPC_MR_NPCKT_Msk;
                return error;
            }
        }

        ${OTPC_INSTANCE_NAME}_REGS->OTPC_HR = backup_header_value;

        /*
         * Write packet payload from offset 0:
         * clear DADDR field and set INCRT to AFTER_WRITE
         */
        ar_reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR;
        ar_reg &= ~(OTPC_AR_DADDR_Msk | OTPC_AR_INCRT_Msk);
        ar_reg |= OTPC_AR_INCRT_AFTER_WRITE;
        ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR = ar_reg;

        /* Start downloading data */
        while (backup_size != 0U)
        {
            ${OTPC_INSTANCE_NAME}_REGS->OTPC_DR = *payload;
            payload++;

            backup_size -= (uint16_t)sizeof(uint32_t);
        }

        if (is_key)
        {
            backup_header_value &= ~OTPC_HR_PACKET_Msk;
            backup_header_value |= OTPC_HR_PACKET_KEY;
            ${OTPC_INSTANCE_NAME}_REGS->OTPC_HR = backup_header_value;
        }
    }

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    /* Set the KEY field * Set PGM field */
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_WRITING) | OTPC_CR_PGM_Msk;

    /* Check whether the data was written correctly */
    isr_reg = otp_wait_isr(OTPC_ISR_EOP_Msk | isr_err);
    if (((isr_reg & OTPC_ISR_EOP_Msk) == 0U) || ((isr_reg & isr_err) != 0U))
    {
        error = OTPC_CANNOT_START_PROGRAMMING;
        ${OTPC_INSTANCE_NAME}_REGS->OTPC_MR &= ~OTPC_MR_NPCKT_Msk;
        return error;

    }

    /* Retrieve the address of the packet header */
    *headerAddress = (uint16_t)((${OTPC_INSTANCE_NAME}_REGS->OTPC_MR & OTPC_MR_ADDR_Msk) >> OTPC_MR_ADDR_Pos);

    if (must_invalidate)
    {
        /* Invalidate packet */
        (void)OTPC_InvalidatePacket(*headerAddress);

        error = OTPC_ERROR_PACKET_INVALIDATED;
        *sizeWritten = size_field;
    } else
    {
        *sizeWritten = payload_size;
    }

    return error;

}


otpc_error_code_t OTPC_UpdatePayload(uint16_t headerAddress, const uint32_t * payload)
{
    static const uint32_t isr_err = OTPC_ISR_WERR_Msk | OTPC_ISR_PGERR_Msk;
    uint32_t hdr_value = 0;
    uint32_t reg;
    uint16_t payload_size = 0;
    otpc_error_code_t error = OTPC_NO_ERROR;

    error = otp_trigger_packet_read(headerAddress, &hdr_value);
    if (error != OTPC_NO_ERROR)
    {
        return error;
    }

    if ((hdr_value & OTPC_HR_INVLD_Msk) == OTPC_HR_INVLD_Msk)
    {
        return OTPC_ERROR_PACKET_IS_INVALID;
    }

    /*
     * Write packet payload from offset 0:
     * clear DADDR field and set INCRT to AFTER_WRITE
     */
    reg = ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR;
    reg &= ~(OTPC_AR_DADDR_Msk | OTPC_AR_INCRT_Msk);
    reg |= OTPC_AR_INCRT_AFTER_WRITE;
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_AR = reg;

    /* The value read from header shall be interpreted as follows: */
    /* 0   ==> 4 bytes */
    /* 255 ==> 1024 bytes */
    payload_size = otp_get_payload_size(hdr_value);

    while (payload_size != 0U) {
        ${OTPC_INSTANCE_NAME}_REGS->OTPC_DR = *payload;
         payload++;

        payload_size -= (uint16_t)sizeof(uint32_t);
    }

    /* dummy read on OTPC_ISR to clear pending interrupts */
    (void)${OTPC_INSTANCE_NAME}_REGS->OTPC_ISR;

    /* Set the KEY field && PGM */
    ${OTPC_INSTANCE_NAME}_REGS->OTPC_CR = OTPC_CR_KEY(OTPC_KEY_FOR_UPDATING) | OTPC_CR_PGM_Msk;

    /* Programming without errors */
    reg = otp_wait_isr(OTPC_ISR_EOP_Msk | isr_err);
    if (((reg & OTPC_ISR_EOP_Msk) == 0U) || ((reg & isr_err) != 0U))
    {
        return OTPC_CANNOT_START_PROGRAMMING;
    }

    return OTPC_NO_ERROR;
}
