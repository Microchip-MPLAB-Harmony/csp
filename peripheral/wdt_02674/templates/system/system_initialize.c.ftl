<#if USE_SYS_WDT == true>
    ${WDT_INSTANCE_NAME}_Initialize();
<#else>	
    ${WDT_INSTANCE_NAME}_Disable(); 		// Disable WDT since not using it
</#if>
