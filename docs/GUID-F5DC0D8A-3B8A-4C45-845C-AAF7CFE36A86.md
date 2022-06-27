# XDMAC\_DESCRIPTOR\_VIEW\_1 Struct

**Parent topic:**[Extensible DMA Controller \(XDMAC\)](GUID-C2B02311-0F9A-41E7-92B8-C2FEEBDFE755.md)

## C

```c
    typedef struct {
        
        /* Next Descriptor Address number. */
        uint32_t mbr_nda;
        
        /* Micro-block Control Member. */
        XDMAC_MICRO_BLOCK_CONTROL mbr_ubc;
        
        /* Source Address Member. */
        uint32_t mbr_sa;
        
        /* Destination Address Member. */
        uint32_t mbr_da;
        
    } XDMAC_DESCRIPTOR_VIEW_1;

```

## Summary

Defines the descriptor view 1 available for master transfer.

## Description

This data type defines the descriptor view 1.

## Remarks

This feature may not be available on all devices. Refer to the specific device data sheet to determine availability.

