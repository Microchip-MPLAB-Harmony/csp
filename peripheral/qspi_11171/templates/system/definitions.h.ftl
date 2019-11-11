<#if QSPI_SMM?string=="MEMORY">
#include "peripheral/qspi/plib_${QSPI_INSTANCE_NAME?lower_case}.h"
<#else>
#include "peripheral/qspi/plib_${QSPI_INSTANCE_NAME?lower_case}_spi.h"
</#if>