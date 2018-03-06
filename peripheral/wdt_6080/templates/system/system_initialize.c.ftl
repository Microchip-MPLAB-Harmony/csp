<#if wdtENABLE == true>
	WDT${wdtIndex?string}_Initialize();
<#else>	_WDT_REGS->WDT_MR.w |= WDT_MR_WDDIS_Msk; 		// Disable WDT </#if>