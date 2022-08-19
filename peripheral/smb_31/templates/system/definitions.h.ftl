<#if I2C_SMBUS_PROTOCOL_EN == true>

<#if I2C_OPERATING_MODE == "Master">
#include "peripheral/i2c/master/plib_${I2C_INSTANCE_NAME?lower_case}_master.h"
<#elseif I2C_OPERATING_MODE == "Slave">
#include "peripheral/i2c/slave/plib_${I2C_INSTANCE_NAME?lower_case}_slave.h"
<#elseif I2C_OPERATING_MODE == "Master and Slave">
#include "peripheral/i2c/plib_${I2C_INSTANCE_NAME?lower_case}_master_slave_common.h"
#include "peripheral/i2c/master/plib_${I2C_INSTANCE_NAME?lower_case}_master.h"
#include "peripheral/i2c/slave/plib_${I2C_INSTANCE_NAME?lower_case}_slave.h"
</#if>

<#else>

<#if I2C_OPERATING_MODE == "Master">
#include "peripheral/i2c/master/plib_i2c${I2C_INSTANCE_NUM}_master.h"
<#else>
#include "peripheral/i2c/slave/plib_i2c${I2C_INSTANCE_NUM}_slave.h"
</#if>

</#if>