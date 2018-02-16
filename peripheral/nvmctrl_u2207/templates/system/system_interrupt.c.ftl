<#if NVMCTRL_INTERRUPT_MODE == true>
void NVMCTRL_Handler(void)
{
    NVMCTRL${NVMCTRL_INDEX}_InterruptHandler();
}
</#if>
