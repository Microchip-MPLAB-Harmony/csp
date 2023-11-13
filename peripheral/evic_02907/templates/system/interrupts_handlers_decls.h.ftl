<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INTERRUT_HANDLER = "EVIC_" + i + "_INTERRUPT_HANDLER">
    <#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_HANDLER_LOCK">
    <#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
    <#assign INT_ENABLE_GENERATE = "EVIC_" + i + "_ENABLE_GENERATE">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true && .vars[INT_HANDLER_LOCK] == true>
        <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
            <#lt>void ${.vars[INTERRUT_HANDLER]}( void );
        </#if>
    </#if>
</#list>
