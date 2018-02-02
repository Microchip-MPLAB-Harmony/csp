<#if SPI_INTERRUPT_MODE == true>
void SPI${SPI_INDEX?string}_Handler(void)
{
	SPI${SPI_INDEX?string}_ISR_Exchange_Handler();
    SPI${SPI_INDEX?string}_ISR_Error_Handler();
}
</#if>