
<#list 0..GIC_INTERRUPT_MAX_INDEX + 1 as index>
<#assign INTERRUPT_ID = "INTERRUPT_ID_" + index>
<#if .vars[INTERRUPT_ID]??>
<#assign MODULE_LIST = .vars[INTERRUPT_ID]?split(" ")>
<#if MODULE_LIST?size &gt; 1>
<#if .vars[MODULE_LIST[0] +"_INTERRUPT_ENABLE"]>
/* Shared Interrupt Handler for ${MODULE_LIST[0]} module */
void ${.vars[MODULE_LIST[0] + "_INTERRUPT_HANDLER"]} (void)
{
<#list 1..MODULE_LIST?size - 1 as i>
<#if .vars[MODULE_LIST[i] + "_INTERRUPT_ENABLE"]>
    /* ${MODULE_LIST[i]} Handler */
    ${.vars[MODULE_LIST[i] + "_INTERRUPT_HANDLER"]}();

</#if>
</#list>
}

</#if>
</#if>
</#if>
</#list>
