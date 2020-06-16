<#if I2C_OPERATING_MODE = "Master">
#include "peripheral/i2c/master/plib_${I2C_INSTANCE_NAME?lower_case}_master.h"
<#else>
#include "peripheral/i2c/slave/plib_${I2C_INSTANCE_NAME?lower_case}_slave.h"
</#if>