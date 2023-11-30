Write a function that calculates the total for a user's cart.


**Requirements**

1. The total should be the sum of all the products' prices.
2. The user may optionally use a coupon,
   in which case its value should be deducted from the total.
3. If the coupon's value is greater than the summed price,
   the function should return a 0 total and indicate
   that the user should receive a new coupon worth the difference.
4. Allow multiple coupons per cart.
5. Some of the products in a user's cart may have an associated discount
   (in percentage). Apply discounts before coupons.
6. Allow multiple discounts per product.
   A product with an initial price of $10
   and two 50% discounts should total $2.50, not $0.
