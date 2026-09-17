<#assign CMCC_CONFIGURE = true>
/* MISRAC 2023 deviation block start */
/* MISRA C-2023 Rule 7.6 deviated in this file. Deviation record ID - H3_MISRAC_2023_R_7_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
<#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate "MISRA C-2023 Rule 7.6" "H3_MISRAC_2023_R_7_6_DR_1"
</#if>
__STATIC_INLINE void __attribute__((optimize("-O1"))) CMCC_Configure(void)
{
    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#if DEVICE_TCM_SIZE != "3">
    <#assign CMCC_CFG_VAL = "CMCC_CFG_CSIZESW(" + DEVICE_TCM_SIZE + "U)">
    <#if !INSTRUCTION_CACHE_ENABLE>
    <#assign CMCC_CFG_VAL = CMCC_CFG_VAL + "| CMCC_CFG_ICDIS_Msk">
    </#if>
    <#if !DATA_CACHE_ENABLE>
    <#assign CMCC_CFG_VAL = CMCC_CFG_VAL + "| CMCC_CFG_DCDIS_Msk">
    </#if>
    CMCC_REGS->CMCC_CFG = ${CMCC_CFG_VAL};
    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
</#if>
}
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2023 Rule 7.6"
<#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2023 deviation block end */