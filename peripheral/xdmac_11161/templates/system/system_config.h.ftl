/* Peripheral address macros for DMA */
<#list 0..XDMAC_CHANNEL_COUNT as i>
<#assign XDMAC_CH_ENABLE = "XDMAC_CH" + i + "_ENABLE">
<#assign XDMAC_CH_PERID = "XDMAC_CC" + i + "_PERID">
<#assign XDMAC_CH_PER_REGISTER = "XDMAC_CH" + i + "_PER_REGISTER">
    <#if .vars[XDMAC_CH_ENABLE]?has_content>
        <#if (.vars[XDMAC_CH_ENABLE] != false)>
            <#if (.vars[XDMAC_CH_PER_REGISTER]?has_content) && (.vars[XDMAC_CH_PER_REGISTER] != "None")>
#define ${.vars[XDMAC_CH_PERID]?upper_case}_ADDRESS  (&${.vars[XDMAC_CH_PER_REGISTER]})
            </#if>
        </#if>
    </#if>
</#list>