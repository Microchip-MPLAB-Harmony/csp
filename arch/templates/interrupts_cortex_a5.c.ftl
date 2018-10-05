/* Brief default interrupt handler for unused IRQs.*/
#if defined(__XC32)
void __attribute__((optimize("-O1"),section(".text.DefaultInterruptHandler"),long_call))AIC_DefaultHandler( void )
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
    while( 1 ){
    }
}

void __attribute__((optimize("-O1"),section(".text.DefaultInterruptHandlerForSpurious"),long_call))AIC_DefaultHandlerForSpurious( void )
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
    while( 1 ){
    }
}
#else
void DefaultInterruptHandler( void )
{
    while( 1 ){
    }
}

void DefaultInterruptHandlerForSpurious( void )
{
    while( 1 ){
    }
}
#endif

${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}
${LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS}