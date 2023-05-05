<#compress>
<#assign IPC_ENABLE_MASK = "">
<#list 0..TOTAL_IPC_IRQS - 1 as index>
<#if .vars["IPC_IRQ"+ index + "_ENABLE"]>
<#assign IPC_ENABLE_MASK = IPC_ENABLE_MASK + "IPC_IECR_IRQ" + index + "_Msk | ">
</#if>
</#list>
<#assign IPC_ENABLE_MASK = IPC_ENABLE_MASK?remove_ending(" | ")>
<#if IPC_ENABLE_MASK != "" || IPC_WRITE_PROTECT>
<#assign IPC_INIT_REQUIRED = true>
<#else>
<#assign IPC_INIT_REQUIRED = false>
</#if>
</#compress>
