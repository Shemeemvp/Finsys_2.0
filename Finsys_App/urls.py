from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('',views.Fin_index,name='Fin_index'),
    path('Company_Registration',views.Fin_CompanyReg,name='Fin_CompanyReg'),
    path('Company_Registration2/<id>',views.Fin_CompanyReg2,name='Fin_CompanyReg2'),
    path('Distributor_Registration',views.Fin_DistributorReg,name='Fin_DistributorReg'),
    path('Distributor_Registration_Action',views.Fin_DReg_Action,name='Fin_DReg_Action'),
    path('Distributor_Registration2/<id>',views.Fin_DReg2,name='Fin_DReg2'), 
    path('Distributor_Registration_Action2/<id>',views.Fin_DReg2_Action2,name='Fin_DReg2_Action2'), 
    path('Staff_Registration',views.Fin_StaffReg,name='Fin_StaffReg'),
    path('Adminhome',views.Fin_Adminhome,name='Fin_Adminhome'),
    path('LogIn',views.Fin_login,name='Fin_login'),
    path('Payment_Terms',views.Fin_PaymentTerm,name='Fin_PaymentTerm'),
    path('add_payment_terms',views.Fin_add_payment_terms,name='Fin_add_payment_terms'),
    path('Distributor',views.Fin_ADistributor,name='Fin_ADistributor'),
    path('Distributor_Request',views.Fin_Distributor_Request,name='Fin_Distributor_Request'),
    path('Distributor_Request_overview/<id>',views.Fin_Distributor_Req_overview,name='Fin_Distributor_Req_overview'),
    path('DReq_Accept/<id>',views.Fin_DReq_Accept,name='Fin_DReq_Accept'), 
    path('DReq_Reject/<id>',views.Fin_DReq_Reject,name='Fin_DReq_Reject'),
    path('All_Distributors',views.Fin_All_distributors,name='Fin_All_distributors'),
    path('All_Distributor_Overview/<id>',views.Fin_All_Distributor_Overview,name='Fin_All_Distributor_Overview'),  
    path('Distributor_Home',views.Fin_DHome,name='Fin_DHome'),
    path('companyReg_action',views.Fin_companyReg_action,name='Fin_companyReg_action'),
    path('CompanyReg2_action2/<id>',views.Fin_CompanyReg2_action2,name='Fin_CompanyReg2_action2'),
    path('Fin_Modules/<id>',views.Fin_Modules,name='Fin_Modules'),
    path('Add_Modules/<id>',views.Fin_Add_Modules,name='Fin_Add_Modules'),
    path('Company_Home',views.Fin_Com_Home,name='Fin_Com_Home'),
    path('AClients',views.Fin_AClients,name='Fin_AClients'), 
    path('Fin_AClients_Request',views.Fin_AClients_Request,name='Fin_AClients_Request'),  
    path('Fin_AClients_Request_OverView/<id>',views.Fin_AClients_Request_OverView,name='Fin_AClients_Request_OverView'),
    path('Client_Req_Accept/<id>',views.Fin_Client_Req_Accept,name='Fin_Client_Req_Accept'),
    path('Client_Req_Reject/<id>',views.Fin_Client_Req_Reject,name='Fin_Client_Req_Reject'),
    path('Fin_Admin_clients',views.Fin_Admin_clients,name='Fin_Admin_clients'), 
    path('Fin_Admin_clients_overview/<id>',views.Fin_Admin_clients_overview,name='Fin_Admin_clients_overview'),
    path('LOgout',views.logout,name="logout"),
    path('Company_Profile',views.Fin_Company_Profile,name="Fin_Company_Profile"),
    path('Fin_staffReg_action',views.Fin_staffReg_action,name='Fin_staffReg_action'),
    path('StaffReg2/<id>',views.Fin_StaffReg2,name='Fin_StaffReg2'),
    path('StaffReg2_Action/<id>',views.Fin_StaffReg2_Action,name='Fin_StaffReg2_Action'),
    path('Staff_Req',views.Fin_Staff_Req,name='Fin_Staff_Req'),
    path('Staff_Req_Accept/<id>',views.Fin_Staff_Req_Accept,name='Fin_Staff_Req_Accept'),
    path('Staff_Req_Reject/<id>',views.Fin_Staff_Req_Reject,name='Fin_Staff_Req_Reject'),
    path('All_Staffs',views.Fin_All_Staff,name='Fin_All_Staff'),
    path('DClient_req',views.Fin_DClient_req,name='Fin_DClient_req'),
    path('DClient_Req_Accept/<id>',views.Fin_DClient_Req_Accept,name='Fin_DClient_Req_Accept'),
    path('DClient_Req_Reject/<id>',views.Fin_DClient_Req_Reject,name='Fin_DClient_Req_Reject'), 
    path('DClients',views.Fin_DClients,name='Fin_DClients'),
    path('DProfile',views.Fin_DProfile,name='Fin_DProfile'),
    path('Edit_Modules',views.Fin_Edit_Modules,name='Fin_Edit_Modules'),
    path('Edit_Modules_Action',views.Fin_Edit_Modules_Action,name='Fin_Edit_Modules_Action'),
    path('Anotification',views.Fin_Anotification,name='Fin_Anotification'),
    path('Anoti_Overview/<id>',views.Fin_Anoti_Overview,name='Fin_Anoti_Overview'), 
    path('Module_Updation_Accept/<id>',views.Fin_Module_Updation_Accept,name='Fin_Module_Updation_Accept'),
    path('Module_Updation_Reject/<id>',views.Fin_Module_Updation_Reject,name='Fin_Module_Updation_Reject'),
    path('Change_payment_terms',views.Fin_Change_payment_terms,name='Fin_Change_payment_terms'),
    path('payment_terms_Updation_Accept/<id>',views.Fin_payment_terms_Updation_Accept,name='Fin_payment_terms_Updation_Accept'),
    path('payment_terms_Updation_Reject/<id>',views.Fin_payment_terms_Updation_Reject,name='Fin_payment_terms_Updation_Reject'),
    path('Dnotification',views.Fin_Dnotification,name='Fin_Dnotification'),
    path('Dnoti_Overview/<id>',views.Fin_Dnoti_Overview,name='Fin_Dnoti_Overview'), 
    path('DModule_Updation_Accept/<id>',views.Fin_DModule_Updation_Accept,name='Fin_DModule_Updation_Accept'),
    path('DModule_Updation_Reject/<id>',views.Fin_DModule_Updation_Reject,name='Fin_DModule_Updation_Reject'),
    path('ADpayment_terms_Updation_Accept/<id>',views.Fin_Dpayment_terms_Updation_Accept,name='Fin_Dpayment_terms_Updation_Accept'),
    path('ADpayment_terms_Updation_Reject/<id>',views.Fin_ADpayment_terms_Updation_Reject,name='Fin_ADpayment_terms_Updation_Reject'),
    path('Cnotification',views.Fin_Cnotification,name='Fin_Cnotification'),
    path('Wrong',views.Fin_Wrong,name='Fin_Wrong'),
    path('Wrong_Action',views.Fin_Wrong_Action,name='Fin_Wrong_Action'),
    path('DChange_payment_terms',views.Fin_DChange_payment_terms,name='Fin_DChange_payment_terms'),
    path('Client_delete/<id>',views.Fin_Client_delete,name='Fin_Client_delete'),
    path('Distributor_delete/<id>',views.Fin_Distributor_delete,name='Fin_Distributor_delete'),
    path('Staff_delete/<id>',views.Fin_Staff_delete,name='Fin_Staff_delete'),
    path('Edit_Company_profile',views.Fin_Edit_Company_profile,name='Fin_Edit_Company_profile'),
    path('Edit_Company_profile_Action',views.Fin_Edit_Company_profile_Action,name='Fin_Edit_Company_profile_Action'),
    path('Edit_Staff_profile',views.Fin_Edit_Staff_profile,name='Fin_Edit_Staff_profile'),
    path('Edit_Staff_profile_Action',views.Fin_Edit_Staff_profile_Action,name='Fin_Edit_Staff_profile_Action'),
    path('Edit_Dprofile',views.Fin_Edit_Dprofile,name='Fin_Edit_Dprofile'),
    path('Edit_Dprofile_Action',views.Fin_Edit_Dprofile_Action,name='Fin_Edit_Dprofile_Action'),
    path('DClient_req_overview/<id>',views.Fin_DClient_req_overview,name='Fin_DClient_req_overview'),
    path('DClients_overview/<id>',views.Fin_DClients_overview,name='Fin_DClients_overview'),
    path('DClient_remove/<id>',views.Fin_DClient_remove,name='Fin_DClient_remove'),
    
    #------shemeem----Items&ChartOfAccounts-----------------------
    # Items
    path('Fin_items',views.Fin_items, name='Fin_items'),
    path('Fin_create_item',views.Fin_createItem, name = 'Fin_createItem'),
    path('Fin_create_new_item',views.Fin_createNewItem, name='Fin_createNewItem'),
    path('Fin_view_item/<int:id>',views.Fin_viewItem, name='Fin_viewItem'),
    path('Fin_save_item_unit',views.Fin_saveItemUnit, name='Fin_saveItemUnit'),
    path('Fin_get_item_units',views.Fin_getItemUnits, name='Fin_getItemUnits'),
    path('Fin_create_new_account_from_items',views.Fin_createNewAccountFromItems, name='Fin_createNewAccountFromItems'),
    path('Fin_change_item_status/<int:id>/<str:status>',views.Fin_changeItemStatus, name='Fin_changeItemStatus'),
    path('Fin_edit_item/<int:id>',views.Fin_editItem, name='Fin_editItem'),
    path('Fin_update_item/<int:id>',views.Fin_updateItem, name='Fin_updateItem'),
    path('Fin_delete_item/<int:id>',views.Fin_deleteItem, name='Fin_deleteItem'),
    path('Fin_item_history/<int:id>',views.Fin_itemHistory, name='Fin_itemHistory'),
    path('Fin_item_transaction_pdf/<int:id>',views.Fin_itemTransactionPdf, name='Fin_itemTransactionPdf'),
    path('Fin_share_item_transactions_to_email/<int:id>',views.Fin_shareItemTransactionsToEmail, name='Fin_shareItemTransactionsToEmail'),
    path('Fin_add_item_comment/<int:id>',views.Fin_addItemComment, name='Fin_addItemComment'),
    path('Fin_delete_item_comment/<int:id>',views.Fin_deleteItemComment, name='Fin_deleteItemComment'),

    # Chart of accounts
    path('Fin_chart_of_accounts',views.Fin_chartOfAccounts, name='Fin_chartOfAccounts'),
    path('Fin_add_account',views.Fin_addAccount, name='Fin_addAccount'),
    path('Fin_check_accounts',views.Fin_checkAccounts, name='Fin_checkAccounts'),
    path('Fin_create_account',views.Fin_createAccount, name='Fin_createAccount'),
    path('Fin_account_overview/<int:id>',views.Fin_accountOverview, name='Fin_accountOverview'),
    path('Fin_change_acc_status/<int:id>/<str:status>',views.Fin_changeAccountStatus, name='Fin_changeAccountStatus'),
    path('Fin_account_transaction_pdf/<int:id>',views.Fin_accountTransactionPdf, name='Fin_accountTransactionPdf'),
    path('Fin_share_acc_transactions_to_email/<int:id>',views.Fin_shareAccountTransactionsToEmail, name='Fin_shareAccountTransactionsToEmail'),
    path('Fin_delete_account/<int:id>',views.Fin_deleteAccount, name= 'Fin_deleteAccount'),
    path('Fin_edit_account/<int:id>',views.Fin_editAccount, name='Fin_editAccount'),
    path('Fin_update_account/<int:id>',views.Fin_updateAccount, name='Fin_updateAccount'),
    path('Fin_account_history/<int:id>',views.Fin_accountHistory, name='Fin_accountHistory'),
    #End
    
    path('Fin_bankholder',views.Fin_bankholder,name='Fin_bankholder'),
    path('Fin_addbank',views.Fin_addbank,name='Fin_addbank'),
    path('Fin_Bankaccountholder',views.Fin_Bankaccountholder,name='Fin_Bankaccountholder'),
    path('Fin_Bankholderview/<int:id>/', views.Fin_Bankholderview, name='Fin_Bankholderview'),
    path('Fin_activebankholder/<int:id>/',views.Fin_activebankholder,name='Fin_activebankholder'),
    path('Fin_inactivatebankaccount/<int:id>/',views.Fin_inactivatebankaccount,name='Fin_inactivatebankaccount'),
    path('Fin_Editholder/<int:id>/',views.Fin_Editholder,name='Fin_Editholder'),
    path('Fin_Editbankholder/<int:id>/',views.Fin_Editbankholder,name='Fin_Editbankholder'),
    path('Fin_deleteholder/<int:id>/',views.Fin_deleteholder,name='Fin_deleteholder'),
    path('Fin_addcomment/<int:id>/', views.Fin_addcomment, name='Fin_addcomment'),
    path('Fin_deletecomment/<int:comment_id>/', views.Fin_deletecomment, name='Fin_deletecomment'),
    path('Fin_Bankhistory/<int:account_id>/', views.Fin_Bankhistory, name='Fin_Bankhistory'),
    
    # -------------Shemeem--------Price List & Customers-------------------------------
    
    path('Fin_price_list',views.Fin_priceList, name='Fin_priceList'),
    path('Fin_add_price_list',views.Fin_addPriceList, name='Fin_addPriceList'),
    path('Fin_create_price_list',views.Fin_createPriceList, name='Fin_createPriceList'),
    path('Fin_view_price_list/<int:id>',views.Fin_viewPriceList, name='Fin_viewPriceList'),
    path('Fin_change_price_list_status/<int:id>/<str:status>',views.Fin_changePriceListStatus, name='Fin_changePriceListStatus'),
    path('Fin_delete_price_list/<int:id>',views.Fin_deletePriceList, name='Fin_deletePriceList'),
    path('Fin_add_price_list_comment/<int:id>',views.Fin_addPriceListComment, name='Fin_addPriceListComment'),
    path('Fin_delete_price_list_comment/<int:id>',views.Fin_deletePriceListComment, name='Fin_deletePriceListComment'),
    path('Fin_price_list_history/<int:id>',views.Fin_priceListHistory, name='Fin_priceListHistory'),
    path('Fin_edit_price_list/<int:id>',views.Fin_editPriceList, name='Fin_editPriceList'),
    path('Fin_update_price_list/<int:id>',views.Fin_updatePriceList, name='Fin_updatePriceList'),
    path('Fin_price_list_view_pdf/<int:id>',views.Fin_priceListViewPdf, name='Fin_priceListViewPdf'),
    path('Fin_share_price_list_view_to_email/<int:id>',views.Fin_sharePriceListViewToEmail, name='Fin_sharePriceListViewToEmail'),
    
    # Customers
    path('Fin_customers',views.Fin_customers, name='Fin_customers'),
    path('Fin_add_customer',views.Fin_addCustomer, name='Fin_addCustomer'),
    path('Fin_check_customer_name',views.Fin_checkCustomerName, name='Fin_checkCustomerName'),
    path('Fin_check_customer_GSTIN',views.Fin_checkCustomerGSTIN, name='Fin_checkCustomerGSTIN'),
    path('Fin_check_customer_PAN',views.Fin_checkCustomerPAN, name='Fin_checkCustomerPAN'),
    path('Fin_check_customer_phone',views.Fin_checkCustomerPhone, name='Fin_checkCustomerPhone'),
    path('Fin_check_customer_email',views.Fin_checkCustomerEmail, name='Fin_checkCustomerEmail'),
    path('Fin_create_customer',views.Fin_createCustomer, name='Fin_createCustomer'),
    path('Fin_new_customer_payment_term',views.Fin_newCustomerPaymentTerm, name='Fin_newCustomerPaymentTerm'),
    path('Fin_view_customer/<int:id>',views.Fin_viewCustomer, name='Fin_viewCustomer'),
    path('Fin_change_customer_status/<int:id>/<str:status>',views.Fin_changeCustomerStatus, name='Fin_changeCustomerStatus'),
    path('Fin_delete_customer/<int:id>',views.Fin_deleteCustomer, name= 'Fin_deleteCustomer'),
    path('Fin_edit_customer/<int:id>',views.Fin_editCustomer, name='Fin_editCustomer'),
    path('Fin_update_customer/<int:id>',views.Fin_updateCustomer, name='Fin_updateCustomer'),
    path('Fin_customer_history/<int:id>',views.Fin_customerHistory, name='Fin_customerHistory'),
    path('Fin_customer_transactions_pdf/<int:id>',views.Fin_customerTransactionsPdf, name='Fin_customerTransactionsPdf'),
    path('Fin_share_customer_transactions_to_email/<int:id>',views.Fin_shareCustomerTransactionsToEmail, name='Fin_shareCustomerTransactionsToEmail'),
    path('Fin_add_customer_comment/<int:id>',views.Fin_addCustomerComment, name='Fin_addCustomerComment'),
    path('Fin_delete_customer_comment/<int:id>',views.Fin_deleteCustomerComment, name='Fin_deleteCustomerComment'),
    
    # harikrishnan (start)--------------------------------
    
    path('employee_list',views.employee_list,name="employee_list"),
    path('employee_create_page',views.employee_create_page,name="employee_create_page"),
    path('employee_save',views.employee_save,name="employee_save"),
    path('employee_overview/<int:pk>',views.employee_overview,name="employee_overview"),
    path('activate/<int:pk>',views.activate,name="activate"),
    path('employee_edit_page/<int:pk>',views.employee_edit_page,name="employee_edit_page"),
    path('employee_update/<int:pk>',views.employee_update,name="employee_update"),
    path('employee_comment/<int:pk>',views.employee_comment,name="employee_comment"),
    path('employee_comment_view/<int:pk>',views.employee_comment_view,name="employee_comment_view"),
    path('employee_delete/<int:pk>',views.employee_delete,name="employee_delete"),
    path('employee_history/<int:pk>',views.employee_history,name="employee_history"),
    path('employee_profile_email/<int:pk>',views.employee_profile_email,name="employee_profile_email"),
    path('Employee_Profile_PDF/<int:pk>',views.Employee_Profile_PDF,name="Employee_Profile_PDF"),

    path('holiday_list',views.holiday_list,name="holiday_list"),
    path('holiday_create_page',views.holiday_create_page,name="holiday_create_page"),
    path('holiday_add',views.holiday_add,name="holiday_add"),
    path('holiday_calendar_view/<int:mn>/<int:yr>', views.holiday_calendar_view, name='holiday_calendar_view'),
    path('holiday_edit_page/<int:pk>', views.holiday_edit_page, name='holiday_edit_page'),
    path('holiday_update/<int:pk>',views.holiday_update,name="holiday_update"),
    path('holiday_delete/<int:pk>',views.holiday_delete,name="holiday_delete"),
    
    # harikrishnan (end)--------------------------------

    # -------------Shemeem--------Invoice & Vendors-------------------------------
    # Invoice

    path('Fin_invoice',views.Fin_invoice, name='Fin_invoice'),
    path('Fin_add_invoice',views.Fin_addInvoice, name='Fin_addInvoice'),
    path('Fin_get_bank_account',views.Fin_getBankAccount, name='Fin_getBankAccount'),
    path('Fin_get_invoice_customer_data',views.Fin_getInvoiceCustomerData, name='Fin_getInvoiceCustomerData'),
    path('Fin_check_invoice_number',views.Fin_checkInvoiceNumber, name='Fin_checkInvoiceNumber'),
    path('Fin_get_inv_item_details',views.Fin_getInvItemDetails, name='Fin_getInvItemDetails'),
    path('Fin_create_invoice',views.Fin_createInvoice, name='Fin_createInvoice'),
    path('Fin_view_invoice/<int:id>',views.Fin_viewInvoice, name='Fin_viewInvoice'),
    path('Fin_convert_invoice/<int:id>',views.Fin_convertInvoice, name='Fin_convertInvoice'),
    path('Fin_add_invoice_comment/<int:id>',views.Fin_addInvoiceComment, name='Fin_addInvoiceComment'),
    path('Fin_delete_invoice_comment/<int:id>',views.Fin_deleteInvoiceComment, name='Fin_deleteInvoiceComment'),
    path('Fin_invoice_history/<int:id>',views.Fin_invoiceHistory, name='Fin_invoiceHistory'),
    path('Fin_delete_invoice/<int:id>',views.Fin_deleteInvoice, name= 'Fin_deleteInvoice'),
    path('Fin_invoicePdf/<int:id>',views.Fin_invoicePdf, name='Fin_invoicePdf'),
    path('Fin_share_invoice_to_email/<int:id>',views.Fin_shareInvoiceToEmail, name='Fin_shareInvoiceToEmail'),
    path('Fin_create_invoice_customer',views.Fin_createInvoiceCustomer, name='Fin_createInvoiceCustomer'),
    path('Fin_get_customers',views.Fin_getCustomers, name='Fin_getCustomers'),
    path('Fin_create_invoice_item',views.Fin_createInvoiceItem, name='Fin_createInvoiceItem'),
    path('Fin_get_items',views.Fin_getItems, name='Fin_getItems'),
    path('Fin_edit_invoice/<int:id>',views.Fin_editInvoice, name='Fin_editInvoice'),
    path('Fin_update_invoice/<int:id>',views.Fin_updateInvoice, name='Fin_updateInvoice'),

    # Vendor
    
    path('Fin_vendors',views.Fin_vendors, name='Fin_vendors'),
    path('Fin_add_vendor',views.Fin_addVendor, name='Fin_addVendor'),
    path('Fin_check_vendor_name',views.Fin_checkVendorName, name='Fin_checkVendorName'),
    path('Fin_check_vendor_GSTIN',views.Fin_checkVendorGSTIN, name='Fin_checkVendorGSTIN'),
    path('Fin_check_vendor_PAN',views.Fin_checkVendorPAN, name='Fin_checkVendorPAN'),
    path('Fin_check_vendor_phone',views.Fin_checkVendorPhone, name='Fin_checkVendorPhone'),
    path('Fin_check_vendor_email',views.Fin_checkVendorEmail, name='Fin_checkVendorEmail'),
    path('Fin_create_vendor',views.Fin_createVendor, name='Fin_createVendor'),
    path('Fin_view_vendor/<int:id>',views.Fin_viewVendor, name='Fin_viewVendor'),
    path('Fin_change_vendor_status/<int:id>/<str:status>',views.Fin_changeVendorStatus, name='Fin_changeVendorStatus'),
    path('Fin_delete_vendor/<int:id>',views.Fin_deleteVendor, name= 'Fin_deleteVendor'),
    path('Fin_edit_vendor/<int:id>',views.Fin_editVendor, name='Fin_editVendor'),
    path('Fin_vendor_history/<int:id>',views.Fin_vendorHistory, name='Fin_vendorHistory'),
    path('Fin_add_vendor_comment/<int:id>',views.Fin_addVendorComment, name='Fin_addVendorComment'),
    path('Fin_delete_vendor_comment/<int:id>',views.Fin_deleteVendorComment, name='Fin_deleteVendorComment'),
    path('Fin_vendor_transactions_pdf/<int:id>',views.Fin_vendorTransactionsPdf, name='Fin_vendorTransactionsPdf'),
    path('Fin_share_vendor_transactions_to_email/<int:id>',views.Fin_shareVendorTransactionsToEmail, name='Fin_shareVendorTransactionsToEmail'),
    path('Fin_update_vendor/<int:id>',views.Fin_updateVendor, name='Fin_updateVendor'),

    # -------------Shemeem--------Sales Order-------------------------------
    path('Fin_sales_orders',views.Fin_salesOrder, name='Fin_salesOrder'),
    path('Fin_add_sales_order',views.Fin_addSalesOrder, name='Fin_addSalesOrder'),
    path('Fin_create_sales_order',views.Fin_createSalesOrder, name='Fin_createSalesOrder'),
    path('Fin_check_sales_order_number',views.Fin_checkSalesOrderNumber, name='Fin_checkSalesOrderNumber'),
    path('Fin_view_sales_order/<int:id>',views.Fin_viewSalesOrder, name='Fin_viewSalesOrder'),
    path('Fin_edit_sales_order/<int:id>',views.Fin_editSalesOrder, name='Fin_editSalesOrder'),
    path('Fin_update_sales_order/<int:id>',views.Fin_updateSalesOrder, name='Fin_updateSalesOrder'),
    path('Fin_convert_sales_order/<int:id>',views.Fin_convertSalesOrder, name='Fin_convertSalesOrder'),
    path('Fin_add_sales_order_comment/<int:id>',views.Fin_addSalesOrderComment, name='Fin_addSalesOrderComment'),
    path('Fin_delete_sales_order_comment/<int:id>',views.Fin_deleteSalesOrderComment, name='Fin_deleteSalesOrderComment'),
    path('Fin_sales_order_history/<int:id>',views.Fin_salesOrderHistory, name='Fin_salesOrderHistory'),
    path('Fin_delete_sales_order/<int:id>',views.Fin_deleteSalesOrder, name= 'Fin_deleteSalesOrder'),
    path('Fin_attach_sales_order_file/<int:id>',views.Fin_attachSalesOrderFile, name='Fin_attachSalesOrderFile'),
    path('Fin_sales_order_pdf/<int:id>',views.Fin_salesOrderPdf, name='Fin_salesOrderPdf'),
    path('Fin_share_sales_order_to_email/<int:id>',views.Fin_shareSalesOrderToEmail, name='Fin_shareSalesOrderToEmail'),
    path('Fin_convert_sales_order_to_invoice/<int:id>',views.Fin_convertSalesOrderToInvoice, name='Fin_convertSalesOrderToInvoice'),
    path('Fin_sales_order_convert_invoice/<int:id>',views.Fin_salesOrderConvertInvoice, name='Fin_salesOrderConvertInvoice'),

    # -------------Shemeem--------Estimate-------------------------------
    path('Fin_estimates',views.Fin_estimates, name='Fin_estimates'),
    path('Fin_add_estimate',views.Fin_addEstimate, name='Fin_addEstimate'),
    path('Fin_create_estimate',views.Fin_createEstimate, name='Fin_createEstimate'),
    path('Fin_check_estimate_number',views.Fin_checkEstimateNumber, name='Fin_checkEstimateNumber'),
    path('Fin_view_estimate/<int:id>',views.Fin_viewEstimate, name='Fin_viewEstimate'),
    path('Fin_edit_estimate/<int:id>',views.Fin_editEstimate, name='Fin_editEstimate'),
    path('Fin_update_estimate/<int:id>',views.Fin_updateEstimate, name='Fin_updateEstimate'),
    path('Fin_convert_estimate/<int:id>',views.Fin_convertEstimate, name='Fin_convertEstimate'),
    path('Fin_add_estimate_comment/<int:id>',views.Fin_addEstimateComment, name='Fin_addEstimateComment'),
    path('Fin_delete_estimate_comment/<int:id>',views.Fin_deleteEstimateComment, name='Fin_deleteEstimateComment'),
    path('Fin_estimate_history/<int:id>',views.Fin_estimateHistory, name='Fin_estimateHistory'),
    path('Fin_delete_estimate/<int:id>',views.Fin_deleteEstimate, name= 'Fin_deleteEstimate'),
    path('Fin_estimate_pdf/<int:id>',views.Fin_estimatePdf, name='Fin_estimatePdf'),
    path('Fin_share_estimate_to_email/<int:id>',views.Fin_shareEstimateToEmail, name='Fin_shareEstimateToEmail'),
    path('Fin_attach_estimate_file/<int:id>',views.Fin_attachEstimateFile, name='Fin_attachEstimateFile'),
    path('Fin_convert_estimate_to_invoice/<int:id>',views.Fin_convertEstimateToInvoice, name='Fin_convertEstimateToInvoice'),
    path('Fin_estimate_convert_invoice/<int:id>',views.Fin_estimateConvertInvoice, name='Fin_estimateConvertInvoice'),
    path('Fin_convert_estimate_to_sales_order/<int:id>',views.Fin_convertEstimateToSalesOrder, name='Fin_convertEstimateToSalesOrder'),
    path('Fin_estimate_convert_sales_order/<int:id>',views.Fin_estimateConvertSalesOrder, name='Fin_estimateConvertSalesOrder'),

    # < ------------- Shemeem -------- > Manual Journals < ------------------------------- >
    path('Fin_manual_journals',views.Fin_manualJournals, name='Fin_manualJournals'),
    path('Fin_add_journal',views.Fin_addJournal, name='Fin_addJournal'),
    path('Fin_check_journal_number',views.Fin_checkJournalNumber, name='Fin_checkJournalNumber'),
    path('Fin_create_journal',views.Fin_createJournal, name='Fin_createJournal'),
    path('Fin_create_new_account_ajax',views.Fin_createNewAccountAjax, name='Fin_createNewAccountAjax'),
    path('Fin_view_journal/<int:id>',views.Fin_viewJournal, name='Fin_viewJournal'),
    path('Fin_edit_journal/<int:id>',views.Fin_editJournal, name='Fin_editJournal'),
    path('Fin_update_journal/<int:id>',views.Fin_updateJournal, name='Fin_updateJournal'),
    path('Fin_convert_journal/<int:id>',views.Fin_convertJournal, name='Fin_convertJournal'),
    path('Fin_add_journal_comment/<int:id>',views.Fin_addJournalComment, name='Fin_addJournalComment'),
    path('Fin_delete_journal_comment/<int:id>',views.Fin_deleteJournalComment, name='Fin_deleteJournalComment'),
    path('Fin_attach_journal_file/<int:id>',views.Fin_attachJournalFile, name='Fin_attachJournalFile'),
    path('Fin_journal_history/<int:id>',views.Fin_journalHistory, name='Fin_journalHistory'),
    path('Fin_delete_journal/<int:id>',views.Fin_deleteJournal, name= 'Fin_deleteJournal'),
    path('Fin_journal_pdf/<int:id>',views.Fin_journalPdf, name='Fin_journalPdf'),
    path('Fin_share_journal_to_email/<int:id>',views.Fin_shareJournalToEmail, name='Fin_shareJournalToEmail'),
    # End
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)