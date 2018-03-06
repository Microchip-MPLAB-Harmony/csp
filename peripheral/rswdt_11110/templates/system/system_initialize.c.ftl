<#if rswdtENABLE == true>	
	RSWDT${rswdtIndex?string}_Initialize();
<#else>	_RSWDT_REGS->RSWDT_MR.w |= RSWDT_MR_WDDIS_Msk;	// Disable RSWDT </#if>