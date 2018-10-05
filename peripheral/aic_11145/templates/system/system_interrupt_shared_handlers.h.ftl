<#if NUM_SHARED_VECTORS?? >
/* Weak definitions for sub-handlers in vectors shared by multiple interrupts */
<#list 0..(NUM_SHARED_VECTORS - 1) as ii>
<#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
<#assign NUM_SHARES_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_NUM_SHARES">
<#assign NUM_SHARES = .vars[ NUM_SHARES_REF ]>
<#list 0..(NUM_SHARES - 1) as jj>
<#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
<#if .vars[SHARE_NAME_REF]?? >
<#assign AIC_HANDLER_REF = .vars[ SHARE_NAME_REF ] + "_INTERRUPT_HANDLER">
<#assign AIC_HANDLER = .vars[SHARE_NAME_REF] + "_Handler( void )">
void ${AIC_HANDLER?right_pad(36)}__attribute__((weak, alias("DefaultInterruptHandler")));
</#if>
</#list>
</#list>
</#if>

<#if NUM_SHARED_VECTORS?? >
/* Handlers for vectors that are shared by multiple interrupts */
<#list 0..(NUM_SHARED_VECTORS - 1) as ii>
<#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
<#assign NUM_SHARES_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_NUM_SHARES">
<#assign NUM_SHARES = .vars[ NUM_SHARES_REF ]>
void
${.vars[ SHARED_VECTOR_NAME ]}_SharedHandler( void )
{
<#list 0..(NUM_SHARES - 1) as jj>
<#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
<#if .vars[SHARE_NAME_REF]?? >
<#assign SHARE_NAME = .vars[ SHARE_NAME_REF ]>
<#assign AIC_ENABLE =   SHARE_NAME + "_INTERRUPT_ENABLE">
<#assign AIC_HANDLER =  SHARE_NAME + "_INTERRUPT_HANDLER">
<#if .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
    ${.vars[AIC_HANDLER]}();
</#if>
</#if>
</#list>
}
</#list>
 </#if>
