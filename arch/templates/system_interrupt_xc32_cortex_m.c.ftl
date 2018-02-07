extern uint32_t _stack;

/* Brief default interrupt handler for unused IRQs.*/
void __attribute__((optimize("-O1"),section(".text.Dummy_Handler"),long_call))Dummy_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D)
    __builtin_software_breakpoint();
#endif
    while (1)
    {
    }
}

/* Cortex-M core handlers */
void NonMaskableInt_Handler     ( void ) __attribute__((weak, alias("Dummy_Handler")));
void HardFault_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
<#if (CoreArchitecture == "CORTEX-M4") || (CoreArchitecture == "CORTEX-M7")>
void MemoryManagement_Handler   ( void ) __attribute__((weak, alias("Dummy_Handler")));
void BusFault_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void UsageFault_Handler         ( void ) __attribute__((weak, alias("Dummy_Handler")));
</#if>
void SVCall_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
<#if (CoreArchitecture == "CORTEX-M4") || (CoreArchitecture == "CORTEX-M7")>
void DebugMonitor_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
</#if>
void PendSV_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));

/* Peripheral handlers */
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}

__attribute__ ((section(".vectors")))
const DeviceVectors exception_table=
{
  /* Configure Initial Stack Pointer, using linker-generated symbols */
  .pvStack = (void*) (&_stack),

<#if CoreUseCustomVector == true>
  .pfnReset_Handler              = (void*) ${CustomVectorName},
<#else>
  .pfnReset_Handler              = (void*) Reset_Handler,
</#if>
  .pfnNonMaskableInt_Handler     = (void*) NonMaskableInt_Handler,
  .pfnHardFault_Handler          = (void*) HardFault_Handler,
<#if CoreArchitecture == "CORTEX-M0PLUS">
  .pvReservedC12                 = (void*) (0UL), /* Reserved */
  .pvReservedC11                 = (void*) (0UL), /* Reserved */
  .pvReservedC10                 = (void*) (0UL), /* Reserved */
  .pvReservedC4                  = (void*) (0UL), /* Reserved */
</#if>
<#if (CoreArchitecture == "CORTEX-M4") || (CoreArchitecture == "CORTEX-M7")>
  .pfnMemoryManagement_Handler   = (void*) MemoryManagement_Handler,
  .pfnBusFault_Handler           = (void*) BusFault_Handler,
  .pfnUsageFault_Handler         = (void*) UsageFault_Handler,
  .pfnDebugMonitor_Handler       = (void*) DebugMonitor_Handler,
</#if>
  .pvReservedC9                  = (void*) (0UL), /* Reserved */
  .pvReservedC8                  = (void*) (0UL), /* Reserved */
  .pvReservedC7                  = (void*) (0UL), /* Reserved */
  .pvReservedC6                  = (void*) (0UL), /* Reserved */
  .pfnSVCall_Handler             = (void*) SVCall_Handler,
  .pvReservedC3                  = (void*) (0UL), /* Reserved */
  .pfnPendSV_Handler             = (void*) PendSV_Handler,

${LIST_SYSTEM_INTERRUPT_HANDLERS}
};