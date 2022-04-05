// helper routines to read and write regions of memory in 128 byte chunks

#define TRANSFER_CHUNK_SIZE 0x80U

__STATIC_INLINE void Read_Chunk(uint32_t address)
{
    __asm__ volatile (
         "MOV      r8, %[addr]\n"
         "PLD      [r8, #0xC0]\n"
         "VLDM     r8,{d0-d15}\n"
           : : [addr] "l" (address) : "r8"
    );
}

__STATIC_INLINE void Write_Chunk(uint32_t address)
{
    __asm__ volatile (
         "MOV      r8, %[addr]\n"
         "VSTM     r8,{d0-d15}\n"
           : : [addr] "l" (address) : "r8"
    );
}

// initialize the ECC for a single TCM region (defined by addr and size) in 128 byte chunks
static void  __attribute__((optimize("-O1")))  TCM_EccInitOne(uint32_t addr, uint32_t size) {

    uint32_t pTcm;

    for (pTcm = addr; pTcm < (addr + size); pTcm += TRANSFER_CHUNK_SIZE)
    {
        //read ECC OFF
        TCMECC_REGS->TCMECC_CR = 0x0U;
        __DSB();
        __ISB();
        Read_Chunk(pTcm);

        //Write ECC ON
        TCMECC_REGS->TCMECC_CR = 0x1U;
        __DSB();
        __ISB();
        Write_Chunk(pTcm);
        __DSB();
        __ISB();
    }
}

/* Initialize ECC for TCM memories */
__STATIC_INLINE void  __attribute__((optimize("-O1"))) TCM_EccInitialize(void)
{

    __DSB();
    __ISB();

    TCMECC_REGS->TCMECC_CR = 0x0U;
    __DSB();
    __ISB();
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk);
    __DSB();
    __ISB();

    //enable Icache and Dcache
    SCB_EnableICache();
    SCB_EnableDCache();



    //  initalize both TCM's (to handle ECC properly prior activating RMW/RETEN features)
    TCM_EccInitOne(ITCM_ADDR, ITCM_SIZE);
    TCM_EccInitOne(DTCM_ADDR, DTCM_SIZE);

    //disable cache I et data D
    SCB_DisableICache();
    SCB_DisableDCache();

    __DSB();
    __ISB();

    TCMECC_REGS->TCMECC_CR = 0x0U;

    //----------------------------------------------------------------------
    // ITCM/DTCM enable with RMW and RETEN + TCMECC ON
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk | SCB_ITCMCR_RMW_Msk | SCB_ITCMCR_RETEN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk | SCB_DTCMCR_RMW_Msk | SCB_DTCMCR_RETEN_Msk);
    __DSB();
    __ISB();

<#if TCM_ECC_ENABLE>
    TCMECC_REGS->TCMECC_CR = 0x1U;
    __DSB();
    __ISB();
</#if>
}


__STATIC_INLINE void  __attribute__((optimize("-O1"))) FlexRAM_EccInitialize(void)
{
    uint32_t pFlexRam;

    __DSB();
    __ISB();

    // FlexRAM initialization loop (to handle ECC properly)
    for (pFlexRam = FLEXRAM_ADDR ; pFlexRam < (FLEXRAM_ADDR + FlexRAM_SIZE) ; pFlexRam += TRANSFER_CHUNK_SIZE)
    {
        Read_Chunk(pFlexRam);
        __DSB();
        __ISB();
        Write_Chunk(pFlexRam);
        __DSB();
        __ISB();
    }


    __DSB();
    __ISB();
}
