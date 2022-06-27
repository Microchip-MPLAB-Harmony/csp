# Cache Controller \(Cache\)

This library provides a brief overview of the L1 Cache peripheral in the PIC32MZ family of devices.

The L1 cache is divided into two parts, a Data Cache \(D-cache\) and an Instruction Cache \(I-cache\). These blocks of high-speed memory both serve to compensate for the lengthy access time of main memory, by fetching instructions and data for the CPU ahead of time. The CPU can then access the information directly through the cache in a single clock cycle, rather than having to wait multiple clock cycles for accesses to main memory. The L1 cache provides a drastic increase in performance, but the user must be aware of hazards that exist when using the cache.

**Using The Library**

Cache Coherency

Cache coherency is the discipline of ensuring that the data stored in main memory matches the corresponding data in the cache. The majority of the cache-related APIs deal with cache coherency. These functions allow the user to flush, clean and invalidate entire cache\(s\), or just a range of addresses within the cache.

Caches most often lose coherency when a bus master other than the CPU modifies memory. This happens frequently with DMA. Two examples are provided in the following section.

Example 1:

Imagine a situation where you would like to transfer data from a source buffer to a destination buffer using DMA. You would write data to the source buffer, start the DMA transfer, and then expect that the same data now appears in the destination buffer. With the cache in write-back mode \(the default mode for the PIC32MZ family\), this will not be the case. When transferring data out of memory using DMA, it is possible that the desired data is held in the D-cache, but has never been written back to main memory. Therefore, in this case, you write data to the source buffer and it gets stored in cache. When the DMA transfer executes, it will pull the data from the source buffer out of RAM and then transfer it to the destination buffer in RAM. The problem is that the fresh data was stored in the cache but never written back to RAM, so what has happened is that stale data was copied over rather than the intended data. What is needed is a way to force the cache to write its data back to main memory before the DMA transfer. This is known as a write-back operation and would be performed with the use of the function:

```c
CACHE_DataCacheClean(uint32_t addr, size_t len)
```

Example 2:

The second situation involves writing data into memory using DMA. Imagine that the cache is holding a chunk of data known as destination\_buffer. You then execute a DMA transfer to copy some new data from a source buffer into destination\_buffer. The issue here is that main memory now contains the correct data, but the cache holds a copy of stale data for destination\_buffer. The CPU cannot see this problem and it will keep pulling the data out of the cache, not even realizing that it’s stale. What is needed is a way to tell the cache to pull the fresh data out of main memory, to replace the stale data that the cache contains. This is known as an invalidate operation. It is performed with the use of the function:

```c
CACHE_DataCacheInvalidate(uint32_t addr, size_t len)
```

The below example application shows how to use the cache maintenance APIs to avoid issues related to cache coherency when the data cache is enabled.

The application uses the USART and the DMA PLIBs to demonstrate the cache maintenance APIs provided by the Cache peripheral library. It registers a callback with the DMA transmit and receive channels. The application first transmits a message using the DMA transmit channel and then schedules a read of ten characters using the DMA receive channel. Once the DMA read is complete, it reads the received data and echoes the same on the terminal using the DMA transmit channel.

The application calls the DCACHE\_CLEAN\_BY\_ADDR API on the write buffer before transmitting it. Calling this API copies the data from the cache memory to the main memory, thereby ensuring that the DMA peripheral uses the updated values in the write buffer.

The application calls the DCACHE\_INVALIDATE\_BY\_ADDR API on the read buffer after reception of data is complete by the DMA receive channel. Calling this API invalidates the cache region corresponding to the read buffer, thereby ensuring that the CPU reads the updated values in the read buffer from the main memory and into the cache.

The cache maintenance operations are always performed on a cache line \(1 cache line = 32 bytes\), the read and write buffers must be aligned to a 32 byte boundary and must be a multiple of 32 bytes. For the same reason, the number of received and echoed back bytes is 10, the size of the receive and echo buffers is 32 bytes.

```c
#define READ_SIZE               10
#define BUFFER_SIZE             (2*CACHE_LINE_SIZE)     // Buffer size in terms of cache lines

char __attribute__ ((aligned (16))) messageStart[] = "**** CACHE maintenance demo with UART ****\r\n\
**** Type a buffer of 10 characters and observe it echo back ****\r\n\
**** LED toggles on each time the buffer is echoed ****\r\n";
char __attribute__ ((aligned (16))) receiveBuffer[BUFFER_SIZE] = {};
char __attribute__ ((aligned (16))) echoBuffer[BUFFER_SIZE] = {};

bool writeStatus  = false;
bool readStatus   = false;

void TX_DMAC_Callback(DMAC_TRANSFER_EVENT status, uintptr_t contextHandle)
{
    writeStatus = true;
}

void RX_DMAC_Callback(DMAC_TRANSFER_EVENT status, uintptr_t contextHandle)
{
    readStatus = true;
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    /* Register callback functions for both write and read contexts */
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_0, TX_DMAC_Callback, 0);
    DMAC_ChannelCallbackRegister(DMAC_CHANNEL_1, RX_DMAC_Callback, 1);

    DCACHE_CLEAN_BY_ADDR((uint32_t)messageStart, sizeof(messageStart));

    DMAC_ChannelTransfer(DMAC_CHANNEL_0, &messageStart, sizeof(messageStart), (const void *)&U2TXREG, 1, 1);

    while(1)
    {
        if(readStatus == true)
        {
            readStatus = false;

            memcpy(echoBuffer, receiveBuffer, READ_SIZE);
            echoBuffer[READ_SIZE] = '\r';
            echoBuffer[(READ_SIZE + 1)] = '\n';

            DCACHE_CLEAN_BY_ADDR((uint32_t)echoBuffer, sizeof(echoBuffer));

            DMAC_ChannelTransfer(DMAC_CHANNEL_0, echoBuffer, READ_SIZE+2, (const void *)&U2TXREG, 1, 1);
        }
        else if(writeStatus == true)
        {
            writeStatus = false;

            /* Invalidate cache lines having received buffer before using it
             * to load the latest data in the actual memory to the cache */
            DCACHE_INVALIDATE_BY_ADDR((uint32_t)receiveBuffer, sizeof(receiveBuffer));

            DMAC_ChannelTransfer(DMAC_CHANNEL_1, (const void *)&U2RXREG, 1, receiveBuffer, READ_SIZE, 1);
        }
    }

      /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

Cache Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|CACHE\_CacheInit|Initialize the L1 cache|
|CACHE\_CacheFlush|Flushes the L1 cache|
|CACHE\_DataCacheFlush|Flushes the L1 data cache|
|CACHE\_InstructionCacheFlush|Flushes \(invalidates\) the L1 instruction cache|
|CACHE\_CacheClean|Write back and invalidate an address range in either cache|
|CACHE\_DataCacheClean|Write back and invalidate an address range in the data cache|
|CACHE\_DataCacheInvalidate|Invalidate an address range in the data cache|
|CACHE\_InstructionCacheInvalidate|Invalidate an address range in the instruction cache|
|CACHE\_InstructionCacheLock|Fetch and lock a block of instructions in the instruction cache|
|CACHE\_DataCacheLock|Fetch and lock a block of data in the data cache|
|CACHE\_CacheSync|Synchronize the instruction and data caches|
|CACHE\_CacheCoherencySet|Set the cache coherency attribute for kseg0|
|CACHE\_CacheCoherencyGet|Returns the current cache coherency attribute for kseg0|
|CACHE\_DataCacheAssociativityGet|Returns the number of ways in the data cache|
|CACHE\_InstructionCacheAssociativityGet|Returns the number of ways in the instruction cache|
|CACHE\_DataCacheLineSizeGet|Returns the data cache line size|
|CACHE\_InstructionCacheLineSizeGet|Returns the instruction cache line size|
|CACHE\_DataCacheLinesPerWayGet|Returns the number of lines per way in the data cache|
|CACHE\_InstructionCacheLinesPerWayGet|Returns the number of lines per way in the instruction cache|
|CACHE\_DataCacheSizeGet|Returns the total number of bytes in the data cache|
|CACHE\_InstructionCacheSizeGet|Returns the total number of bytes in the instruction cache|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|CACHE\_COHERENCY|Enum|L1 cache coherency settings|

-   **[CACHE\_InstructionCacheSizeGet Function](GUID-88ADBA40-9BD1-4259-A736-0DC921C69977.md)**  

-   **[CACHE\_InstructionCacheLock Function](GUID-406EBF09-C00D-416C-9732-012F3A54246B.md)**  

-   **[CACHE\_InstructionCacheLinesPerWayGet Function](GUID-0F046B08-6703-4BF8-BB33-09E8D51AB67A.md)**  

-   **[CACHE\_InstructionCacheLineSizeGet Function](GUID-CB8F81AE-5DCA-4B50-9E3F-8BA271D4D5AF.md)**  

-   **[CACHE\_InstructionCacheInvalidate Function](GUID-B2B4DE8C-4C15-4A66-B4A8-27A972ED505B.md)**  

-   **[CACHE\_InstructionCacheFlush Function](GUID-A4E4D79B-366F-4402-9A38-900614A256F1.md)**  

-   **[CACHE\_InstructionCacheAssociativityGet Function](GUID-64FB2CD6-273D-47B0-B98C-D65AA6A76C47.md)**  

-   **[CACHE\_DataCacheSizeGet Function](GUID-423F53DC-1EFF-451A-A604-72B0C1856D1E.md)**  

-   **[CACHE\_DataCacheLock Function](GUID-2041F826-EFB4-42CD-815C-ACA333D96087.md)**  

-   **[CACHE\_DataCacheLinesPerWayGet Function](GUID-F44B9961-E15B-4ADE-94FF-E907074944D9.md)**  

-   **[CACHE\_DataCacheLineSizeGet Function](GUID-CC71ADE4-170D-44BB-BDD2-9AB4F48A8500.md)**  

-   **[CACHE\_DataCacheInvalidate Function](GUID-F3886AD1-391C-466F-A741-8DBC16B494F9.md)**  

-   **[CACHE\_DataCacheFlush Function](GUID-18D154AC-263D-452D-929F-4BF278B205E0.md)**  

-   **[CACHE\_DataCacheClean Function](GUID-E74B33FD-9275-4F0D-8385-8DADC62D20CB.md)**  

-   **[CACHE\_DataCacheAssociativityGet Function](GUID-F2FF7FF0-4D15-4B3D-8AC9-34F5FBAA9712.md)**  

-   **[CACHE\_COHERENCY Enum](GUID-664788EE-AE26-4ADF-8906-14D7F3977496.md)**  

-   **[CACHE\_CacheSync Function](GUID-0B020914-2272-4921-A235-6772BFA45639.md)**  

-   **[CACHE\_CacheInit Function](GUID-939D0124-1068-40B3-BBED-BFE846A51D56.md)**  

-   **[CACHE\_CacheFlush Function](GUID-9FE1C8A1-0A0E-422C-9FF1-E51C034A4B19.md)**  

-   **[CACHE\_CacheCoherencySet Function](GUID-49BC7678-B982-4316-B57A-CE2DEE6A90AF.md)**  

-   **[CACHE\_CacheCoherencyGet Function](GUID-2CF68EFD-A3FC-4882-B550-95FB36F91101.md)**  

-   **[CACHE\_CacheClean Function](GUID-1F5839CC-AFF8-4B1C-A0FF-74EA685F7E77.md)**  


**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

**Parent topic:**[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)

