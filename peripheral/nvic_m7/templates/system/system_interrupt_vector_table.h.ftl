<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#assign NVIC_VECTOR = "NVIC_" + i + "_VECTOR">
    <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_HANDLER">
    <#if .vars[NVIC_VECTOR]?has_content>
        <#assign NVIC_VECTOR_NAME_HANDLER = .vars[NVIC_VECTOR] + "_Handler">
        <#if (.vars[NVIC_VECTOR] != "None")>
  .pfn${NVIC_VECTOR_NAME_HANDLER?right_pad(26)} = (void*)${.vars[NVIC_VECTOR_HANDLER]},
        </#if>
    </#if>
</#list>