<#if COMPILER_CHOICE == "XC32">
extern uint32_t _stack;
extern const H3DeviceVectors exception_table;

extern void Dummy_Handler(void);

/* Brief default interrupt handler for unused IRQs.*/
void __attribute__((optimize("-O1"),section(".text.Dummy_Handler"),long_call, noreturn))Dummy_Handler(void)
{
<#if CoreArchitecture != "CORTEX-M0PLUS">
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
</#if>
    while (true)
    {
    }
}
<#elseif COMPILER_CHOICE == "KEIL">
extern const H3DeviceVectors exception_table;

extern void Dummy_Handler(void);

/* Brief default interrupt handler for unused IRQs.*/
void __attribute__((section(".text.Dummy_Handler")))Dummy_Handler(void)
{
    while (true)
    {
    }
}
<#elseif COMPILER_CHOICE == "IAR">
extern const H3DeviceVectors exception_table;

extern void Dummy_Handler(void);

#pragma section="CSTACK"

void Dummy_Handler( void )
{
    while(true)
    {

    }
}
</#if>
/* Device vectors list dummy definition*/
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}

/* Multiple handlers for vector */
${LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS}

<#if COMPILER_CHOICE == "XC32">
__attribute__ ((section(".vectors")))
<#elseif COMPILER_CHOICE == "IAR">
#pragma location = ".intvec"
<#elseif COMPILER_CHOICE == "KEIL">
extern uint32_t Image$$ARM_LIB_STACKHEAP$$ZI$$Limit;

__attribute__ ((section("RESET")))
</#if>
<#if COMPILER_CHOICE == "XC32">
const H3DeviceVectors exception_table=
{
    /* Configure Initial Stack Pointer, using linker-generated symbols */
    .pvStack = &_stack,
<#elseif COMPILER_CHOICE == "KEIL">
const H3DeviceVectors __Vectors=
{
    /* Configure Initial Stack Pointer, using linker-generated symbols */
    .pvStack = &Image$$ARM_LIB_STACKHEAP$$ZI$$Limit,
<#elseif COMPILER_CHOICE == "IAR">
__root const H3DeviceVectors __vector_table=
{
    /* Configure Initial Stack Pointer, using linker-generated symbols */
    .pvStack = __sfe( "CSTACK" ),
  </#if>

${LIST_SYSTEM_INTERRUPT_HANDLERS}
};
