<#if USART_MODE == "USART">
#include "peripheral/usart/plib_${USART_INSTANCE_NAME?lower_case}.h"
<#elseif USART_MODE == "SPI_MASTER" >
#include "peripheral/usart/plib_${USART_INSTANCE_NAME?lower_case}_spi.h"
<#elseif USART_MODE == "LIN_MASTER" || USART_MODE == "LIN_SLAVE" >
#include "peripheral/usart/plib_${USART_INSTANCE_NAME?lower_case}_lin.h"
</#if>
