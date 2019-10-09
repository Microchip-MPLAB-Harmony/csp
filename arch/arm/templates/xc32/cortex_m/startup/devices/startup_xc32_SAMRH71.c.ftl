/** Program GPNVM fuse for TCM configuration */
<#if TCM_ECC_ENABLE>
__STATIC_INLINE void TCM_EccInitialize()
{
    uint64_t i = 0;
    uint64_t *pItcm = (uint64_t*) ITCM_ADDR;
    uint64_t *pDtcm = (uint64_t*) DTCM_ADDR;
    __DSB();
    __ISB();

    TCMECC_REGS->TCMECC_CR = 0x0;
    __DSB();
    __ISB();
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk);
    __DSB();
    __ISB();

    //enable cache I et data D
    SCB_EnableICache();
    SCB_EnableDCache();

    // ITCM initalization loop (to handle ECC properly prior activating RMW/RETEN features)
    for (i = 0; i < (0x4000); i += 0x10) // ITCM size/copy size in bytes = 0x20000/0x80 = 0x400 ( increment in 64 bits words = 0x80 / 8 = 0x10)
    {
        //read ECC OFF
        TCMECC_REGS->TCMECC_CR = 0x0;
        __DSB();
        __ISB();
        FPU_MemToFpu((unsigned int) (pItcm + i));
        //Write ECC ON
        TCMECC_REGS->TCMECC_CR = 0x1;
        __DSB();
        __ISB();
        FPU_FpuToMem((unsigned int) (pItcm + i));
        __DSB();
        __ISB();
    }
    __DSB();
    __ISB();

    // DTCM initalization loop (to handle ECC properly prior activating RMW/RETEN features)
    for (i = 0; i < (0x8000); i += 0x10) // DTCM size/copy size in bytes = 0x40000/0x80 = 0x800 ( increment in 64 bits words : 0x80 / 8 = 0x10)
    {
        //read ECC OFF
        TCMECC_REGS->TCMECC_CR = 0x0;
        __DSB();
        __ISB();
        FPU_MemToFpu((unsigned int) (pDtcm + i));

        //Write ECC ON
        TCMECC_REGS->TCMECC_CR = 0x1;
        __DSB();
        __ISB();
        FPU_FpuToMem((unsigned int) (pDtcm + i));
        __DSB();
        __ISB();
    }
    __DSB();
    __ISB();

    //disable cache I et data D
    SCB_DisableICache();
    SCB_DisableDCache();

    __DSB();
    __ISB();

    TCMECC_REGS->TCMECC_CR = 0x0;

    //----------------------------------------------------------------------
    // ITCM/DTCM enable with RMW and RETEN + TCMECC ON
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk | SCB_ITCMCR_RMW_Msk | SCB_ITCMCR_RETEN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk | SCB_DTCMCR_RMW_Msk | SCB_DTCMCR_RETEN_Msk);
    __DSB();
    __ISB();

    TCMECC_REGS->TCMECC_CR = 0x1;
    __DSB();
    __ISB();
}
</#if>

<#if TCM_ENABLE>
/** Enable TCM memory */
__STATIC_INLINE void <#if COMPILER_CHOICE == "XC32">__attribute__((optimize("-O1"))) </#if>TCM_Enable(void)
{
    __DSB();
    __ISB();
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk  | SCB_ITCMCR_RMW_Msk | SCB_ITCMCR_RETEN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk | SCB_DTCMCR_RMW_Msk | SCB_DTCMCR_RETEN_Msk);
    __DSB();
    __ISB();
}

<#else>
/* Disable TCM memory */
__STATIC_INLINE void <#if COMPILER_CHOICE == "XC32">__attribute__((optimize("-O1"))) </#if>TCM_Disable(void)
{
    __DSB();
    __ISB();
    SCB->ITCMCR &= ~(uint32_t)SCB_ITCMCR_EN_Msk;
    SCB->DTCMCR &= ~(uint32_t)SCB_ITCMCR_EN_Msk;
    __DSB();
    __ISB();
}
</#if>

<#if FLEXRAM_ECC_SUPPORTED??>
__STATIC_INLINE void FlexRAM_EccInitialize(void)
{
    uint64_t i = 0;
    uint64_t *pFlexRam = (uint64_t*) FLEXRAM_ADDR;

    //enable cache I et data D
    SCB_EnableICache();
    SCB_EnableDCache();
    __DSB();
    __ISB();

    // FlexRAM initialization loop (to handle ECC properly)
    for (i = 0; i < (0x18000); i += 0x10) // FlexRAM size/copy size in bytes = 0xC0000/0x80 = 0x1800 ( increment in 64 bits words : 0x80 / 8 = 0x10)
    {
        FPU_MemToFpu((unsigned int) (pFlexRam + i));
        //Write ECC ON
        __DSB();
        __ISB();
        FPU_FpuToMem((unsigned int) (pFlexRam + i));
        __DSB();
        __ISB();
    }
    //disable cache I et data D
    SCB_DisableICache();
    SCB_DisableDCache();
    __DSB();
    __ISB();
}
</#if>