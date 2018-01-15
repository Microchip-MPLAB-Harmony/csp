<#if rtcEnableInterrupt == true>
	<#lt>void RTC_Handler ()
	<#lt>{
	<#lt>	RTC${INDEX?string}_ALARM_Handler();
	<#lt>}
</#if>