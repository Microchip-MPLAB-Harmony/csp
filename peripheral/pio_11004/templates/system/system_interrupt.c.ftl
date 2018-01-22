<#macro PIO_ISR_HANDLER PIO_CHANNEL>

void PORT${PIO_CHANNEL}_Handler(void)
{
    /* PIO Interrupt Handler */
    _PIO_Interrupt_Handler(PIO_PORT_${PIO_CHANNEL});
}
</#macro>
<#if PIO_A_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="A"
/>
</#if>
<#if PIO_B_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="B"
/>
</#if>
<#if PIO_C_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="C"
/>
</#if>
<#if PIO_D_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="D"
/>
</#if>
<#if PIO_E_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="E"
/>
</#if>