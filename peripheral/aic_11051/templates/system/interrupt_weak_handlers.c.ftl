/* Weak default handler for spurious interrupts */
void __attribute__((weak)) SPURIOUS_INTERRUPT_Handler(void)
{
    static uint32_t spuriousEventCount = 0U;
    ++spuriousEventCount;
}
