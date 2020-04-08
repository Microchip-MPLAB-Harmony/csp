<#if TCM_ENABLE>
__STATIC_INLINE void TCM_Enable(void);
<#else>
__STATIC_INLINE void TCM_Disable(void);
</#if>
__STATIC_INLINE void TCM_Configure(uint32_t tcmSize);
__STATIC_INLINE void ICache_Enable(void);
<#if DATA_CACHE_ENABLE??>
<#if (DATA_CACHE_ENABLE)>
__STATIC_INLINE void DCache_Enable(void);
</#if>
</#if>
#if (__FPU_USED == 1)
__STATIC_INLINE void FPU_Enable(void);
#endif //__FPU_USED

/* Enable Instruction Cache */
__STATIC_INLINE void ICache_Enable(void)
{
    SCB_EnableICache();
}

<#if DATA_CACHE_ENABLE??>
<#if (DATA_CACHE_ENABLE)>
/* Enable Data Cache */
__STATIC_INLINE void DCache_Enable(void)
{
    SCB_EnableDCache();
}
</#if>
</#if>

#if (__FPU_USED == 1)

/* Enable FPU */
__STATIC_INLINE void FPU_Enable(void)
{
    uint32_t prim;
    prim = __get_PRIMASK();
    __disable_irq();

     SCB->CPACR |= (0xFu << 20);
    __DSB();
    __ISB();

    if (!prim)
    {
        __enable_irq();
    }
}
#endif /* (__FPU_USED == 1) */
