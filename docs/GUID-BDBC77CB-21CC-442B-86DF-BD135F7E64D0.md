# RNG\_Poly1Get Function

**Parent topic:**[Random Number Generator \(RNG\)](GUID-BA368FE6-8615-4C2E-A9D5-39DF808D9FEF.md)

**Parent topic:**[Random Number Generator \(RNG\)](GUID-A3112C88-7C07-437B-B8E0-6EACE6B7C467.md)

## C

```c
uint32_t RNG_Poly1Get (void);
```

## Summary

Returns the value of the RNGPOLY1 register.

## Description

The polynomial equation for PRNG is set via the RNGPOLYx registers. Use<br />this function to read the polynomial.

## Precondition

None.

## Parameters

None.

## Returns

Value of the RNGPOLY1 register.

## Example

```c
uint32_t poly1 = 0;
poly1 = RNG_Poly1Get();
```

## Remarks

None.

