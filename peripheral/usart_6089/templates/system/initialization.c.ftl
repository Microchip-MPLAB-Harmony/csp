<#if USART_MODE == "USART">
    ${USART_INSTANCE_NAME}_Initialize();
<#else>
    ${USART_INSTANCE_NAME}_SPI_Initialize();
</#if>
