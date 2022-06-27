# SUPC\_SelectTempSenorChannel Function

**Parent topic:**[Supply Controller \(SUPC\)](GUID-CAEF0560-90E6-45AA-96D0-FAEAF26EDC48.md)

## C

```c
void SUPC_SelectTempSenorChannel( SUPC_TSSEL sensor );
```

## Summary

Selects a specific channel of the temperature sensor.

## Description

There are two temperature sensor channels controlled by the SUPC. These<br />channels can be used by the ADCs on the device to measure temperature.<br />Refer datasheet chapters for ADC and SUPC on the temperature sensor<br />configuration and usage.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|sensor|Identifies the temperature sensor to be selected|

## Returns

None.

## Example

```c
SUPC_SelectTempSenorChannel( SUPC_TSSEL_PTAT );
```

## Remarks

None.

