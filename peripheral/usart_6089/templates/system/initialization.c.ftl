<#if USART_MODE == "USART" || USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE">
    ${USART_INSTANCE_NAME}_Initialize();
<#elseif USART_MODE == "SPI_MASTER" >
    ${USART_INSTANCE_NAME}_SPI_Initialize();
</#if>
