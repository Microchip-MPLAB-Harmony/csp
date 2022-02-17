<#assign CMCC_CONFIGURE = true>
__STATIC_INLINE void CMCC_Configure(void)
{
    /*Configure ICache and ITCM */
    CMCC0_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC0_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#if DEVICE_ITCM_SIZE != "0">
    <#assign CMCC0_CFG_VAL = "CMCC_CFG_PRGCSIZE(" + DEVICE_ITCM_SIZE + "U)">
    <#if !INSTRUCTION_CACHE_ENABLE>
    <#assign CMCC0_CFG_VAL = CMCC0_CFG_VAL + "| CMCC_CFG_ICDIS_Msk">
    </#if>
    CMCC0_REGS->CMCC_CFG = ${CMCC0_CFG_VAL};
    CMCC0_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
</#if>

    /* Configure DCache and DTCM */
    CMCC1_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC1_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#if DEVICE_DTCM_SIZE != "0">
    <#assign CMCC1_CFG_VAL = "CMCC_CFG_PRGCSIZE(" + DEVICE_DTCM_SIZE + "U)">
    <#if !DATA_CACHE_ENABLE>
    <#assign CMCC1_CFG_VAL = CMCC1_CFG_VAL + "| CMCC_CFG_DCDIS_Msk">
    </#if>
    CMCC0_REGS->CMCC_CFG = ${CMCC1_CFG_VAL};
    CMCC0_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
</#if>

}