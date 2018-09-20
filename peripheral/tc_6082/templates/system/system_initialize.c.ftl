<#assign start = 0>
<#if TC_ENABLE_QEI == true>
    ${TC_INSTANCE_NAME}_QuadratureInitialize();
	<#if TC_BMR_POSEN == "POSITION">
		<#assign start = 2>
	<#else>
		<#assign start = 3>
	</#if>
</#if>	
<#list start..2 as i>
	<#if i == 3>
		<#break>
	</#if> <#-- break the loop if quadrature mode is enabled -->
${""?left_pad(4)}<#compress>
<#assign TC_CH_ENABLE = "TC" + i + "_ENABLE">
<#assign TC_CH_OPERATINGMODE = "TC" + i +"_OPERATING_MODE">
<#assign TC_NUM = i >
<#if .vars[TC_CH_ENABLE] == true>
	<#if .vars[TC_CH_OPERATINGMODE] == "TIMER">
	<#lt>${TC_INSTANCE_NAME}_CH${TC_NUM}_TimerInitialize();
	</#if> <#-- TIMER -->
	<#if .vars[TC_CH_OPERATINGMODE] == "CAPTURE">
	<#lt>${TC_INSTANCE_NAME}_CH${TC_NUM}_CaptureInitialize();
	</#if> <#-- CAPTURE -->
	<#if .vars[TC_CH_OPERATINGMODE] == "COMPARE">
	<#lt>${TC_INSTANCE_NAME}_CH${TC_NUM}_CompareInitialize();
	</#if> <#-- COMPARE -->
</#if> <#-- CH_ENABLE --> 
</#compress>
</#list>
