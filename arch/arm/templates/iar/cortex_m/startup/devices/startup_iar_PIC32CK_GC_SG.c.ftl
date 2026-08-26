<#-- PIC32CK_GC_SG IAR startup device configuration -->

<#-- Always declare function prototypes - unconditional -->
__STATIC_INLINE void TCM_Disable(void);
__STATIC_INLINE void TCM_Enable(void);
__STATIC_INLINE void TCM_Configure(uint32_t tcmSize);
__STATIC_INLINE void ICache_Enable(void);
__STATIC_INLINE void DCache_Enable(void);

<#-- Include CMCC plib header -->
#include "peripheral/cmcc/plib_cmcc.h"

<#-- Set variables for main template -->
<#assign TCM_ENABLE = true>
<#assign INSTRUCTION_CACHE_ENABLE = true>
<#assign DATA_CACHE_ENABLE = true>

<#-- TCM configuration - always provide implementations -->
__STATIC_INLINE void TCM_Configure(uint32_t tcmSize)
{
    (void)tcmSize;
}

__STATIC_INLINE void TCM_Enable(void)
{
    /* TCM cannot be enabled or disabled in PIC32CK family */
}

__STATIC_INLINE void TCM_Disable(void)
{
    /* TCM cannot be enabled or disabled in PIC32CK family */
}

<#-- Instruction cache enable -->
__STATIC_INLINE void ICache_Enable(void)
{
    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#if DEVICE_TCM_SIZE?? && DEVICE_TCM_SIZE != "3">
    CMCC_REGS->CMCC_CFG = CMCC_CFG_CSIZESW(${DEVICE_TCM_SIZE}U);
</#if>
    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

<#-- Data cache enable -->
__STATIC_INLINE void DCache_Enable(void)
{
    CMCC_REGS->CMCC_CTRL &= ~(CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#if DEVICE_TCM_SIZE?? && DEVICE_TCM_SIZE != "3">
    CMCC_REGS->CMCC_CFG = CMCC_CFG_CSIZESW(${DEVICE_TCM_SIZE}U);
</#if>
    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}
