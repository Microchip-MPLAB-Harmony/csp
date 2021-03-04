
<#if PRODUCT_FAMILY != "PIC32MX1290">
    /* Configure KSEG0 as cacheable memory. This is needed for Prefetch Buffer */
    __builtin_mtc0(16, 0,(__builtin_mfc0(16, 0) | 0x3));

</#if>
<#if CONFIG_CHECON_PFMWS?? && CONFIG_CHECON_PREFEN??>
    /* Configure Flash Wait States and Prefetch */
    CHECONbits.PFMWS = ${CONFIG_CHECON_PFMWS};
    CHECONbits.PREFEN = ${CONFIG_CHECON_PREFEN};

</#if>
    /* Set the SRAM wait states to zero */
    BMXCONbits.BMXWSDRM = 0;

<#if (DDPCON_JTAG_ENABLE?? && DDPCON_JTAG_ENABLE == false) || (DDPCON_TDO_ENABLE?? && DDPCON_TDO_ENABLE == true) || (DDPCON_TRACE_ENABLE?? && DDPCON_TRACE_ENABLE == true)>
    /* Configure Debug Data Port */
</#if>
<#if DDPCON_JTAG_ENABLE?? && DDPCON_JTAG_ENABLE == false>
    DDPCONbits.JTAGEN = 0;
</#if>
<#if DDPCON_TDO_ENABLE?? && DDPCON_TDO_ENABLE == true>
    DDPCONbits.TDOEN = 1;
</#if>
<#if DDPCON_TRACE_ENABLE?? && DDPCON_TRACE_ENABLE == true>
    DDPCONbits.TROEN = 1;
</#if>        
