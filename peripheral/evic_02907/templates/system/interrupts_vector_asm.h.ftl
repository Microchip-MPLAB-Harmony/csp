<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign INT_NUMBER = "EVIC_" + i + "_NUMBER">
    <#assign INT_HANDLER  = "EVIC_" + i + "_HANDLER">
    <#assign INT_ENABLE = "EVIC_" + i + "_ENABLE">
    <#assign INT_ENABLE_GENERATE = "EVIC_" + i + "_ENABLE_GENERATE">
    <#if .vars[INT_ENABLE]?? && .vars[INT_ENABLE] == true>
        <#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS != "BareMetal">
            <#if !((.vars[INT_ENABLE_GENERATE]??) && (.vars[INT_ENABLE_GENERATE] == false))>
                <#if __PROCESSOR?matches("PIC32MX.*") == false>
                    <#lt>    .extern  ${.vars[INT_HANDLER]}

                    <#lt>    .section   .vector_${.vars[INT_NUMBER]},code, keep
                    <#lt>    .equ     __vector_dispatch_${.vars[INT_NUMBER]}, IntVector${.vars[INT_HANDLER]}
                    <#lt>    .global  __vector_dispatch_${.vars[INT_NUMBER]}
                    <#lt>    .set     nomicromips
                    <#lt>    .set     noreorder
                    <#lt>    .set     nomips16
                    <#lt>    .set     noat
                    <#lt>    .ent  IntVector${.vars[INT_HANDLER]}

                    <#lt>IntVector${.vars[INT_HANDLER]}:
                    <#lt>    portSAVE_CONTEXT
                    <#lt>    la    s6,  ${.vars[INT_HANDLER]}
                    <#lt>    jalr  s6
                    <#lt>    nop
                    <#lt>    portRESTORE_CONTEXT
                    <#lt>    .end   IntVector${.vars[INT_HANDLER]}
                <#else>
                    <#lt>   .extern  ${.vars[INT_HANDLER]}

                    <#lt>   .section .vector_${.vars[INT_NUMBER]},code, keep
                    <#lt>   .equ     __vector_dispatch_${.vars[INT_NUMBER]}, IntVector${.vars[INT_HANDLER]}
                    <#lt>   .global  __vector_dispatch_${.vars[INT_NUMBER]}
                    <#lt>   .set     nomicromips
                    <#lt>   .set     noreorder
                    <#lt>   .set     nomips16
                    <#lt>   .set     noat
                    <#lt>   .ent  IntVector${.vars[INT_HANDLER]}

                    <#lt>IntVector${.vars[INT_HANDLER]}:
                    <#lt>    la    $26,  ${.vars[INT_HANDLER]}
                    <#lt>    jr    $26
                    <#lt>    nop
                    <#lt>    .end    IntVector${.vars[INT_HANDLER]}

                    <#lt>   .section .${.vars[INT_HANDLER]}_vector_text, code, keep
                    <#lt>   .set     nomicromips
                    <#lt>   .set     noreorder
                    <#lt>   .set     nomips16
                    <#lt>   .set     noat
                    <#lt>   .ent  _${.vars[INT_HANDLER]}

                    <#lt>_${.vars[INT_HANDLER]}:
                    <#lt>    portSAVE_CONTEXT
                    <#lt>    la    s6,  ${.vars[INT_HANDLER]}
                    <#lt>    jalr  s6
                    <#lt>    nop
                    <#lt>    portRESTORE_CONTEXT
                    <#lt>    .end    _${.vars[INT_HANDLER]}
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
