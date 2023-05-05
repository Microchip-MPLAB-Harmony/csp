<#if I2C_SMBUS_PROTOCOL_EN == true>    
    I2C${I2C_INSTANCE_NAME}_Initialize();
<#else>
    I2C${I2C_INSTANCE_NUM}_Initialize();
</#if>    