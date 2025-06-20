# # from django.contrib import admin

# # Register your models here.
# # admin.py
# from django.contrib import admin
# from .models import Brand, Category, Product, ColorVariant
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# class UserAdmin(BaseUserAdmin):
#     list_display = ['username', 'email', 'role', 'brand']
#     fieldsets = BaseUserAdmin.fieldsets + (
#         ('Role Info', {'fields': ('role', 'brand')}),
#     )

# class ColorVariantInline(admin.TabularInline):
#     model = ColorVariant
#     extra = 1

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "product" and request.user.role == "brand_admin":
#             kwargs["queryset"] = Product.objects.filter(brand=request.user.brand)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'brand', 'category']
#     list_filter = ['brand', 'category']
#     inlines = [ColorVariantInline]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.role == 'brand_admin':
#             return qs.filter(brand=request.user.brand)
#         return qs
    


    
#     def has_add_permission(self, request):
#         return True

#     def save_model(self, request, obj, form, change):
#         if request.user.role == 'brand_admin':
#             obj.brand = request.user.brand
#         super().save_model(request, obj, form, change)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "brand" and request.user.role == "brand_admin":
#             kwargs["queryset"] = Brand.objects.filter(id=request.user.brand.id)
#             kwargs["initial"] = request.user.brand
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
#     def has_add_permission(self, request):
#         return True

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "product" and request.user.role == "brand_admin":
#             kwargs["queryset"] = Product.objects.filter(brand=request.user.brand)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)


# class ColorVariantAdmin(admin.ModelAdmin):
#     list_display = ['product', 'color', 'price', 'stock']
#     list_filter = ['product__brand', 'product__category', 'color']

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.role == 'brand_admin':
#             return qs.filter(product__brand=request.user.brand)
#         return qs

# admin.site.register(User, UserAdmin)
# admin.site.register(Brand)
# admin.site.register(Category)
# admin.site.register(Product,ProductAdmin)
# admin.site.register(ColorVariant ,ColorVariantAdmin)

# # from .models import Brand , Category , Product, ColorVariant
# # from django.contrib import admin

# # admin.site.register(Brand)
# # admin.site.register(Category)
# # admin.site.register(Product)
# # admin.site.register(ColorVariant)



from django.contrib import admin
from .models import Brand, Category, Product, ColorVariant, User,FormModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'role', 'brand']

    list_filter = ['is_staff','role','brand']
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'brand')}),
    )


    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs.filter(brand=request.user.brand)
    #     return qs
    
   

class ColorVariantInline(admin.StackedInline):
    model = ColorVariant
    extra = 1

    # list_filter = []

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product" and request.user.role == "brand_admin":
            kwargs["queryset"] = Product.objects.filter(brand=request.user.brand)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category']
    # list_filter =  ['name','category']
    inlines = [ColorVariantInline]

    def get_list_filter(self, request):

        if  request.user.is_authenticated  and request.user.role == 'super_admin':
            return  ['brand','category','name']
        
        else:
            return ['category','name',]
        
           

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'brand_admin':
            return qs.filter(brand=request.user.brand)
        return qs

    # def save_model(self, request, obj, form, change):
    #     if request.user.role == 'brand_admin':
    #         obj.brand = request.user.brand
    #     super().save_model(request, obj, form, change)
    
    def save_model(self, request, obj, form, change):
        # If user is brand_admin, set their brand automatically
        if request.user.role == 'brand_admin':
            obj.brand = request.user.brand

        # For superusers or others, make sure brand is set in the form
        if not obj.brand:
            raise ValueError("Brand must be selected before saving.")

        super().save_model(request, obj, form, change)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "brand":
            if request.user.role == 'super_admin':
                kwargs["queryset"] = Brand.objects.all()
            elif request.user.role == "brand_admin" and request.user.brand:
                kwargs["queryset"] = Brand.objects.filter(id=request.user.brand.id)
                kwargs["initial"] = request.user.brand
            else:
                kwargs["queryset"] = Brand.objects.none()
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

            # formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
            # formfield.disabled = True
            # return formfield
        
        


        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

    



class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'price', 'stock','size']
    list_filter = [ 'product__category', 'color']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'brand_admin':
            return qs.filter(product__brand=request.user.brand)
        return qs
    

    def get_list_filter(self, request):
        if request.user.is_authenticated and request.user.role == 'super_admin':
            return ['product__brand', 'product__category', 'color','size']
        return ['product__category', 'color','size']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            if request.user.is_authenticated and request.user.role == "brand_admin":
                kwargs["queryset"] = Product.objects.filter(brand=request.user.brand)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

    

    
class CategoryAdmin(admin.ModelAdmin):
    
    list_filter = ['name']

    


admin.site.register(User, UserAdmin)
# admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ColorVariant, ColorVariantAdmin)


# Then, conditionally register it only for superusers
class BrandAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return request.user.is_authenticated and request.user.role == 'super_admin'

    def has_view_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.role == 'super_admin' 

    def has_change_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.role == 'super_admin' 

    def has_add_permission(self, request):
        return request.user.is_authenticated and request.user.role == 'super_admin' 

    def has_delete_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.role == 'super_admin' 


    # list_display = ['name']  # or any other fields you need

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_authenticated and request.user.role == 'brand_admin':
    #         return qs.filter(id=request.user.brand_id)
    #     return qs  # super_admin sees all

    # def has_view_permission(self, request, obj=None):
    #     if request.user.role == 'super_admin':
    #         return True
    #     if request.user.role == 'brand_admin':
    #         return obj is None or obj.id == request.user.brand_id
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     if request.user.role == 'super_admin':
    #         return True
    #     if request.user.role == 'brand_admin':
    #         return obj is None or obj.id == request.user.brand_id
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     if request.user.role == 'super_admin':
    #         return True
    #     if request.user.role == 'brand_admin':
    #         return obj is not None and obj.id == request.user.brand_id
    #     return False

    # def has_add_permission(self, request):
    #     # Brand admins can only add brand if they don't already have one
    #     if request.user.role == 'super_admin':

    #         return True
    #     if request.user.role == 'brand_admin':
    #         return request.user.brand is None
    #     return False

    # def save_model(self, request, obj, form, change):
    #     if request.user.role == 'brand_admin':
    #         obj.id = request.user.brand_id or None  # Ensure not overwriting others
    #     super().save_model(request, obj, form, change)
    

# Then, conditionally register it only for superusers
# class BrandAdmin(admin.ModelAdmin):

#     def has_module_permission(self, request):
#         return request.user.is_authenticated and request.user.is_superuser

#     def has_view_permission(self, request, obj=None):
#         return request.user.is_authenticated and request.user.is_superuser

#     def has_change_permission(self, request, obj=None):
#         return request.user.is_authenticated and request.user.is_superuser

#     def has_add_permission(self, request):
#         return request.user.is_authenticated and request.user.is_superuser

#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_authenticated and request.user.is_superuser 


    
    

admin.site.register(Brand, BrandAdmin)

# admin.site.register(FormModel)


