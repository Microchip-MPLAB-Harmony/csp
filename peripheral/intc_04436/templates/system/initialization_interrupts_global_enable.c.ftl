<#-- Scan through all the interrupts.  If at least 1 is enabled, then enable the global interrupts -->
<#assign ANY_INT_ENABLED = false>
<#list INTC_VECTOR_MIN..INTC_VECTOR_MAX as i>
    <#lt><#assign INT_ENABLE   = "INTC_" + i + "_ENABLE">
    <#lt><#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
        <#lt><#assign ANY_INT_ENABLED = true>
    <#lt></#if>
</#list>
<#if ANY_INT_ENABLED == true>
    <#-- enable global interrupts -->
	/* Enable global interrupts */
    __builtin_enable_interrupts();
</#if>