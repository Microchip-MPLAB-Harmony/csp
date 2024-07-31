<@compress single_line=true><#lt>   ${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA =
<#if FCR_AUTOWS == false>
    <#lt>   ((${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA) & (FCR_CTRLA_RDBUFWS_Msk)) |
    <#lt>   FCR_CTRLA_FWS(${FCR_FWS}) |
<#else>
    <#lt>   ((${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA) & (FCR_CTRLA_RDBUFWS_Msk | FCR_CTRLA_FWS_Msk)) |
</#if>
<#lt>   FCR_CTRLA_ADRWS(${FCR_ADRWS?then('1U', '0U')}) |
<#lt>   FCR_CTRLA_AUTOWS(${FCR_AUTOWS?then('1U', '0U')});</@compress>