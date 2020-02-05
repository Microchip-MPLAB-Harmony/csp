<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#assign NVIC_VECTOR_GENERIC_HANDLER = "NVIC_" + i + "_" + j + "_GENERIC_HANDLER">
        <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + j + "_SECURITY_TYPE">
        <#assign coreHandlers = ["Reset_Handler", "NonMaskableInt_Handler", "HardFault_Handler", "SVCall_Handler", "PendSV_Handler", "SysTick_Handler"]>
        <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
        <#if (coreHandlers?seq_contains(.vars[NVIC_VECTOR_GENERIC_HANDLER])) || ((.vars[NVIC_VECTOR_NONSECURE])?? && (.vars[NVIC_VECTOR_NONSECURE] == "SECURE"))>
    .pfn${.vars[NVIC_VECTOR_GENERIC_HANDLER]?right_pad(26)} = ( void * ) ${.vars[NVIC_VECTOR_GENERIC_HANDLER]},
            <#break> 
        </#if>
        <#else>
            <#assign NVIC_VECTOR = "NVIC_" + i + "_" + j + "_VECTOR">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
            <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + j + "_SECURITY_TYPE">
            <#assign coreHandlers = ["Reset_Handler", "NonMaskableInt_Handler", "HardFault_Handler", "SVCall_Handler", "PendSV_Handler", "SysTick_Handler"]>
            <#if .vars[NVIC_VECTOR]?has_content && (.vars[NVIC_VECTOR] != "None")>
                <#assign NVIC_VECTOR_NAME_HANDLER = .vars[NVIC_VECTOR] + "_Handler">
            <#if (coreHandlers?seq_contains(.vars[NVIC_VECTOR_HANDLER])) || ((.vars[NVIC_VECTOR_NONSECURE])?? && (.vars[NVIC_VECTOR_NONSECURE] == "SECURE"))>
    .pfn${NVIC_VECTOR_NAME_HANDLER?right_pad(26)} = ( void * ) ${.vars[NVIC_VECTOR_HANDLER]},
                <#break>
            </#if>
            </#if>
        </#if>
    </#list>
</#list>
