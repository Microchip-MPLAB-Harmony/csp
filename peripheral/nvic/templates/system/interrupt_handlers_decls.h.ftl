<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#compress>
    <#assign INTERRUPT_HANDLERS = "">
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + "0_SECURITY_TYPE">
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?? && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if (.vars[NVIC_VECTOR_NONSECURE]?? && (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE"))>
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains(.vars[NVIC_VECTOR_HANDLER]))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">
                </#if>
                </#if>
            </#list>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
            <#if (i < 0) || ((.vars[NVIC_VECTOR_NONSECURE])?? && (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE"))>
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains(.vars[NVIC_VECTOR_HANDLER]))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">
                </#if>
            </#if>
        </#if>
    </#list>
</#compress>
<#list INTERRUPT_HANDLERS?remove_ending(",")?split(",") as INTERRUPT_HANDLER>
void ${INTERRUPT_HANDLER} (void);
</#list>
<#else>
<#compress>
    <#assign INTERRUPT_HANDLERS = "">
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?? && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains(.vars[NVIC_VECTOR_HANDLER]))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">    
                </#if>
            </#list>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
                <#if !([-5,-2]?seq_contains(i)) && .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains(.vars[NVIC_VECTOR_HANDLER]))>
                <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + "," >
                </#if>
        </#if>
    </#list>
</#compress>
<#list INTERRUPT_HANDLERS?remove_ending(",")?split(",") as INTERRUPT_HANDLER>
void ${INTERRUPT_HANDLER} (void);
</#list>
</#if>