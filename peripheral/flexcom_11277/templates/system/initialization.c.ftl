<#if FLEXCOM_MODE = "SPI">
    ${FLEXCOM_INSTANCE_NAME}_SPI_Initialize();
<#elseif FLEXCOM_MODE = "TWI">
    ${FLEXCOM_INSTANCE_NAME}_TWI_Initialize();
<#elseif FLEXCOM_MODE = "USART">
    ${FLEXCOM_INSTANCE_NAME}_USART_Initialize();
</#if>
