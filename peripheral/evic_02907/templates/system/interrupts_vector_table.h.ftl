<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INT_VECTOR = "EVIC_" + i + "_VECTOR">
    <#assign INTERRUT_HANDLER = "EVIC_" + i + "_INTERRUPT_HANDLER">
    <#assign INT_HANDLER  = "EVIC_" + i + "_HANDLER">
    <#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_HANDLER_LOCK">
    <#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
    <#assign INT_ENABLE_GENERATE = "EVIC_" + i + "_ENABLE_GENERATE">
    <#assign INT_PRIORITY = "EVIC_" + i + "_PRIORITY">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
        <#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS != "BareMetal">
            <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                <#lt>void ${.vars[INT_HANDLER]} (void)
                <#lt>{
                <#if .vars[INT_HANDLER_LOCK] == true>
                    <#lt>    ${.vars[INTERRUT_HANDLER]}();
                </#if>
                <#lt>}
            </#if>
        <#else>
            <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}AUTO) ${.vars[INT_HANDLER]} (void)
            <#lt>{
            <#if .vars[INT_HANDLER_LOCK] == true>
                <#lt>    ${.vars[INTERRUT_HANDLER]}();
            </#if>
            <#lt>}
        </#if>

    </#if>
</#list>
