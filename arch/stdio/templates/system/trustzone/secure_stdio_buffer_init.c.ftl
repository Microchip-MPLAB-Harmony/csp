<#if core.COMPILER_CHOICE == "XC32" && (!SECURE_STDIN_BUFF_MODE || !SECURE_STDOUT_BUFF_MODE)>

/*******************************************************************************
  Function:
    void STDIO_BufferModeSet ( void )

  Summary:
    Sets the buffering mode for stdin and stdout

  Remarks:
 ********************************************************************************/
static void STDIO_BufferModeSet(void)
{
<#if !SECURE_STDIN_BUFF_MODE>

    /* Make stdin unbuffered */
    setbuf(stdin, NULL);
</#if>
<#if !SECURE_STDOUT_BUFF_MODE>

    /* Make stdout unbuffered */
    setbuf(stdout, NULL);
</#if>
}
</#if>