<#if TCM_ENABLE??>
__STATIC_INLINE void TCM_Disable(void);
__STATIC_INLINE void TCM_Enable(void);
__STATIC_INLINE void TCM_Configure(uint32_t tcmSize);
</#if>
<#if (INSTRUCTION_CACHE_ENABLE)??>
<#if (INSTRUCTION_CACHE_ENABLE)>
__STATIC_INLINE void ICache_Enable(void);
</#if>
</#if>
<#if (DATA_CACHE_ENABLE)??>
<#if (DATA_CACHE_ENABLE)>
__STATIC_INLINE void DCache_Enable(void);
</#if>
</#if>

<#if TCM_ENABLE??>
/** Program CMCC PRGCSIZE bits for TCM and cache configuration */
__STATIC_INLINE void TCM_Configure(uint32_t tcmSize)
{
<#if DEVICE_TCM_SIZE != "0">
    CMCC_REGS->CMCC_CFG = CMCC_CFG_PRGCSIZE(tcmSize);
</#if>
}

/** Enable TCM memory */
__STATIC_INLINE void  <#if COMPILER_CHOICE == "XC32">__attribute__((optimize("-O1"))) </#if>TCM_Enable(void)
{
    /* TCM cannot be enabled or disabled in SAMG55 family*/
}

/* Disable TCM memory */
__STATIC_INLINE void  <#if COMPILER_CHOICE == "XC32">__attribute__((optimize("-O1"))) </#if>TCM_Disable(void)
{
    /* TCM cannot be enabled or disabled in SAMG55 family*/
}
</#if>

<#if (INSTRUCTION_CACHE_ENABLE)??>
<#if (INSTRUCTION_CACHE_ENABLE)>
__STATIC_INLINE void ICache_Enable(void)
{
    <#if DEVICE_TCM_SIZE != "0">
        <#if (INSTRUCTION_CACHE_ENABLE)??>
            <#if (INSTRUCTION_CACHE_ENABLE)>
                <#if DATA_CACHE_ENABLE??>
                    <#if (DATA_CACHE_ENABLE)>
                    <#else>
                    <#lt>    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
                    <#lt>    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
                    <#lt>    {
                    <#lt>        /*Wait for the operation to complete*/
                    <#lt>    }
                    <#lt>    CMCC_REGS->CMCC_CFG |= (CMCC_CFG_DCDIS_Msk);
                    </#if>
                </#if>
                <#lt>    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
            </#if>
        </#if>
    </#if>
}
</#if>
</#if>

<#if (DATA_CACHE_ENABLE)??>
<#if (DATA_CACHE_ENABLE)>
__STATIC_INLINE void DCache_Enable(void)
{
    <#if DEVICE_TCM_SIZE != "0">
        <#if (DATA_CACHE_ENABLE)??>
            <#if (DATA_CACHE_ENABLE)>
                <#if INSTRUCTION_CACHE_ENABLE??>
                    <#if (INSTRUCTION_CACHE_ENABLE)>
                    <#else>
                    <#lt>    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
                    <#lt>    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
                    <#lt>    {
                    <#lt>        /*Wait for the operation to complete*/
                    <#lt>    }
                    <#lt>    CMCC_REGS->CMCC_CFG |= (CMCC_CFG_ICDIS_Msk);
                    <#lt>    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
                    </#if>
                </#if>
            </#if>
        </#if>
    </#if>
}
</#if>
</#if>