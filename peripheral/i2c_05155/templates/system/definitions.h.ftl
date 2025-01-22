<#if I2C_OPERATING_MODE = "Host">
#include "peripheral/i2c/host/plib_${moduleName?lower_case}_host.h"
<#else>
#include "peripheral/i2c/client/plib_${moduleName?lower_case}_client.h"
</#if>