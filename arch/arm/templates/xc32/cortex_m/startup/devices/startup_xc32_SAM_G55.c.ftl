<#assign CMCC_CONFIGURE = true>
__STATIC_INLINE void CMCC_Configure(void)
{
    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    <#assign CMCC_CFG_VAL = "CMCC_CFG_PRGCSIZE(" + DEVICE_TCM_SIZE + "U)">
    <#if !INSTRUCTION_CACHE_ENABLE>
    <#assign CMCC_CFG_VAL = CMCC_CFG_VAL + "| CMCC_CFG_ICDIS_Msk">
    </#if>
    <#if !DATA_CACHE_ENABLE>
    <#assign CMCC_CFG_VAL = CMCC_CFG_VAL + "| CMCC_CFG_DCDIS_Msk">
    </#if>
    CMCC_REGS->CMCC_CFG = ${CMCC_CFG_VAL};
    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}