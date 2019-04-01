
<#if DEVICE_FAMILY != "DS60001290">
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


