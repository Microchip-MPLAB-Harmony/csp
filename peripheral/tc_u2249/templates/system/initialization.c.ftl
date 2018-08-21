<#if TC_SLAVE_MODE == false>
<#if TC_OPERATION_MODE = "Timer">
    TC${TC_INDEX}_TimerInitialize();
<#elseif TC_OPERATION_MODE = "Compare">
    TC${TC_INDEX}_CompareInitialize();
<#elseif TC_OPERATION_MODE = "Capture">
    TC${TC_INDEX}_CaptureInitialize();
</#if>
</#if>