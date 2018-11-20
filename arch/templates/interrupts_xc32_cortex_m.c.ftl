extern uint32_t _stack;

/* Brief default interrupt handler for unused IRQs.*/
void __attribute__((optimize("-O1"),section(".text.Dummy_Handler"),long_call))Dummy_Handler(void)
{
<#if CoreArchitecture != "CORTEX-M0PLUS">
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
</#if>
    while (1)
    {
    }
}

/* Device vectors list dummy definition*/
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}

/* Mutiple handlers for vector */
${LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS}

__attribute__ ((section(".vectors")))
const DeviceVectors exception_table=
{
  /* Configure Initial Stack Pointer, using linker-generated symbols */
  .pvStack = (void*) (&_stack),

${LIST_SYSTEM_INTERRUPT_HANDLERS}
};
