# FCW\_IsBusy Function

**Parent topic:**[Flash Write Control \(FCW\)](GUID-90E21DD6-5AB3-4211-8633-884EC95A6246.md)

## C

```c
bool FCW_IsBusy( void )
```

## Summary

Returns the current status of FCW controller.

## Description

This function returns the busy status of the FCW Controller. This function should be called to check for module readiness before initiating a Erase or a Write operation.

The controller becomes busy on a FCW Write, Erase. Once initiated, this function can be called to poll the completion of the Erase or Write operation.

This function can be used as an alternative to the callback function. In that, the application can call this function periodically to check for<br />operation completion instead of waiting for callback to be called.

## Precondition

None.

## Parameters

None

## Returns

*true* - FCW controller is busy.

*false* - FCW controller is ready for a new operation.

## Example

```c
// Erase the row. This will erase all the pages in the row.
FCW_PageErase(0xC088608U);

while(FCW_IsBusy());

// Now write the page.
FCW_RowWrite((uint32_t *)buffer, 0xC088608U);

while(FCW_IsBusy());

```

## Remarks

None

