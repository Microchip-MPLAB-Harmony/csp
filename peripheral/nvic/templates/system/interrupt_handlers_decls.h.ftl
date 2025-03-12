<#assign BARE_METAL = ((!((HarmonyCore.SELECT_RTOS)??)) || HarmonyCore.SELECT_RTOS == "BareMetal")>
<#assign FREERTOS = (((HarmonyCore.SELECT_RTOS)??) && HarmonyCore.SELECT_RTOS == "FreeRTOS")>
<#assign THREADX = (((HarmonyCore.SELECT_RTOS)??) && HarmonyCore.SELECT_RTOS == "ThreadX")>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#compress>
    <#assign INTERRUPT_HANDLERS = ",">
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_VECTOR_NONSECURE = "NVIC_" + i + "_" + "0_SECURITY_TYPE">
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?? && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if (.vars[NVIC_VECTOR_NONSECURE]?? && (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE"))>
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains("," + .vars[NVIC_VECTOR_HANDLER] +","))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">
                </#if>
                </#if>
            </#list>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
            <#if (i < 0) || ((.vars[NVIC_VECTOR_NONSECURE])?? && (.vars[NVIC_VECTOR_NONSECURE] == "NON-SECURE"))>
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains("," + .vars[NVIC_VECTOR_HANDLER] +","))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">
                </#if>
            </#if>
        </#if>
    </#list>
</#compress>
<#list INTERRUPT_HANDLERS?remove_beginning(",")?remove_ending(",")?split(",") as INTERRUPT_HANDLER>
void ${INTERRUPT_HANDLER} (void);
</#list>
<#else>
<#compress>
    <#assign INTERRUPT_HANDLERS = ",">
    <#list NVIC_VECTOR_MIN..NVIC_VECTOR_MAX as i>
        <#assign NVIC_COMMON_ENABLE = false>
        <#assign NVIC_NEXT_VECTOR = "NVIC_" + i + "_1_VECTOR">
        <#if .vars[NVIC_NEXT_VECTOR]?? && (.vars[NVIC_NEXT_VECTOR] != "None")>
            <#list 0..NVIC_VECTOR_MAX_MULTIPLE_HANDLERS as j>
                <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_" + j + "_ENABLE">
                <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_" + j + "_HANDLER">
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains("," + .vars[NVIC_VECTOR_HANDLER] +","))>
                    <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + ",">
                </#if>
            </#list>
        <#else>
            <#assign NVIC_VECTOR_ENABLE = "NVIC_" + i + "_0_ENABLE">
            <#assign NVIC_VECTOR_HANDLER = "NVIC_" + i + "_0_HANDLER">
                <#if .vars[NVIC_VECTOR_ENABLE]?? && .vars[NVIC_VECTOR_ENABLE] && !(INTERRUPT_HANDLERS?contains("," + .vars[NVIC_VECTOR_HANDLER] +","))>
                <#if !([-5, -2]?seq_contains(i) && (CoreArchitecture?matches("CORTEX-M[2|3]3") || (CoreArchitecture == "CORTEX-M0PLUS" && FREERTOS) || BARE_METAL))>
                <#assign INTERRUPT_HANDLERS = INTERRUPT_HANDLERS + .vars[NVIC_VECTOR_HANDLER] + "," >
                </#if>
                </#if>
        </#if>
    </#list>
</#compress>
<#if THREADX>
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.2 deviated 3 times. Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_1 */
/* MISRA C-2012 Rule 8.6 deviated 3 times.  Deviation record ID -  H3_MISRAC_2012_R_8_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block \
(deviate:3 "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_1")\
(deviate:3 "MISRA C-2012 Rule 8.6" "H3_MISRAC_2012_R_8_6_DR_1")
</#if>
</#if>
<#list INTERRUPT_HANDLERS?remove_beginning(",")?remove_ending(",")?split(",") as INTERRUPT_HANDLER>
void ${INTERRUPT_HANDLER} (void);
</#list>
<#if THREADX>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 8.6"
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
#pragma GCC diagnostic pop
</#if>
/* MISRAC 2012 deviation block end */
</#if>
</#if>