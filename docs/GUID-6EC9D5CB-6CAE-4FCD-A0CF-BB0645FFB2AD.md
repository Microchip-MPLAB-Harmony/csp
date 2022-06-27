# RNG\_PrngEnable Function

**Parent topic:**[Random Number Generator \(RNG\)](GUID-BA368FE6-8615-4C2E-A9D5-39DF808D9FEF.md)

**Parent topic:**[Random Number Generator \(RNG\)](GUID-A3112C88-7C07-437B-B8E0-6EACE6B7C467.md)

## C

```c
void RNG_PrngEnable (void);
```

## Summary

Enables the PRNG block inside the RNG peripheral

## Description

This function triggers PRNG to generate a pseudo-random number using the<br />configured parameters.

## Precondition

RNG\_Initialize must have been called before using this function.

## Parameters

None.

## Returns

None.

## Example

```c
RNG_PrngEnable();
```

## Remarks

The RNG\_PrngDisable\(\) function can be used to stop the PRNG operation.

