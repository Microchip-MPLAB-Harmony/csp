<#if PRODUCT_FAMILY?contains("PIC32CX_BZ3")>
    /* MISRAC 2012 deviation block start */
    /* MISRA C-2012 Rule 11.1 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_11_1_DR_1 */
    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    #pragma coverity compliance block deviate:1 "MISRA C-2012 Rule 11.1" "H3_MISRAC_2012_R_11_1_DR_1"
    </#if>

    /* Configure Prefetch, Wait States by calling the ROM function whose address is available at address 0xF2D0 */
    typedef void (*FUNC_PCHE_SETUP)(uint32_t setup);
    (void)((FUNC_PCHE_SETUP)(*(uint32_t*)0xF2D0))((PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN})  | PCHE_CHECON_ADRWS(${CONFIG_CHECON_ADRWS})));

    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma coverity compliance end_block "MISRA C-2012 Rule 11.1"
    #pragma GCC diagnostic pop
    </#if>
    /* MISRAC 2012 deviation block end */
<#elseif PRODUCT_FAMILY?contains("PIC32CX_BZ2")>
    /* Configure Prefetch, Wait States */
    PCHE_REGS->PCHE_CHECON = (PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN}) | PCHE_CHECON_ADRWS(${CONFIG_CHECON_ADRWS}));
<#elseif PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
    <#if SYS_CLK_FREQ != "128000000">
    /* MISRAC 2012 deviation block start */
    /* MISRA C-2012 Rule 11.1 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_11_1_DR_1 */
    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    #pragma coverity compliance block deviate:1 "MISRA C-2012 Rule 11.1" "H3_MISRAC_2012_R_11_1_DR_1"
    </#if>
    /* Configure Prefetch, Wait States by calling the ROM function whose address is available at address 0xF2D0 */
    typedef void (*FUNC_PCHE_SETUP)(uint32_t setup);
    (void)((FUNC_PCHE_SETUP)(*(uint32_t*)0xF2D0))((PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN}) | PCHE_CHECON_ADRWS(${CONFIG_CHECON_ADRWS})));
    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma coverity compliance end_block "MISRA C-2012 Rule 11.1"
    #pragma GCC diagnostic pop
    </#if>
    /* MISRA C-2012 Rule 11.1 deviation block end */
    </#if>
</#if>