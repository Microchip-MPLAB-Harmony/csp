
<#if rswdtENABLE == true>	
	RSWDT${rswdtIndex?string}_Initialize();
<#else>
	/*Disable Reinforced Safety Watchdog Timer*/
	RSWDT->RSWDT_MR |= RSWDT_MR_WDDIS_Msk;
</#if>
