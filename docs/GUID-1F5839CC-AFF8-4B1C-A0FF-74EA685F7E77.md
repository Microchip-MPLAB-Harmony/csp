# CACHE\_CacheClean Function

**Parent topic:**[Cache Controller \(Cache\)](GUID-FA7730F3-DFC4-4DED-92DE-B53A0AF23AC6.md)

## C

```c
void CACHE_CacheClean(uint32_t addr, size_t len)
```

## Summary

Write back and invalidate an address range in either cache.

## Description

Write back \(data\) and invalidate \(data and address\) an address range in either cache.

## Parameters

|Param|Description|
|-----|-----------|
|uint32\_t addr|address \(aligned to 32-byte boundary\)|
|size\_t len|size of memory block \(in number of bytes\)|

## Returns

None.

## Example

```c
CACHE_CacheClean(addr, len);
```

## Remarks

None.

