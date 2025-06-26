/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/

/*------------------------------------------------------------------------------
 *      Linker script for running in internal SRAM on the SAMA5D2
 *----------------------------------------------------------------------------*/

OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
OUTPUT_ARCH(arm)
ENTRY(entry)
SEARCH_DIR(.)

/* Memory Spaces Definitions */
MEMORY
{
	sram        (LWX!R) : ORIGIN = 0x200000,   LENGTH = 128K /* sram */
	ram         (W!RX) : ORIGIN = ${DDRAM_CACHE_START_ADDR}, LENGTH = ${DDRAM_CACHE_SIZE}  /* ram */
	ram_nocache  (RWX) : ORIGIN = ${DDRAM_NO_CACHE_START_ADDR}, LENGTH = ${DDRAM_NO_CACHE_SIZE}  /* ram (non-cached) */
}

/* Sizes of the stacks used by the application. NOTE: you need to adjust */
<#lt><#assign USR_STACK_SIZE = XC32_USR_STACK_SIZE!"0x800">
<#lt><#assign FIQ_STACK_SIZE = XC32_FIQ_STACK_SIZE!"0x60">
<#lt><#assign IRQ_STACK_SIZE = XC32_IRQ_STACK_SIZE!"0x60">
<#lt><#assign SVC_STACK_SIZE = XC32_SVC_STACK_SIZE!"0x800">
<#lt><#assign ABT_STACK_SIZE = XC32_ABT_STACK_SIZE!"0x40">
<#lt><#assign UND_STACK_SIZE = XC32_UND_STACK_SIZE!"0x40">
C_STACK_SIZE   = ${USR_STACK_SIZE};
IRQ_STACK_SIZE = ${IRQ_STACK_SIZE};
FIQ_STACK_SIZE = ${FIQ_STACK_SIZE};
SVC_STACK_SIZE = ${SVC_STACK_SIZE};
ABT_STACK_SIZE = ${ABT_STACK_SIZE};
UND_STACK_SIZE = ${UND_STACK_SIZE};
HEAP_SIZE      = ${XC32_HEAP_SIZE};

/* Section Definitions */
SECTIONS
{
	.vectors :
	{
		. = ALIGN(4);
		_sfixed = .;
		KEEP(*(.vectors .vectors.*))
		*(.textEntry)
	} > sram
	.fixed0 :
	{
		*(.text .text.* .gnu.linkonce.t.*)
		*(.glue_7t) *(.glue_7)
		*(.rodata .rodata* .gnu.linkonce.r.*)
		*(.ARM.extab* .gnu.linkonce.armextab.*)

		. = ALIGN(4);
		KEEP(*(.init))
		. = ALIGN(4);
		__preinit_array_start = .;
		KEEP(*(.preinit_array))
		__preinit_array_end = .;

		. = ALIGN(4);
		__init_array_start = .;
		KEEP(*(SORT(.init_array.*)))
		KEEP(*(.init_array))
		__init_array_end = .;

		. = ALIGN(0x4);
		KEEP(*crtbegin.o(.ctors))
		KEEP(*(EXCLUDE_FILE (*crtend.o) .ctors))
		KEEP(*(SORT(.ctors.*)))
		KEEP(*crtend.o(.ctors))

		. = ALIGN(4);
		KEEP(*(.fini))

		. = ALIGN(4);
		__fini_array_start = .;
		KEEP(*(.fini_array))
		KEEP(*(SORT(.fini_array.*)))
		__fini_array_end = .;

		KEEP(*crtbegin.o(.dtors))
		KEEP(*(EXCLUDE_FILE (*crtend.o) .dtors))
		KEEP(*(SORT(.dtors.*)))
		KEEP(*crtend.o(.dtors))
		. = ALIGN(4);
		_efixed = .;            /* End of text section */

		/* no relocation when running from sram */
		_srelocate = .;
		_erelocate = .;
	} >sram

	.data : {
		*(.data .data*);
	} > sram

	/* .ARM.exidx is sorted, so has to go in its own output section.  */
	PROVIDE_HIDDEN (__exidx_start = .);
	.ARM.exidx :
	{
		*(.ARM.exidx* .gnu.linkonce.armexidx.*)
	} >sram
	PROVIDE_HIDDEN (__exidx_end = .);

	. = ALIGN(4);
	_etext = .;

	.region_cache_aligned_const :
	{
		. = ALIGN(32);
		*(.region_cache_aligned_const*)
		. = ALIGN(32);
	} >sram

	.region_sram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_sram*)
	} >sram

	.region_ram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_ram*)
	} >ram

	.region_nocache (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_nocache*)
	} >ram_nocache

	/* .bss section which is used for uninitialized data */
	.bss (NOLOAD) :
	{
		. = ALIGN(4);
		_szero = .;
		*(.bss .bss.*)
		*(COMMON)
		. = ALIGN(4);
		_ezero = .;
	} >sram

	.region_cache_aligned (NOLOAD) :
	{
		. = ALIGN(32);
		*(.region_cache_aligned*)
		. = ALIGN(32);
	} >sram

	.region_ram_cache_aligned (NOLOAD) :
	{
		. = ALIGN(32);
		*(.region_ram_cache_aligned*)
		. = ALIGN(32);
	} >ram

	.heap (NOLOAD) :
	{
		. = ALIGN(4);
		__heap_start__ = .;
		. += HEAP_SIZE;
		__heap_end__ = .;
	} >sram

	.stacks (NOLOAD) :
	{
		. += IRQ_STACK_SIZE;
		. = ALIGN(8);
		_irqstack = .;

		. += FIQ_STACK_SIZE;
		. = ALIGN(8);
		_fiqstack = .;

		. += ABT_STACK_SIZE;
		. = ALIGN(8);
		_abtstack = .;

		. += UND_STACK_SIZE;
		. = ALIGN(8);
		_undstack = .;

		. += SVC_STACK_SIZE;
		. = ALIGN(8);
		_svcstack = .;

		. += C_STACK_SIZE;
		. = ALIGN(8);
		_cstack = .;
	} >sram
}
