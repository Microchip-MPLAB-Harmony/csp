<#assign CMCC_CONFIGURE = true>
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

<#if RAM_INIT?? && RAM_INIT == true>

__STATIC_INLINE void  __attribute__((optimize("-O1")))  RAM_Initialize(void)
{
    register uint32_t *pRam;
    
    for (pRam = (uint32_t*)${RAM_START}U ; pRam < ((uint32_t*)(${RAM_START}U + ${ECC_RAM_LENGTH}U)) ; pRam++)
    {
        *pRam = 0U;
    }
}
</#if>