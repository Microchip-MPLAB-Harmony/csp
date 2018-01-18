#include "arch/arm/arm_cm_mpu.h"

void mpu_configure(const void* config)
{
	uint32_t* values = (uint32_t*)config;

	while (*values != 0)
    {
		MPU->RBAR = *values++;
		MPU->RASR = *values++;
	}
}

int mpu_is_enabled(void)
{
	return (MPU->CTRL & MPU_CTRL_ENABLE_Msk) != 0;
}

void mpu_enable(void)
{
	/* Activate MemFault, BusFault & UsageFault exceptions */
	SCB->SHCSR |= (SCB_SHCSR_MEMFAULTENA_Msk |
	               SCB_SHCSR_BUSFAULTENA_Msk |
	               SCB_SHCSR_USGFAULTENA_Msk);

	/* Enable the MPU without the background region */
	MPU->CTRL = MPU_CTRL_ENABLE_Msk;

    __DSB();
    __ISB();
}

void mpu_disable(void)
{
	MPU->CTRL = 0;
}
