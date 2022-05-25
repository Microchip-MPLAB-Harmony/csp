/*------------------------------------------------------------------------------
 *      Linker script for running in internal DDRAM on the SAM9
 *----------------------------------------------------------------------------*/

OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
OUTPUT_ARCH(arm)
ENTRY(entry)
SEARCH_DIR(.)

/* Memory Spaces Definitions */
MEMORY
{
	sram        (WX) : ORIGIN = 0x300000,   LENGTH = 64K  /* sram */
	ram         (LWX!R) : ORIGIN = ${DDRAM_CACHE_START_ADDR}, LENGTH = ${DDRAM_CACHE_SIZE}  /* ram */
	ram_nocache  (!RWX) : ORIGIN = ${DDRAM_NO_CACHE_START_ADDR}, LENGTH = ${DDRAM_NO_CACHE_SIZE}  /* ram (non-cached) */
	rom         (LRX) : ORIGIN = 0, LENGTH = 0
}

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

/* Section Definitions */
SECTIONS
{
	.text ${APP_START_ADDRESS} :
	{
		. = ALIGN(4);
		PROVIDE(_sfixed = .);
		*(.textEntry)
		*(.text .text.* .gnu.linkonce.t.*)
		*(.rodata .rodata* .gnu.linkonce.r.*)
		*(.ARM.extab* .gnu.linkonce.armextab.*)

		. = ALIGN(4);
		KEEP(*(.init))
		. = ALIGN(4);
		PROVIDE(__preinit_array_start = .);
		KEEP(*(.preinit_array))
		PROVIDE(__preinit_array_end = .);

		. = ALIGN(4);
		PROVIDE(__init_array_start = .);
		KEEP(*(SORT(.init_array.*)))
		KEEP(*(.init_array))
		PROVIDE(__init_array_end = .);

		. = ALIGN(0x4);
		KEEP(*crtbegin.o(.ctors))
		KEEP(*(EXCLUDE_FILE (*crtend.o) .ctors))
		KEEP(*(SORT(.ctors.*)))
		KEEP(*crtend.o(.ctors))

		. = ALIGN(4);
		KEEP(*(.fini))

		. = ALIGN(4);
		PROVIDE(__fini_array_start = .);
		KEEP(*(.fini_array))
		KEEP(*(SORT(.fini_array.*)))
		PROVIDE(__fini_array_end = .);

		KEEP(*crtbegin.o(.dtors))
		KEEP(*(EXCLUDE_FILE (*crtend.o) .dtors))
		KEEP(*(SORT(.dtors.*)))
		KEEP(*crtend.o(.dtors))

	    *(.dinit*)
		. = ALIGN(4);
	} >ram

	.data :
    {
		*(.data .data.*);
		. = ALIGN(4);
		PROVIDE(_efixed = .);            /* End of text section */
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
	PROVIDE(_etext = .);

	.relocate :
	{
		. = ALIGN(4);
		PROVIDE(_srelocate = .);
		KEEP(*(.vectors .vectors.*))
		*(.ramfunc)
		. = ALIGN(4);
		PROVIDE(_erelocate = .);
	} >sram AT>ram

	.region_cache_aligned_const :
	{
		. = ALIGN(32);
		*(.region_cache_aligned_const .region_cache_aligned_const.*)
		. = ALIGN(32);
	} >ram

	.region_sram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_sram .region_sram.*)
	} >sram

	.region_ram (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_ram .region_ram.*)
	} >ram

	.region_nocache (NOLOAD) :
	{
		. = ALIGN(4);
		*(.region_nocache .region_nocache.*)
	} >ram_nocache

	/* .bss section which is used for uninitialized data */
	.bss (NOLOAD) :
	{
		. = ALIGN(4);
		PROVIDE(_szero = .);
		*(.bss .bss.*)
		*(COMMON)
		. = ALIGN(4);
		PROVIDE(_ezero = .);
	} >ram

<#if USE_THREADX_VECTORS>
	PROVIDE (end = .);
	_end = .;

</#if>
	.region_cache_aligned (NOLOAD) :
	{
		. = ALIGN(32);
		*(.region_cache_aligned .region_cache_aligned.*)
		. = ALIGN(32);
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

		. += SVC_STACK_SIZE;
		. = ALIGN(8);
		_svcstack = .;

		. += C_STACK_SIZE;
		. = ALIGN(8);
		_cstack = .;
	} >ram

	_end = .;
	_ramcode_lma = _end;
	.ramcode :
	AT ( _ramcode_lma )
	{
		_sramcode = .; *(.ramcode_section .ramcode_section.*); _eramcode = .;
	} > sram
	_ramdata_lma = _end + _eramcode - _sramcode;
	.ramdata :
	AT ( _ramdata_lma )
	{
		_sramdata = .; *(.ramdata_section .ramdata_section.*); _eramdata = .;
	} > sram
}
