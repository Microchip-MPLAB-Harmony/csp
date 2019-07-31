<#-- Scan through all the interrupts.  If at least 1 is enabled, then enable the global interrupts -->
<#assign ANY_INT_ENABLED = false>
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INT_VECTOR_SUB_IRQ_COUNT = "EVIC_" + i + "_VECTOR_SUB_IRQ_COUNT">
    <#if .vars[INT_VECTOR_SUB_IRQ_COUNT]?? && ((.vars[INT_VECTOR_SUB_IRQ_COUNT] > 1) == true)>
        <#list 0..(.vars[INT_VECTOR_SUB_IRQ_COUNT]) as j>
            <#assign INT_ENABLE = "EVIC_" + i + "_" + j + "_ENABLE">
            <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
                <#assign ANY_INT_ENABLED = true>
                <#break>
            </#if>
        </#list>
    <#else>
        <#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
        <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
            <#assign ANY_INT_ENABLED = true>
            <#break>
        </#if>
    </#if>
</#list>
<#if ANY_INT_ENABLED == true>
    <#-- enable global interrupts -->
    /* Enable global interrupts */
    __builtin_enable_interrupts();
</#if>