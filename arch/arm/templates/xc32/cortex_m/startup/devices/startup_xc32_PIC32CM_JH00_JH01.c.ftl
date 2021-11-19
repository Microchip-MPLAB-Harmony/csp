<#if RAM_INIT??>

__STATIC_INLINE void  __attribute__((optimize("-O1")))  RAM_Initialize(void)
{
	register uint32_t wdt_ctrl = 0;
    register uint32_t *pRam;   
    
	/* Save the WDT control register to be restored after RAM init is complete */
	wdt_ctrl = WDT_REGS->WDT_CTRLA;
	
    if ((WDT_REGS->WDT_CTRLA & WDT_CTRLA_ENABLE_Msk) && (!(WDT_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk)))
    {
        /* Wait for synchronization */
        while(WDT_REGS->WDT_SYNCBUSY != 0U)
        {

        }

        /* Disable Watchdog Timer */
        WDT_REGS->WDT_CTRLA &= (uint8_t)(~WDT_CTRLA_ENABLE_Msk);

        /* Wait for synchronization */
        while(WDT_REGS->WDT_SYNCBUSY != 0U)
        {

        }
    }    
    
    if ((WDT_REGS->WDT_CTRLA & WDT_CTRLA_WEN_Msk) && (WDT_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk))
    {            
        while(WDT_REGS->WDT_SYNCBUSY != 0U)
        {

        }

        /* Disable window mode */
        WDT_REGS->WDT_CTRLA &= (uint8_t)(~WDT_CTRLA_WEN_Msk);

        while(WDT_REGS->WDT_SYNCBUSY != 0U)
        {

        }
    }  
               
	__DSB();
    __ISB();
               
    // MCRAMC initialization loop (to handle ECC properly)
    // Write to entire RAM (leaving initial 16 bytes) to initialize ECC checksum
    for (pRam = (uint32_t*)${RAM_START} ; pRam < ((uint32_t*)(${RAM_START} + ${RAM_LENGTH})) ; pRam++)
    {
        *pRam = 0;
                        
        if ((WDT_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_CLEAR_Msk) != WDT_SYNCBUSY_CLEAR_Msk)
        {
            
            /* Clear WDT and reset the WDT timer before the
            timeout occurs */
            WDT_REGS->WDT_CLEAR = (uint8_t)WDT_CLEAR_CLEAR_KEY;
        }
    }    
	
	__DSB();
    __ISB();
	
	/* Wait for synchronization */
	while(WDT_REGS->WDT_SYNCBUSY != 0U)
	{

	}
	
	/* Restore back the WDT control register */
	WDT_REGS->WDT_CTRLA = wdt_ctrl;
	
	/* Wait for synchronization */
	while(WDT_REGS->WDT_SYNCBUSY != 0U)
	{

	}
}
</#if>