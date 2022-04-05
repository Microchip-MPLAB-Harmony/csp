<#assign STARTUP_TCM_SIZE_CONFIGURE = true>
#define GPNVM_TCM_SIZE_Pos        7u
#define GPNVM_TCM_SIZE_Msk        (0x3u << GPNVM_TCM_SIZE_Pos)

/** Program GPNVM fuse for TCM configuration */
__STATIC_INLINE void TCM_Configure(uint32_t neededGpnvmValue)
{
    static uint32_t gpnvmReg;
    static uint32_t cmd;

    /* Read GPNVM fuse setting  */
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | EEFC_FCR_FCMD_GGPB);
    while ((EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk) == 0U)
    {
        /* Wait for FRDY bit */
    }

    gpnvmReg = EFC_REGS->EEFC_FRR;

    /* Program only if change is needed */
    if (((gpnvmReg & GPNVM_TCM_SIZE_Msk) >> GPNVM_TCM_SIZE_Pos) != neededGpnvmValue)
    {
        if((neededGpnvmValue & 0x2U) != 0U)
        {
            cmd = EEFC_FCR_FCMD_SGPB;
        }
        else
        {
            cmd = EEFC_FCR_FCMD_CGPB;
        }
        EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | cmd | EEFC_FCR_FARG(8U));
        while ((EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk) == 0U)
        {
            /* Wait for FRDY bit */
        }

        if((neededGpnvmValue & 0x1U) != 0U)
        {
            cmd = EEFC_FCR_FCMD_SGPB;
        }
        else
        {
            cmd = EEFC_FCR_FCMD_CGPB;
        }

        EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | cmd | EEFC_FCR_FARG(7U));
        while ((EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk) == 0U)
        {
            /* Wait for FRDY bit */
        }

        /* Reset the device for the programmed fuse value to take effect */
        RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | RSTC_CR_PROCRST_Msk;
    }
}
