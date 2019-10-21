<#if PDEC_CTRLA_MODE == "QDEC">
    ${PDEC_INSTANCE_NAME}_QDECInitialize();
<#elseif PDEC_CTRLA_MODE == "HALL">
    ${PDEC_INSTANCE_NAME}_HALLInitialize();
<#else>
    ${PDEC_INSTANCE_NAME}_COUNTERInitialize();
</#if>
