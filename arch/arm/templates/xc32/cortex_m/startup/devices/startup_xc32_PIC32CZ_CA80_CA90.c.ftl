<#if RAM_INIT??>
#if defined ECC_INIT_START
#define START_ADDR  ECC_INIT_START
#else
#define START_ADDR  FLEXRAM_ADDR
#endif

#if defined ECC_INIT_LEN
#define INIT_LEN  ECC_INIT_LEN
#else
#define INIT_LEN  FLEXRAM_SIZE
#endif

__STATIC_INLINE void  __attribute__((optimize("-O1")))  RAM_Initialize(void)
{
    register uint64_t *pFlexRam;

    __DSB();
    __ISB();

    // FlexRAM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*)START_ADDR ; pFlexRam < ((uint64_t*)(START_ADDR + INIT_LEN)) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }

    // ITCM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*) ITCM_ADDR ; pFlexRam < (uint64_t*)(ITCM_ADDR + ITCM_SIZE) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }
    // DTCM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*) DTCM_ADDR ; pFlexRam < (uint64_t*)(DTCM_ADDR + DTCM_SIZE) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }

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
