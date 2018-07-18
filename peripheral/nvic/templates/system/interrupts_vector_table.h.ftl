<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#assign NVIC_VECTOR_GENERIC_HANDLER = "NVIC_" + i + "_" + j + "_GENERIC_HANDLER">
        <#if .vars[NVIC_NEXT_VECTOR]?has_content>
            <#if (.vars[NVIC_NEXT_VECTOR] != "None")>
    .pfn${.vars[NVIC_VECTOR_GENERIC_HANDLER]?right_pad(26)} = ( void * ) ${.vars[NVIC_VECTOR_GENERIC_HANDLER]},
            <#break>
            </#if>
        <#else>
            <#assign NVIC_VECTOR = "NVIC_" + i + "_" + j + "_VECTOR">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
            <#if .vars[NVIC_VECTOR]?has_content>
                <#assign NVIC_VECTOR_NAME_HANDLER = .vars[NVIC_VECTOR] + "_Handler">
                <#if (.vars[NVIC_VECTOR] != "None")>
    .pfn${NVIC_VECTOR_NAME_HANDLER?right_pad(26)} = ( void * ) ${.vars[NVIC_VECTOR_HANDLER]},
                <#break>
                </#if>
            </#if>
        </#if>
    </#list>
</#list>