<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
void ${.vars[NVIC_VECTOR_HANDLER]} (void);
                </#if>
            </#list>
            </#if>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
            <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + "0_SECURITY_TYPE">
            <#if (i < 0) || ((.vars[NVIC_VECTOR_NONSECURE])?? && (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE"))>
                <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
void ${.vars[NVIC_VECTOR_HANDLER]} (void);
                </#if>
            </#if>
        </#if>
</#list>
<#else>
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
void ${.vars[NVIC_VECTOR_HANDLER]} (void);
                </#if>
            </#list>
            </#if>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
                <#if (!([-5,-2]?seq_contains(i))) && (.vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false))>
void ${.vars[NVIC_VECTOR_HANDLER]} (void);
                </#if>
        </#if>
</#list>
</#if>