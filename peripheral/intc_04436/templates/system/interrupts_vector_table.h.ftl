<#assign FREERTOS_ENABLED = ((HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS") || ((FreeRTOS.SET_RTOS)?? && FreeRTOS.SET_RTOS == "FreeRTOS")>
<#assign ANY_INTERRUPT_ENABLED = false>
// Section: System Interrupt Vector declarations
<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#assign INT_ENABLE = "INTC_" + i + "_ENABLE">
    <#assign INT_HANDLER  = "INTC_" + i + "_HANDLER">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
	  <#if !((FREERTOS_ENABLED) && (.vars[INT_HANDLER] == "T1Interrupt"))>
      <#assign ANY_INTERRUPT_ENABLED = true>
      </#if>
    </#if>
</#list>

<#if ANY_INTERRUPT_ENABLED == true>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"

/* Following MISRA-C rules are deviated in the below code block */
/* MISRA C-2012 Rule 21.2 - Deviation record ID - H3_MISRAC_2012_R_21_2_DR_1 */
#pragma coverity compliance block deviate "MISRA C-2012 Rule 21.2"  "H3_MISRAC_2012_R_21_2_DR_1"
</#if>

<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#assign INT_ENABLE = "INTC_" + i + "_ENABLE">
    <#assign INT_HANDLER  = "INTC_" + i + "_HANDLER">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
	  <#if !((FREERTOS_ENABLED) && (.vars[INT_HANDLER] == "T1Interrupt"))>
      <#assign ANY_INTERRUPT_ENABLED = true>
void _${.vars[INT_HANDLER]} (void);
      </#if>
    </#if>
</#list>

// Section: System Interrupt Vector definitions

<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#assign INTERRUPT_HANDLER = "INTC_" + i + "_INTERRUPT_HANDLER">
    <#assign INT_HANDLER  = "INTC_" + i + "_HANDLER">
    <#assign INT_HANDLER_LOCK  = "INTC_" + i + "_HANDLER_LOCK">
    <#assign INT_ENABLE = "INTC_" + i + "_ENABLE">
    <#assign INT_CONTEXT = "INTC_" + i + "_ENABLE_CONTEXT">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
    <#if !((FREERTOS_ENABLED) && (.vars[INT_HANDLER] == "T1Interrupt"))>
    <#if .vars[INT_CONTEXT] == true >
        <#lt>void __attribute__ (( interrupt, no_auto_psv, context)) _${.vars[INT_HANDLER]} (void)
    <#else>
        <#lt>void __attribute__ (( interrupt, no_auto_psv)) _${.vars[INT_HANDLER]} (void)
    </#if>
        <#lt>{
        <#if .vars[INT_HANDLER_LOCK] == true>
            <#lt>    ${.vars[INTERRUPT_HANDLER]}();
        </#if>
        <#lt>}

    </#if>
    </#if>
</#list>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
</#if>
</#if>
