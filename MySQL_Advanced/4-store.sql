-- Script that creates a trigger to update an item's quantity when a new order is created 


-- Create trigger
CREATE TRIGGER new_order_update_quantity 
AFTER INSERT ON orders 
FOR EACH ROW
UPDATE items SET items.quantity = items.quantity - NEW.number WHERE items.name = NEW.item_name;
