<#if core.COMPILER_CHOICE == "XC32" && (!SECURE_STDIN_BUFF_MODE || !SECURE_STDOUT_BUFF_MODE)>
    STDIO_BufferModeSet();

</#if>