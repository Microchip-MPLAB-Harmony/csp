<#if LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION?has_content>
<@mhc_expand_list list=LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION/>
</#if>

// Configuration Bit Settings
<#if FUSE_CONFIG_ENABLE>
${FUSE_CONFIG_CODE_GEN}
</#if>




