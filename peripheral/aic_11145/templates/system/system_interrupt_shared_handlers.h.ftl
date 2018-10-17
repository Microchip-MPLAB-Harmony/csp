<#lt><#if NUM_SHARED_VECTORS?? >
    <#lt>/* Weak definitions for sub-handlers in vectors shared by multiple interrupts */
    <#lt><#list 0..(NUM_SHARED_VECTORS - 1) as ii>
        <#lt><#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
        <#lt><#assign NUM_SHARES_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_NUM_SHARES">
        <#lt><#assign NUM_SHARES = .vars[ NUM_SHARES_REF ]>
        <#lt><#list 0..(NUM_SHARES - 1) as jj>
            <#lt><#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
            <#lt><#if .vars[SHARE_NAME_REF]?? >
                <#lt><#assign AIC_HANDLER = .vars[SHARE_NAME_REF] + "_Handler( void )">
                <#lt>void ${AIC_HANDLER?right_pad(36)}__attribute__((weak, alias("DefaultInterruptHandler")));
            <#lt></#if>
        <#lt></#list>
    <#lt></#list>
<#lt></#if>

<#lt><#if NUM_SHARED_VECTORS?? >
    <#lt>/* Handlers for vectors that are shared by multiple interrupts */
    <#lt><#list 0..(NUM_SHARED_VECTORS - 1) as ii>
        <#lt><#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
        <#lt><#assign NUM_SHARES_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_NUM_SHARES">
        <#lt><#assign NUM_SHARES = .vars[ NUM_SHARES_REF ]>
        <#lt><#list 0..(NUM_SHARES - 1) as jj>
            <#lt><#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
            <#lt><#if .vars[SHARE_NAME_REF]?? >
                <#lt><#assign SHARE_NAME = .vars[ SHARE_NAME_REF ]>
                <#lt><#assign AIC_ENABLE =   SHARE_NAME + "_INTERRUPT_ENABLE">
                <#lt><#assign AIC_HANDLER =  SHARE_NAME + "_INTERRUPT_HANDLER">
                <#lt><#if .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
                    <#lt>void ${.vars[AIC_HANDLER]}( void );
                <#lt></#if>
            <#lt></#if>
        <#lt></#list>
        <#lt>void ${.vars[ SHARED_VECTOR_NAME ]}_SharedHandler( void )
        <#lt>{
        <#lt><#list 0..(NUM_SHARES - 1) as jj>
            <#lt><#assign SHARE_NAME_REF = .vars[ SHARED_VECTOR_NAME ]?string + "_SHARE_" + jj?string>
            <#lt><#if .vars[SHARE_NAME_REF]?? >
                <#lt><#assign SHARE_NAME = .vars[ SHARE_NAME_REF ]>
                <#lt><#assign AIC_ENABLE =   SHARE_NAME + "_INTERRUPT_ENABLE">
                <#lt><#assign AIC_HANDLER =  SHARE_NAME + "_INTERRUPT_HANDLER">
                <#lt><#if .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
                <#lt>    ${.vars[AIC_HANDLER]}();
                <#lt></#if>
            <#lt></#if>
        <#lt></#list>
        <#lt><#lt>}
    <#lt></#list>
<#lt></#if>

/* initialize table of interrupts to be installed */
<#lt><#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#lt><#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#lt><#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#lt><#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#lt><#assign AIC_HANDLER = AIC_FIRST_NAME + "_INTERRUPT_HANDLER">
        <#lt><#assign DEFAULT_VECTOR_NAME = AIC_FIRST_NAME + "_Handler">
        <#lt><#assign DEFAULT_SHARED_NAME = AIC_FIRST_NAME + "_SharedHandler">
        <#lt><#if !DEFAULT_VECTOR_NAME?matches(.vars[AIC_HANDLER])>        
            <#lt><#if !DEFAULT_SHARED_NAME?matches(.vars[AIC_HANDLER])>        
                <#lt><#assign PROTOTYPE = "void " + (.vars[AIC_HANDLER] + "(")?right_pad(36) + "void );">
                <#lt>${PROTOTYPE}
            <#lt></#if>
        <#lt></#if>
    <#lt></#if>
<#lt></#list>

IrqHandler irqHandlerTable[] = {
<#lt><#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#lt><#assign COMMENT = ii?item_cycle( ' // ' + ii, '', '', '', '')>
    <#lt><#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#lt><#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#lt><#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#lt><#assign AIC_HANDLER = AIC_FIRST_NAME + "_INTERRUPT_HANDLER">
        <#lt>    ${.vars[AIC_HANDLER]}<#sep>,</#sep><#if COMMENT?has_content>${COMMENT}</#if>
    <#lt><#else>
        <#lt>    (IrqHandler) NULL<#sep>,</#sep><#if COMMENT?has_content>${COMMENT}</#if>
    <#lt></#if>
<#lt></#list>
};