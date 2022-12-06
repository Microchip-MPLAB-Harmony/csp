<#compress>
<#assign DEVIATE_COUNT = 0>
<#if !STDIN_BUFF_MODE>
<#assign DEVIATE_COUNT = DEVIATE_COUNT + 1>
</#if>
<#if !STDOUT_BUFF_MODE>
<#assign DEVIATE_COUNT = DEVIATE_COUNT + 1>
</#if>
</#compress>
<#if core.COMPILER_CHOICE == "XC32" && DEVIATE_COUNT gt 0>

/*******************************************************************************
  Function:
    void STDIO_BufferModeSet ( void )

  Summary:
    Sets the buffering mode for stdin and stdout

  Remarks:
 ********************************************************************************/
static void STDIO_BufferModeSet(void)
{
    /* MISRAC 2012 deviation block start */
    /* MISRA C-2012 Rule 21.6 deviated ${DEVIATE_COUNT} times in this file.  Deviation record ID -  H3_MISRAC_2012_R_21_6_DR_3 */
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    #pragma coverity compliance block deviate "MISRA C-2012 Rule 21.6" "H3_MISRAC_2012_R_21_6_DR_3"

</#if>
<#if !STDIN_BUFF_MODE>

    /* Make stdin unbuffered */
    setbuf(stdin, NULL);
</#if>
<#if !STDOUT_BUFF_MODE>

    /* Make stdout unbuffered */
    setbuf(stdout, NULL);
</#if>
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>

    #pragma coverity compliance end_block "MISRA C-2012 Rule 21.6"
    #pragma GCC diagnostic pop
</#if>
}
</#if>