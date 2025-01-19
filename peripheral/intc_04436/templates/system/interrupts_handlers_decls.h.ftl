<#assign FREERTOS_ENABLED = ((HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS") || ((FreeRTOS.SET_RTOS)?? && FreeRTOS.SET_RTOS == "FreeRTOS")>
<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#assign INTERRUPT_HANDLER = "INTC_" + i + "_INTERRUPT_HANDLER">
    <#assign INT_HANDLER_LOCK  = "INTC_" + i + "_HANDLER_LOCK">
    <#assign INT_ENABLE = "INTC_" + i + "_ENABLE">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] && .vars[INT_HANDLER_LOCK] == true>
      <#if !((FREERTOS_ENABLED) && (.vars[INTERRUPT_HANDLER] == "T1_InterruptHandler"))>
            <#lt>void ${.vars[INTERRUPT_HANDLER]}( void );
      </#if>
    </#if>
</#list>
