
<#if DEVICE_TCM_SIZE?has_content>
#pragma config TCM_CONFIGURATION = ${DEVICE_TCM_SIZE}
</#if>
<#if DEVICE_SECURITY?has_content>
#pragma config SECURITY_BIT = ${DEVICE_SECURITY}
</#if>
<#if DEVICE_BOOT?has_content>
#pragma config BOOT_MODE = ${DEVICE_BOOT}
</#if>
