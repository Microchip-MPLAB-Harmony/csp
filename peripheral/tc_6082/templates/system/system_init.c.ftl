<#list 0..2 as i>
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign TC_NUM = i >
<#if .vars[TC_CH_ENABLE] == true>
	<#if .vars[TC_CH_OPERATINGMODE] == "TIMER">
	<#lt>	TC${INDEX}_CH${TC_NUM}_TimerInitialize (void);
	</#if> <#-- TIMER -->
	<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">
	<#lt>	TC${INDEX}_CH${TC_NUM}_CaptureInitialize (void);
	</#if> <#-- CAPTURE -->
	<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">
	<#lt>	TC${INDEX}_CH${TC_NUM}_CompareInitialize (void);
	</#if> <#-- COMPARE -->
</#if> <#-- CH_ENABLE -->
</#list>