<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#assign NVIC_VECTOR = "NVIC_" + i + "_VECTOR">
    <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_HANDLER">
    <#if .vars[NVIC_VECTOR]?has_content>
        <#if (.vars[NVIC_VECTOR] != "None")>
void ${.vars[NVIC_VECTOR_HANDLER]?right_pad(26)} ( void ) __attribute__((weak, alias("Dummy_Handler")));
        </#if>
    </#if>
</#list>