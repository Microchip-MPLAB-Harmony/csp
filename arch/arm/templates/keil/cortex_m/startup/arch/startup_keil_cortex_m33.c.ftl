__STATIC_INLINE void FPU_Enable(void);

#if (__FPU_USED == 1)

/* Enable FPU */
__STATIC_INLINE void FPU_Enable(void)
{
    uint32_t primask = __get_PRIMASK();
    __disable_irq();
    SCB->CPACR |= (((uint32_t)0xFU) << 20);
    __DSB();
    __ISB();

    if (primask == 0U)
    {
        __enable_irq();
    }
}
#endif /* (__FPU_USED == 1) */
