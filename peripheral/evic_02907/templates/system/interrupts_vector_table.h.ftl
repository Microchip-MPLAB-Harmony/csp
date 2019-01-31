<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#lt><#assign INT_VECTOR = "EVIC_" + i + "_VECTOR">
    <#lt><#assign INTERRUT_HANDLER = "EVIC_" + i + "_INTERRUPT_HANDLER">
    <#lt><#assign INT_HANDLER  = "EVIC_" + i + "_HANDLER">
    <#lt><#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_HANDLER_LOCK">
    <#lt><#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
    <#lt><#assign INT_PRIORITY = "EVIC_" + i + "_PRIORITY">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
    <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}AUTO) ${.vars[INT_HANDLER]} (void)
    <#lt>{
        <#if .vars[INT_HANDLER_LOCK] == true>
    <#lt>    ${.vars[INTERRUT_HANDLER]}();
        </#if>
    <#lt>}

    </#if>
</#list>
