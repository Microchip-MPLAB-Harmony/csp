    /* Configure Prefetch, Wait States */
    PCHE_REGS->PCHE_CHECON = (PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_PREFEN_Msk))) 
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN}));