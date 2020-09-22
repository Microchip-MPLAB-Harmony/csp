<#if SPI_MR_MSTR == "MASTER">
#include "peripheral/spi/spi_master/plib_${SPI_INSTANCE_NAME?lower_case}_master.h"
<#else>
#include "peripheral/spi/spi_slave/plib_${SPI_INSTANCE_NAME?lower_case}_slave.h"
</#if>
