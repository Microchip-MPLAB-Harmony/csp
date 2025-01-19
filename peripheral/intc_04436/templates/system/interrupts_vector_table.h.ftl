<#assign FREERTOS_ENABLED = ((HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS") || ((FreeRTOS.SET_RTOS)?? && FreeRTOS.SET_RTOS == "FreeRTOS")>
// Section: System Interrupt Vector declarations

<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#assign INT_ENABLE = "INTC_" + i + "_ENABLE">
    <#assign INT_HANDLER  = "INTC_" + i + "_HANDLER">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
	  <#if !((FREERTOS_ENABLED) && (.vars[INT_HANDLER] == "T1Interrupt"))>
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

