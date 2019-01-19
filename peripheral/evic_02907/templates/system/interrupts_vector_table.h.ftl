<#list INT_VECTOR_MIN..INT_VECTOR_MAX as ii>
    <#lt><#assign INT_FIRST_NAME_KEY =  "INT_FIRST_NAME_KEY_" + ii?string >
    <#lt><#if .vars[INT_FIRST_NAME_KEY]?has_content>
        <#lt><#assign INT_FIRST_NAME = .vars[INT_FIRST_NAME_KEY]>
        <#lt><#assign INT_NAME = "INT_FIRST_NAME_STRING_" + ii?string>
        <#lt><#assign FINAL_VECTOR_NAME = "_" + .vars[INT_NAME] + "_VECTOR">
        <#lt><#assign INT_HANDLER  = "NVIC_" + INT_FIRST_NAME + "_0_HANDLER">
        <#lt><#assign INT_ENABLE = "NVIC_" + ii?string + "_0_ENABLE">
        <#lt><#assign INT_PRIORITY = "NVIC_" + ii?string + "_0_PRIORITY">
        <#if .vars[INT_ENABLE]?c == "true">
        <#lt>void __ISR(${FINAL_VECTOR_NAME}, ipl${.vars[INT_PRIORITY]}AUTO) ${.vars[INT_HANDLER]} (void)
        <#lt>{
        <#lt>   ${.vars[INT_NAME]}_Tasks();
        <#lt>}
        </#if>
    <#lt></#if>
</#list>
