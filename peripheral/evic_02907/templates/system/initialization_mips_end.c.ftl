<#-- Scan through all the interrupts.  If at least 1 is enabled, then enable the global interrupts -->
<#assign ANY_INT_ENABLED = "false">
<#list INT_VECTOR_MIN..INT_VECTOR_MAX as ii>
    <#lt><#assign INT_FIRST_NAME_KEY =  "INT_FIRST_NAME_KEY_" + ii?string >
    <#lt><#if .vars[INT_FIRST_NAME_KEY]?has_content>
        <#lt><#assign INT_FIRST_NAME = .vars[INT_FIRST_NAME_KEY]>
        <#lt><#assign INT_VECTOR   = "_" + INT_FIRST_NAME + "_VECTOR">
        <#lt><#assign INT_ENABLE   = "NVIC_" + INT_FIRST_NAME + "_0_ENABLE">
        <#lt><#assign INT_PRIORITY = INT_FIRST_NAME + "_PRIORITY">
        <#lt><#assign INT_SUBPRIORITY = INT_FIRST_NAME + "_SUBPRIORITY">
        <#lt><#assign INT_HANDLER  = "NVIC_" + INT_FIRST_NAME + "_0_HANDLER">
        <#lt><#if .vars[INT_ENABLE]?c =="true">
            <#lt><#assign ANY_INT_ENABLED = "true">
        <#lt></#if>
    <#lt></#if>
</#list>
<#if ANY_INT_ENABLED == "true">
    <#-- enable global interrupts -->
    __builtin_enable_interrupts();
</#if>