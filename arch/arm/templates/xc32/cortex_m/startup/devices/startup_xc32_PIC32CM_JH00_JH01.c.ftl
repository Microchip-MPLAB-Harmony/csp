<#if RAM_INIT?? && RAM_INIT == true>

__STATIC_INLINE void  __attribute__((optimize("-O1"))) __attribute__((always_inline)) RAM_Initialize(void)
{
    register uint32_t *pRam;

    // MCRAMC initialization loop (to handle ECC properly)
    // Write to entire RAM to initialize ECC checksum

    if (((WDT_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != 0U) || ((WDT_REGS->WDT_CTRLA & WDT_CTRLA_ENABLE_Msk) != 0U))
    {
        if ((WDT_REGS->WDT_CTRLA & WDT_CTRLA_WEN_Msk) != 0U)
        {
            for (pRam = (uint32_t*)${RAM_START}U ; pRam < ((uint32_t*)(${RAM_START}U + ${RAM_LENGTH}U)) ; pRam++)
            {
                *pRam = 0U;

                if ((WDT_REGS->WDT_INTFLAG & WDT_INTFLAG_EW_Msk) == WDT_INTFLAG_EW_Msk)
                {
                    if ((WDT_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_CLEAR_Msk) == 0U)
                    {

                        /* Clear WDT and reset the WDT timer before the
                        timeout occurs */
                        WDT_REGS->WDT_CLEAR = (uint8_t)WDT_CLEAR_CLEAR_KEY;

                        WDT_REGS->WDT_INTFLAG |= WDT_INTFLAG_EW_Msk;
                    }
                }
            }
        }
        else
        {
            for (pRam = (uint32_t*)${RAM_START}U ; pRam < ((uint32_t*)(${RAM_START}U + ${RAM_LENGTH}U)) ; pRam++)
            {
                *pRam = 0U;

                if ((WDT_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_CLEAR_Msk) == 0U)
                {

                    /* Clear WDT and reset the WDT timer before the timeout occurs */
                    WDT_REGS->WDT_CLEAR = (uint8_t)WDT_CLEAR_CLEAR_KEY;
                }
            }
        }
    }
    else
    {
        for (pRam = (uint32_t*)${RAM_START}U ; pRam < ((uint32_t*)(${RAM_START}U + ${RAM_LENGTH}U)) ; pRam++)
        {
            *pRam = 0U;
        }
    }
}
</#if>