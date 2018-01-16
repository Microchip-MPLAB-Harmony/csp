<#if eefcEnableInterrupt == true >
	<#lt>void EFC_Handler ()
	<#lt>{
	<#lt>	EEFC${INDEX?string}_OPR_Handler();
	<#lt>}
</#if>