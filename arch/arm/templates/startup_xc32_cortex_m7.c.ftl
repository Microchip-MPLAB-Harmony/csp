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
/* These functions are used only when compiling with -mfloat-abi=softfp or -mfloat-abi=hard */
/* Save and restore IRQs */
typedef uint32_t irqflags_t;
static bool g_interrupt_enabled;
#define cpu_irq_is_enabled()    (__get_PRIMASK() == 0)
#  define cpu_irq_enable()                             \
        do {                                           \
                g_interrupt_enabled = true;            \
                __DMB();                               \
                __enable_irq();                        \
        } while (0)
#  define cpu_irq_disable()                            \
        do {                                           \
                __disable_irq();                       \
                __DMB();                               \
                g_interrupt_enabled = false;           \
        } while (0)
__always_inline __STATIC_INLINE bool __attribute__((optimize("-O1"))) cpu_irq_is_enabled_flags(irqflags_t flags)
{
    return (flags);
}
__always_inline __STATIC_INLINE void __attribute__((optimize("-O1"))) cpu_irq_restore(irqflags_t flags)
{
    if (cpu_irq_is_enabled_flags(flags))
            cpu_irq_enable();
}
__always_inline __STATIC_INLINE __attribute__((optimize("-O1"))) irqflags_t cpu_irq_save(void)
{
    volatile irqflags_t flags = cpu_irq_is_enabled();
    cpu_irq_disable();
    return flags;
}

///** Address for ARM CPACR */
//#define ADDR_CPACR 0xE000ED88
///** CPACR Register */
//#define REG_CPACR  (*((volatile uint32_t *)ADDR_CPACR))

/**
* \brief Enable FPU
*/
__always_inline __STATIC_INLINE void __attribute__((optimize("-O1"))) fpu_enable(void)
{
    irqflags_t flags;
    flags = cpu_irq_save();
//    REG_CPACR |=  (0xFu << 20);
    SCB->CPACR |= (0xFu << 20);
    __DSB();
    __ISB();
    cpu_irq_restore(flags);
}
#endif /* (__ARM_FP==14) || (__ARM_FP==4) */


