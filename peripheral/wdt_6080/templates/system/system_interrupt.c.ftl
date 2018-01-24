<#if wdtinterruptMode == true>
	<#lt>void WDT_Handler(void)
	<#lt>{
	<#lt>	WDT${wdtIndex?string}_TIMEOUT_Handler();
	<#lt>}
</#if>
