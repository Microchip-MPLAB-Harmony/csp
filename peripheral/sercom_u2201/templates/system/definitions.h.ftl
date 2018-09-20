<#if SERCOM_MODE = "SPIM">
#include "peripheral/sercom/spim/plib_${SERCOM_INSTANCE_NAME?lower_case}_spi.h"
<#elseif SERCOM_MODE = "I2CM">
#include "peripheral/sercom/i2cm/plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c.h"
<#elseif SERCOM_MODE = "USART_INT">
#include "peripheral/sercom/usart/plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"
</#if>
