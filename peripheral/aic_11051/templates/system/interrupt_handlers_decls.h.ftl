<#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as index>
    <#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + index>
    <#if .vars[AIC_FIRST_NAME_KEY]?? && .vars[AIC_FIRST_NAME_KEY] != "">
        <#assign INTERRUPT_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#assign INTERRUPT_ENABLE = .vars[INTERRUPT_NAME + "_INTERRUPT_ENABLE"]>
        <#if INTERRUPT_ENABLE>
            <#assign INTERRUPT_HANDLER = .vars[INTERRUPT_NAME + "_INTERRUPT_HANDLER"]>
void ${INTERRUPT_HANDLER} (void);
        </#if>
    </#if>
</#list>

<#if NUM_SHARED_VECTORS??>
    <#list 0..(NUM_SHARED_VECTORS - 1) as ii>
        <#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
        <#assign NUM_SHARES_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_NUM_SHARES">
        <#assign NUM_SHARES = .vars[ NUM_SHARES_REF ]>
        <#list 0..(NUM_SHARES - 1) as jj>
            <#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
            <#if .vars[SHARE_NAME_REF]?? >
                <#assign SHARE_NAME = .vars[ SHARE_NAME_REF ]>
                <#assign AIC_ENABLE =   SHARE_NAME + "_INTERRUPT_ENABLE">
                <#assign AIC_HANDLER =  SHARE_NAME + "_INTERRUPT_HANDLER">
                <#if .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
void ${.vars[AIC_HANDLER]} (void);
                </#if>
            </#if>
        </#list>
    </#list>
</#if>

/* Interrupt Handler for spurious interrupts */
void SPURIOUS_INTERRUPT_Handler (void);