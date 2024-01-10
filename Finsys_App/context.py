from .models import *

def minStock(request):
    if 's_id' in request.session:
        s_id = request.session['s_id']
        data = Fin_Login_Details.objects.get(id = s_id)
        if data.User_Type == "Company":
            com = Fin_Company_Details.objects.get(Login_Id = s_id)
        else:
            com = Fin_Staff_Details.objects.get(Login_Id = s_id).company_id
        
        items = Fin_Items.objects.filter(Company = com)
        
        stockLow = []
        for item in items:
            if item.min_stock > 0 and item.current_stock < item.min_stock:
                stockLow.append({'name':item.name})

        context = {
            'stockAlert': True, 'stockLow':stockLow
        }    
        return context
    else:
        return {'alert': False}