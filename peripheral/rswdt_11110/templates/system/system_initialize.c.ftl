
<#if rswdtENABLE == true>	
	RSWDT${rswdtIndex?string}_Initialize();
<#else>
	/*Disable Reinforced Safety Watchdog Timer*/
	_RSWDT_REGS->RSWDT_MR.w |= RSWDT_MR_WDDIS_Msk;
</#if>
