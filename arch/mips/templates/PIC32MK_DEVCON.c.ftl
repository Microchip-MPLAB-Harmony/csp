
    /* Configure CP0.K0 for optimal performance (cached instruction pre-fetch) */
    __builtin_mtc0(16, 0,(__builtin_mfc0(16, 0) | 0x3));

    /* Configure Wait States and Prefetch */
    CHECONbits.PFMWS = ${CONFIG_CHECON_PFMWS};
    CHECONbits.PREFEN = ${CONFIG_CHECON_PREFEN};
