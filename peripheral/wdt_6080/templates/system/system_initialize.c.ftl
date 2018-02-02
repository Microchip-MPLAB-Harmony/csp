
<#if wdtENABLE == true>
	WDT${wdtIndex?string}_Initialize();
<#else>
	/*Disable Watchdog Timer*/
	_WDT_REGS->WDT_MR.w |= WDT_MR_WDDIS_Msk;
</#if>
