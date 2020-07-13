<#if core.COMPILER_CHOICE == "XC32" && (!STDIN_BUFF_MODE || !STDOUT_BUFF_MODE)>
    STDIO_BufferModeSet();

</#if>