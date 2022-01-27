<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#assign GEN_INIT = false>
<#list 0..TOTAL_CHANNEL as i>
<#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
<#if .vars[CHANNEL_ENABLE]?has_content>
<#if (.vars[CHANNEL_ENABLE] != false)>
<#assign GEN_INIT = true>
<#break>
</#if>
</#if>
</#list>
<#if GEN_INIT = true>
    ${EVSYS_INSTANCE_NAME}_Initialize();
</#if>
