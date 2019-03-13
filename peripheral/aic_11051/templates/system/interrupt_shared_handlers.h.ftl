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
<#lt><#if NUM_SHARED_VECTORS?? >
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
                    <#lt><#assign PROTOTYPE = "void " + (.vars[AIC_HANDLER] + "(")?right_pad(36) + "void );">
                    <#lt>${PROTOTYPE}
                <#lt></#if>
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

/* data for irq register initialization */
IrqData irqData[] = {
<#lt><#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#lt><#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#lt><#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#lt><#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#lt><#assign AIC_HANDLER = AIC_FIRST_NAME + "_INTERRUPT_HANDLER">
        <#lt><#assign AIC_ENABLE =  AIC_FIRST_NAME + "_INTERRUPT_ENABLE">
        <#lt><#if .vars[AIC_HANDLER]?? && .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
            <#lt><#assign AIC_MAP_TYPE = AIC_FIRST_NAME + "_INTERRUPT_MAP_TYPE">
            <#lt><#assign AIC_SRC_TYPE = AIC_FIRST_NAME + "_INTERRUPT_SRC_TYPE">
            <#lt><#assign AIC_PRIORITY = AIC_FIRST_NAME + "_INTERRUPT_PRIORITY">
            <#lt><#assign PERIPH_ID = (ii + ",")?right_pad(5)>
            <#lt><#if (.vars[AIC_MAP_TYPE]?string == "NonSecure") || (.vars[AIC_MAP_TYPE]?string == "NeverSecure") ||(.vars[AIC_MAP_TYPE]?string == "RedirectedToNonSecure")>
                <#lt><#assign REG_NAME_STR = "AIC">
            <#lt><#else>
                <#lt><#assign REG_NAME_STR = "SAIC">
            <#lt></#if>
            <#lt><#assign TARGET_REGISTERS_STR = ("(uint32_t) " + REG_NAME_STR + "_REGS,")?right_pad(24)>
            <#lt><#assign AIC_HANDLER_STR   = (.vars[AIC_HANDLER]  + ",")?right_pad(28) >
            <#lt><#assign AIC_SRC_TYPE_STR  = (REG_NAME_STR + "_SMR_SRCTYPE_"  + .vars[AIC_SRC_TYPE] + "_Val,")?right_pad(42) >
            <#lt><#if AIC_SMR_PRIORITY_SYMBOL?matches(".*PRIORITY.*")>
                <#lt><#assign AIC_PRIORITY_STR  = (REG_NAME_STR + "_SMR_PRIORITY_" + .vars[AIC_PRIORITY] + "_Val ")?right_pad(30) >
            <#lt><#else>
                <#lt><#assign AIC_PRIORITY_STR  = .vars[AIC_PRIORITY] >
            <#lt></#if>
            <#lt>    { ${PERIPH_ID}${TARGET_REGISTERS_STR}${AIC_HANDLER_STR}${AIC_SRC_TYPE_STR}${AIC_PRIORITY_STR} }<#sep>,</#sep>
        <#lt></#if>
    <#lt></#if>
<#lt></#list>
};

uint32_t irqDataEntryCount = sizeof( irqData ) / sizeof( irqData[ 0 ]);
