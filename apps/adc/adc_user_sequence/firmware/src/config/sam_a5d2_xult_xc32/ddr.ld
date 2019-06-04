/* ----------------------------------------------------------------------------
 *         SAM Software Package License
 * ----------------------------------------------------------------------------
 * Copyright (c) 2015, Atmel Corporation
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * - Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the disclaimer below.
 *
 * Atmel's name may not be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * DISCLAIMER: THIS SOFTWARE IS PROVIDED BY ATMEL "AS IS" AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT ARE
 * DISCLAIMED. IN NO EVENT SHALL ATMEL BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
 * OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * ----------------------------------------------------------------------------
 */

/*------------------------------------------------------------------------------
 *      Linker script for running in internal DDRAM on the SAMA5-MIURA
 *----------------------------------------------------------------------------*/

OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
OUTPUT_ARCH(arm)
ENTRY(entry)
SEARCH_DIR(.)

/* Memory Spaces Definitions */
MEMORY
{
	sram        (!RWX) : ORIGIN = 0x200000,   LENGTH = 128K /* sram */
	ram         (RWX) : ORIGIN = 0x21000000, LENGTH = 496M  /* ram */
	ram_nocache  (!RWX) : ORIGIN = 0x20000000, LENGTH = 16M  /* ram (non-cached) */
}

/* Sizes of the stacks used by the application. NOTE: you need to adjust */
C_STACK_SIZE   = 4096;
IRQ_STACK_SIZE = 96;
FIQ_STACK_SIZE = 96;
SYS_STACK_SIZE = 64;
ABT_STACK_SIZE = 64;
UND_STACK_SIZE = 64;
HEAP_SIZE      = 512;

/* Section Definitions */
SECTIONS
{
	.text 0x26F00000 :
	{
		. = ALIGN(4);
		_sfixed = .;
		*(.textEntry)
		*(.text .text.* .gnu.linkonce.t.*)
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
		*(.data .data.*);
		. = ALIGN(4);
		_efixed = .;            /* End of text section */
	} >ram

	/* .ARM.exidx is sorted, so has to go in its own output section.  */
	PROVIDE_HIDDEN (__exidx_start = .);
	.ARM.exidx :
	{
		*(.ARM.exidx* .gnu.linkonce.armexidx.*)
	} >ram
	PROVIDE_HIDDEN (__exidx_end = .);

	/* _etext must be just before .relocate section */
	. = ALIGN(4);
	_etext = .;

	.relocate :
	{
		. = ALIGN(4);
		_srelocate = .;
		KEEP(*(.vectors .vectors.*))
		*(.ramfunc)
		. = ALIGN(4);
		_erelocate = .;
	} >sram AT>ram

	/* Please see drivers/mm/cache.h for details on the "Cache-aligned" sections */

	.region_cache_aligned_const :
	{
		. = ALIGN(32);
		*(.region_cache_aligned_const)
		. = ALIGN(32);
	} >ram

	.region_sram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_sram)
	} >sram

	.region_ram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_ram)
	} >ram

	.region_nocache (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_nocache)
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
	} >ram

	/* Please see drivers/mm/cache.h for details on the "Cache-aligned" sections */

	.region_cache_aligned (NOLOAD) :
	{
		. = ALIGN(32);
		*(.region_cache_aligned)
		. = ALIGN(32);
	} >ram

	.heap (NOLOAD) :
	{
		. = ALIGN(4);
		__heap_start__ = .;
		. += HEAP_SIZE;
		__heap_end__ = .;
	} >ram

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

		. += SYS_STACK_SIZE;
		. = ALIGN(8);
		_sysstack = .;

		. += C_STACK_SIZE;
		. = ALIGN(8);
		_cstack = .;
	} >ram
}
