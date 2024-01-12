from .models import *

def minStock(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id = s_id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
        
        itemsAvailable = Fin_Items.objects.filter(Company = com)

        if Fin_CNotification.objects.filter(Company_id=com, Item__isnull=False).exists():
            alertItems = Fin_CNotification.objects.filter(Company_id=com, Item__isnull=False)
            for item in alertItems:
                stockItem = Fin_Items.objects.get(id = item.Item.id)
                if stockItem.current_stock > stockItem.min_stock:
                    item.status = 'Old'
                    item.save()
                else:
                    item.status = 'New'
                    item.save()
            
            for itm in itemsAvailable:
                if not Fin_CNotification.objects.filter(Item = itm).exists():
                    if itm.min_stock > 0 and itm.current_stock < itm.min_stock:
                        Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Item = itm, Title = 'Stock Alert.!!', Discription = f'{itm.name} is below the minimum stock threshold..')

        else:
            for itm in itemsAvailable:
                if itm.min_stock > 0 and itm.current_stock < itm.min_stock:
                    Fin_CNotification.objects.create(Company_id = com, Login_Id = data, Item = itm, Title = 'Stock Alert.!!', Discription = f'{itm.name} is below the minimum stock threshold..')
        
        stockLow = Fin_CNotification.objects.filter(Company_id = com, Item__isnull=False, status = 'New')
        nCount = Fin_CNotification.objects.filter(Company_id = com, status = 'New')
        if stockLow:
            context = {
                'stockAlert': True,
                'stockLow': stockLow,
                'n': len(nCount)
            }    
            return context
        else:
            return {'alert': False,'n': len(nCount)}
    else:
        return {'alert': False}