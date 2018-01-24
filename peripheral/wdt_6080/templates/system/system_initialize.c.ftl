
<#if wdtENABLE == true>
	WDT${wdtIndex?string}_Initialize();
<#else>
	/*Disable Watchdog Timer*/
	WDT->WDT_MR |= WDT_MR_WDDIS_Msk;
</#if>
