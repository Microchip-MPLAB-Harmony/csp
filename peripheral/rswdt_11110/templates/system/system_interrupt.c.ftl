<#if rswdtinterruptMode == true>
	<#lt>void RSWDT_Handler(void)
	<#lt>{
	<#lt>	RSWDT${INDEX?string}_TIMEOUT_Handler();
	<#lt>}
</#if>