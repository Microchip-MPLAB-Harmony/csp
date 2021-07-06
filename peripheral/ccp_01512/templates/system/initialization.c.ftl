<#if CCP_OPERATION_MODE == "Timer">
    ${CCP_INSTANCE_NAME}_TimerInitialize();
<#elseif CCP_OPERATION_MODE == "Compare">
    ${CCP_INSTANCE_NAME}_CompareInitialize();
<#else>
    ${CCP_INSTANCE_NAME}_CaptureInitialize();
</#if>
