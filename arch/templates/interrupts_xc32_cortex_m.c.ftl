
<#assign WEAK_HANDLER_COUNT = LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS?split("extern")?size - 1>
<#if COMPILER_CHOICE == "XC32">
/* MISRA C-2012 Rule 8.6 deviated below. Deviation record ID -  H3_MISRAC_2012_R_8_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance deviate "MISRA C-2012 Rule 8.6" "H3_MISRAC_2012_R_8_6_DR_1"
</#if>
extern uint32_t _stack;
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic pop

</#if>
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

/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 8.6 deviated ${WEAK_HANDLER_COUNT} times.  Deviation record ID -  H3_MISRAC_2012_R_8_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance block deviate:${WEAK_HANDLER_COUNT} "MISRA C-2012 Rule 8.6" "H3_MISRAC_2012_R_8_6_DR_1"
</#if>
/* Device vectors list dummy definition*/
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 8.6"
</#if>
/* MISRAC 2012 deviation block end */

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
