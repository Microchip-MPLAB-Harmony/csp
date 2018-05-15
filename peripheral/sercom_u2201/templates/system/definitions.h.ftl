<#if SERCOM_MODE = "SPIM">
#include "peripheral/sercom/spim/plib_sercom${SERCOM_INDEX}_spi.h"
<#elseif SERCOM_MODE = "I2CM">
#include "peripheral/sercom/i2cm/plib_sercom${SERCOM_INDEX}_i2c.h"
<#elseif SERCOM_MODE = "USART_INT" || SERCOM_MODE = "USART_EXT">
#include "peripheral/sercom/usart/plib_sercom${SERCOM_INDEX}_usart.h"
</#if>
