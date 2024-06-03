<#if RAM_INIT??>

<#if TRUSTZONE_SUPPORTED?? >
#if defined(SECURE)
#define RAM_START  ${DEVICE_RAM_START}
#define RAM_END    (RAM_START + ${IDAU_RS_SIZE})
#elif defined(NONSECURE)
#define RAM_START  (${DEVICE_RAM_START} + ${IDAU_RS_SIZE})
#define RAM_END    (RAM_START + ${IDAU_RNS_SIZE})
#endif
<#else>
#define RAM_START  ${DEVICE_RAM_START}
#define RAM_END    (RAM_START + ${DEVICE_RAM_SIZE})
</#if>



__STATIC_INLINE void  __attribute__((optimize("-O1")))  RAM_Initialize(void)
{
    register uint32_t *pSRam;

    __DSB();
    __ISB();

    // SRAM initialization loop (to handle ECC properly)
    // We need to initialize all of SRAM with 32 bit aligned writes
    for (pSRam = (uint32_t*)RAM_START; pSRam < ((uint32_t*)RAM_END) ; pSRam++)
    {
        *pSRam = 0;
    }

    __DSB();
    __ISB();
}
</#if>
