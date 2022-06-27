# SUPC\_WaitModeEnter Function

**Parent topic:**[Supply Controller \(SUPC\)](GUID-78E65C62-E36B-4FDE-9E7C-B7E671C321F5.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-AAEA9536-A589-47D4-B8D4-9C401B40C9AC.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-9BDF339F-E2FE-41C7-96E3-E550DAE91D45.md)

## C

```c
void SUPC_WaitModeEnter
(
WAITMODE_FLASH_STATE flash_lpm,
WAITMODE_WKUP_SOURCE source
);
```

## Summary

Puts the device into Wait mode

## Description

This functions is used to put the device into Wait mode to achieve very low<br />power consumption while maintaining the whole device in a powered state for<br />a startup time of less than 10μs.

In Wait mode, the clocks of the core, peripherals and memories are stopped.<br />However, the core, peripherals and memories power supplies are still<br />powered.

When entering Wait mode, the embedded Flash can be placed in one of the<br />low\_power modes \(Deep\_power\_down or Standby mode\).

Exit from Wait mode occurs as a result of one of the following enabled<br />wakeup events:

-   WKUP0 to WKUP13 pins

-   RTC alarm

-   RTT alarm

-   USB alarm

-   GMAC wake on LAN event


A fast startup is enabled upon the detection of a programmed level on one of<br />the 14 wake-up inputs \(WKUP\) or upon an active alarm from the RTC, RTT and<br />USB Controller. The polarity of the 14 wakeup inputs is programmable by<br />writing the PMC Fast Startup Polarity register \(PMC\_FSPR\).

## Precondition

The peripherals \(RTT, RTC etc\) must be configured to generate wakeup event.

## Parameters

|Param|Description|
|-----|-----------|
|WAITMODE\_FLASH\_STATE|Identifies Flash Low\_power mode|
|WAITMODE\_WKUP\_SOURCE|Identifies possible wakeup input source|

## Returns

None.

## Example

```c
SUPC_WaitModeEnter (PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN, WAITMODE_WKUP_RTC);
```

## Remarks

None.

