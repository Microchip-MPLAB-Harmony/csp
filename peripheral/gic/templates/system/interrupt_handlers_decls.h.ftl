<#list 16..GIC_INTERRUPT_MAX_INDEX + 1 as index>
<#assign INTERRUPT_ID = "INTERRUPT_ID_" + index>
<#if .vars[INTERRUPT_ID]??>
<#list .vars[INTERRUPT_ID]?split(" ") as INSTANCE>
<#if .vars[INSTANCE + "_INTERRUPT_ENABLE"]>
void ${.vars[INSTANCE + "_INTERRUPT_HANDLER"]} (void);
</#if>
</#list>
</#if>
</#list>