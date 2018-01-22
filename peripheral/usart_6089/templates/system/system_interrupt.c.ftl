<#if INTERRUPT_MODE == true>
void USART${INDEX?string}_Handler(void)
{
	USART${INDEX?string}_ISR_ERR_Handler();
	USART${INDEX?string}_ISR_RX_Handler();
	USART${INDEX?string}_ISR_TX_Handler();
}
</#if>