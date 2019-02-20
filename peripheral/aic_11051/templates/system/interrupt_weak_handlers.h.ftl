/*  Weak definitions for default handlers.  Users may override these with
    implementations of their own or provide alternate functions to the 
    interrupt controller.  PLIB implementations provide alternate functions, 
    with the name {periph}_InterruptHandler so as they will not collide with
    user {periph}_Handler definitions.
*/
<#lt><#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#lt><#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#lt><#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#lt><#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#lt><#assign AIC_VECTOR = AIC_FIRST_NAME + "_INTERRUPT_VECTOR">
        <#lt><#assign AIC_HANDLER = AIC_FIRST_NAME + "_Handler( void )">
        <#lt><#if .vars[AIC_VECTOR]?has_content>
            <#lt><#if (.vars[AIC_VECTOR] != "None")>
                <#lt>void ${AIC_HANDLER?right_pad(36)}__attribute__((weak, alias("DefaultInterruptHandler")));
            <#lt></#if>
        <#lt></#if>
    <#lt></#if>
<#lt></#list>