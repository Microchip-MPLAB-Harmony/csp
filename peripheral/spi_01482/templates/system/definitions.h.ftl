<#if SPI_CON1__MSTEN == "1">
#include "peripheral/spi/spi_host/plib_${SPI_INSTANCE_NAME?lower_case}_host.h"
<#else>
#include "peripheral/spi/spi_client/plib_${SPI_INSTANCE_NAME?lower_case}_client.h"
</#if>
