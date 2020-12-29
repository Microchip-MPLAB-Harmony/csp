<#if TCC_OPERATION_MODE == "PWM">
    ${TCC_INSTANCE_NAME}_PWMInitialize();
<#elseif TCC_OPERATION_MODE == "Timer">
    ${TCC_INSTANCE_NAME}_TimerInitialize();
<#elseif TCC_OPERATION_MODE == "Compare">
    ${TCC_INSTANCE_NAME}_CompareInitialize();
<#elseif TCC_OPERATION_MODE == "Capture">
    ${TCC_INSTANCE_NAME}_CaptureInitialize();
</#if>
