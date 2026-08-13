Reason for exclusion of dimension
- Order dimension: The order_id was kept since it can be used for grouping orders together but the attributes in the dataset containing orders was deemed unnecessary in the analysis of the sales. 
- Payment dimension: The payment dimension was excluded because payments and sales each have a different one-to-many relationship with orders which means it would lead to duplicate rows when combining the two tables.
- Review dimension: The review dimension was excluded since the grain of sales is incomparable to the reviews.
- Geolocation dimension: The geological dimension was excluded because of the irrelevance of the data. The useful geological informations like state and city are already stored in the other dimensions.

