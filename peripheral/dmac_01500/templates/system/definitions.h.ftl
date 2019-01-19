<#-- Decide whether to generate code for this system service.
     If no channels are enabled, then no need to generate code. -->
<#assign DMA_ENABLE = "false">
<#list 0..NUM_DMA_CHANS-1 as i>
<#assign CHANENABLE = "DMAC_CHAN"+i+"_ENBL">
<#if .vars[CHANENABLE]?c == "true">
<#assign DMA_ENABLE = "true">
</#if>
</#list>
<#if DMA_ENABLE == "true">
#include "peripheral/dmac/plib_${DMA_INSTANCE_NAME?lower_case}.h"
</#if>