<#if INTERRUPT_MODE == true>
void UART${INDEX?string}_Handler(void)
{
	UART${INDEX?string}_ISR_ERR_Handler();
	UART${INDEX?string}_ISR_RX_Handler();
	UART${INDEX?string}_ISR_TX_Handler();
}
</#if>