<#if TC_SLAVE_MODE == false>
<#if TC_OPERATION_MODE = "Timer">
    ${TC_INSTANCE_NAME}_TimerInitialize();
<#elseif TC_OPERATION_MODE = "Compare">
    ${TC_INSTANCE_NAME}_CompareInitialize();
<#elseif TC_OPERATION_MODE = "Capture">
    ${TC_INSTANCE_NAME}_CaptureInitialize();
</#if>
</#if>
