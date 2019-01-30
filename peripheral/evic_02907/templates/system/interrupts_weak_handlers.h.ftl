<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#lt><#assign INT_VECTOR = "EVIC_" + i + "_VECTOR">
    <#lt><#assign INTERRUT_HANDLER = "EVIC_" + i + "_INTERRUPT_HANDLER">
    <#lt><#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_HANDLER_LOCK">
    <#lt><#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true && .vars[INT_HANDLER_LOCK] == true>
void ${.vars[INTERRUT_HANDLER]}( void );
    </#if>
</#list>
