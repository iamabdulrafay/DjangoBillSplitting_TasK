from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import math
# Create your views here.



# Task 1: Basic Bill Splitting
@csrf_exempt 
def Basic_Splitting(request):
     try:
        data=json.loads(request.body)
        user_ids=data.get("user_ids",[])
        bill=data.get("price",0)
        split=math.floor(bill/len(user_ids))
        return JsonResponse({"split":split})
     except json.JSONDecodeError:
         return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
     

# Task 2: unevenly Bill Splitting
@csrf_exempt
def split_unevenly(request):
    data=json.loads(request.body)
    
    total_price=data.get("total_price",0)
    
    transaction_dets=data.get("details",[])
    new_dic={
       
    }
    evenly_contribution=total_price/len(transaction_dets)

    for item in transaction_dets:
         name=item.get('name')
         amount=item.get('amount')

         
         if new_dic!="name" and new_dic!="amount":
                    new_dic[name]={"unevenly_pay":amount}
        #  print(amount-new_dic["evenly_contribution"])
        
              

    new_dic["total_price"]=total_price
    new_dic["evenly_contribution"]=evenly_contribution
    for name, details in new_dic.items():
        print(details)
         
 
        if name not in ["total_price", "evenly_contribution"]:
           unevenly_pay = details.get("unevenly_pay", 0)
        #    print(unevenly_pay)
         
            
            
           if unevenly_pay > evenly_contribution:
                payable = unevenly_pay - evenly_contribution
                details["payable"] = payable
         
           else:
                due =  evenly_contribution-unevenly_pay
                details["due"] = due
                
   
         
    
              


    return JsonResponse(new_dic)
   



# Task3)split-including-tip-tax
@csrf_exempt
def Tip_And_Tax(request):
     data=json.loads(request.body)
     user_ids=data.get("user_ids",[])
    
     total=data.get("total_amount",0)
     tip_percentage=data.get("tip_percentage",0)
     tax_percentage=data.get("tax_percentage",0)
     evenely_distribution=total/len(user_ids)
     tip_and_tax={
          

           
          "total_amount":total,
          "tip_percentage":tip_percentage,
          "tax_percentage":tax_percentage
     }
    
     for i in user_ids:
            tip_value_conversion=tip_percentage.replace("%","")
            tax_value_conversion=tax_percentage.replace("%","")
            tip_value=float(tip_value_conversion)/100*evenely_distribution
            tax_value=float(tax_value_conversion)/100*evenely_distribution
            total_amount= evenely_distribution+tip_value+tax_value
            tip_and_tax[i] = {
                "net_amount": evenely_distribution,
                "tip": tip_value,
                "tax": tax_value,
                "total_value": total_amount
            }

     return JsonResponse(tip_and_tax)

# Task4)split-including-tip-tax
@csrf_exempt
def Discount(request):
     data=json.loads(request.body)
     user_ids=data.get("user_ids",[])
    
     total=data.get("total_amount",0)
     discount_percentage=data.get("discount_percentage",0)
     
     evenely_distribution=total/len(user_ids)
     discount_dict={
          

           
          "total_amount":total,
          "discount_percentage":discount_percentage
        
     }
    
     for i in user_ids:
           
            discount_percentage_conversion=discount_percentage.replace("%","")
            discount_value=float(discount_percentage_conversion)/100*evenely_distribution
            total_amount=evenely_distribution-discount_value
            
            discount_dict[i] = {
                "net_amount": evenely_distribution,
                "discount":discount_value,
                "total_amount":total_amount
            }

     return JsonResponse(discount_dict)





# task 5    
@csrf_exempt   
def Bill_Splitting(request):
    try:
        data = json.loads(request.body)
        user_ids=data.get("user_ids",[])
        items=data.get("items",[])
        shared_items=data.get("shared_items",{})
        
        new_shared_items={}
        net_amount=0 #net amount
        total_price=0 #total net_amount
        discount=0.10 #10% tax
        
        tax=0.16 #16% tax
        tip=0.02 #2% tax

        per_person_bill = {user_id: {} for user_id in user_ids} #per person details
        for item in items:
             item_name=item["name"]
             item_price=item["price"]
             net_amount+=item_price
             
     
             
             user_sharing=shared_items.get(item_name,[])
             new_shared_items[item_name]=user_sharing
            
             

             if user_sharing:
                per_person = item_price / len(user_sharing)
                
                for user in user_sharing:
                
                    per_person_bill[user] = per_person_bill.get(user, {})
                    
                    
                    per_person_bill[user][item_name] = per_person_bill[user].get(item_name, 0) + per_person

        discounted_price = net_amount - (net_amount * discount)
        taxed_price = discounted_price + (discounted_price * tax)
        total_price = math.floor(taxed_price + (taxed_price * tip)    ) 
            
              

        for user,user_items in per_person_bill.items():
            total_price_per_person=0
            for item_name,item_price in user_items.items():
                 if item_name!="discount" and item_name!="price" and item_name!="total_amount":
                      total_price_per_person+=item_price


            discount_price=total_price_per_person*discount
            tip_price=total_price_per_person*tip
            tax_price=total_price_per_person*tax
            
            # over all total calculationof all net_amount of user 
            total_price_with_discount=total_price_per_person-discount_price
            total_price_with_tax=total_price_with_discount+tax_price
            total_price_with_tip=math.floor(total_price_with_tax+tip_price)

            per_person_bill[user]["discount"]=discount_price
            per_person_bill[user]["tip"]=tip_price
            per_person_bill[user]["total_amount"]=total_price_with_tip    
            

        new_dictoneries={
                        
   
            
            "user_ids":user_ids,
            "item":items,
            "shared_items":new_shared_items,
            "per_person_bill":per_person_bill,
            "net_amount":net_amount,
            "discount":"10%",
            "tip":"2%",
            "tax":"16% ",
            "total_amount":total_price

            
            

        }
       
             
        return JsonResponse(new_dictoneries)
    except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
  
    



     