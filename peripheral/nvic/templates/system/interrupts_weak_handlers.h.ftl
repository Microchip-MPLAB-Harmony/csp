<#assign dummyHandlers = [] />
<#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
    <#assign NVIC_COMMON_ENABLE = false>
    <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
    <#assign NVIC_VECTOR_GENERIC_HANDLER = "NVIC_" + i + "_" + "0_GENERIC_HANDLER">
    <#if .vars[NVIC_NEXT_VECTOR]?has_content && (.vars[NVIC_NEXT_VECTOR] != "None")>
        <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
            <#if .vars[NVIC_VECTOR_ENABLE]?has_content && (.vars[NVIC_VECTOR_ENABLE] != false)>
                <#assign NVIC_COMMON_ENABLE = true>
                <#break>
            </#if>
        </#list>
        <#if NVIC_COMMON_ENABLE == false>
        <#if COMPILER_CHOICE == "XC32">
void ${.vars[NVIC_VECTOR_GENERIC_HANDLER]?right_pad(26)} ( void ) __attribute__((weak, alias("Dummy_Handler")));
        <#elseif COMPILER_CHOICE == "IAR">
void ${.vars[NVIC_VECTOR_GENERIC_HANDLER]} ( void );
#pragma weak ${.vars[NVIC_VECTOR_GENERIC_HANDLER]}=Dummy_Handler
        </#if>
        <#else>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR = "NVIC_" + i + "_" + j + "_VECTOR">
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if .vars[NVIC_VECTOR]?has_content && (.vars[NVIC_VECTOR] != "None")>
                <#if COMPILER_CHOICE == "XC32">
void ${.vars[NVIC_VECTOR_HANDLER]?right_pad(26)} ( void ) __attribute__((weak, alias("Dummy_Handler")));
                <#elseif COMPILER_CHOICE == "IAR">
void ${.vars[NVIC_VECTOR_HANDLER]} ( void );
#pragma weak ${.vars[NVIC_VECTOR_HANDLER]}=Dummy_Handler
                </#if>
                </#if>
            </#list>
        </#if>
    <#else>
        <#assign NVIC_VECTOR = "NVIC_" + i + "_"  + "0_VECTOR">
        <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + "0_ENABLE">
        <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + "0_HANDLER">
        <#if .vars[NVIC_VECTOR]?has_content && (.vars[NVIC_VECTOR] != "None")>
            <#assign handler = .vars[NVIC_VECTOR_HANDLER]>
            <#if !dummyHandlers?seq_contains(handler)>
                <#assign dummyHandlers = dummyHandlers + [handler] />
                <#if COMPILER_CHOICE == "XC32">
void ${.vars[NVIC_VECTOR_HANDLER]?right_pad(26)} ( void ) __attribute__((weak, alias("Dummy_Handler")));
                <#elseif COMPILER_CHOICE == "IAR">
void ${.vars[NVIC_VECTOR_HANDLER]} ( void );
#pragma weak ${.vars[NVIC_VECTOR_HANDLER]}=Dummy_Handler
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
