
/** Program GPNVM fuse for TCM configuration */
__STATIC_INLINE void TCM_Configure(uint32_t neededGpnvmValue)
{
}

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
