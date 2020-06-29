<#if SERCOM_MODE = "SPIM">
#include "peripheral/sercom/spi_master/plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_master.h"
<#elseif SERCOM_MODE = "SPIS">
#include "peripheral/sercom/spi_slave/plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_slave.h"
<#elseif SERCOM_MODE = "I2CM">
#include "peripheral/sercom/i2c_master/plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c_master.h"
<#elseif SERCOM_MODE = "I2CS">
#include "peripheral/sercom/i2c_slave/plib_${SERCOM_INSTANCE_NAME?lower_case}_i2c_slave.h"
<#elseif SERCOM_MODE = "USART_INT">
#include "peripheral/sercom/usart/plib_${SERCOM_INSTANCE_NAME?lower_case}_usart.h"
</#if>
