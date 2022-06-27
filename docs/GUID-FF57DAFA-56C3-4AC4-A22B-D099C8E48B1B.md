# HSMCI\_CommandErrorGet Function

**Parent topic:**[High Speed MultiMedia Card Interface \(HSMCI\)](GUID-E5CEFDBB-10FA-4C89-AAAF-A8ED4107A071.md)

## C

```c
uint16_t HSMCI_CommandErrorGet(void)
```

## Summary

Returns the errors associated with a command transfer.

## Description

Returns the errors associated with a command transfer. For a command<br />transfer, the returned value is a bit wise ORing of the following errors,<br />defined in the HSMCI\_ERROR\_FLAGS enum.

The error flags are cleared after a call to this API.

## Precondition

A command must have been initiated using the HSMCI\_CommandSend\(\) function.

## Parameters

None.

## Returns

Bit wise OR of the command error flags defined under the enum HSMCI\_ERROR\_FLAGS - HSMCI\_CMD\_TIMEOUT\_ERROR, HSMCI\_CMD\_CRC\_ERROR, HSMCI\_CMD\_END\_BIT\_ERROR, HSMCI\_CMD\_INDEX\_ERROR.

## Example

```c
uint16_t cmd_error = HSMCI_CommandErrorGet();

if (cmd_error & (HSMCI_CMD_TIMEOUT_ERROR | HSMCI_CMD_CRC_ERROR |
HSMCI_CMD_END_BIT_ERROR | HSMCI_CMD_INDEX_ERROR))
{
    // Handle command error
}
```

## Remarks

None.

