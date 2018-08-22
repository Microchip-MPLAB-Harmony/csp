<#if rswdtENABLE == true>	
	RSWDT${rswdtIndex?string}_Initialize();
<#else>	RSWDT_REGS->RSWDT_MR = RSWDT_MR_WDDIS_Msk;	// Disable RSWDT </#if>