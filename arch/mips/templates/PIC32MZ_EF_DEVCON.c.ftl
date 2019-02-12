
    /* Configure Prefetch, Wait States and ECC */
    PRECONbits.PREFEN = ${CONFIG_PRECON_PREFEN};
    PRECONbits.PFMWS = ${CONFIG_PRECON_PFMWS};
    CFGCONbits.ECCCON = ${CONFIG_CFGCON_ECCCON};
