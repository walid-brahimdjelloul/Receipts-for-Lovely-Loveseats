##Let’s add in our first item, the Lovely Loveseat that is the store’s namesake.
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
##now let’s create a price for the loveseat
lovely_loveseat_price = 254.00

##Let’s extend our inventory with another characteristic piece of furniture!
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
##Now let’s set the price for our Stylish Settee
stylish_settee_price = 180.50

##we just need one more item before we’re ready for business.
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
##Let’s set the price for this item.
luxurious_lamp_price = 52.15
##In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.
sales_tax = .088

## they haven’t purchased anything yet
customer_one_total = 0
##We should also keep a list of the descriptions of things they’re purchasing
customer_one_itemization = ""

### Our customer has decided they are going to purchase our Lovely Loveseat!

customer_one_total += lovely_loveseat_price
## Add the description of the Lovely Loveseat to customer_one_itemization.
customer_one_itemization += lovely_loveseat_description

####Our customer has also decided to purchase the Luxurious Lamp!
customer_one_total += luxurious_lamp_price

## add the description of the Luxurious Lamp to our itemization.
customer_one_itemization += ' '+luxurious_lamp_description

## They’re ready to check out! Let’s begin by calculating sales tax.
customer_one_tax = customer_one_total * sales_tax

## Add the sales tax to the customer’s total cost.
customer_one_total += customer_one_tax

## Let’s start printing up their receipt!
print('Customer One Items:')
print(customer_one_itemization)

print('Customer One Total:')
print(customer_one_total)










