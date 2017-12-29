<#if rttINCIEN == true || rttALMIEN == true>
	<#lt>void RTT_Handler ()
	<#lt>{
	<#lt>	RTT${INDEX?string}_INT_HANDLER();
	<#lt>}
</#if>