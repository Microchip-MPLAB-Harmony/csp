# DMA\_TRANSFER\_EVENT Typedef and Macros

**Parent topic:**[Direct Memory Access Controller \(DMA\)](GUID-FC435976-A639-435D-9C8F-0A08C3D59195.md)

## C

```c
typedef uint32_t DMA_TRANSFER_EVENT;

/* Block was transferred successfully. */
#define DMA_TRANSFER_EVENT_BLOCK_TRANSFER_COMPLETE          0x01

/* Error while processing the request */
#define DMA_TRANSFER_EVENT_ERROR                            0x02

/* An start trigger event has been detected and the block transfer has started */
#define DMA_TRANSFER_EVENT_START_DETECTED                   0x04

/* An abort trigger event has been detected and the DMA transfer has been aborted */
#define DMA_TRANSFER_EVENT_TRANSFER_ABORTED                 0x08

/* A cell transfer has been completed (CSZ bytes has been transferred) */
#define DMA_TRANSFER_EVENT_CELL_TRANSFER_COMPLETE           0x10

/* A half block transfer has been completed */
#define DMA_TRANSFER_EVENT_HALF_BLOCK_TRANSFER_COMPLETE     0x20

/* A link list done event has been completed */
#define DMA_TRANSFER_EVENT_LINKED_LIST_TRANSFER_COMPLETE    0x40
```

## Summary

Defines the data type for DMA\_TRANSFER\_EVENT and its macros

## Description

Defines data type and macros for the DMA transfer event.

## Remarks

None.

