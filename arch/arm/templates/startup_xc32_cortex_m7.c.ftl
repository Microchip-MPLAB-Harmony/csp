__STATIC_INLINE void TCM_Disable(void);
__STATIC_INLINE void TCM_Enable(void);
__STATIC_INLINE void TCM_ConfigureSize(void);
__STATIC_INLINE void ICache_Enable(void);
__STATIC_INLINE void DCache_Enable(void);

/** \brief  Instruction cache enable

 The function enables instruction caching.
 */
__STATIC_INLINE void ICache_Enable(void)
{
    SCB_EnableICache();
}

/** \brief  Data cache enable

 The function enables data caching.
 */
__STATIC_INLINE void DCache_Enable(void)
{
    SCB_EnableDCache();
}

#if (__ARM_FP==14) || (__ARM_FP==4)

__always_inline __STATIC_INLINE void __attribute__((optimize("-O1"))) fpu_enable(void)
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
#endif /* (__ARM_FP==14) || (__ARM_FP==4) */


