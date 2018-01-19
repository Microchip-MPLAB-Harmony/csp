<#if trngEnableInterrupt == true>
	<#lt>void TRNG_Handler ()
	<#lt>{
	<#lt>	TRNG${INDEX?string}_DATARDY_Handler();
	<#lt>}
</#if>