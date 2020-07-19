<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INT_PRIORITY = "EVIC_" + i + "_PRIORITY">
    <#assign INT_VECTOR_SUB_IRQ_COUNT = "EVIC_" + i + "_VECTOR_SUB_IRQ_COUNT">
    <#if .vars[INT_VECTOR_SUB_IRQ_COUNT]?? && ((.vars[INT_VECTOR_SUB_IRQ_COUNT] > 1) == true)>
        <#list 0..(.vars[INT_VECTOR_SUB_IRQ_COUNT]) as j>
            <#assign INT_VECTOR = "EVIC_" + i + "_" + j + "_VECTOR">
            <#assign INT_NAME = "EVIC_" + i + "_" + j + "_NAME">
            <#assign INTERRUT_HANDLER = "EVIC_" + i + "_" + j + "_INTERRUPT_HANDLER">
            <#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_" + j + "_HANDLER_LOCK">
            <#assign INT_ENABLE = "EVIC_" + i + "_" + j + "_ENABLE">
            <#assign INT_ENABLE_GENERATE = "EVIC_" + i + "_ENABLE_GENERATE">
            <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
            <#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS">
                <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                    <#lt>void ${.vars[INT_NAME]}_Handler (void)
                    <#lt>{
                    <#if .vars[INT_HANDLER_LOCK] == true>
                        <#lt>    ${.vars[INTERRUT_HANDLER]}();
                    </#if>
                    <#lt>}
                </#if>
            <#elseif (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "ThreadX">
                <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                    <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}${.vars["EVIC_PRIORITY_" + .vars[INT_PRIORITY] + "ATTRIBUTE"]}) ${.vars[INT_NAME]}_Handler (void)
                    <#lt>{
                    <#lt>    /* Call ThreadX context save. */
                    <#lt>    _tx_thread_context_save();

                    <#if .vars[INT_HANDLER_LOCK] == true>
                        <#lt>    ${.vars[INTERRUT_HANDLER]}();
                    </#if>

                    <#lt>    /* Call ThreadX context restore. */
                    <#lt>    _tx_thread_context_restore();
                    <#lt>}
                </#if>
            <#else>
                <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}${.vars["EVIC_PRIORITY_" + .vars[INT_PRIORITY] + "ATTRIBUTE"]}) ${.vars[INT_NAME]}_Handler (void)
                <#lt>{
                <#if .vars[INT_HANDLER_LOCK] == true>
                    <#lt>    ${.vars[INTERRUT_HANDLER]}();
                </#if>
                <#lt>}
            </#if>

        </#if>
        </#list>
    <#else>
        <#assign INT_VECTOR = "EVIC_" + i + "_VECTOR">
        <#assign INT_NAME = "EVIC_" + i + "_NAME">
        <#assign INTERRUT_HANDLER = "EVIC_" + i + "_INTERRUPT_HANDLER">
        <#assign INT_HANDLER_LOCK  = "EVIC_" + i + "_HANDLER_LOCK">
        <#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
        <#assign INT_ENABLE_GENERATE = "EVIC_" + i + "_ENABLE_GENERATE">
        <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
            <#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS">
                <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                    <#lt>void ${.vars[INT_NAME]}_Handler (void)
                    <#lt>{
                    <#if .vars[INT_HANDLER_LOCK] == true>
                        <#lt>    ${.vars[INTERRUT_HANDLER]}();
                    </#if>
                    <#lt>}
                </#if>
            <#elseif (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "ThreadX">
                <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                    <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}${.vars["EVIC_PRIORITY_" + .vars[INT_PRIORITY] + "ATTRIBUTE"]}) ${.vars[INT_NAME]}_Handler (void)
                    <#lt>{
                    <#lt>    /* Call ThreadX context save. */
                    <#lt>    _tx_thread_context_save();

                    <#if .vars[INT_HANDLER_LOCK] == true>
                        <#lt>    ${.vars[INTERRUT_HANDLER]}();
                    </#if>

                    <#lt>    /* Call ThreadX context restore. */
                    <#lt>    _tx_thread_context_restore();
                    <#lt>}
                </#if>
            <#else>
                <#lt>void __ISR(${.vars[INT_VECTOR]}, ipl${.vars[INT_PRIORITY]}${.vars["EVIC_PRIORITY_" + .vars[INT_PRIORITY] + "ATTRIBUTE"]}) ${.vars[INT_NAME]}_Handler (void)
                <#lt>{
                <#if .vars[INT_HANDLER_LOCK] == true>
                    <#lt>    ${.vars[INTERRUT_HANDLER]}();
                </#if>
                <#lt>}
            </#if>

        </#if>
    </#if>
</#list>
