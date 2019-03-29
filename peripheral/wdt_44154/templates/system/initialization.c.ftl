<#if WDT_ENABLE == true>
    ${WDT_INSTANCE_NAME}_Initialize();
<#else>
    ${WDT_INSTANCE_NAME}_REGS->WDT_MR = WDT_MR_WDDIS_Msk;       // Disable WDT
</#if>