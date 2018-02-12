#include "arch/arm/arm_cm_mpu.h"

<#macro MPU_CONFIG region address size attribute access xn enable share>
	MPU->RBAR = MPU_REGION( ${region},  ${address});
	MPU->RASR = MPU_REGION_SIZE(${size}) \
				| MPU_RASR_AP(${access}) \
				| ${attribute} \
				<#if xn == 'true'>
				| MPU_ATTR_EXECUTE_NEVER
				</#if>
				<#if enable == 'true'>
				| MPU_ATTR_ENABLE \
				</#if>
				<#if share == 'true'>
				| MPU_ATTR_SHAREABLE \
				</#if>
				;
				
</#macro>

void mpu_configure(const void* config)
{
<#if MPU_Region_0 == true>
    <@MPU_CONFIG 
		region = 0
		address = "${MPU_Region_0_Address}"
		size = "${MPU_Region_0_Size}"
		attribute = "${MPU_Region_0_Attribute}"
		access = "${MPU_Region_0_Access}"
		xn = "${MPU_Region_0_XN?c}"
		enable = "${MPU_Region_0_Enable?c}" 
		share =  "${MPU_Region_0_S?c}"
	/>  
</#if>
<#if MPU_Region_1 == true>
    <@MPU_CONFIG 
		region = 1
		address = "${MPU_Region_1_Address}"
		size = "${MPU_Region_1_Size}"
		attribute = "${MPU_Region_1_Attribute}"
		access = "${MPU_Region_1_Access}"
		xn = "${MPU_Region_1_XN?c}"
		enable = "${MPU_Region_1_Enable?c}" 
		share =  "${MPU_Region_1_S?c}"
	/>  
</#if>
<#if MPU_Region_2 == true>
    <@MPU_CONFIG 
		region = 2
		address = "${MPU_Region_2_Address}"
		size = "${MPU_Region_2_Size}"
		attribute = "${MPU_Region_2_Attribute}"
		access = "${MPU_Region_2_Access}"
		xn = "${MPU_Region_2_XN?c}"
		enable = "${MPU_Region_2_Enable?c}" 
		share =  "${MPU_Region_2_S?c}"
	/>  
</#if>
<#if MPU_Region_3 == true>
    <@MPU_CONFIG 
		region = 3
		address = "${MPU_Region_3_Address}"
		size = "${MPU_Region_3_Size}"
		attribute = "${MPU_Region_3_Attribute}"
		access = "${MPU_Region_3_Access}"
		xn = "${MPU_Region_3_XN?c}"
		enable = "${MPU_Region_3_Enable?c}" 
		share =  "${MPU_Region_3_S?c}"
	/>  
</#if>
<#if MPU_Region_4 == true>
    <@MPU_CONFIG 
		region = 4
		address = "${MPU_Region_4_Address}"
		size = "${MPU_Region_4_Size}"
		attribute = "${MPU_Region_4_Attribute}"
		access = "${MPU_Region_4_Access}"
		xn = "${MPU_Region_4_XN?c}"
		enable = "${MPU_Region_4_Enable?c}" 
		share =  "${MPU_Region_4_S?c}"
	/>  
</#if>
<#if MPU_Region_5 == true>
    <@MPU_CONFIG 
		region = 5
		address = "${MPU_Region_5_Address}"
		size = "${MPU_Region_5_Size}"
		attribute = "${MPU_Region_5_Attribute}"
		access = "${MPU_Region_5_Access}"
		xn = "${MPU_Region_5_XN?c}"
		enable = "${MPU_Region_5_Enable?c}" 
		share =  "${MPU_Region_5_S?c}"
	/>   
</#if>
<#if MPU_Region_6 == true>
    <@MPU_CONFIG 
		region = 6
		address = "${MPU_Region_6_Address}"
		size = "${MPU_Region_6_Size}"
		attribute = "${MPU_Region_6_Attribute}"
		access = "${MPU_Region_6_Access}"
		xn = "${MPU_Region_6_XN?c}"
		enable = "${MPU_Region_6_Enable?c}" 
		share =  "${MPU_Region_6_S?c}"
	/> 
</#if>
<#if MPU_Region_7 == true>
    <@MPU_CONFIG 
		region = 7
		address = "${MPU_Region_7_Address}"
		size = "${MPU_Region_7_Size}"
		attribute = "${MPU_Region_7_Attribute}"
		access = "${MPU_Region_7_Access}"
		xn = "${MPU_Region_7_XN?c}"
		enable = "${MPU_Region_7_Enable?c}" 
		share =  "${MPU_Region_7_S?c}"
	/>   
</#if>
<#if MPU_Region_8 == true>
    <@MPU_CONFIG 
		region = 8
		address = "${MPU_Region_8_Address}"
		size = "${MPU_Region_8_Size}"
		attribute = "${MPU_Region_8_Attribute}"
		access = "${MPU_Region_8_Access}"
		xn = "${MPU_Region_8_XN?c}"
		enable = "${MPU_Region_8_Enable?c}" 
		share =  "${MPU_Region_8_S?c}"
	/> 
</#if>
<#if MPU_Region_9 == true>
    <@MPU_CONFIG 
		region = 9
		address = "${MPU_Region_9_Address}"
		size = "${MPU_Region_9_Size}"
		attribute = "${MPU_Region_9_Attribute}"
		access = "${MPU_Region_9_Access}"
		xn = "${MPU_Region_9_XN?c}"
		enable = "${MPU_Region_9_Enable?c}" 
		share =  "${MPU_Region_9_S?c}"
	/>  
</#if>
<#if MPU_Region_10 == true>
    <@MPU_CONFIG 
		region = 10
		address = "${MPU_Region_10_Address}"
		size = "${MPU_Region_10_Size}"
		attribute = "${MPU_Region_10_Attribute}"
		access = "${MPU_Region_10_Access}"
		xn = "${MPU_Region_10_XN?c}"
		enable = "${MPU_Region_10_Enable?c}" 
		share =  "${MPU_Region_10_S?c}"
	/>  
</#if>
<#if MPU_Region_11 == true>
    <@MPU_CONFIG 
		region = 11
		address = "${MPU_Region_11_Address}"
		size = "${MPU_Region_11_Size}"
		attribute = "${MPU_Region_11_Attribute}"
		access = "${MPU_Region_11_Access}"
		xn = "${MPU_Region_11_XN?c}"
		enable = "${MPU_Region_11_Enable?c}" 
		share =  "${MPU_Region_11_S?c}"
	/> 
</#if>
<#if MPU_Region_12 == true>
    <@MPU_CONFIG 
		region = 12
		address = "${MPU_Region_12_Address}"
		size = "${MPU_Region_12_Size}"
		attribute = "${MPU_Region_12_Attribute}"
		access = "${MPU_Region_12_Access}"
		xn = "${MPU_Region_12_XN?c}"
		enable = "${MPU_Region_12_Enable?c}" 
		share =  "${MPU_Region_12_S?c}"
	/>  
</#if>
<#if MPU_Region_13 == true>
    <@MPU_CONFIG 
		region = 13
		address = "${MPU_Region_13_Address}"
		size = "${MPU_Region_13_Size}"
		attribute = "${MPU_Region_13_Attribute}"
		access = "${MPU_Region_13_Access}"
		xn = "${MPU_Region_13_XN?c}"
		enable = "${MPU_Region_13_Enable?c}" 
		share =  "${MPU_Region_13_S?c}"
	/>  
</#if>
<#if MPU_Region_14 == true>
    <@MPU_CONFIG 
		region = 14
		address = "${MPU_Region_14_Address}"
		size = "${MPU_Region_14_Size}"
		attribute = "${MPU_Region_14_Attribute}"
		access = "${MPU_Region_14_Access}"
		xn = "${MPU_Region_14_XN?c}"
		enable = "${MPU_Region_14_Enable?c}" 
		share =  "${MPU_Region_14_S?c}"
	/>  
</#if>
<#if MPU_Region_15 == true>
    <@MPU_CONFIG 
		region = 15
		address = "${MPU_Region_15_Address}"
		size = "${MPU_Region_15_Size}"
		attribute = "${MPU_Region_15_Attribute}"
		access = "${MPU_Region_15_Access}"
		xn = "${MPU_Region_15_XN?c}"
		enable = "${MPU_Region_15_Enable?c}" 
		share =  "${MPU_Region_15_S?c}"
	/> 
</#if>
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
