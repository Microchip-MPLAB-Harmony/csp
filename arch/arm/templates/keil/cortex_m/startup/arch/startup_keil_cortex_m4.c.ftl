__STATIC_INLINE void FPU_Enable(void);

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
