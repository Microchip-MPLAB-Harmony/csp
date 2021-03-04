<#if PRODUCT_FAMILY != 'PIC32MZW'>
    /* Configure Prefetch, Wait States and ECC */
    PRECONbits.PREFEN = ${CONFIG_PRECON_PREFEN};
    PRECONbits.PFMWS = ${CONFIG_PRECON_PFMWS};
    CFGCONbits.ECCCON = ${CONFIG_CFGCON_ECCCON};
<#else>
    /* Configure Wait States */
    PRECONbits.PFMWS = ${CONFIG_PRECON_PFMWS};
</#if>
