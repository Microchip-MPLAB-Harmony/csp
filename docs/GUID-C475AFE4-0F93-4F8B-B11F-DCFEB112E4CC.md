# PLIB\_L2CC\_InvalidateCache Function

**Parent topic:**[L2 Cache Controller \(L2CC\)](GUID-02165AAF-FFAF-48FC-9A3A-14E414DEB6A6.md)

## C

```c
void PLIB_L2CC_InvalidateCache(void);
```

## Summary

Invalidates L2 cache entries.

## Description

This function will mark all cache entries as invalid.

## Precondition

PLIB\_L2CC\_Initialize has been called.

## Parameters

None.

## Returns

None.

## Example

```c
PLIB_L2CC_InvalidateCache();
```

