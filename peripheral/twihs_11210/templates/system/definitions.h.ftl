<#if TWIHS_OPMODE == "MASTER">
#include "peripheral/twihs/master/plib_${TWIHS_INSTANCE_NAME?lower_case}_master.h"
<#else>
#include "peripheral/twihs/slave/plib_${TWIHS_INSTANCE_NAME?lower_case}_slave.h"
</#if>
