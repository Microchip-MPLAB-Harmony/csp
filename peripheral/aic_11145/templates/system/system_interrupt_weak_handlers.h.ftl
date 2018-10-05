/*  Refer to INT_Initialize() method to see which handlers are active */
/*  Weak definitions for default handlers.  Users may override these with
    implementations of their own or provide alternate functions to the 
    interrupt controller.  PLIB implementations provide alternate functions, 
    with the name {periph}_InterruptHandler so as they will not collide with
    user {periph}_Handler definitions.
*/
<#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#assign AIC_VECTOR = AIC_FIRST_NAME + "_INTERRUPT_VECTOR">
        <#assign AIC_HANDLER = AIC_FIRST_NAME + "_Handler( void )">
        <#if .vars[AIC_VECTOR]?has_content>
            <#if (.vars[AIC_VECTOR] != "None")>
void ${AIC_HANDLER?right_pad(36)}__attribute__((weak, alias("DefaultInterruptHandler")));
            </#if>
        </#if>
    </#if>
</#list>