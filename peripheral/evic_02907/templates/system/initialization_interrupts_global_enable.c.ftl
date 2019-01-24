<#-- Scan through all the interrupts.  If at least 1 is enabled, then enable the global interrupts -->
<#assign ANY_INT_ENABLED = false>
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#lt><#assign INT_ENABLE   = "EVIC_" + i + "_ENABLE">
    <#lt><#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
        <#lt><#assign ANY_INT_ENABLED = true>
    <#lt></#if>
</#list>
<#if ANY_INT_ENABLED == true>
    <#-- enable global interrupts -->
	/* Enable global interrupts */
    __builtin_enable_interrupts();
</#if>