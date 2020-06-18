<#if USART_MODE == "USART">
#include "peripheral/usart/plib_${USART_INSTANCE_NAME?lower_case}.h"
<#else>
#include "peripheral/usart/plib_${USART_INSTANCE_NAME?lower_case}_spi.h"
</#if>
