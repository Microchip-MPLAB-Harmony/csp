#define GPNVM_TCM_SIZE_Pos        7u
#define GPNVM_TCM_SIZE_Msk        (0x3u << GPNVM_TCM_SIZE_Pos)

/** Program GPNVM fuse for TCM configuration */
__STATIC_INLINE void TCM_Configure(uint32_t neededGpnvmValue)
{
    static uint32_t gpnvmReg;
    static uint32_t cmd;

    /* Read GPNVM fuse setting  */
    EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | EEFC_FCR_FCMD_GGPB);

    while (!(EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk))
    {
    }

    gpnvmReg=EFC_REGS->EEFC_FRR;

    /* Program only if change is needed */
    if (((gpnvmReg & GPNVM_TCM_SIZE_Msk)>>GPNVM_TCM_SIZE_Pos) != neededGpnvmValue)
    {
        if(neededGpnvmValue & 0x2)
            cmd=EEFC_FCR_FCMD_SGPB;
        else
            cmd=EEFC_FCR_FCMD_CGPB;

        EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | cmd | EEFC_FCR_FARG(8));
        while (!(EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk))
        {
        }

        if(neededGpnvmValue & 0x1)
            cmd=EEFC_FCR_FCMD_SGPB;
        else
            cmd=EEFC_FCR_FCMD_CGPB;

        EFC_REGS->EEFC_FCR = (EEFC_FCR_FKEY_PASSWD | cmd | EEFC_FCR_FARG(7));
        while (!(EFC_REGS->EEFC_FSR & EEFC_FSR_FRDY_Msk))
        {
        }

        /* Reset the device for the programmed fuse value to take effect */
        RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | RSTC_CR_PROCRST_Msk;
    }
}


/** Enable TCM memory */
__STATIC_INLINE void __attribute__((optimize("-O1"))) TCM_Enable(void)
{
    __DSB();
    __ISB();
    SCB->ITCMCR = (SCB_ITCMCR_EN_Msk  | SCB_ITCMCR_RMW_Msk | SCB_ITCMCR_RETEN_Msk);
    SCB->DTCMCR = (SCB_DTCMCR_EN_Msk | SCB_DTCMCR_RMW_Msk | SCB_DTCMCR_RETEN_Msk);
    __DSB();
    __ISB();
}

/* Disable TCM memory */
__STATIC_INLINE void __attribute__((optimize("-O1"))) TCM_Disable(void)
{
    __DSB();
    __ISB();
    SCB->ITCMCR &= ~(uint32_t)SCB_ITCMCR_EN_Msk;
    SCB->DTCMCR &= ~(uint32_t)SCB_ITCMCR_EN_Msk;
    __DSB();
    __ISB();
}