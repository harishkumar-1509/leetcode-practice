def divide(dividend: int, divisor: int) -> int:
    # Constants to handle overflow.
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Handle special cases
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    if dividend == 0:
        return 0
    
    # Determine the sign of the result
    negative = (dividend < 0) ^ (divisor < 0)
    
    # Use absolute values to simplify calculation
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    # Perform division using bit shifting
    for i in range(31, -1, -1):
        if (dividend >> i) >= divisor:
            quotient += 1 << i
            dividend -= divisor << i
    
    # Apply the sign to the result
    if negative:
        quotient = -quotient
    
    # Handle overflow
    if quotient < INT_MIN:
        return INT_MIN
    if quotient > INT_MAX:
        return INT_MAX
    
    return quotient

# Example usage:
print(divide(10, 3))  # Output: 3
print(divide(7, -3))  # Output: -2
