<#if FLEXCOM_MODE = "SPI">
<#if FLEXCOM_SPI_MR_MSTR == "MASTER">
#include "peripheral/flexcom/spi/master/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_master.h"
<#else>
#include "peripheral/flexcom/spi/slave/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_spi_slave.h"
</#if>
<#elseif FLEXCOM_MODE = "TWI">
<#if FLEXCOM_TWI_OPMODE = "MASTER">
#include "peripheral/flexcom/twi/master/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi_master.h"
<#else>
#include "peripheral/flexcom/twi/slave/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_twi_slave.h"
</#if>
<#elseif FLEXCOM_MODE = "USART">
#include "peripheral/flexcom/usart/plib_${FLEXCOM_INSTANCE_NAME?lower_case}_usart.h"
</#if>
