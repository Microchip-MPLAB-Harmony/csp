<#if wdtENABLE == true>
	WDT${wdtIndex?string}_Initialize();
<#else>	WDT_REGS->WDT_MR|= WDT_MR_WDDIS_Msk; 		// Disable WDT </#if>