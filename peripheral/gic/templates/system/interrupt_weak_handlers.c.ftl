/*  Weak definitions for default handlers.  Users may override these with
    implementations of their own or provide alternate functions to the 
    interrupt controller.  PLIB implementations provide alternate functions, 
    with the name {periph}_InterruptHandler so as they will not collide with
    user {periph}_Handler definitions.
*/
<#list 16..GIC_INTERRUPT_MAX_INDEX + 1 as index>
<#assign INTERRUPT_ID = "INTERRUPT_ID_" + index>
<#if .vars[INTERRUPT_ID]??>
<#assign MODULE = .vars[INTERRUPT_ID]?split(" ")[0]>
<#assign ENABLE = .vars[MODULE + "_INTERRUPT_ENABLE"]>
<#assign HANDLER = .vars[MODULE + "_INTERRUPT_HANDLER"] + "( void )">
<#if !ENABLE>
void ${HANDLER?right_pad(36)}__attribute__((weak, alias("DefaultInterruptHandler")));
</#if>
</#if>
</#list>


/* Array of interrupt handlers indexed by its IRQn_Type IDs */

PPI_SPI_HANDLER gicPIVectorTable[${GIC_INTERRUPT_MAX_INDEX - 15}U] = 
{
<#list 16..GIC_INTERRUPT_MAX_INDEX as index>
<#assign INTERRUPT_ID = "INTERRUPT_ID_" + index>
<#if .vars[INTERRUPT_ID]??>
<#assign MODULE = .vars[INTERRUPT_ID]?split(" ")[0]>
<#assign HANDLER = .vars[MODULE + "_INTERRUPT_HANDLER"]>
<#else>
<#assign HANDLER = "NULL">
</#if>
    ${HANDLER}${(index != GIC_INTERRUPT_MAX_INDEX )?string(",", "")}
</#list>
};

