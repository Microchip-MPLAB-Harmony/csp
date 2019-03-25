<#assign start = 0>
<#if TC_ENABLE_QEI == true>
    ${TC_INSTANCE_NAME}_QuadratureInitialize();
    <#if TC_BMR_POSEN == "POSITION">
        <#if TC_INDEX_PULSE == true>
            <#assign start = 2>
        <#else>
            <#assign start = 1>
        </#if>
    <#else>
        <#if TC_INDEX_PULSE == true>
            <#assign start = 3>
        <#else>
            <#assign start = 1>
        </#if>
    </#if>
</#if>
<#list start..(TC_MAX_CHANNELS - 1) as i>
    <#if i == TC_MAX_CHANNELS>
        <#break>
    </#if> <#-- break the loop if quadrature mode is enabled -->
    <#if TC_ENABLE_QEI == true && TC_INDEX_PULSE == false && TC_BMR_POSEN == "SPEED" && i == 2>
        <#break>
    </#if>
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
