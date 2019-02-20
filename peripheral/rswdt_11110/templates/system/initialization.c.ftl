<#if rswdtENABLE == true>	
	${RSWDT_INSTANCE_NAME}_Initialize();
<#else>	${RSWDT_INSTANCE_NAME}_REGS->RSWDT_MR = RSWDT_MR_WDDIS_Msk;	// Disable RSWDT </#if>
