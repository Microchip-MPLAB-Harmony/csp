# CACHE\_DataCacheAssociativityGet Function

**Parent topic:**[Cache Controller \(Cache\)](GUID-FA7730F3-DFC4-4DED-92DE-B53A0AF23AC6.md)

## C

```c
size_t CACHE_DataCacheAssociativityGet(void)
```

## Summary

Returns the number of ways in the data cache.

## Description

Returns the number of ways in the data cache.

## Parameters

None.

## Returns

*size\_t* - number of ways in the data cache.

## Example

```c
size_t dataCacheSize;
dataCacheSize = CACHE_DataCacheAssociativityGet();
```

## Remarks

None.

