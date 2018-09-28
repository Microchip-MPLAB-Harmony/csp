<#if FLEXCOM_MODE = "SPI">
#include "peripheral/flexcom/spi/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi.h"
<#elseif FLEXCOM_MODE = "TWI">
#include "peripheral/flexcom/twi/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi.h"
<#elseif FLEXCOM_MODE = "USART">
#include "peripheral/flexcom/usart/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_usart.h"
</#if>
