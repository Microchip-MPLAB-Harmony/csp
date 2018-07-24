<#if SERCOM_MODE = "SPIM">
    SERCOM${SERCOM_INDEX}_SPI_Initialize();
<#elseif SERCOM_MODE = "I2CM">
    SERCOM${SERCOM_INDEX}_I2C_Initialize();
<#elseif SERCOM_MODE = "USART_INT">
    SERCOM${SERCOM_INDEX}_USART_Initialize();
</#if>
