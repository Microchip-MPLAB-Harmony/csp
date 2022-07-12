<#if NUM_SHARED_VECTORS??>
/* Handlers for vectors that are shared by multiple interrupts */
    <#list 0..(NUM_SHARED_VECTORS - 1) as ii>
        <#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii>
        <#assign NUM_SHARES_REF = .vars[SHARED_VECTOR_NAME] + "_NUM_SHARES">
        <#assign NUM_SHARES = .vars[NUM_SHARES_REF]>
        <#assign DEF_DONE = false>
        <#list 0..(NUM_SHARES - 1) as jj>
            <#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ] + "_SHARE_" + jj>
            <#if .vars[SHARE_NAME_REF]??>
                <#assign SHARE_NAME = .vars[SHARE_NAME_REF]>
                <#assign AIC_ENABLE =   SHARE_NAME + "_INTERRUPT_ENABLE">
                <#if .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
                    <#if !DEF_DONE>
void ${.vars[ SHARED_VECTOR_NAME ]}_SharedHandler( void )
{
                    <#assign DEF_DONE = true>
                    </#if>
                    <#assign AIC_HANDLER =  SHARE_NAME + "_INTERRUPT_HANDLER">
    ${.vars[AIC_HANDLER]}();
                </#if>
            </#if>
        </#list>
        <#if DEF_DONE>
}
        </#if>
    </#list>
</#if>