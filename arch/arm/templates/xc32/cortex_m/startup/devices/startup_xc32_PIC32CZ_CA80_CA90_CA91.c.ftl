<#if RAM_INIT?? && RAM_INIT == "true">
#ifndef RAM_START_ADDR
#define RAM_START_ADDR FLEXRAM_ADDR
#endif

#if defined ECC_INIT_START
#define START_ADDR  ECC_INIT_START
#else
#define START_ADDR  RAM_START_ADDR
#endif

#ifndef RAM_SIZE
#define RAM_SIZE FLEXRAM_SIZE
#endif

#if defined ECC_INIT_LEN
#define INIT_LEN  ECC_INIT_LEN
#else
#define INIT_LEN  RAM_SIZE
#endif

__STATIC_INLINE void  __attribute__((optimize("-O1"))) __attribute__((always_inline)) RAM_Initialize(void)
{
    register uint64_t *pFlexRam;

    __DSB();
    __ISB();

    // FlexRAM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*)START_ADDR ; pFlexRam < ((uint64_t*)(START_ADDR + INIT_LEN)) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }

    // ITCM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*) ITCM_ADDR ; pFlexRam < (uint64_t*)(ITCM_ADDR + ITCM_SIZE) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }
    // DTCM initialization loop (to handle ECC properly)
    // we need to initialize all of RAM with 64 bit aligned writes
    for (pFlexRam = (uint64_t*) DTCM_ADDR ; pFlexRam < (uint64_t*)(DTCM_ADDR + DTCM_SIZE) ; pFlexRam++)
    {
        *pFlexRam = 0;
    }

    __DSB();
    __ISB();
}
</#if>
