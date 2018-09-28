Example Names:
    qspi_xip

xip_image application Description:
    This example is used to generate a xip image hex pattern to run from the On-Board
    QSPI Flash (SST26VF032B) memory device.

    It uses a custom linker file to place the binary generated into the QSPI Flash memory region.

Modules Used:
    - SYSTICK Peripheral Library

xip_main application Description:
    This example application shows how to use QSPI PLIB to program and execute xip_image_pattern
    example built to run from On-Board QSPI Flash (SST26VF032B) memory device.

    Once program and verification is successfull, It jumps to the reset handler of xip_image application
    programed in QSPI Flash memory to perform execute in place.

Modules Used:
    - QSPI Peripheral Library

Hardware Used:
    - SAM E70 Xplained Ultra Evaluation Kit

Setup:
    - Enable MPU for QSPI FLASH memory region
    - xip_image_pattern_hex to be programmed should be generated using xip_image example.

Running the Example:
    - Build the xip_image example using MPLABX IDE and do not program.

    - Run xip_image_pattern_gen.py script to generate xip_image_pattern_hex.h
        python xip_image_pattern_gen.py ./xip_image/firmware/sam_e70_xult.X/dist/default/production/sam_e70_xult.X.production.bin

    - Copy the generated xip_image_pattern_hex.h to ./xip_main/firmware/src/config/sam_e70_xult to be programmed
      and executed from QSPI flash memory.

    - Program and run the xip_main example code using MPLABX

    - Observe on board LED1.
        - If LED1 is blinking, data written on the memory matches with expected data.
        - If LED1 is continuously ON, there was some error

Related Example Projects:
    qspi_read_write