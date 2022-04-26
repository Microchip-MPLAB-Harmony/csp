<#if PRODUCT_FAMILY?contains("PIC32CX_BZ3")>
    /* Configure Prefetch, Wait States by calling the ROM function whose address is available at address 0xF2D0 */
    typedef int (*FUNC_PCHE_SETUP)(uint32_t);
    ((FUNC_PCHE_SETUP)(*(uint32_t*)0xF2D0))((PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN})));
<#else>
    /* Configure Prefetch, Wait States */
    PCHE_REGS->PCHE_CHECON = (PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN}));
</#if>