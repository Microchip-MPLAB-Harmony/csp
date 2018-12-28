<#if COMPILER_CHOICE == "XC32">
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
<#elseif COMPILER_CHOICE == "IAR">
#pragma section="CSTACK"

void Dummy_Handler( void )
{
    while(1)
    {

    }
}
</#if>
/* Device vectors list dummy definition*/
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}

/* Mutiple handlers for vector */
${LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS}

<#if COMPILER_CHOICE == "XC32">
__attribute__ ((section(".vectors")))
<#elseif COMPILER_CHOICE == "IAR">
#pragma location = ".intvec"
</#if>
const DeviceVectors exception_table=
{<#if COMPILER_CHOICE == "XC32">
  /* Configure Initial Stack Pointer, using linker-generated symbols */
  .pvStack = (void*) (&_stack),
  <#elseif COMPILER_CHOICE == "IAR">
  .pvStack = __sfe( "CSTACK" ),
  </#if>

${LIST_SYSTEM_INTERRUPT_HANDLERS}
};
