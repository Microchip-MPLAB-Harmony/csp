/* Brief default interrupt handler for unused IRQs */
<#lt><#if "XC32" == COMPILER_CHOICE>
    <#lt>void __attribute__((optimize("-O1"),section(".text.DefaultInterruptHandler"),long_call))DefaultInterruptHandler( void )
    <#lt>{
        <#lt>#if defined(__DEBUG) || defined(__DEBUG_D)
        <#lt>    __builtin_software_breakpoint();
        <#lt>#endif
    <#lt>    while( 1 ){
    <#lt>    }
    <#lt>}
    <#lt>
    <#lt>void __attribute__((optimize("-O1"),section(".text.DefaultInterruptHandlerForSpurious"),long_call))DefaultInterruptHandlerForSpurious( void )
    <#lt>{
        <#lt>#if defined(__DEBUG) || defined(__DEBUG_D)
        <#lt>    __builtin_software_breakpoint();
        <#lt>#endif
    <#lt>    while( 1 ){
    <#lt>    }
    <#lt>}
    <#lt>
<#lt><#elseif "IAR" == COMPILER_CHOICE>
    <#lt>void DefaultInterruptHandler( void )
    <#lt>{
    <#lt>    while( 1 ){
    <#lt>    }
    <#lt>}
    <#lt>
    <#lt>uint32_t spuriousEventCount = 0;
    <#lt>void DefaultInterruptHandlerForSpurious( void )
    <#lt>{
    <#lt>    ++spuriousEventCount;
    <#lt>}
    <#lt>
<#lt></#if>
<#lt><#if AIC_CODE_GENERATION != "NONE" >
${LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS}
${LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS}
<#lt></#if>
